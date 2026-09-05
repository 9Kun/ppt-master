from __future__ import annotations

import json
from pathlib import Path
from xml.etree import ElementTree as ET

PROJECT = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
SVG_DIR = PROJECT / 'svg_output'
SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)

# 1) Normalize trigger rows to the syntax already used by the verified WPS reference project.
anim_path = PROJECT / 'animations.json'
data = json.loads(anim_path.read_text(encoding='utf-8'))
for slide_cfg in data.get('slides', {}).values():
    groups = slide_cfg.get('groups', {}) if isinstance(slide_cfg, dict) else {}
    for group_cfg in groups.values():
        entries = group_cfg.get('effects', []) if isinstance(group_cfg, dict) and 'effects' in group_cfg else [group_cfg]
        for e in entries:
            if isinstance(e, dict) and e.get('trigger_shape'):
                e.pop('trigger', None)
anim_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

# 2) Normalize root structure. Anonymous helper groups are unwrapped back to static root
#    primitives, matching the pipeline rule for framing/decorative atoms. Each promoted
#    primitive gets a stable id because data-pptx-role requires one in the current gate.
for svg_path in sorted(SVG_DIR.glob('*.svg')):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    helper_serial = 0
    for child in list(root):
        tag = child.tag.rsplit('}', 1)[-1]
        if tag != 'g':
            continue
        gid = child.get('id')
        if not gid:
            helper_serial += 1
            idx = list(root).index(child)
            kids = list(child)
            root.remove(child)
            for offset, kid in enumerate(kids, 1):
                kid_tag = kid.tag.rsplit('}', 1)[-1]
                if not kid.get('id'):
                    kid.set('id', f'static-decoration-{helper_serial:02d}-{offset:02d}-{kid_tag}')
                kid.set('data-pptx-role', 'decoration')
                root.insert(idx + offset - 1, kid)
        elif gid.startswith('footer-'):
            child.set('data-pptx-bounds', '48 674 1184 30')
            child.set('data-pptx-role', 'footer')
    # Mark full-page atmosphere images as decoration so they are not treated as loose content.
    for child in list(root):
        tag = child.tag.rsplit('}', 1)[-1]
        if tag == 'image' and child.get('id') in {'route-bg', 'chapter-bg'}:
            child.set('data-pptx-role', 'decoration')
    tree.write(svg_path, encoding='utf-8', xml_declaration=False)

# 3) Legacy density patches retained for reproducibility. The semantic repair pass below
#    rebuilds P27 and restores P26 to projection-readable code sizes, so these are no
#    longer the final authored state.
p26 = SVG_DIR / '26_三次口令门代码拆解.svg'
s = p26.read_text(encoding='utf-8')
for i in range(20):
    old_y = 228 + i * 34
    new_y = 202 + i * 21
    s = s.replace(
        f'y="{old_y}" font-family="Consolas, Courier New, monospace" font-size="18"',
        f'y="{new_y}" font-family="Consolas, Courier New, monospace" font-size="15"',
    )
p26.write_text(s, encoding='utf-8')

p27 = SVG_DIR / '27_三次口令门_运行验证.svg'
s = p27.read_text(encoding='utf-8')
for i in range(18):
    old_y = 326 + i * 30
    new_y = 316 + i * 19
    s = s.replace(
        f'y="{old_y}" font-family="Consolas, Microsoft YaHei, monospace" font-size="17"',
        f'y="{new_y}" font-family="Consolas, Microsoft YaHei, monospace" font-size="14"',
    )
p27.write_text(s, encoding='utf-8')

p31 = SVG_DIR / '31_常见问题与处理.svg'
s = p31.read_text(encoding='utf-8').replace('先停止运行，再检查 tries/count 是否变化', '先停止，再检查计数是否变化')
p31.write_text(s, encoding='utf-8')

# 4) Named typography roles required by the current official SVG gate.
lock_path = PROJECT / 'spec_lock.md'
lock = lock_path.read_text(encoding='utf-8')
needle = '- footer: 14\n'
if '- chapter_number: 180' not in lock:
    lock = lock.replace(needle, needle + '- chapter_number: 180\n- section_title: 56\n- counter_display: 70\n')
lock_path.write_text(lock, encoding='utf-8')

design_path = PROJECT / 'design_spec.md'
design = design_path.read_text(encoding='utf-8')
needle2 = '| Footer | 14 |\n'
if '| Chapter number | 180 |' not in design:
    design = design.replace(needle2, needle2 + '| Chapter number | 180 |\n| Section title | 56 |\n| Counter display | 70 |\n')
design_path.write_text(design, encoding='utf-8')

# 5) Final semantic/interaction repair pass. This is intentionally last: it owns the
#    final authored state for reveal z-order, quiz answer coloring, P10-style consoles,
#    P26/P27 readability, output sequencing, and content/interaction invariants.
from agent_lesson12_repair import main as repair_lesson12
repair_lesson12()

print('postprocess + semantic repair complete')
