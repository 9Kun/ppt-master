#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "projects/Python应用课_第06课_阶段测评与复盘_阳光积木实验室_20260905_ppt169_20260905"
SVG_OUTPUT = PROJECT / "svg_output"
SVG_FINAL = PROJECT / "svg_final"
ANIMATIONS = PROJECT / "animations.json"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parent_map(root: ET.Element) -> dict[int, ET.Element]:
    return {id(child): parent for parent in root.iter() for child in list(parent)}


def direct_group_ids(root: ET.Element) -> set[str]:
    return {
        (child.get("id") or "").strip()
        for child in list(root)
        if local_name(child.tag) == "g" and (child.get("id") or "").strip()
    }


def find_group(root: ET.Element, group_id: str) -> ET.Element | None:
    found = [
        el for el in root.iter()
        if local_name(el.tag) == "g" and (el.get("id") or "").strip() == group_id
    ]
    if len(found) > 1:
        raise RuntimeError(f"duplicate group id {group_id!r}")
    return found[0] if found else None


def referenced_ids(slide_cfg: dict) -> set[str]:
    refs: set[str] = set()
    groups = slide_cfg.get("groups", {})
    if not isinstance(groups, dict):
        return refs
    for target_id, group_cfg in groups.items():
        refs.add(str(target_id))
        if not isinstance(group_cfg, dict):
            continue
        effects = group_cfg.get("effects", [])
        if not isinstance(effects, list):
            continue
        for effect in effects:
            if not isinstance(effect, dict):
                continue
            trigger_shape = effect.get("trigger_shape")
            if isinstance(trigger_shape, str) and trigger_shape.strip():
                refs.add(trigger_shape.strip())
    return refs


def strip_legacy_bounds(root: ET.Element) -> int:
    count = 0
    for el in root.iter():
        if "data-pptx-bounds" in el.attrib:
            del el.attrib["data-pptx-bounds"]
            count += 1
    return count


def promote_referenced_groups(root: ET.Element, refs: set[str], slide_name: str) -> int:
    promoted = 0
    while True:
        direct = direct_group_ids(root)
        pending = sorted(refs - direct)
        if not pending:
            return promoted
        changed = False
        parents = parent_map(root)
        for ref in pending:
            group = find_group(root, ref)
            if group is None:
                raise RuntimeError(f"{slide_name}: animation reference {ref!r} is missing from SVG")
            parent = parents.get(id(group))
            if parent is None:
                raise RuntimeError(f"{slide_name}: cannot resolve parent for {ref!r}")
            # Moving an animated/trigger group to the SVG root is safe only when
            # its ancestor chain has no transforms. Fail closed otherwise.
            cursor = parent
            while cursor is not root:
                if cursor.get("transform"):
                    raise RuntimeError(
                        f"{slide_name}: cannot promote {ref!r}; ancestor has transform={cursor.get('transform')!r}"
                    )
                cursor = parents.get(id(cursor))
                if cursor is None:
                    raise RuntimeError(f"{slide_name}: broken ancestor chain for {ref!r}")
            parent.remove(group)
            root.append(group)
            promoted += 1
            changed = True
        if not changed:
            return promoted


def normalize_animation_config(data: dict) -> tuple[int, int]:
    removed_modes = 0
    normalized_clicks = 0
    slides = data.get("slides", {})
    if not isinstance(slides, dict):
        raise RuntimeError("animations.json: top-level 'slides' must be an object")
    for slide_cfg in slides.values():
        if not isinstance(slide_cfg, dict):
            continue
        if "interactive_sequence_mode" in slide_cfg:
            del slide_cfg["interactive_sequence_mode"]
            removed_modes += 1
        groups = slide_cfg.get("groups", {})
        if not isinstance(groups, dict):
            continue
        for group_cfg in groups.values():
            if not isinstance(group_cfg, dict):
                continue
            effects = group_cfg.get("effects", [])
            if not isinstance(effects, list):
                continue
            for effect in effects:
                if not isinstance(effect, dict):
                    continue
                if isinstance(effect.get("trigger_shape"), str) and effect["trigger_shape"].strip():
                    if effect.get("trigger") != "on-click":
                        effect["trigger"] = "on-click"
                        normalized_clicks += 1
    return removed_modes, normalized_clicks


def main() -> int:
    if not SVG_OUTPUT.is_dir() or not SVG_FINAL.is_dir() or not ANIMATIONS.is_file():
        raise RuntimeError("lesson06 project structure is incomplete")

    # The previous redesign accidentally updated only svg_final/. Native PPTX
    # export and the official quality gate read svg_output/ by default. Restore
    # one canonical source by copying P05-P36 redesigned SVGs back to svg_output/.
    copied = 0
    for src in sorted(SVG_FINAL.glob("*.svg")):
        try:
            page = int(src.name[:2])
        except ValueError:
            continue
        if 5 <= page <= 36:
            shutil.copy2(src, SVG_OUTPUT / src.name)
            copied += 1
    if copied != 32:
        raise RuntimeError(f"expected 32 redesigned SVGs (P05-P36), copied {copied}")

    data = json.loads(ANIMATIONS.read_text(encoding="utf-8"))
    removed_modes, normalized_clicks = normalize_animation_config(data)

    slides = data.get("slides", {})
    stripped_bounds = 0
    promoted = 0
    checked_slides = 0
    for svg_path in sorted(SVG_OUTPUT.glob("*.svg")):
        try:
            page = int(svg_path.name[:2])
        except ValueError:
            continue
        if not (5 <= page <= 36):
            continue
        tree = ET.parse(svg_path)
        root = tree.getroot()
        stripped_bounds += strip_legacy_bounds(root)
        slide_cfg = slides.get(svg_path.stem, {})
        refs = referenced_ids(slide_cfg) if isinstance(slide_cfg, dict) else set()
        promoted += promote_referenced_groups(root, refs, svg_path.stem)
        # Final fail-closed assertion: every configured target/trigger is a direct root group.
        missing = refs - direct_group_ids(root)
        if missing:
            raise RuntimeError(f"{svg_path.stem}: unresolved top-level animation groups: {sorted(missing)}")
        tree.write(svg_path, encoding="unicode", xml_declaration=False)
        checked_slides += 1

    ANIMATIONS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Protect the user's explicit invariant: P01-P04 are never touched.
    print(f"copied redesigned pages to svg_output: {copied}")
    print(f"checked P05-P36 SVGs: {checked_slides}")
    print(f"removed legacy data-pptx-bounds: {stripped_bounds}")
    print(f"promoted referenced groups to top level: {promoted}")
    print(f"removed unsupported interactive_sequence_mode entries: {removed_modes}")
    print(f"normalized trigger_shape effects to on-click: {normalized_clicks}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"repair failed: {exc}", file=sys.stderr)
        raise
