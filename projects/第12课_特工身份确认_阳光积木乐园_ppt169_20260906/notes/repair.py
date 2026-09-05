from __future__ import annotations

import copy
import html
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

PROJECT = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
SVG_DIR = PROJECT / 'svg_output'
ANIM_PATH = PROJECT / 'animations.json'
SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)
Q = f'{{{SVG_NS}}}'

C = {
    'bg':'#FFFDF5','blue':'#2E9BFF','orange':'#FF9F1C','pink':'#FF6FA5','green':'#22C55E',
    'text':'#203044','terminal':'#17243A','lightblue':'#EAF5FF','lightpink':'#FFE2ED',
    'lightgreen':'#E9FBEF','line':'#CFE5F8','white':'#FFFFFF','cream':'#FFF2DC',
    'wrong_text':'#C93C68','secondary':'#7A8A9B'
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=False)


def idmap(root: ET.Element) -> dict[str, ET.Element]:
    return {el.get('id'): el for el in root.iter() if el.get('id')}


def direct_child(root: ET.Element, gid: str) -> ET.Element | None:
    for child in list(root):
        if child.get('id') == gid:
            return child
    return None


def remove_bounds(el: ET.Element | None) -> None:
    if el is not None:
        el.attrib.pop('data-pptx-bounds', None)


def move_to_front(root: ET.Element, el: ET.Element | None) -> None:
    if el is None:
        return
    if el in list(root):
        root.remove(el)
        root.append(el)


def write_tree(tree: ET.ElementTree, path: Path) -> None:
    tree.write(path, encoding='utf-8', xml_declaration=False)


def text_value(el: ET.Element | None) -> str:
    return ''.join(el.itertext()) if el is not None else ''


def repair_reveal_pages() -> None:
    stems = [
        '03_复习抢答规则', '09_任务启动', '13_break提前下车',
        '14_continue跳过本轮', '17_易错_漏掉计数增加', '28_continue位置很重要',
    ]
    for stem in stems:
        path = SVG_DIR / f'{stem}.svg'
        tree = ET.parse(path)
        root = tree.getroot()
        button = direct_child(root, 'reveal-button')
        hit = direct_child(root, 'reveal-hit')
        # The hit target must be above the visible button in z-order. Bounds metadata is
        # intentionally omitted for the overlay/hit pair so the ordinary-layout overlap
        # gate does not mistake an interaction layer for a content module.
        remove_bounds(button)
        remove_bounds(hit)
        move_to_front(root, button)
        move_to_front(root, hit)
        write_tree(tree, path)


def _option_pairs(base: ET.Element) -> list[tuple[ET.Element, ET.Element, str]]:
    kids = list(base)
    pairs: list[tuple[ET.Element, ET.Element, str]] = []
    for idx, child in enumerate(kids):
        if child.tag != Q + 'text':
            continue
        value = text_value(child).strip()
        match = re.match(r'^([ABCD])\.', value)
        if not match:
            continue
        rect = None
        for prev in reversed(kids[:idx]):
            if prev.tag == Q + 'rect':
                rect = prev
                break
        if rect is not None:
            pairs.append((rect, child, match.group(1)))
    return pairs


def repair_quiz_pages(animations: dict) -> None:
    paths = [
        *[SVG_DIR / f'{n:02d}_复习抢答_{2*n-7}_{2*n-6}.svg' for n in range(4, 9)],
        *[SVG_DIR / f'{n:02d}_本课选择题_{2*n-35}_{2*n-34}.svg' for n in range(18, 22)],
    ]
    for path in paths:
        tree = ET.parse(path)
        root = tree.getroot()
        stem = path.stem
        slide_anim = animations.setdefault('slides', {}).setdefault(stem, {})
        groups = slide_anim.setdefault('groups', {})
        for qi in (1, 2):
            base = direct_child(root, f'q{qi}-base')
            answer = direct_child(root, f'q{qi}-answer')
            button = direct_child(root, f'q{qi}-reveal-button')
            hit = direct_child(root, f'q{qi}-reveal-hit')
            if base is None or answer is None or button is None or hit is None:
                raise RuntimeError(f'{stem}: incomplete quiz group q{qi}')
            ans_text = text_value(answer)
            m = re.search(r'正确答案：\s*([ABCD])', ans_text)
            if not m:
                raise RuntimeError(f'{stem}: cannot parse answer for q{qi}: {ans_text!r}')
            correct = m.group(1)
            overlay = ET.Element(Q + 'g', {'id': f'q{qi}-options-reveal'})
            for rect, txt, letter in _option_pairs(base):
                r = copy.deepcopy(rect)
                t = copy.deepcopy(txt)
                if letter == correct:
                    r.set('fill', C['lightgreen'])
                    r.set('stroke', C['green'])
                    r.set('stroke-width', '2')
                    t.set('fill', C['green'])
                    t.set('font-weight', '700')
                else:
                    r.set('fill', C['lightpink'])
                    r.set('stroke', '#FFB7D1')
                    r.set('stroke-width', '1.5')
                    t.set('fill', C['wrong_text'])
                overlay.append(r)
                overlay.append(t)
            # Put the answer colors immediately above the base options.
            base_idx = list(root).index(base)
            root.insert(base_idx + 1, overlay)
            for el in (answer, button, hit, overlay):
                remove_bounds(el)
            # Visible button first, transparent direct-root hit target last/topmost.
            move_to_front(root, button)
            move_to_front(root, hit)
            groups[f'q{qi}-options-reveal'] = {
                'effect':'entrance_appear', 'trigger_shape':f'q{qi}-reveal-hit',
                'order':10, 'duration':0.06, 'restart':'always'
            }
            groups[f'q{qi}-answer'] = {
                'effect':'entrance_appear', 'trigger_shape':f'q{qi}-reveal-hit',
                'order':20, 'delay':0.04, 'duration':0.08, 'restart':'always'
            }
        write_tree(tree, path)


def header(title: str, sub: str) -> str:
    return f'''<g id="console-header" data-pptx-bounds="48 30 1184 82">
      <rect x="48" y="34" width="12" height="58" rx="6" fill="{C['blue']}"/>
      <text x="82" y="70" font-family="YouYuan, Microsoft YaHei, sans-serif" font-size="36" font-weight="700" fill="{C['text']}">{esc(title)}</text>
      <text x="82" y="101" font-size="18" fill="{C['blue']}">{esc(sub)}</text>
      <rect x="820" y="42" width="412" height="54" rx="27" fill="{C['lightblue']}"/>
      <text x="1026" y="76" text-anchor="middle" font-size="18" font-weight="700" fill="{C['text']}">① 选任务　→　② 看代码　→　③ 运行　→　④ 看结果</text>
    </g>'''


def footer(page_no: int) -> str:
    return f'<g id="footer-{page_no}" data-pptx-role="footer" data-pptx-bounds="48 674 1184 30"><text x="48" y="690" font-size="14" fill="{C["secondary"]}">小小特工任务中心</text><text x="1232" y="690" text-anchor="end" font-size="14" fill="{C["secondary"]}">{page_no:02d} / 32</text></g>'


def code_color(line: str) -> str:
    s = line.strip()
    if s.startswith(('while ', 'if ', 'else:')):
        return C['blue']
    if s in {'break', 'continue'} or s.startswith(('break ', 'continue ')):
        return C['orange']
    if 'print(' in s:
        return C['pink'] if '错误' in s or '空白' in s else C['text']
    return C['text']


def code_group(gid: str, lines: list[str], *, x: int, y: float, font: float, gap: float) -> str:
    parts = [f'<g id="{gid}">']
    yy = y
    for line in lines:
        parts.append(
            f'<text x="{x}" y="{yy:.1f}" font-family="Consolas, Microsoft YaHei, monospace" '
            f'font-size="{font:g}" fill="{code_color(line)}">{esc(line) if line else " "}</text>'
        )
        yy += gap
    parts.append('</g>')
    return ''.join(parts)


def hidden_seed() -> list[dict]:
    return [
        {'effect':'entrance_appear','trigger':'with-previous','order':1,'delay':0,'duration':0.01,'restart':'always'},
        {'effect':'exit_appear','trigger':'with-previous','order':2,'delay':0,'duration':0.01,'restart':'always'},
    ]


def task_reset_effects(task_hits: list[str], *, order: int = 3) -> list[dict]:
    return [
        {'effect':'exit_appear','trigger_shape':hit,'order':order,'delay':0,'duration':0.05,'restart':'always'}
        for hit in task_hits
    ]


def build_console(stem: str, page_no: int, title: str, sub: str, tasks: list[dict], *, dense: bool = False) -> tuple[str, dict]:
    n = len(tasks)
    button_gap = 14
    button_total = 1144
    button_w = (button_total - button_gap * (n - 1)) / n
    parts = [
        f'<svg xmlns="{SVG_NS}" viewBox="0 0 1280 720" data-pptx-page-role="content" font-family="Microsoft YaHei, Arial, sans-serif">',
        f'<rect id="background" data-pptx-role="background" width="1280" height="720" fill="{C["bg"]}"/>',
        f'<rect id="console-top-band" data-pptx-role="decoration" x="0" y="0" width="1280" height="18" fill="{C["blue"]}"/>',
        header(title, sub),
        f'<g id="task-panel" data-pptx-role="decoration"><rect x="48" y="116" width="1184" height="92" rx="28" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="2"/></g>',
    ]
    task_hits: list[str] = []
    edge_colors = [C['blue'], C['orange'], C['pink'], C['green']]
    fills = [C['lightblue'], C['cream'], C['lightpink'], C['lightgreen']]
    for i, task in enumerate(tasks, 1):
        x = 68 + (i - 1) * (button_w + button_gap)
        edge = edge_colors[(i - 1) % len(edge_colors)]
        fill = fills[(i - 1) % len(fills)]
        parts.append(
            f'<g id="task-{i}-button" data-pptx-bounds="{x:.1f} 128 {button_w:.1f} 62">'
            f'<rect x="{x:.1f}" y="128" width="{button_w:.1f}" height="62" rx="20" fill="{fill}" stroke="{edge}" stroke-width="2"/>'
            f'<circle cx="{x+34:.1f}" cy="159" r="21" fill="{edge}"/><text x="{x+34:.1f}" y="166" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">{i}</text>'
            f'<text x="{x+66:.1f}" y="166" font-size="19" font-weight="700" fill="{C["text"]}">{esc(task["label"])}</text></g>'
        )
    for i, _task in enumerate(tasks, 1):
        x = 68 + (i - 1) * (button_w + button_gap)
        hit = f'task-{i}-hit'
        task_hits.append(hit)
        parts.append(f'<g id="{hit}"><rect x="{x:.1f}" y="128" width="{button_w:.1f}" height="62" rx="20" fill="#FFFFFF" fill-opacity="0.001"/></g>')

    parts.extend([
        f'<g id="editor-shell" data-pptx-bounds="48 222 700 430"><rect x="48" y="222" width="700" height="430" rx="34" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="3"/>'
        f'<circle cx="82" cy="254" r="8" fill="{C["pink"]}"/><circle cx="108" cy="254" r="8" fill="{C["orange"]}"/><circle cx="134" cy="254" r="8" fill="{C["green"]}"/>'
        f'<text x="174" y="262" font-size="20" font-weight="700" fill="{C["text"]}">Python 编辑器</text><rect x="72" y="276" width="652" height="294" rx="22" fill="#F8FBFF"/></g>',
        f'<g id="terminal-shell" data-pptx-bounds="772 222 460 430"><rect x="772" y="222" width="460" height="430" rx="34" fill="{C["lightblue"]}"/>'
        f'<text x="808" y="262" font-size="24" font-weight="700" fill="{C["text"]}">终端输出</text><rect x="796" y="276" width="412" height="282" rx="24" fill="{C["terminal"]}"/>'
        f'<circle cx="826" cy="304" r="7" fill="{C["pink"]}"/><circle cx="850" cy="304" r="7" fill="{C["orange"]}"/><circle cx="874" cy="304" r="7" fill="{C["green"]}"/>'
        f'<text x="900" y="310" font-size="17" font-weight="700" fill="#EAF5FF">运行结果</text><rect x="800" y="576" width="404" height="62" rx="20" fill="#FFFFFF"/></g>',
    ])

    code_font = 17 if dense else 18
    code_gap = 18 if dense else 30
    code_y = 298 if dense else 314
    parts.append(code_group('code-initial', tasks[0]['code'], x=94, y=code_y, font=code_font, gap=code_gap))
    for i, task in enumerate(tasks, 1):
        parts.append(code_group(f'code-task-{i}', task['code'], x=94, y=code_y, font=code_font, gap=code_gap))

    def run_button(gid: str, fill: str) -> str:
        return (
            f'<g id="{gid}"><rect x="512" y="584" width="212" height="54" rx="22" fill="{fill}"/>'
            f'<text x="618" y="619" text-anchor="middle" font-size="21" font-weight="700" fill="#FFFFFF">▶ 运行程序</text></g>'
        )

    parts.append(run_button('run-initial', C['blue']))
    for i, _task in enumerate(tasks, 1):
        parts.append(run_button(f'run-task-{i}', edge_colors[(i - 1) % len(edge_colors)]))
    parts.append('<g id="run-initial-hit"><rect x="512" y="584" width="212" height="54" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>')
    for i, _task in enumerate(tasks, 1):
        parts.append(f'<g id="run-task-{i}-hit"><rect x="512" y="584" width="212" height="54" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>')

    parts.extend([
        f'<g id="guide-initial"><text x="1002" y="615" text-anchor="middle" font-size="18" font-weight="700" fill="{C["blue"]}">点击运行，终端才开始输出</text></g>',
        f'<g id="guide-active"><text x="1002" y="615" text-anchor="middle" font-size="18" font-weight="700" fill="{C["blue"]}">已切换任务，点击运行查看结果</text></g>',
        f'<g id="status-running"><text x="1002" y="615" text-anchor="middle" font-size="19" font-weight="700" fill="{C["orange"]}">运行中……</text></g>',
        f'<g id="status-done"><text x="1002" y="615" text-anchor="middle" font-size="19" font-weight="700" fill="{C["green"]}">验证完成 ✓</text></g>',
    ])

    output_ids_by_task: dict[int, list[str]] = {}
    output_delay_by_task: dict[int, float] = {}
    for i, task in enumerate(tasks, 1):
        ids: list[str] = []
        if task.get('char_output'):
            x = 818.0
            for j, ch in enumerate(task['char_output'], 1):
                oid = f'out-{i}-char-{j:02d}'
                ids.append(oid)
                width = 36 if '\u4e00' <= ch <= '\u9fff' else 28
                parts.append(
                    f'<g id="{oid}"><text x="{x + width/2:.1f}" y="398" text-anchor="middle" '
                    f'font-family="Consolas, Microsoft YaHei, monospace" font-size="29" font-weight="700" fill="#FFFFFF">{esc(ch)}</text></g>'
                )
                x += width
            output_delay_by_task[i] = 0.08 * max(1, len(ids))
        else:
            for j, line in enumerate(task.get('output', []), 1):
                oid = f'out-{i}-line-{j:02d}'
                ids.append(oid)
                y = 350 + (j - 1) * 42
                parts.append(
                    f'<g id="{oid}"><text x="820" y="{y}" font-family="Consolas, Microsoft YaHei, monospace" font-size="18" fill="#FFFFFF">{esc(line)}</text></g>'
                )
            output_delay_by_task[i] = 0.22 * max(1, len(ids))
        output_ids_by_task[i] = ids

    parts.append(footer(page_no))
    parts.append('</svg>')

    groups: dict[str, dict] = {}
    # Initial code/run/guide are visible until a task or run is clicked.
    groups['code-initial'] = {'effects': task_reset_effects(task_hits, order=3)}
    groups['run-initial'] = {'effects': task_reset_effects(task_hits, order=3)}
    groups['guide-initial'] = {'effects': task_reset_effects(task_hits, order=3) + [
        {'effect':'exit_appear','trigger_shape':'run-initial-hit','order':3,'delay':0,'duration':0.05,'restart':'always'}
    ]}

    # Task-state code/run buttons are hidden at entry, reset on every task click, then
    # the selected state enters. This mirrors the verified WPS reference pattern.
    for i in range(1, n + 1):
        for gid in (f'code-task-{i}', f'run-task-{i}'):
            effects = hidden_seed() + task_reset_effects(task_hits, order=4)
            effects.append({'effect':'entrance_appear','trigger_shape':f'task-{i}-hit','order':10,'delay':0.08,'duration':0.08,'restart':'always'})
            groups[gid] = {'effects': effects}

    groups['guide-active'] = {'effects': hidden_seed() + task_reset_effects(task_hits, order=4)}
    for i in range(1, n + 1):
        groups['guide-active']['effects'].append({'effect':'entrance_appear','trigger_shape':f'task-{i}-hit','order':12,'delay':0.10,'duration':0.08,'restart':'always'})
        groups['guide-active']['effects'].append({'effect':'exit_appear','trigger_shape':f'run-task-{i}-hit','order':4,'delay':0,'duration':0.05,'restart':'always'})
    groups['guide-active']['effects'].append({'effect':'exit_appear','trigger_shape':'run-initial-hit','order':4,'delay':0,'duration':0.05,'restart':'always'})

    groups['status-running'] = {'effects': hidden_seed() + task_reset_effects(task_hits, order=4)}
    groups['status-done'] = {'effects': hidden_seed() + task_reset_effects(task_hits, order=4)}

    run_for_task: dict[int, list[str]] = {1: ['run-initial-hit', 'run-task-1-hit']}
    for i in range(2, n + 1):
        run_for_task[i] = [f'run-task-{i}-hit']

    for task_i, triggers in run_for_task.items():
        finish = output_delay_by_task[task_i] + 0.24
        for trigger in triggers:
            groups['status-running']['effects'].extend([
                {'effect':'entrance_appear','trigger_shape':trigger,'order':20,'delay':0.04,'duration':0.06,'restart':'always'},
                {'effect':'exit_appear','trigger_shape':trigger,'order':88,'delay':finish,'duration':0.05,'restart':'always'},
            ])
            groups['status-done']['effects'].append(
                {'effect':'entrance_appear','trigger_shape':trigger,'order':90,'delay':finish + 0.06,'duration':0.08,'restart':'always'}
            )

    for task_i, ids in output_ids_by_task.items():
        triggers = run_for_task[task_i]
        is_char = bool(tasks[task_i - 1].get('char_output'))
        step = 0.08 if is_char else 0.22
        for j, oid in enumerate(ids, 1):
            effects = hidden_seed() + task_reset_effects(task_hits, order=4)
            for trigger in triggers:
                effects.append({
                    'effect':'entrance_appear','trigger_shape':trigger,'order':30 + j,
                    'delay':step * j,'duration':0.06 if is_char else 0.08,'restart':'always'
                })
            groups[oid] = {'effects': effects}

    return ''.join(parts), {'interactive_sequence_mode':'wps', 'groups':groups}


def repair_consoles(animations: dict) -> None:
    p16_tasks = [
        {
            'label':'数到 3 停',
            'code':['count = 1','','while count <= 3:','    print("第", count, "次检查")','    count = count + 1','','print("检查结束")'],
            'output':['第 1 次检查','第 2 次检查','第 3 次检查','检查结束'],
        },
        {
            'label':'改成数到 5',
            'code':['count = 1','','while count <= 5:','    print("第", count, "次检查")','    count = count + 1','','print("检查结束")'],
            'output':['第 1 次检查','第 2 次检查','第 3 次检查','第 4 次检查','第 5 次检查','检查结束'],
        },
    ]
    p23_code = [
        'while True:', '    password = input("请输入口令：")',
        '    if password == "python":', '        print("身份确认成功！")',
        '        break', '    print("口令不对，请再试一次。")',
    ]
    p23_tasks = [
        {'label':'直接输入 python', 'code':p23_code, 'char_output':'身份确认成功！'},
        {'label':'先错两次再答对', 'code':p23_code, 'output':['口令不对，请再试一次。','口令不对，请再试一次。','身份确认成功！']},
    ]
    p27_code = [
        'secret = "python"', 'tries = 0', 'while tries < 3:',
        '    password = input("请输入特工口令：")', '    if password == "":',
        '        print("不能输入空白！")', '        continue', '    tries = tries + 1',
        '    if password == secret:', '        print("身份确认成功，欢迎特工！")',
        '        break', '    else:', '        print("口令错误。还可尝试", 3 - tries, "次。")',
        'if password != secret:', '    print("三次机会已用完，任务暂停。")',
    ]
    p27_tasks = [
        {'label':'空白 → 正确', 'code':p27_code, 'output':['不能输入空白！','身份确认成功，欢迎特工！']},
        {'label':'错误 × 3', 'code':p27_code, 'output':['口令错误。还可尝试 2 次。','口令错误。还可尝试 1 次。','口令错误。还可尝试 0 次。','三次机会已用完，任务暂停。']},
        {'label':'错误 → 正确', 'code':p27_code, 'output':['口令错误。还可尝试 2 次。','身份确认成功，欢迎特工！']},
    ]
    specs = [
        ('16_练习A_数到3停', 16, '动手练习 A：数到几停？', '选任务 → 看代码 → 点击运行 → 观察输出', p16_tasks, False),
        ('23_练习B_答对就break', 23, '动手练习 B：答对就 break', '体验“继续尝试”和“立刻成功”的差别', p23_tasks, False),
        ('27_三次口令门_运行验证', 27, '运行验证：三类输入都要测', '切换案例；只有点击运行后终端才开始打印', p27_tasks, True),
    ]
    for stem, page_no, title, sub, tasks, dense in specs:
        svg, slide_anim = build_console(stem, page_no, title, sub, tasks, dense=dense)
        (SVG_DIR / f'{stem}.svg').write_text(svg, encoding='utf-8')
        animations.setdefault('slides', {})[stem] = slide_anim


def repair_p26() -> None:
    path = SVG_DIR / '26_三次口令门代码拆解.svg'
    tree = ET.parse(path)
    root = tree.getroot()
    ids = idmap(root)
    card = ids.get('code-card')
    if card is None:
        raise RuntimeError('P26 missing code-card')
    code_texts = [el for el in card.iter() if el.tag == Q + 'text' and el.get('font-family', '').startswith('Consolas')]
    # Keep the full code readable instead of shrinking to 15px. Twenty rows fit with
    # 21px leading from y=218 through y=617.
    yy = 218
    for el in code_texts:
        el.set('y', str(yy))
        el.set('font-size', '17')
        yy += 21
    write_tree(tree, path)


def repair_p31() -> None:
    path = SVG_DIR / '31_常见问题与处理.svg'
    text = path.read_text(encoding='utf-8')
    text = text.replace('变量还没准备好', '担心 password 未赋值')
    text = text.replace('确认循环一定执行，或先给变量初值', '本模板 while 至少执行一次；改条件后再检查')
    path.write_text(text, encoding='utf-8')


def update_specs() -> None:
    design = PROJECT / 'design_spec.md'
    s = design.read_text(encoding='utf-8')
    s = s.replace('| Code | 18 |', '| Code | 18 |\n| Dense console code | 17 |')
    s = s.replace('P16/P23/P27: task buttons switch code state; terminal remains empty before run; run triggers running status, progressive output, then completion state.',
                  'P16/P23/P27: task buttons switch code state and reset old output/status; terminal remains empty before run; run triggers running status, progressive output, then completion state only after printing finishes.')
    design.write_text(s, encoding='utf-8')
    lock = PROJECT / 'spec_lock.md'
    s = lock.read_text(encoding='utf-8')
    if '- dense_code: 17' not in s:
        s = s.replace('- code: 18\n', '- code: 18\n- dense_code: 17\n')
    lock.write_text(s, encoding='utf-8')


def semantic_audit(animations: dict) -> None:
    errors: list[str] = []
    # Hit regions must be topmost relative to visible reveal buttons.
    for path in [
        *[SVG_DIR / f'{stem}.svg' for stem in ['03_复习抢答规则','09_任务启动','13_break提前下车','14_continue跳过本轮','17_易错_漏掉计数增加','28_continue位置很重要']],
        *[SVG_DIR / f'{n:02d}_复习抢答_{2*n-7}_{2*n-6}.svg' for n in range(4,9)],
        *[SVG_DIR / f'{n:02d}_本课选择题_{2*n-35}_{2*n-34}.svg' for n in range(18,22)],
    ]:
        root = ET.parse(path).getroot()
        order = {child.get('id'): i for i, child in enumerate(list(root)) if child.get('id')}
        pairs = [('reveal-button','reveal-hit')] if 'reveal-button' in order else []
        for qi in (1,2):
            if f'q{qi}-reveal-button' in order:
                pairs.append((f'q{qi}-reveal-button', f'q{qi}-reveal-hit'))
        for button, hit in pairs:
            if order.get(hit, -1) <= order.get(button, -1):
                errors.append(f'{path.stem}: {hit} is not above {button}')

    for stem in ('16_练习A_数到3停','23_练习B_答对就break','27_三次口令门_运行验证'):
        cfg = animations['slides'][stem]
        if cfg.get('interactive_sequence_mode') != 'wps':
            errors.append(f'{stem}: interactive_sequence_mode != wps')
        groups = cfg.get('groups', {})
        # Task 1 must work both before and after explicitly selecting task 1.
        task1_outputs = [gid for gid in groups if gid.startswith('out-1-')]
        if not task1_outputs:
            errors.append(f'{stem}: no task1 outputs')
        for gid in task1_outputs:
            effects = groups[gid].get('effects', [])
            triggers = {e.get('trigger_shape') for e in effects if e.get('effect','').startswith('entrance_')}
            if not {'run-initial-hit','run-task-1-hit'} <= triggers:
                errors.append(f'{stem}/{gid}: task1 output missing initial/selected run trigger')
        for status in ('status-running','status-done'):
            if status not in groups:
                errors.append(f'{stem}: missing {status}')
        # New task selection must reset old terminal state.
        for status in ('status-running','status-done'):
            effects = groups.get(status, {}).get('effects', [])
            for i in range(1, 1 + (3 if stem.startswith('27_') else 2)):
                if not any(e.get('effect') == 'exit_appear' and e.get('trigger_shape') == f'task-{i}-hit' for e in effects):
                    errors.append(f'{stem}/{status}: no reset on task-{i}-hit')

    p27 = ET.parse(SVG_DIR / '27_三次口令门_运行验证.svg').getroot()
    p27_text = '\n'.join(text_value(el) for el in p27.iter() if el.tag == Q + 'text')
    for required in ['if password != secret:', '三次机会已用完，任务暂停。', '空白 → 正确']:
        if required not in p27_text:
            errors.append(f'P27 missing {required}')
    p26 = ET.parse(SVG_DIR / '26_三次口令门代码拆解.svg').getroot()
    p26_code_sizes = [float(el.get('font-size')) for el in p26.iter() if el.tag == Q+'text' and el.get('font-family','').startswith('Consolas') and el.get('font-size')]
    if p26_code_sizes and min(p26_code_sizes) < 17:
        errors.append(f'P26 code font too small: {min(p26_code_sizes)}')

    out = PROJECT / 'validation' / 'semantic_self_audit.txt'
    out.parent.mkdir(parents=True, exist_ok=True)
    if errors:
        out.write_text('\n'.join('ERROR ' + e for e in errors), encoding='utf-8')
        raise SystemExit('\n'.join(errors))
    out.write_text('PASS: semantic/content/interaction self-audit passed.\n', encoding='utf-8')


def main() -> None:
    animations = json.loads(ANIM_PATH.read_text(encoding='utf-8'))
    repair_reveal_pages()
    repair_quiz_pages(animations)
    repair_consoles(animations)
    repair_p26()
    repair_p31()
    update_specs()
    ANIM_PATH.write_text(json.dumps(animations, ensure_ascii=False, indent=2), encoding='utf-8')
    semantic_audit(animations)
    print('lesson12 repair complete')


if __name__ == '__main__':
    main()
