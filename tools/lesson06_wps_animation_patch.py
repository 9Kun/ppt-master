from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# 1) Sidecar schema: allow an explicit WPS interactive-sequence serialization mode.
config = ROOT / "skills/ppt-master/scripts/svg_to_pptx/animation_config.py"
replace_once(
    config,
    "            'trigger',\n            *ANIMATION_TIMING_OPTION_FIELDS,",
    "            'trigger',\n            'interactive_sequence_mode',\n            *ANIMATION_TIMING_OPTION_FIELDS,",
)
replace_once(
    config,
    "    if 'trigger' in animation:\n        trigger_error = _animation_trigger_error(animation['trigger'], label)\n        if trigger_error:\n            errors.append(trigger_error)\n",
    "    if 'trigger' in animation:\n        trigger_error = _animation_trigger_error(animation['trigger'], label)\n        if trigger_error:\n            errors.append(trigger_error)\n    if 'interactive_sequence_mode' in animation:\n        mode = animation['interactive_sequence_mode']\n        if mode not in {'standard', 'wps'}:\n            errors.append(\n                f'animations.json {label} animation interactive_sequence_mode '\n                f'must be \\\"standard\\\" or \\\"wps\\\": {mode!r}'\n            )\n",
)

# 2) Add the WPS serializer overlay module. It merges sibling interactiveSeq
# containers that share the same trigger shape while preserving each row's
# PowerPoint-authored clickEffect metadata and its authored delay.
wps = ROOT / "skills/ppt-master/scripts/svg_to_pptx/wps_compat.py"
wps.write_text('''"""WPS-specific OOXML serialization helpers for click-triggered timelines.

The public animation sidecar remains PowerPoint-semantic.  In WPS mode we only
change the timing-tree container layout: rows sharing one trigger shape are
placed under one interactiveSeq so one click starts the entire authored
preview/typewriter timeline.
"""

from __future__ import annotations

from xml.etree import ElementTree as ET

PML_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
ET.register_namespace("p", PML_NS)


def _q(tag: str) -> str:
    return f"{{{PML_NS}}}{tag}"


def normalize_interactive_sequence_mode(value: object) -> str:
    mode = "standard" if value is None else str(value).strip().lower()
    if mode not in {"standard", "wps"}:
        raise ValueError(
            "interactive_sequence_mode must be 'standard' or 'wps': "
            f"{value!r}"
        )
    return mode


def rewrite_interactive_sequences_for_wps(timing_xml: str) -> str:
    """Merge same-trigger interactiveSeq containers into one WPS-safe chain."""
    if "interactiveSeq" not in timing_xml:
        return timing_xml
    wrapper = ET.fromstring(
        f'<root xmlns:p="{PML_NS}">{timing_xml}</root>'
    )
    timing = next(iter(wrapper), None)
    if timing is None:
        return timing_xml
    tm_root = next(
        (
            node for node in timing.iter(_q("cTn"))
            if node.get("nodeType") == "tmRoot"
        ),
        None,
    )
    if tm_root is None:
        return timing_xml
    child_list = tm_root.find(_q("childTnLst"))
    if child_list is None:
        return timing_xml

    first_by_trigger: dict[str, ET.Element] = {}
    for seq in list(child_list):
        if seq.tag != _q("seq"):
            continue
        ctn = seq.find(_q("cTn"))
        if ctn is None or ctn.get("nodeType") != "interactiveSeq":
            continue
        trigger = ctn.find(f"./{_q('stCondLst')}//{_q('spTgt')}")
        trigger_id = trigger.get("spid") if trigger is not None else None
        if not trigger_id:
            continue
        first = first_by_trigger.get(trigger_id)
        if first is None:
            first_by_trigger[trigger_id] = seq
            continue
        first_ctn = first.find(_q("cTn"))
        first_children = (
            first_ctn.find(_q("childTnLst")) if first_ctn is not None else None
        )
        other_children = ctn.find(_q("childTnLst"))
        if first_children is None or other_children is None:
            continue
        for child in list(other_children):
            first_children.append(child)
        child_list.remove(seq)

    rendered = ET.tostring(timing, encoding="unicode")
    # The surrounding slide already declares p; keep the fragment compact.
    rendered = rendered.replace(f' xmlns:p="{PML_NS}"', "")
    return rendered
''', encoding="utf-8")

# 3) Builder: resolve per-slide mode, serialize through the WPS overlay, and
# validate against the same logical sidecar rows.
builder = ROOT / "skills/ppt-master/scripts/svg_to_pptx/pptx_package/builder.py"
replace_once(
    builder,
    "from ..semantic_markers import (\n    chrome_token_from_markers,\n    page_layout_name_from_svg,\n)\n",
    "from ..semantic_markers import (\n    chrome_token_from_markers,\n    page_layout_name_from_svg,\n)\nfrom ..wps_compat import (\n    normalize_interactive_sequence_mode,\n    rewrite_interactive_sequences_for_wps,\n)\n",
)
replace_once(
    builder,
    "                        timing_xml = '\\n' + create_sequence_timing_xml(\n                            seq_targets, duration=slide_animation_duration,\n                            trigger=slide_animation_trigger,\n                        )\n",
    "                        interactive_sequence_mode = normalize_interactive_sequence_mode(\n                            slide_animation_cfg.get('interactive_sequence_mode', 'standard')\n                        )\n                        timing_body = create_sequence_timing_xml(\n                            seq_targets, duration=slide_animation_duration,\n                            trigger=slide_animation_trigger,\n                        )\n                        if interactive_sequence_mode == 'wps':\n                            timing_body = rewrite_interactive_sequences_for_wps(timing_body)\n                        timing_xml = '\\n' + timing_body\n",
)
replace_once(
    builder,
    "                            trigger=expected_animation_trigger,\n                        )\n",
    "                            trigger=expected_animation_trigger,\n                            interactive_sequence_mode=interactive_sequence_mode,\n                        )\n",
)

# 4) Core read-back validator: accept either the canonical one-row-per-sequence
# layout or the WPS one-sequence-per-trigger layout, and compare rows in the
# serialized grouping order when WPS mode is selected.
anim = ROOT / "skills/ppt-master/scripts/pptx_animations.py"
replace_once(
    anim,
    "        if len(interactive_sequences) != len(interactive_rows):\n            errors.append(\n                'each generated trigger-shape animation must have one '\n                'interactiveSeq time node'\n            )\n",
    "        valid_interactive_counts = {len(interactive_rows)}\n        if interactive_rows:\n            valid_interactive_counts.add(\n                len({row.trigger_shape_id for row in interactive_rows})\n            )\n        if len(interactive_sequences) not in valid_interactive_counts:\n            errors.append(\n                'generated trigger-shape animations must use either one '\n                'interactiveSeq per row or one per trigger shape'\n            )\n",
)
replace_once(
    anim,
    "def validate_generated_animation_xml(\n    slide_xml: str | bytes,\n    targets: Sequence[Sequence[object] | Mapping[str, object]],\n    *,\n    duration: float = 0.3,\n    trigger: str = 'after-previous',\n) -> AnimationSequenceSummary:\n",
    "def validate_generated_animation_xml(\n    slide_xml: str | bytes,\n    targets: Sequence[Sequence[object] | Mapping[str, object]],\n    *,\n    duration: float = 0.3,\n    trigger: str = 'after-previous',\n    interactive_sequence_mode: str = 'standard',\n) -> AnimationSequenceSummary:\n",
)
replace_once(
    anim,
    "    trigger = normalize_animation_trigger(trigger)\n    default_duration_ms = _seconds_to_ms(\n",
    "    trigger = normalize_animation_trigger(trigger)\n    if interactive_sequence_mode not in {'standard', 'wps'}:\n        raise ValueError(\n            'interactive_sequence_mode must be standard or wps: '\n            f'{interactive_sequence_mode!r}'\n        )\n    default_duration_ms = _seconds_to_ms(\n",
)
old_expected = """    expected = tuple(\n        target\n        for target in normalized_expected\n        if target.trigger_shape_id is None\n    ) + tuple(\n        target\n        for target in normalized_expected\n        if target.trigger_shape_id is not None\n    )\n"""
new_expected = """    expected_main = tuple(\n        target\n        for target in normalized_expected\n        if target.trigger_shape_id is None\n    )\n    expected_interactive = [\n        target\n        for target in normalized_expected\n        if target.trigger_shape_id is not None\n    ]\n    if interactive_sequence_mode == 'wps':\n        grouped: dict[int, list[AnimationTarget]] = {}\n        for target in expected_interactive:\n            grouped.setdefault(int(target.trigger_shape_id), []).append(target)\n        expected_interactive = [\n            target\n            for rows in grouped.values()\n            for target in rows\n        ]\n    expected = expected_main + tuple(expected_interactive)\n"""
replace_once(anim, old_expected, new_expected)

# 5) Target only the actual code-demo pages discovered from run-* triggers.
project = ROOT / "projects/Python应用课_第06课_阶段测评与复盘_阳光积木实验室_20260905_ppt169_20260905"
animations_path = project / "animations.json"
data = json.loads(animations_path.read_text(encoding="utf-8"))
affected: list[str] = []
for slide, slide_cfg in data.get("slides", {}).items():
    has_run_trigger = False
    for group_cfg in (slide_cfg.get("groups", {}) or {}).values():
        if not isinstance(group_cfg, dict):
            continue
        rows = group_cfg.get("effects")
        if rows is None and group_cfg.get("effect"):
            rows = [group_cfg]
        for row in rows or []:
            if isinstance(row, dict) and str(row.get("trigger_shape", "")).startswith("run-"):
                has_run_trigger = True
                break
        if has_run_trigger:
            break
    if has_run_trigger:
        slide_cfg.setdefault("animation", {})["interactive_sequence_mode"] = "wps"
        affected.append(slide)
animations_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
expected = {
    "16_海龟显隐实验站",
    "18_窗口标题实验站",
    "20_练习A_六片花瓣",
    "21_花瓣颜色实验站",
    "28_练习B_花心和花茎",
    "29_花茎长度实验站",
    "32_小红花作品实验站",
}
if set(affected) != expected:
    raise RuntimeError(f"unexpected affected slides: {affected!r}")
print("Patched WPS interactive sequence mode for:", ", ".join(affected))
