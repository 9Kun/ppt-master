from __future__ import annotations

import json
from pathlib import Path
from xml.etree import ElementTree as ET

P = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
cfg = json.loads((P / 'animations.json').read_text(encoding='utf-8'))
required = ['16_练习A_数到3停', '23_练习B_答对就break', '27_三次口令门_运行验证']
errors: list[str] = []

for stem in required:
    slide_cfg = cfg.get('slides', {}).get(stem, {})
    if slide_cfg.get('interactive_sequence_mode') != 'wps':
        errors.append(f'{stem}: interactive_sequence_mode != wps')

    root = ET.parse(P / 'svg_output' / f'{stem}.svg').getroot()
    direct = [el for el in list(root) if el.get('id')]
    byid = {el.get('id'): el for el in direct}
    zorder = {el.get('id'): i for i, el in enumerate(direct)}
    groups = slide_cfg.get('groups', {})
    triggers: set[str] = set()

    for gid, raw in groups.items():
        entries = raw.get('effects', []) if isinstance(raw, dict) and 'effects' in raw else [raw]
        for effect in entries:
            if not isinstance(effect, dict):
                continue
            trigger = effect.get('trigger_shape')
            if not trigger:
                continue
            triggers.add(str(trigger))
            if effect.get('restart') != 'always':
                errors.append(f'{stem}/{gid}: trigger animation restart != always')

    for trigger in triggers:
        group = byid.get(trigger)
        if group is None:
            errors.append(f'{stem}: {trigger} is not a direct-root trigger group')
            continue
        rect = next((el for el in group.iter() if el.tag.endswith('rect')), None)
        if rect is None or rect.get('fill') != '#FFFFFF' or rect.get('fill-opacity') != '0.001':
            errors.append(f'{stem}/{trigger}: hit region must use #FFFFFF / 0.001')

    task_count = 3 if stem.startswith('27_') else 2
    for i in range(1, task_count + 1):
        button = f'task-{i}-button'
        hit = f'task-{i}-hit'
        if zorder.get(hit, -1) <= zorder.get(button, -1):
            errors.append(f'{stem}: {hit} must be above {button}')

    output_ids = [gid for gid in groups if gid.startswith('out-')]
    if not output_ids:
        errors.append(f'{stem}: no progressive output groups')
    for gid in output_ids:
        entries = groups[gid].get('effects', []) if isinstance(groups[gid], dict) else []
        if not any(
            isinstance(effect, dict)
            and str(effect.get('effect', '')).startswith('entrance_')
            and str(effect.get('trigger_shape', '')).startswith('run-')
            for effect in entries
        ):
            errors.append(f'{stem}/{gid}: output is not run-triggered')

    # Task 1 must run in both states: immediately on page entry and after selecting task 1.
    for gid in [name for name in groups if name.startswith('out-1-')]:
        entrances = {
            effect.get('trigger_shape')
            for effect in groups[gid].get('effects', [])
            if isinstance(effect, dict) and str(effect.get('effect', '')).startswith('entrance_')
        }
        if not {'run-initial-hit', 'run-task-1-hit'} <= entrances:
            errors.append(f'{stem}/{gid}: missing initial/selected task-1 run trigger')

    # Switching tasks must clear stale running/done states.
    for status in ('status-running', 'status-done'):
        entries = groups.get(status, {}).get('effects', [])
        for i in range(1, task_count + 1):
            if not any(
                isinstance(effect, dict)
                and effect.get('effect') == 'exit_appear'
                and effect.get('trigger_shape') == f'task-{i}-hit'
                for effect in entries
            ):
                errors.append(f'{stem}/{status}: not reset by task-{i}-hit')

    # Completion must occur after the final output entrance on each run trigger.
    done_entries = groups.get('status-done', {}).get('effects', [])
    for run_trigger in sorted(t for t in triggers if t.startswith('run-')):
        done_delays = [
            float(effect.get('delay', 0) or 0)
            for effect in done_entries
            if isinstance(effect, dict)
            and effect.get('trigger_shape') == run_trigger
            and str(effect.get('effect', '')).startswith('entrance_')
        ]
        output_delays = []
        for gid in output_ids:
            for effect in groups[gid].get('effects', []):
                if (
                    isinstance(effect, dict)
                    and effect.get('trigger_shape') == run_trigger
                    and str(effect.get('effect', '')).startswith('entrance_')
                ):
                    output_delays.append(float(effect.get('delay', 0) or 0))
        if output_delays and (not done_delays or min(done_delays) <= max(output_delays)):
            errors.append(f'{stem}/{run_trigger}: completion appears before output finishes')

report = P / 'validation' / 'wps_interaction_gate.txt'
report.parent.mkdir(parents=True, exist_ok=True)
if errors:
    report.write_text('\n'.join('ERROR ' + item for item in errors), encoding='utf-8')
    raise SystemExit('\n'.join(errors))

message = (
    'PASS: WPS mode, direct-root 0.001 hit regions, trigger z-order, restart=always, '
    'task-1 dual run path, stale-state reset, progressive output and completion ordering validated.'
)
report.write_text(message + '\n', encoding='utf-8')
print(message)
