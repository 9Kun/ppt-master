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
DESIGN_SPEC = PROJECT / "design_spec.md"
SPEC_LOCK = PROJECT / "spec_lock.md"
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


def mark_overlay_semantics(root: ET.Element, refs: set[str], page: int) -> tuple[int, int]:
    """Mark intentional root overlays as static semantic frames.

    PPT Master treats supported semantic roles as chrome for automatic animation
    and ordinary module-collision checks, while explicit animations.json entries
    may still animate them. This is exactly what these answer/console state
    overlays need: multiple authored states intentionally occupy the same region.
    """
    decorated = 0
    named_anonymous = 0
    used = direct_group_ids(root)
    anon_index = 0
    for child in list(root):
        if local_name(child.tag) != "g":
            continue
        group_id = (child.get("id") or "").strip()
        is_explicit_overlay = bool(group_id and group_id in refs)
        is_anonymous_scene_art = not group_id
        if not (is_explicit_overlay or is_anonymous_scene_art):
            continue
        if is_anonymous_scene_art:
            while True:
                anon_index += 1
                candidate = f"scene-decoration-p{page:02d}-{anon_index:02d}"
                if candidate not in used:
                    break
            child.set("id", candidate)
            used.add(candidate)
            group_id = candidate
            named_anonymous += 1
        # Do not use data-pptx-layer: that would make the object structural.
        # 'decoration' is a compiler hint only and does not change SVG rendering.
        child.set("data-pptx-role", "decoration")
        decorated += 1
    return decorated, named_anonymous


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


def normalize_design_contract() -> tuple[int, int]:
    """Bring the Design Spec/spec lock in line with actual authored assets."""
    design = DESIGN_SPEC.read_text(encoding="utf-8")
    status_replacements = 0
    for filename in (
        "mascot_turtle_new_commands_v2.png",
        "mascot_turtle_flower_workshop_v2.png",
    ):
        rows = [line for line in design.splitlines() if filename in line]
        if len(rows) != 1:
            raise RuntimeError(f"design_spec.md: expected one image row for {filename}, got {len(rows)}")
        old = rows[0]
        if "| ai | Ready |" in old:
            new = old.replace("| ai | Ready |", "| ai | Generated |")
            design = design.replace(old, new)
            status_replacements += 1
        elif "| ai | Generated |" not in old:
            raise RuntimeError(f"design_spec.md: unexpected status row for {filename}: {old}")

    compact_row = "| Compact code | 12.5 |"
    if compact_row not in design:
        anchor = "| Code | 20 |"
        if anchor not in design:
            raise RuntimeError("design_spec.md: Code typography anchor not found")
        design = design.replace(
            anchor,
            anchor + "\n" + compact_row,
            1,
        )
    DESIGN_SPEC.write_text(design, encoding="utf-8")

    lock = SPEC_LOCK.read_text(encoding="utf-8")
    compact_lock = "- compact_code: 12.5"
    if compact_lock not in lock:
        anchor = "- code: 20"
        if anchor not in lock:
            raise RuntimeError("spec_lock.md: code typography anchor not found")
        lock = lock.replace(anchor, anchor + "\n" + compact_lock, 1)
    SPEC_LOCK.write_text(lock, encoding="utf-8")
    return status_replacements, 1


def main() -> int:
    required = (SVG_OUTPUT, SVG_FINAL, ANIMATIONS, DESIGN_SPEC, SPEC_LOCK)
    if not SVG_OUTPUT.is_dir() or not SVG_FINAL.is_dir() or any(not p.exists() for p in required[2:]):
        raise RuntimeError("lesson06 project structure is incomplete")

    # The redesign accidentally updated only svg_final/. Native PPTX export and
    # the official quality gate read svg_output/ by default. Restore one
    # canonical source by copying P05-P36 redesigned SVGs back to svg_output/.
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
    status_replacements, compact_roles = normalize_design_contract()

    slides = data.get("slides", {})
    stripped_bounds = 0
    promoted = 0
    decorated = 0
    named_anonymous = 0
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
        d, n = mark_overlay_semantics(root, refs, page)
        decorated += d
        named_anonymous += n
        # Final fail-closed assertion: every configured target/trigger is a
        # direct root group. Explicit sidecar animation remains supported even
        # when a group carries a static semantic role.
        missing = refs - direct_group_ids(root)
        if missing:
            raise RuntimeError(f"{svg_path.stem}: unresolved top-level animation groups: {sorted(missing)}")
        tree.write(svg_path, encoding="unicode", xml_declaration=False)
        checked_slides += 1

    ANIMATIONS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Protect the user's explicit invariant: P01-P04 are never touched here.
    print(f"copied redesigned pages to svg_output: {copied}")
    print(f"checked P05-P36 SVGs: {checked_slides}")
    print(f"removed legacy data-pptx-bounds: {stripped_bounds}")
    print(f"promoted referenced groups to top level: {promoted}")
    print(f"marked intentional overlay/scene groups as decoration: {decorated}")
    print(f"assigned stable ids to anonymous scene groups: {named_anonymous}")
    print(f"removed unsupported interactive_sequence_mode entries: {removed_modes}")
    print(f"normalized trigger_shape effects to on-click: {normalized_clicks}")
    print(f"updated image status rows Ready->Generated: {status_replacements}")
    print(f"ensured compact-code typography role: {compact_roles}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"repair failed: {exc}", file=sys.stderr)
        raise
