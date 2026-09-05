#!/usr/bin/env python3
"""Make Lesson 06 code-demo trigger sequences play from one click in WPS.

The canonical animations.json stays PowerPoint-semantic.  PPT Master's standard
writer emits one interactiveSeq for every trigger_shape row.  WPS Presentation
can treat those sibling interactiveSeq nodes as repeated-click steps.  For the
Lesson 06 code-demo slides, collapse sibling sequences that share one trigger
shape into one interactiveSeq: the first animation row remains clickEffect and
all following rows become afterEffect.  Existing per-row TriggerDelayTime is
preserved, so terminal/result steps continue automatically after the click.

Only slides whose sidecar contains a trigger_shape beginning with ``run-`` are
eligible.  Within those slides all same-shape interactive sequences are
collapsed, which also makes the task selector buttons complete their state
switch in one click.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

PML_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
P = f"{{{PML_NS}}}"


def q(tag: str) -> str:
    return P + tag


def _register_namespaces(xml_bytes: bytes) -> None:
    text = xml_bytes.decode("utf-8", errors="ignore")
    for prefix, uri in re.findall(r'xmlns:([A-Za-z_][\w.-]*)="([^"]+)"', text):
        if prefix not in {"xml", "xmlns"}:
            try:
                ET.register_namespace(prefix, uri)
            except ValueError:
                pass


def _iter_effect_rows(group_cfg: object):
    if not isinstance(group_cfg, dict):
        return []
    effects = group_cfg.get("effects")
    if isinstance(effects, list):
        return [row for row in effects if isinstance(row, dict)]
    if group_cfg.get("effect"):
        return [group_cfg]
    return []


def affected_slide_numbers(project: Path) -> list[int]:
    cfg = json.loads((project / "animations.json").read_text(encoding="utf-8"))
    affected: list[int] = []
    for slide_name, slide_cfg in (cfg.get("slides") or {}).items():
        if not isinstance(slide_cfg, dict):
            continue
        has_run_trigger = False
        for group_cfg in (slide_cfg.get("groups") or {}).values():
            for row in _iter_effect_rows(group_cfg):
                trigger_shape = row.get("trigger_shape")
                if isinstance(trigger_shape, str) and trigger_shape.startswith("run-"):
                    has_run_trigger = True
                    break
            if has_run_trigger:
                break
        if not has_run_trigger:
            continue
        match = re.match(r"^(\d+)_", slide_name)
        if not match:
            raise ValueError(f"cannot resolve slide number from sidecar key: {slide_name!r}")
        affected.append(int(match.group(1)))
    return sorted(set(affected))


def _trigger_shape_id(interactive_ctn: ET.Element) -> str | None:
    st_cond = interactive_ctn.find(q("stCondLst"))
    if st_cond is None:
        return None
    for sp_target in st_cond.iter(q("spTgt")):
        spid = sp_target.get("spid")
        if spid:
            return spid
    return None


def _leaf_effect_rows(interactive_ctn: ET.Element) -> list[ET.Element]:
    return [
        node
        for node in interactive_ctn.iter(q("cTn"))
        if node.get("presetClass")
    ]


def _timing_root_children(slide_root: ET.Element) -> ET.Element | None:
    timing = slide_root.find(q("timing"))
    if timing is None:
        return None
    tn_list = timing.find(q("tnLst"))
    if tn_list is None:
        return None
    top_par = tn_list.find(q("par"))
    if top_par is None:
        return None
    tm_root = top_par.find(q("cTn"))
    if tm_root is None:
        return None
    return tm_root.find(q("childTnLst"))


def collapse_slide(xml_bytes: bytes, slide_number: int) -> tuple[bytes, dict[str, int]]:
    _register_namespaces(xml_bytes)
    root = ET.fromstring(xml_bytes)
    timing_children = _timing_root_children(root)
    if timing_children is None:
        raise ValueError(f"slide {slide_number}: no timing tree found")

    groups: dict[str, list[ET.Element]] = defaultdict(list)
    for seq in list(timing_children):
        if seq.tag != q("seq"):
            continue
        ctn = seq.find(q("cTn"))
        if ctn is None or ctn.get("nodeType") != "interactiveSeq":
            continue
        trigger_id = _trigger_shape_id(ctn)
        if trigger_id:
            groups[trigger_id].append(seq)

    collapsed = 0
    input_sequences = 0
    output_sequences = 0
    output_rows = 0
    for trigger_id, sequences in groups.items():
        input_sequences += len(sequences)
        if len(sequences) == 1:
            output_sequences += 1
            ctn = sequences[0].find(q("cTn"))
            output_rows += len(_leaf_effect_rows(ctn)) if ctn is not None else 0
            continue

        base_seq = sequences[0]
        base_ctn = base_seq.find(q("cTn"))
        if base_ctn is None:
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} has no sequence cTn")
        base_children = base_ctn.find(q("childTnLst"))
        if base_children is None:
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} has no childTnLst")

        expected_rows = 0
        for index, seq in enumerate(sequences):
            ctn = seq.find(q("cTn"))
            if ctn is None:
                raise ValueError(f"slide {slide_number}: malformed interactive sequence")
            rows = _leaf_effect_rows(ctn)
            if len(rows) != 1:
                raise ValueError(
                    f"slide {slide_number}: trigger {trigger_id} sequence must contain "
                    f"exactly one effect row before WPS collapse; found {len(rows)}"
                )
            expected_rows += 1
            rows[0].set("nodeType", "clickEffect" if index == 0 else "afterEffect")

            if index == 0:
                continue
            child_list = ctn.find(q("childTnLst"))
            if child_list is None:
                raise ValueError(f"slide {slide_number}: trigger {trigger_id} missing child list")
            for child in list(child_list):
                child_list.remove(child)
                base_children.append(child)
            timing_children.remove(seq)

        # Standard interactiveSeq output includes a next-click condition for
        # every row.  Once rows are collapsed, keeping that condition can make
        # WPS wait for another click instead of honoring afterEffect chaining.
        next_conditions = base_seq.find(q("nextCondLst"))
        if next_conditions is not None:
            base_seq.remove(next_conditions)

        final_rows = _leaf_effect_rows(base_ctn)
        if len(final_rows) != expected_rows:
            raise ValueError(
                f"slide {slide_number}: trigger {trigger_id} row count changed "
                f"during collapse ({expected_rows} -> {len(final_rows)})"
            )
        if final_rows[0].get("nodeType") != "clickEffect":
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} lost click anchor")
        if any(row.get("nodeType") != "afterEffect" for row in final_rows[1:]):
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} has non-auto tail row")

        collapsed += len(sequences) - 1
        output_sequences += 1
        output_rows += len(final_rows)

    if not groups:
        raise ValueError(f"slide {slide_number}: no interactive sequences found")
    if collapsed == 0:
        raise ValueError(f"slide {slide_number}: no repeated trigger sequences to collapse")

    xml_out = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return xml_out, {
        "triggers": len(groups),
        "input_sequences": input_sequences,
        "output_sequences": output_sequences,
        "collapsed_sequences": collapsed,
        "effect_rows": output_rows,
    }


def verify_slide(xml_bytes: bytes, slide_number: int) -> dict[str, int]:
    root = ET.fromstring(xml_bytes)
    timing_children = _timing_root_children(root)
    if timing_children is None:
        raise ValueError(f"slide {slide_number}: no timing tree found after patch")
    by_trigger: dict[str, list[ET.Element]] = defaultdict(list)
    for seq in list(timing_children):
        if seq.tag != q("seq"):
            continue
        ctn = seq.find(q("cTn"))
        if ctn is None or ctn.get("nodeType") != "interactiveSeq":
            continue
        trigger_id = _trigger_shape_id(ctn)
        if trigger_id:
            by_trigger[trigger_id].append(seq)
    if not by_trigger:
        raise ValueError(f"slide {slide_number}: no interactive sequences after patch")

    rows = 0
    for trigger_id, sequences in by_trigger.items():
        if len(sequences) != 1:
            raise ValueError(
                f"slide {slide_number}: trigger {trigger_id} still has {len(sequences)} interactiveSeq nodes"
            )
        seq = sequences[0]
        ctn = seq.find(q("cTn"))
        leaf_rows = _leaf_effect_rows(ctn)
        if not leaf_rows:
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} has no effect rows")
        if leaf_rows[0].get("nodeType") != "clickEffect":
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} first row is not clickEffect")
        if any(row.get("nodeType") != "afterEffect" for row in leaf_rows[1:]):
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} tail is not automatic")
        if seq.find(q("nextCondLst")) is not None:
            raise ValueError(f"slide {slide_number}: trigger {trigger_id} still has next-click condition")
        rows += len(leaf_rows)
    return {"triggers": len(by_trigger), "effect_rows": rows}


def patch_pptx(project: Path, source: Path, output: Path) -> None:
    slide_numbers = affected_slide_numbers(project)
    if not slide_numbers:
        raise ValueError("animations.json contains no run-* code-demo triggers")

    modified: dict[str, bytes] = {}
    summaries: dict[int, dict[str, int]] = {}
    with zipfile.ZipFile(source, "r") as zin:
        for number in slide_numbers:
            member = f"ppt/slides/slide{number}.xml"
            xml_out, summary = collapse_slide(zin.read(member), number)
            modified[member] = xml_out
            summaries[number] = summary

        output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            prefix=output.stem + ".", suffix=".tmp.pptx", dir=output.parent, delete=False
        ) as handle:
            temp_path = Path(handle.name)
        try:
            with zipfile.ZipFile(temp_path, "w") as zout:
                for info in zin.infolist():
                    data = modified.get(info.filename)
                    if data is None:
                        data = zin.read(info.filename)
                    zout.writestr(info, data)
            temp_path.replace(output)
        finally:
            temp_path.unlink(missing_ok=True)

    with zipfile.ZipFile(output, "r") as z:
        for number in slide_numbers:
            verify_slide(z.read(f"ppt/slides/slide{number}.xml"), number)

    print("WPS code-demo animation patch complete")
    print("source:", source)
    print("output:", output)
    print("slides:", ", ".join(f"P{n:02d}" for n in slide_numbers))
    for number in slide_numbers:
        summary = summaries[number]
        print(
            f"P{number:02d}: triggers={summary['triggers']} "
            f"interactiveSeq {summary['input_sequences']} -> {summary['output_sequences']} "
            f"collapsed={summary['collapsed_sequences']} rows={summary['effect_rows']}"
        )


def check_pptx(project: Path, pptx: Path) -> None:
    slide_numbers = affected_slide_numbers(project)
    with zipfile.ZipFile(pptx, "r") as z:
        print("WPS code-demo animation structure check")
        print("pptx:", pptx)
        for number in slide_numbers:
            summary = verify_slide(z.read(f"ppt/slides/slide{number}.xml"), number)
            print(f"P{number:02d}: triggers={summary['triggers']} rows={summary['effect_rows']} OK")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    pptx = args.pptx.resolve()
    if args.check:
        check_pptx(project, pptx)
        return 0
    output = (args.output or pptx.with_name(pptx.stem + "_wps.pptx")).resolve()
    patch_pptx(project, pptx, output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
