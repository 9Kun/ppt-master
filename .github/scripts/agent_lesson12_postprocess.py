from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

PROJECT = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
SVG_DIR = PROJECT / 'svg_output'
SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)

# 1) Normalize WPS animation syntax to the already-verified reference project pattern:
#    trigger_shape means the click trigger; do not redundantly set trigger on that row.
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

# 2) SVG root-group normalization. Static anonymous helpers become explicit static decoration
#    atoms, while footer gets a stable geometry box.
for svg_path in sorted(SVG_DIR.glob('*.svg')):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    auto = 0
    for child in list(root):
        tag = child.tag.rsplit('}', 1)[-1]
        if tag != 'g':
            continue
        gid = child.get('id')
        if not gid:
            auto += 1
            child.set('id', f'static-helper-{auto:02d}')
            child.set('data-pptx-role', 'decoration')
        elif gid.startswith('footer-'):
            child.set('data-pptx-bounds', '48 674 1184 30')
            child.set('data-pptx-role', 'footer')
    tree.write(svg_path, encoding='utf-8', xml_declaration=False)

# 3) Fix the few known density/overflow cases without changing lesson content.
# P26: compact 20-line code block.
p26 = SVG_DIR / '26_三次口令门代码拆解.svg'
s = p26.read_text(encoding='utf-8')
# Reduce only code-card text font and vertical spacing by mapping authored y positions.
ys = [244 + i * 34 for i in range(20)]
new_ys = [218 + i * 21 for i in range(20)]
for old, new in zip(ys, new_ys):
    s = s.replace(f'y="{old}" font-family="Consolas, Courier New, monospace" font-size="18"',
                  f'y="{new}" font-family="Consolas, Courier New, monospace" font-size="15"')
p26.write_text(s, encoding='utf-8')

# P27: compact all code state rows to fit editor pane.
p27 = SVG_DIR / '27_三次口令门_运行验证.svg'
s = p27.read_text(encoding='utf-8')
for old_i in range(0, 18):
    old_y = 326 + old_i * 30
    new_y = 316 + old_i * 19
    s = s.replace(f'y="{old_y}" font-family="Consolas, Microsoft YaHei, monospace" font-size="17"',
                  f'y="{new_y}" font-family="Consolas, Microsoft YaHei, monospace" font-size="14"')
p27.write_text(s, encoding='utf-8')

# P31: shorten the single line that exceeded its card while preserving meaning.
p31 = SVG_DIR / '31_常见问题与处理.svg'
s = p31.read_text(encoding='utf-8').replace('先停止运行，再检查 tries/count 是否变化', '先停止，再检查计数是否变化')
p31.write_text(s, encoding='utf-8')

# 4) Add named typography roles required by the current official SVG gate.
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

print('postprocess complete')
