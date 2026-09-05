from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

PROJECT = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
SVG = PROJECT / 'svg_output'
NOTES = PROJECT / 'notes'
IMAGES = PROJECT / 'images'
SVG.mkdir(parents=True, exist_ok=True)
NOTES.mkdir(parents=True, exist_ok=True)
IMAGES.mkdir(parents=True, exist_ok=True)

REF = Path('projects/初识_Cpp_阳光积木乐园_ppt169_20260826/images')
for name in ['daxian_teacher_mascot_halfbody_v1.png', 'bg_three_act_blocks_v1.png', 'bg_new_knowledge_portal_v1.png']:
    src = REF / name
    if src.exists():
        shutil.copy2(src, IMAGES / name)

C = {
    'bg':'#FFFDF5','blue':'#2E9BFF','orange':'#FF9F1C','pink':'#FF6FA5','green':'#22C55E',
    'text':'#203044','terminal':'#17243A','lightblue':'#EAF5FF','lightpink':'#FFE2ED',
    'lightgreen':'#E9FBEF','line':'#CFE5F8','white':'#FFFFFF','cream':'#FFF2DC'
}

slides: list[tuple[str,str]] = []
animations: dict = {'version':1,'defaults':{'transition':{'effect':'fade','duration':0.35},'animation':{'effect':'none','duration':0.3,'trigger':'after-previous'}},'slides':{}}


def esc(s: object) -> str:
    return html.escape(str(s), quote=False)


def root(extra: str='') -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" data-pptx-page-role="content" font-family="Microsoft YaHei, Arial, sans-serif">{extra}'


def footer(n: int, tag: str='小小特工任务中心') -> str:
    return f'<g id="footer-{n}" data-pptx-role="footer"><text x="48" y="690" font-size="14" fill="#7A8A9B">{esc(tag)}</text><text x="1232" y="690" text-anchor="end" font-size="14" fill="#7A8A9B">{n:02d} / 32</text></g>'


def header(title: str, sub: str='', color: str|None=None) -> str:
    color = color or C['blue']
    return f'''<g id="page-header" data-pptx-bounds="48 32 1184 78">
      <rect x="48" y="36" width="12" height="56" rx="6" fill="{color}"/>
      <text x="82" y="70" font-family="YouYuan, Microsoft YaHei, sans-serif" font-size="38" font-weight="700" fill="{C['text']}">{esc(title)}</text>
      <text x="82" y="100" font-size="18" fill="{color}">{esc(sub)}</text>
    </g>'''


def pill(x:int,y:int,w:int,text:str,fill:str,fg:str='#203044') -> str:
    return f'<g><rect x="{x}" y="{y}" width="{w}" height="44" rx="22" fill="{fill}"/><text x="{x+w/2}" y="{y+29}" text-anchor="middle" font-size="18" font-weight="700" fill="{fg}">{esc(text)}</text></g>'


def add_slide(stem: str, body: str, *, page_role='content') -> None:
    idx = len(slides)+1
    text = root().replace('data-pptx-page-role="content"', f'data-pptx-page-role="{page_role}"')
    text += f'<rect id="background" data-pptx-role="background" width="1280" height="720" fill="{C["bg"]}"/>'
    text += body
    text += footer(idx)
    text += '</svg>'
    (SVG / f'{stem}.svg').write_text(text, encoding='utf-8')
    slides.append((stem, body))


def reveal_slide(stem: str, title: str, sub: str, left_title: str, left_lines: list[str], reveal_title: str, reveal_lines: list[str], accent: str='#2E9BFF') -> None:
    body = header(title, sub, accent)
    body += f'''<g id="base-card" data-pptx-bounds="48 132 564 490"><rect x="48" y="132" width="564" height="490" rx="34" fill="#FFFFFF" stroke="{C['line']}" stroke-width="2"/><text x="82" y="180" font-size="28" font-weight="700" fill="{C['text']}">{esc(left_title)}</text>'''
    y=226
    for line in left_lines:
        body += f'<circle cx="88" cy="{y-7}" r="7" fill="{accent}"/><text x="112" y="{y}" font-size="23" fill="{C["text"]}">{esc(line)}</text>'
        y += 54
    body += '</g>'
    body += f'''<g id="reveal-card" data-pptx-bounds="640 132 592 490"><rect x="640" y="132" width="592" height="490" rx="34" fill="{C['lightgreen']}" stroke="#BDECCB" stroke-width="2"/><text x="676" y="180" font-size="28" font-weight="700" fill="{C['green']}">{esc(reveal_title)}</text>'''
    y=228
    for line in reveal_lines:
        body += f'<text x="680" y="{y}" font-size="22" fill="{C["text"]}">{esc(line)}</text>'; y += 52
    body += '</g>'
    body += f'''<g id="reveal-hit" data-pptx-bounds="998 570 210 52"><rect x="998" y="570" width="210" height="52" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>
    <g id="reveal-button" data-pptx-bounds="998 570 210 52"><rect x="998" y="570" width="210" height="52" rx="22" fill="{accent}"/><text x="1103" y="604" text-anchor="middle" font-size="20" font-weight="700" fill="#FFFFFF">点击揭晓</text></g>'''
    add_slide(stem, body)
    animations['slides'][stem]={'groups':{'reveal-card':{'effect':'entrance_fade','trigger':'on-click','trigger_shape':'reveal-hit','order':1,'duration':0.28,'restart':'always'}}}


def quiz_pair(stem: str, title: str, q1: tuple[str,list[str],str,str], q2: tuple[str,list[str],str,str], label='课堂抢答') -> None:
    body = header(title, '先选答案，再点击“揭晓”', C['pink']) + pill(1002,46,210,label,C['lightpink'],C['pink'])
    for i,(q,opts,ans,why) in enumerate([q1,q2],1):
        y0=140+(i-1)*250
        body += f'<g id="q{i}-base" data-pptx-bounds="48 {y0} 1184 220"><rect x="48" y="{y0}" width="1184" height="220" rx="30" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="2"/><circle cx="88" cy="{y0+42}" r="22" fill="{C["pink"]}"/><text x="88" y="{y0+50}" text-anchor="middle" font-size="20" font-weight="700" fill="#FFFFFF">{i}</text><text x="126" y="{y0+50}" font-size="24" font-weight="700" fill="{C["text"]}">{esc(q)}</text>'
        x=90
        for opt in opts:
            body += f'<rect x="{x}" y="{y0+82}" width="250" height="52" rx="18" fill="{C["lightblue"]}"/><text x="{x+125}" y="{y0+116}" text-anchor="middle" font-size="19" fill="{C["text"]}">{esc(opt)}</text>'
            x += 270
        body += '</g>'
        body += f'<g id="q{i}-answer" data-pptx-bounds="84 {y0+148} 780 52"><rect x="84" y="{y0+148}" width="780" height="52" rx="18" fill="{C["lightgreen"]}"/><text x="108" y="{y0+182}" font-size="20" font-weight="700" fill="{C["green"]}">正确答案：{esc(ans)}</text><text x="270" y="{y0+182}" font-size="19" fill="{C["text"]}">{esc(why)}</text></g>'
        body += f'<g id="q{i}-reveal-button" data-pptx-bounds="900 {y0+148} 280 52"><rect x="900" y="{y0+148}" width="280" height="52" rx="22" fill="{C["pink"]}"/><text x="1040" y="{y0+182}" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">揭晓第 {i} 题</text></g><g id="q{i}-reveal-hit" data-pptx-bounds="900 {y0+148} 280 52"><rect x="900" y="{y0+148}" width="280" height="52" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>'
    add_slide(stem, body)
    animations['slides'][stem]={'groups':{
      'q1-answer':{'effect':'entrance_appear','trigger':'on-click','trigger_shape':'q1-reveal-hit','order':1,'duration':0.12,'restart':'always'},
      'q2-answer':{'effect':'entrance_appear','trigger':'on-click','trigger_shape':'q2-reveal-hit','order':1,'duration':0.12,'restart':'always'}
    }}


def chapter(stem: str, num: str, title: str, sub: str, bgimg='bg_new_knowledge_portal_v1.png') -> None:
    body=f'<image id="chapter-bg" href="../images/{bgimg}" x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice" opacity="0.23"/>'
    body += f'<g id="chapter-stage" data-pptx-bounds="64 108 1120 492"><rect x="64" y="108" width="1120" height="492" rx="52" fill="#FFFFFF" fill-opacity="0.92" stroke="{C["line"]}" stroke-width="2"/><text x="120" y="286" font-family="YouYuan, Microsoft YaHei, sans-serif" font-size="180" font-weight="700" fill="{C["blue"]}">{esc(num)}</text><text x="390" y="280" font-family="YouYuan, Microsoft YaHei, sans-serif" font-size="56" font-weight="700" fill="{C["text"]}">{esc(title)}</text><text x="394" y="338" font-size="26" fill="{C["orange"]}">{esc(sub)}</text><rect x="394" y="382" width="600" height="12" rx="6" fill="{C["lightblue"]}"/><rect x="394" y="382" width="320" height="12" rx="6" fill="{C["blue"]}"/></g>'
    add_slide(stem, body, page_role='section')


def code_card(lines:list[str], x=68,y=150,w=700,h=450, highlight:int|None=None) -> str:
    s=f'<g id="code-card" data-pptx-bounds="{x} {y} {w} {h}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="32" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="2"/><circle cx="{x+34}" cy="{y+34}" r="8" fill="{C["pink"]}"/><circle cx="{x+60}" cy="{y+34}" r="8" fill="{C["orange"]}"/><circle cx="{x+86}" cy="{y+34}" r="8" fill="{C["green"]}"/><text x="{x+124}" y="{y+42}" font-size="19" font-weight="700" fill="{C["text"]}">Python 编辑器</text>'
    yy=y+94
    for i,line in enumerate(lines):
        if highlight==i:
            s+=f'<rect x="{x+24}" y="{yy-29}" width="{w-48}" height="40" rx="12" fill="{C["lightpink"]}"/>'
        color=C['blue'] if line.strip().startswith(('while','if','else')) else C['orange'] if any(k in line for k in ['break','continue']) else C['text']
        s+=f'<text x="{x+34}" y="{yy}" font-family="Consolas, Courier New, monospace" font-size="18" fill="{color}">{esc(line) if line else " "}</text>'; yy+=34
    s+='</g>'
    return s


def console_slide(stem:str,title:str,sub:str,tasks:list[dict]) -> None:
    body=header(title,sub,C['blue'])
    n=len(tasks); gap=16; total=1184; bw=(total-gap*(n-1))/n
    for i,t in enumerate(tasks):
        x=48+i*(bw+gap); fill=[C['lightblue'],C['cream'],C['lightpink']][i%3]; edge=[C['blue'],C['orange'],C['pink']][i%3]
        body+=f'<g id="task-{i+1}-button" data-pptx-bounds="{x:.0f} 124 {bw:.0f} 66"><rect x="{x:.0f}" y="124" width="{bw:.0f}" height="66" rx="22" fill="{fill}" stroke="{edge}" stroke-width="2"/><text x="{x+bw/2:.0f}" y="164" text-anchor="middle" font-size="20" font-weight="700" fill="{C["text"]}">{esc(t["label"])}</text></g><g id="task-{i+1}-hit" data-pptx-bounds="{x:.0f} 124 {bw:.0f} 66"><rect x="{x:.0f}" y="124" width="{bw:.0f}" height="66" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>'
    body+=f'<g id="editor-shell" data-pptx-bounds="48 214 704 432"><rect x="48" y="214" width="704" height="432" rx="34" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="3"/><circle cx="82" cy="248" r="8" fill="{C["pink"]}"/><circle cx="108" cy="248" r="8" fill="{C["orange"]}"/><circle cx="134" cy="248" r="8" fill="{C["green"]}"/><text x="174" y="256" font-size="20" font-weight="700" fill="{C["text"]}">代码编辑器</text><rect x="72" y="278" width="656" height="280" rx="22" fill="#F8FBFF"/></g>'
    body+=f'<g id="terminal-shell" data-pptx-bounds="776 214 456 432"><rect x="776" y="214" width="456" height="432" rx="34" fill="{C["lightblue"]}"/><text x="810" y="256" font-size="23" font-weight="700" fill="{C["text"]}">终端输出</text><rect x="800" y="278" width="408" height="280" rx="24" fill="{C["terminal"]}"/><circle cx="830" cy="306" r="7" fill="{C["pink"]}"/><circle cx="854" cy="306" r="7" fill="{C["orange"]}"/><circle cx="878" cy="306" r="7" fill="{C["green"]}"/><rect x="800" y="574" width="408" height="56" rx="20" fill="#FFFFFF"/></g>'
    body+=f'<g id="code-initial" data-pptx-bounds="88 304 620 238">{code_lines_svg(tasks[0]["code"], 94, 326)}</g><g id="run-initial" data-pptx-bounds="506 578 222 54"><rect x="506" y="578" width="222" height="54" rx="22" fill="{C["blue"]}"/><text x="617" y="613" text-anchor="middle" font-size="21" font-weight="700" fill="#FFFFFF">▶ 运行程序</text></g><g id="run-initial-hit" data-pptx-bounds="506 578 222 54"><rect x="506" y="578" width="222" height="54" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>'
    body+=f'<g id="guide-initial" data-pptx-bounds="820 584 368 38"><text x="1004" y="610" text-anchor="middle" font-size="18" font-weight="700" fill="{C["blue"]}">点击运行，终端才开始输出</text></g><g id="status-running" data-pptx-bounds="820 584 368 38"><text x="1004" y="610" text-anchor="middle" font-size="19" font-weight="700" fill="{C["orange"]}">运行中……</text></g><g id="status-done" data-pptx-bounds="820 584 368 38"><text x="1004" y="610" text-anchor="middle" font-size="19" font-weight="700" fill="{C["green"]}">验证完成 ✓</text></g>'
    for i,t in enumerate(tasks,1):
        body+=f'<g id="code-task-{i}" data-pptx-bounds="88 304 620 238">{code_lines_svg(t["code"],94,326)}</g><g id="run-task-{i}" data-pptx-bounds="506 578 222 54"><rect x="506" y="578" width="222" height="54" rx="22" fill="{[C["blue"],C["orange"],C["pink"]][(i-1)%3]}"/><text x="617" y="613" text-anchor="middle" font-size="21" font-weight="700" fill="#FFFFFF">▶ 运行程序</text></g><g id="run-task-{i}-hit" data-pptx-bounds="506 578 222 54"><rect x="506" y="578" width="222" height="54" rx="22" fill="#FFFFFF" fill-opacity="0.001"/></g>'
        if t.get('char_output'):
            x=824
            for j,ch in enumerate(t['char_output'],1):
                body+=f'<g id="out-{i}-char-{j:02d}" data-pptx-bounds="{x} 350 26 40"><text x="{x}" y="382" font-family="Consolas, Microsoft YaHei, monospace" font-size="25" font-weight="700" fill="#FFFFFF">{esc(ch)}</text></g>'; x+=26
        else:
            yy=356
            for j,line in enumerate(t['output'],1):
                body+=f'<g id="out-{i}-line-{j:02d}" data-pptx-bounds="824 {yy-28} 356 38"><text x="824" y="{yy}" font-family="Consolas, Microsoft YaHei, monospace" font-size="19" fill="#FFFFFF">{esc(line)}</text></g>'; yy+=42
    add_slide(stem,body)
    g={}
    # Initial visible states exit when any task is selected.
    for initial in ['code-initial','run-initial']:
        g[initial]={'effects':[{'effect':'exit_appear','trigger':'on-click','trigger_shape':f'task-{i}-hit','order':1,'duration':0.05,'restart':'always'} for i in range(1,n+1)]}
    # Task state switching and output reset.
    all_out=[]
    for i,t in enumerate(tasks,1):
        ids=[f'out-{i}-char-{j:02d}' for j,_ in enumerate(t.get('char_output',''),1)] if t.get('char_output') else [f'out-{i}-line-{j:02d}' for j,_ in enumerate(t['output'],1)]
        all_out += ids
    for i in range(1,n+1):
        g[f'code-task-{i}']={'effects':[]}; g[f'run-task-{i}']={'effects':[]}
        for k in range(1,n+1):
            g[f'code-task-{i}']['effects'].append({'effect':'exit_appear','trigger':'on-click','trigger_shape':f'task-{k}-hit','order':1,'duration':0.04,'restart':'always'})
            g[f'run-task-{i}']['effects'].append({'effect':'exit_appear','trigger':'with-previous','trigger_shape':f'task-{k}-hit','order':2,'duration':0.04,'restart':'always'})
        g[f'code-task-{i}']['effects'].append({'effect':'entrance_appear','trigger':'with-previous','trigger_shape':f'task-{i}-hit','order':5,'delay':0.05,'duration':0.05,'restart':'always'})
        g[f'run-task-{i}']['effects'].append({'effect':'entrance_appear','trigger':'with-previous','trigger_shape':f'task-{i}-hit','order':6,'delay':0.05,'duration':0.05,'restart':'always'})
    # Guide disappears on runs and returns on task selection.
    g['guide-initial']={'effects':[{'effect':'exit_appear','trigger':'on-click','trigger_shape':'run-initial-hit','order':1,'duration':0.04,'restart':'always'}]+[{'effect':'exit_appear','trigger':'on-click','trigger_shape':f'run-task-{i}-hit','order':1,'duration':0.04,'restart':'always'} for i in range(1,n+1)]}
    g['status-running']={'effects':[]}; g['status-done']={'effects':[]}
    run_triggers=['run-initial-hit']+[f'run-task-{i}-hit' for i in range(1,n+1)]
    for tr in run_triggers:
        g['status-running']['effects'] += [{'effect':'entrance_appear','trigger':'with-previous','trigger_shape':tr,'order':2,'duration':0.05,'restart':'always'},{'effect':'exit_appear','trigger':'with-previous','trigger_shape':tr,'order':3,'delay':0.18,'duration':0.05,'restart':'always'}]
        g['status-done']['effects'].append({'effect':'entrance_appear','trigger':'with-previous','trigger_shape':tr,'order':90,'delay':0.18,'duration':0.08,'restart':'always'})
    # outputs: reset on task click, print on run.
    for i,t in enumerate(tasks,1):
        ids=[f'out-{i}-char-{j:02d}' for j,_ in enumerate(t.get('char_output',''),1)] if t.get('char_output') else [f'out-{i}-line-{j:02d}' for j,_ in enumerate(t['output'],1)]
        tr='run-initial-hit' if i==1 else f'run-task-{i}-hit'
        for j,oid in enumerate(ids,1):
            effects=[]
            for k in range(1,n+1):
                effects.append({'effect':'exit_appear','trigger':'on-click','trigger_shape':f'task-{k}-hit','order':1,'duration':0.03,'restart':'always'})
            effects.append({'effect':'entrance_appear','trigger':'with-previous','trigger_shape':tr,'order':10+j,'delay':0.08*j,'duration':0.04,'restart':'always'})
            g[oid]={'effects':effects}
    animations['slides'][stem]={'interactive_sequence_mode':'wps','groups':g}


def code_lines_svg(lines:list[str], x:int, y:int) -> str:
    out=''; yy=y
    for line in lines:
        color=C['blue'] if line.strip().startswith(('while','if','else')) else C['orange'] if any(k in line for k in ('break','continue')) else C['text']
        out+=f'<text x="{x}" y="{yy}" font-family="Consolas, Microsoft YaHei, monospace" font-size="17" fill="{color}">{esc(line) if line else " "}</text>'; yy+=30
    return out

# 01 cover
body='<rect x="0" y="0" width="1280" height="720" fill="#FFFCF1"/><circle cx="110" cy="110" r="76" fill="#EAF5FF"/><rect x="96" y="96" width="350" height="46" rx="23" fill="#EAF5FF"/><text x="270" y="127" text-anchor="middle" font-size="19" font-weight="700" fill="#2E9BFF">第12课 · 小小特工任务中心</text><text x="86" y="278" font-family="YouYuan, Microsoft YaHei, sans-serif" font-size="66" font-weight="700" fill="#203044">特工身份确认</text><text x="90" y="344" font-size="29" fill="#FF9F1C">while · break · continue</text><rect x="88" y="390" width="600" height="116" rx="34" fill="#FFFFFF" stroke="#CFE5F8" stroke-width="2"/><text x="124" y="437" font-size="23" font-weight="700" fill="#203044">今天的驱动问题</text><text x="124" y="478" font-size="22" fill="#203044">怎样让口令门反复询问，答对就开门，答错三次就停止？</text><image id="teacher" href="../images/daxian_teacher_mascot_halfbody_v1.png" x="860" y="132" width="330" height="450" preserveAspectRatio="xMidYMid meet"/><rect x="720" y="530" width="460" height="66" rx="26" fill="#17243A"/><text x="950" y="572" text-anchor="middle" font-family="Consolas, monospace" font-size="23" fill="#FFFFFF">AGENT LOGIN · READY</text>'
add_slide('01_特工身份确认',body,page_role='cover')

# 02 route
body='<image id="route-bg" href="../images/bg_three_act_blocks_v1.png" x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice" opacity="0.20"/>'+header('今天的任务路线','120分钟：先复习，再学守门循环，最后完成三次口令门')
for i,(t,m,c) in enumerate([('01 复习热身','0–20 min',C['blue']),('02 新知精学','20–65 min',C['orange']),('03 动手验证','75–110 min',C['pink']),('04 展示总结','110–120 min',C['green'])]):
    x=70+i*296; body+=f'<g id="route-{i+1}" data-pptx-bounds="{x} 212 252 250"><rect x="{x}" y="212" width="252" height="250" rx="34" fill="#FFFFFF" stroke="{c}" stroke-width="3"/><circle cx="{x+126}" cy="270" r="38" fill="{c}"/><text x="{x+126}" y="280" text-anchor="middle" font-size="24" font-weight="700" fill="#FFFFFF">{i+1}</text><text x="{x+126}" y="346" text-anchor="middle" font-size="25" font-weight="700" fill="{C["text"]}">{t}</text><text x="{x+126}" y="394" text-anchor="middle" font-size="20" fill="{c}">{m}</text></g>'
body+=pill(370,520,540,'最终作品：最多尝试三次、会跳过空输入的口令验证器',C['cream'],C['orange'])
add_slide('02_今天的任务路线',body)

# 03 review rules
reveal_slide('03_复习抢答规则','第11课知识抢答','10题 · 每题约40秒 · 答错不扣分','玩法',['教师读题，学生用手势或小白板抢答','先口答，不看答案','答错后立刻口头修正'],'准备好了吗？',['上一课：幸运抽奖箱','核心工具：random + if-elif-else','接下来 5 页，每页 2 题'],'#2E9BFF')

review=[
('随机模块叫什么？',['A. random','B. turtle','C. time','D. math'],'A','random。'),('导入随机模块怎么写？',['A. random import','B. import random','C. use random','D. from random'],'B','import random。'),
('生成1到6随机数用什么？',['A. random(1,6)','B. randint 1,6','C. random.randint(1,6)','D. input(1,6)'],'C','random.randint(1,6)。'),('randint(1,6)包含6吗？',['A. 包含','B. 不包含','C. 只含6','D. 不确定'],'A','包含左右端点。'),
('随机结果会不会重复？',['A. 不会','B. 可能重复','C. 一定重复','D. 只能重复一次'],'B','每次生成彼此独立，可能重复。'),('随机号码适合保存在哪里？',['A. 图片','B. 注释','C. 变量','D. 文件名'],'C','用变量保存后再判断。'),
('号码对应不同奖品可使用什么？',['A. while','B. if-elif-else','C. print','D. input'],'B','多分支判断。'),('比较号码是否等于1使用什么？',['A. =','B. !=','C. ==','D. >='],'C','== 用于比较相等。'),
('else可以接住没单独列出的情况吗？',['A. 可以','B. 不可以','C. 只在循环里','D. 只能接数字'],'A','else 处理其余情况。'),('上节课项目是什么？',['A. 海龟画图','B. 幸运抽奖箱','C. 口令门','D. 计算器'],'B','幸运抽奖箱。')]
for p in range(5):
    quiz_pair(f'{4+p:02d}_复习抢答_{p*2+1}_{p*2+2}',f'复习抢答 · 第 {p*2+1}–{p*2+2} 题',review[p*2],review[p*2+1],'第11课复习')

# 09 launch
reveal_slide('09_任务启动','特工任务启动','先看最终挑战，再想一想程序需要什么能力','驱动问题',['口令错误时：继续问','口令正确时：马上开门','错误三次后：停止任务','空白输入：跳过，不算次数'],'今天要拼出的4块积木',['while：按条件反复','tries：记录有效尝试','break：成功就离开','continue：空白就跳过'],'#FF9F1C')
chapter('10_新知精学','01','新知精学','把“反复问、及时停、跳过本轮”拆成三个命令')

# 11 while
body=header('while 像值班守卫','只要条件还成立，就继续值班',C['blue'])
body+=f'<g id="guard-loop" data-pptx-bounds="70 150 720 430"><rect x="70" y="150" width="720" height="430" rx="38" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="2"/><circle cx="250" cy="330" r="98" fill="{C["lightblue"]}" stroke="{C["blue"]}" stroke-width="4"/><text x="250" y="318" text-anchor="middle" font-size="25" font-weight="700" fill="{C["text"]}">条件成立？</text><text x="250" y="358" text-anchor="middle" font-family="Consolas, monospace" font-size="22" fill="{C["blue"]}">tries &lt; 3</text><rect x="490" y="266" width="220" height="128" rx="30" fill="{C["cream"]}"/><text x="600" y="316" text-anchor="middle" font-size="24" font-weight="700" fill="{C["orange"]}">继续询问</text><text x="600" y="354" text-anchor="middle" font-size="20" fill="{C["text"]}">输入 → 判断 → 更新</text><path d="M350 330 L470 330" stroke="{C["blue"]}" stroke-width="8" fill="none"/><path d="M600 410 C600 510 250 510 250 445" stroke="{C["orange"]}" stroke-width="8" fill="none"/></g>'
body+=f'<g id="while-rule" data-pptx-bounds="830 170 350 330"><rect x="830" y="170" width="350" height="330" rx="34" fill="{C["lightgreen"]}"/><text x="866" y="224" font-size="26" font-weight="700" fill="{C["green"]}">一句话记忆</text><text x="866" y="282" font-size="23" fill="{C["text"]}">条件为真 → 重复</text><text x="866" y="330" font-size="23" fill="{C["text"]}">条件为假 → 停止</text><text x="866" y="404" font-size="20" fill="{C["text"]}">关键：循环里必须让</text><text x="866" y="438" font-size="20" fill="{C["text"]}">“停止条件”有机会出现。</text></g>'
add_slide('11_while像值班守卫',body)
animations['slides']['11_while像值班守卫']={'groups':{'while-rule':{'effect':'entrance_fade','trigger':'on-click','order':1,'duration':0.3}}}

#12 counter
body=header('计数变量：让守卫知道问了几次','tries 从 0 开始，每一次有效尝试都 +1',C['orange'])
for i,(v,txt) in enumerate([('0','刚开始'),('1','问过1次'),('2','问过2次'),('3','机会用完')]):
    x=90+i*284; color=C['green'] if i<3 else C['pink']; body+=f'<g id="count-{i}" data-pptx-bounds="{x} 196 230 210"><rect x="{x}" y="196" width="230" height="210" rx="34" fill="#FFFFFF" stroke="{color}" stroke-width="3"/><text x="{x+115}" y="296" text-anchor="middle" font-family="Consolas, monospace" font-size="70" font-weight="700" fill="{color}">{v}</text><text x="{x+115}" y="354" text-anchor="middle" font-size="21" fill="{C["text"]}">{txt}</text></g>'
body+=f'<g id="count-code" data-pptx-bounds="300 456 680 120"><rect x="300" y="456" width="680" height="120" rx="28" fill="{C["terminal"]}"/><text x="340" y="505" font-family="Consolas, monospace" font-size="25" fill="#FFFFFF">while tries &lt; 3:</text><text x="380" y="548" font-family="Consolas, monospace" font-size="25" fill="{C["orange"]}">tries = tries + 1</text></g>'
add_slide('12_计数防止不停',body)

#13 break
reveal_slide('13_break提前下车','break：成功就立刻离开','它结束的是“整个循环”，不是只跳过一行','想象一辆循环公交',['每一轮 = 公交又绕一圈','口令不对 = 继续坐','口令正确 = 到站'],'break 做什么？',['身份确认成功时执行 break','马上跳出 while','后面的循环轮次都不再执行'],'#FF9F1C')
#14 continue
reveal_slide('14_continue跳过本轮','continue：跳过本轮剩余代码','空白输入时，不做下面的判断，直接回到下一轮','遇到空白输入',['password == ""','提示“不能输入空白！”','这次不应该算有效尝试'],'continue 做什么？',['跳过本轮剩余代码','直接回到 while 条件','因此要放在 tries + 1 之前'],'#FF6FA5')
#15 for vs while
body=header('for 还是 while？','先问自己：我知道要重复几次吗？',C['blue'])
body+=f'<g id="for-card" data-pptx-bounds="90 170 500 390"><rect x="90" y="170" width="500" height="390" rx="40" fill="{C["lightblue"]}"/><text x="340" y="240" text-anchor="middle" font-family="Consolas, monospace" font-size="40" font-weight="700" fill="{C["blue"]}">for</text><text x="340" y="302" text-anchor="middle" font-size="25" font-weight="700" fill="{C["text"]}">次数清楚</text><text x="340" y="360" text-anchor="middle" font-size="22" fill="{C["text"]}">例：画4条边</text><text x="340" y="406" text-anchor="middle" font-size="22" fill="{C["text"]}">例：重复10次</text></g><g id="while-card" data-pptx-bounds="690 170 500 390"><rect x="690" y="170" width="500" height="390" rx="40" fill="{C["cream"]}"/><text x="940" y="240" text-anchor="middle" font-family="Consolas, monospace" font-size="40" font-weight="700" fill="{C["orange"]}">while</text><text x="940" y="302" text-anchor="middle" font-size="25" font-weight="700" fill="{C["text"]}">看条件继续</text><text x="940" y="360" text-anchor="middle" font-size="22" fill="{C["text"]}">例：直到答对</text><text x="940" y="406" text-anchor="middle" font-size="22" fill="{C["text"]}">例：机会还没用完</text></g><g id="vs-takeaway" data-pptx-bounds="352 580 576 56"><rect x="352" y="580" width="576" height="56" rx="24" fill="{C["lightgreen"]}"/><text x="640" y="616" text-anchor="middle" font-size="21" font-weight="700" fill="{C["green"]}">次数明确 → for　｜　条件驱动 → while</text></g>'
add_slide('15_for和while怎么选',body)
animations['slides']['15_for和while怎么选']={'groups':{'while-card':{'effect':'entrance_fade','trigger':'on-click','order':1,'duration':0.25},'vs-takeaway':{'effect':'entrance_fade','trigger':'on-click','order':2,'duration':0.25}}}

#16 console A
console_slide('16_练习A_数到3停','动手练习 A：数到几停？','选任务 → 看代码 → 点击运行 → 观察输出',[{
'label':'数到 3 停','code':['count = 1','','while count <= 3:','    print("第", count, "次检查")','    count = count + 1','','print("检查结束")'],'output':['第 1 次检查','第 2 次检查','第 3 次检查','检查结束']},{
'label':'改成数到 5','code':['count = 1','','while count <= 5:','    print("第", count, "次检查")','    count = count + 1','','print("检查结束")'],'output':['第 1 次检查','第 2 次检查','第 3 次检查','第 4 次检查','第 5 次检查','检查结束']}])
#17 missing increment
reveal_slide('17_易错_漏掉计数增加','易错提醒：少一行，循环可能停不下来','先找问题，再点击揭晓','危险代码',['count = 1','while count <= 3:','    print("检查")','—— count 一直没有变化'],'为什么危险？',['条件 count <= 3 一直为真','程序会不停重复','先知道 IDLE / Thonny 的停止按钮在哪里'],'#FF6FA5')

quiz=[
('while循环在什么时候继续？',['A. 条件成立时','B. 永远不执行','C. 只有画图时','D. 保存时'],'A','条件为真时重复。'),('防止while不停常用的方法是？',['A. 更新计数或条件','B. 加颜色','C. 加图片','D. 删除print'],'A','让停止条件有机会出现。'),
('break的作用是？',['A. 立刻结束循环','B. 跳过注释','C. 开始循环','D. 输出'],'A','break 直接离开整个循环。'),('continue的作用是？',['A. 结束程序','B. 跳过本轮剩余代码','C. 删除变量','D. 导入模块'],'B','回到下一轮判断。'),
('while True表示？',['A. 条件一直为真','B. 循环3次','C. 不执行','D. 画圆'],'A','需要 break 等方式停止。'),('count=count+1有什么作用？',['A. 计数增加','B. 计数清零','C. 输出图片','D. 改颜色'],'A','每轮增加计数。'),
('已知重复4次画正方形更适合？',['A. for','B. 无break的while True','C. input','D. type'],'A','次数明确时 for 更直接。'),('不知道尝试几次、直到答对更适合？',['A. while','B. turtle','C. print一次','D. 注释'],'A','按条件持续时 while 更合适。')]
for p in range(4):
    quiz_pair(f'{18+p:02d}_本课选择题_{p*2+1}_{p*2+2}',f'本课选择题 · 第 {p*2+1}–{p*2+2} 题',quiz[p*2],quiz[p*2+1],'本课练习')
chapter('22_break实战','02','break 实战','答对口令就提前结束循环')
#23 console B
console_slide('23_练习B_答对就break','动手练习 B：答对就 break','体验“继续尝试”和“立刻成功”的差别',[{
'label':'直接输入 python','code':['while True:','    password = input("请输入口令：")','    if password == "python":','        print("身份确认成功！")','        break','    print("口令不对，请再试一次。")'],'char_output':'身份确认成功！','output':[]},{
'label':'先错再答对','code':['while True:','    password = input("请输入口令：")','    if password == "python":','        print("身份确认成功！")','        break','    print("口令不对，请再试一次。")'],'output':['口令不对，请再试一次。','口令不对，请再试一次。','身份确认成功！']}])
#24 walkthrough
body=header('break 发生在哪一刻？','从输入到离开循环，一步一步走',C['orange'])
steps=[('1','输入口令','password = input(...)'),('2','判断是否正确','password == "python"'),('3','输出成功','print("身份确认成功！")'),('4','立刻离开','break')]
for i,(num,t,code) in enumerate(steps):
    x=64+i*296; body+=f'<g id="step-{i+1}" data-pptx-bounds="{x} 190 248 260"><rect x="{x}" y="190" width="248" height="260" rx="34" fill="#FFFFFF" stroke="{C["line"]}" stroke-width="2"/><circle cx="{x+124}" cy="248" r="32" fill="{C["orange"]}"/><text x="{x+124}" y="258" text-anchor="middle" font-size="24" font-weight="700" fill="#FFFFFF">{num}</text><text x="{x+124}" y="326" text-anchor="middle" font-size="23" font-weight="700" fill="{C["text"]}">{esc(t)}</text><text x="{x+124}" y="382" text-anchor="middle" font-family="Consolas, Microsoft YaHei, monospace" font-size="15" fill="{C["blue"]}">{esc(code)}</text></g>'
body+=pill(356,506,568,'break 后：整个 while 循环结束，不再询问',C['lightgreen'],C['green'])
add_slide('24_break执行路径',body)
chapter('25_微项目三次口令门','03','微项目：三次口令门','把 while + 计数 + break + continue 拼成完整作品')
#26 code anatomy
micro=['secret = "python"','tries = 0','','while tries < 3:','    password = input("请输入特工口令：")','','    if password == "":','        print("不能输入空白！")','        continue','','    tries = tries + 1','','    if password == secret:','        print("身份确认成功，欢迎特工！")','        break','    else:','        print("口令错误。还可尝试", 3 - tries, "次。")','','if password != secret:','    print("三次机会已用完，任务暂停。")']
body=header('完整代码：四块积木怎样配合？','重点不是背代码，而是看清顺序',C['blue'])+code_card(micro,48,134,750,500)
for i,(t,d,c) in enumerate([('① 条件','tries < 3','blue'),('② 空白','continue','pink'),('③ 计数','tries + 1','orange'),('④ 成功','break','green')]):
    y=156+i*104; col=C[c]; body+=f'<g id="anatomy-{i+1}" data-pptx-bounds="832 {y} 368 82"><rect x="832" y="{y}" width="368" height="82" rx="24" fill="#FFFFFF" stroke="{col}" stroke-width="2"/><text x="860" y="{y+32}" font-size="21" font-weight="700" fill="{col}">{t}</text><text x="860" y="{y+62}" font-family="Consolas, Microsoft YaHei, monospace" font-size="18" fill="{C["text"]}">{esc(d)}</text></g>'
add_slide('26_三次口令门代码拆解',body)
#27 console three scenarios
short_code=['secret = "python"','tries = 0','while tries < 3:','    password = input("请输入特工口令：")','    if password == "":','        print("不能输入空白！")','        continue','    tries = tries + 1','    if password == secret:','        print("身份确认成功，欢迎特工！")','        break','    print("口令错误。还可尝试", 3-tries, "次。")']
console_slide('27_三次口令门_运行验证','运行验证：三类输入都要测','任务按钮切换案例；只有点击运行后终端才输出',[{
'label':'空白输入','code':short_code,'char_output':'不能输入空白！','output':[]},{
'label':'错误 × 3','code':short_code,'output':['口令错误。还可尝试 2 次。','口令错误。还可尝试 1 次。','口令错误。还可尝试 0 次。','三次机会已用完，任务暂停。']},{
'label':'错误 → 正确','code':short_code,'output':['口令错误。还可尝试 2 次。','身份确认成功，欢迎特工！']}])
#28 continue order
reveal_slide('28_continue位置很重要','continue 放哪里，决定空白算不算一次','先比较两种顺序，再揭晓','两种写法',['A：先判断空白 → continue → 再 tries + 1','B：先 tries + 1 → 再判断空白 → continue','目标：空白输入“不计次数”'],'正确顺序是 A',['空白时应在计数之前 continue','这样 tries 不会增加','记忆：先过滤无效输入，再计数有效尝试'],'#FF6FA5')
#29 checklist
body=header('项目实施：5步完成三次口令门','基础版先跑通，再做个性化修改',C['blue'])
items=[('1','口令游戏','说出“继续 / 停止”'),('2','数到3停','确认 count 会变化'),('3','体验 break','正确就提前结束'),('4','完成三次门','测试空白 / 错误 / 正确'),('5','同桌解释','说清 break 与 continue')]
for i,(n,t,d) in enumerate(items):
    y=142+i*94; body+=f'<g id="task-step-{i+1}" data-pptx-bounds="120 {y} 1040 74"><rect x="120" y="{y}" width="1040" height="74" rx="24" fill="{C["white"]}" stroke="{C["line"]}" stroke-width="2"/><circle cx="166" cy="{y+37}" r="25" fill="{[C["blue"],C["orange"],C["pink"],C["green"],C["blue"]][i]}"/><text x="166" y="{y+45}" text-anchor="middle" font-size="20" font-weight="700" fill="#FFFFFF">{n}</text><text x="214" y="{y+32}" font-size="22" font-weight="700" fill="{C["text"]}">{t}</text><text x="214" y="{y+58}" font-size="18" fill="#5B6B7B">{d}</text></g>'
add_slide('29_项目实施步骤',body)
#30 acceptance
body=header('作品验收与同伴展示','能运行，还要能解释',C['green'])
checks=['错误输入不会超过三次有效尝试','正确口令能够提前结束循环','能够解释计数为什么必须增加']
for i,t in enumerate(checks):
    y=166+i*96; body+=f'<g id="check-{i+1}" data-pptx-bounds="100 {y} 650 72"><rect x="100" y="{y}" width="650" height="72" rx="24" fill="{C["lightgreen"]}"/><circle cx="142" cy="{y+36}" r="20" fill="{C["green"]}"/><text x="142" y="{y+43}" text-anchor="middle" font-size="20" font-weight="700" fill="#FFFFFF">✓</text><text x="184" y="{y+44}" font-size="21" font-weight="700" fill="{C["text"]}">{esc(t)}</text></g>'
body+=f'<g id="show-sentence" data-pptx-bounds="790 166 390 360"><rect x="790" y="166" width="390" height="360" rx="36" fill="{C["lightblue"]}"/><text x="830" y="220" font-size="25" font-weight="700" fill="{C["blue"]}">展示句式</text><text x="830" y="278" font-size="21" fill="{C["text"]}">我的作品是……</text><text x="830" y="326" font-size="21" fill="{C["text"]}">我使用了……命令</text><text x="830" y="374" font-size="21" fill="{C["text"]}">我修改了……</text><text x="830" y="422" font-size="21" fill="{C["text"]}">下一次我想……</text><text x="830" y="486" font-size="18" fill="#5B6B7B">同伴只提 1 条友善建议</text></g>'
add_slide('30_作品验收与展示',body)
#31 bugs
body=header('常见问题：先判断是哪一类错误','停止、顺序、变量——三类问题三种检查法',C['pink'])
bugs=[('循环停不下','漏掉计数增加','先停止运行，再检查 tries/count 是否变化',C['pink']),('空白也被计次','continue 放在计数后','先过滤空白，再做 tries + 1',C['orange']),('变量还没准备好','循环后使用 password','确认循环一定执行，或先给变量初值',C['blue'])]
for i,(t,why,fix,col) in enumerate(bugs):
    x=70+i*398; body+=f'<g id="bug-{i+1}" data-pptx-bounds="{x} 176 356 360"><rect x="{x}" y="176" width="356" height="360" rx="36" fill="#FFFFFF" stroke="{col}" stroke-width="3"/><circle cx="{x+48}" cy="224" r="24" fill="{col}"/><text x="{x+48}" y="232" text-anchor="middle" font-size="22" font-weight="700" fill="#FFFFFF">!</text><text x="{x+88}" y="232" font-size="23" font-weight="700" fill="{C["text"]}">{t}</text><text x="{x+34}" y="302" font-size="18" font-weight="700" fill="{col}">可能原因</text><text x="{x+34}" y="340" font-size="20" fill="{C["text"]}">{why}</text><text x="{x+34}" y="406" font-size="18" font-weight="700" fill="{C["green"]}">处理方法</text><text x="{x+34}" y="444" font-size="18" fill="{C["text"]}">{fix}</text></g>'
add_slide('31_常见问题与处理',body)
#32 summary
body='<rect x="0" y="0" width="1280" height="720" fill="#FFFCF1"/>'+header('任务完成：特工身份确认成功！','离堂前，用自己的话说出今天会用的命令',C['green'])
for i,(k,t,c) in enumerate([('while','条件成立就重复',C['blue']),('break','立刻结束整个循环',C['orange']),('continue','跳过本轮剩余代码',C['pink'])]):
    x=76+i*386; body+=f'<g id="summary-{i+1}" data-pptx-bounds="{x} 176 340 190"><rect x="{x}" y="176" width="340" height="190" rx="36" fill="#FFFFFF" stroke="{c}" stroke-width="3"/><text x="{x+170}" y="250" text-anchor="middle" font-family="Consolas, monospace" font-size="38" font-weight="700" fill="{c}">{k}</text><text x="{x+170}" y="310" text-anchor="middle" font-size="21" fill="{C["text"]}">{t}</text></g>'
body+=f'<g id="exit-ticket" data-pptx-bounds="190 414 900 160"><rect x="190" y="414" width="900" height="160" rx="38" fill="{C["lightgreen"]}"/><text x="236" y="464" font-size="23" font-weight="700" fill="{C["green"]}">离堂小结</text><text x="236" y="510" font-size="21" fill="{C["text"]}">我学会了“条件循环”；我完成了“最多三次、会跳过空输入”的口令验证器。</text><text x="236" y="550" font-size="21" fill="{C["text"]}">下次遇到报错：先检查拼写、符号和缩进。</text></g>'
add_slide('32_离堂小结',body,page_role='section')

# Design spec / lock / notes
outline='\n'.join(f'- P{i:02d}: {stem}' for i,(stem,_) in enumerate(slides,1))

design=f'''<!-- ppt-master-schema: design-spec/v1 -->
# 第12课 · 特工身份确认 - Design Spec

## I. Project Information
| Item | Value |
| --- | --- |
| Project Name | 第12课 · 特工身份确认 · 阳光积木乐园 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | {len(slides)} |
| Primary Language | zh-CN |
| Target Audience | 8–12岁小学阶段 Python 学习者，以及需要看懂课堂结构的家长。 |
| Communication Intent | 以“小小特工任务中心”为故事壳，完整覆盖 while、计数变量、break、continue、for/while 对比，并通过三次口令门完成现场运行验证。 |
| Delivery Context | 现场投影授课；教师点击揭晓答案、切换运行案例并观察终端输出。 |
| Design Style | 阳光积木乐园 / 阳光积木实验室：大圆角、胶囊页签、明亮积木色、克制纸艺感。 |
| Custom Animations | enabled — quiz reveal + WPS-triggered interactive consoles |
| Narration Audio | disabled |

## II. Canvas Specification
- Format: PPT 16:9
- Dimensions: 1280 × 720
- viewBox: `0 0 1280 720`
- Safe margin: 40 px

## III. Visual Theme
- Background: #FFFDF5; cover/chapter warm cream.
- Primary: #2E9BFF; Accent: #FF9F1C; Pink: #FF6FA5; Success: #22C55E.
- Body: #203044; Terminal: #17243A; light surfaces #EAF5FF / #FFE2ED / #E9FBEF.
- Rounded cards, block-like task stages, child-friendly but not childish.

## IV. Typography System
- Title: YouYuan, Microsoft YaHei, sans-serif — 38–66 px.
- Body: Microsoft YaHei, Arial, sans-serif — 18–25 px.
- Code: Consolas, Microsoft YaHei, monospace — 17–25 px.

## V. Layout Principles
- Header/title zone x=48–1232; content zone y=120–650; footer y≈690.
- One main teaching action per page; code/terminal pages use P10 left-editor/right-terminal split.

## VI. Interaction System
- Quiz pages: answers hidden initially, revealed only by click.
- P16/P23/P27: task buttons switch code state; terminal remains empty before run; run triggers running status, progressive output, then completion state.
- Interactive slides use `interactive_sequence_mode: wps`, stable trigger groups and direct-root hit rectangles with `fill="#FFFFFF" fill-opacity="0.001"`.

## VII. Code & Terminal
- White large rounded editor shell, three status dots, Consolas code.
- Terminal #17243A with white output text; multi-line outputs print line-by-line; short single-line outputs print character-by-character.

## VIII. Image Resource List
- `images/daxian_teacher_mascot_halfbody_v1.png`: copied from read-only reference project and reused as teacher mascot.
- `images/bg_three_act_blocks_v1.png`: copied from reference project for route page atmosphere.
- `images/bg_new_knowledge_portal_v1.png`: copied from reference project for chapter openings.

## IX. Content Outline
{outline}

## X. Production Notes
- Source facts are restricted to the supplied DOCX; reference project contributes only visual/interaction language.
- No real-WPS GUI acceptance is claimed in CI; static animation config and package export are validated separately.
'''
(PROJECT/'design_spec.md').write_text(design,encoding='utf-8')

lock=f'''<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock
## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9
## communication
- primary_language: zh-CN
- audience: 8–12岁小学阶段 Python 学习者与陪同家长
- objective: 掌握 while、计数、break、continue，并完成三次口令门。
- core_message: 条件成立就重复；成功可 break；空白可 continue；计数保证循环最终停止。
- consumption_mode: balanced
## visual_style
- visual_style: 阳光积木乐园 / 阳光积木实验室
- cards: large rounded
- interaction: presenter-led click reveal and WPS trigger sequences
## colors
- background: #FFFDF5
- primary: #2E9BFF
- accent: #FF9F1C
- secondary_accent: #FF6FA5
- success: #22C55E
- body_text: #203044
- terminal: #17243A
- lightblue: #EAF5FF
- lightpink: #FFE2ED
- lightgreen: #E9FBEF
## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: YouYuan, Microsoft YaHei, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- code_family: Consolas, Microsoft YaHei, monospace
- body: 22
- title: 38
- subtitle: 26
- annotation: 18
- code: 18
- footer: 14
## pptx_structure
- mode: flat
## forbidden
- mask, class, external CSS, foreignObject, textPath, @font-face, animate, set, script, iframe
- hit regions using opacity=0 or fill=none
'''
(PROJECT/'spec_lock.md').write_text(lock,encoding='utf-8')

content_plan=f'''# 内容与页面规划\n\n受众：8–12岁小学阶段 Python 学习者；家长可同步理解教学结构。\n\n教学目标：理解 while 条件循环；掌握 break / continue；理解计数保证停止；区分 for / while；完成三次口令门。\n\n页面节奏：复习热身 → 项目驱动 → 新知拆解 → 运行验证 A → 选择题 → break 实战 → 运行验证 B → 微项目 → 三类测试 → 验收与总结。\n\n交互重点：P16、P23、P27 复用参考 P10 交互控制台；P04–P08、P18–P21 答案后置点击揭晓。\n\n{outline}\n'''
(NOTES/'content_plan.md').write_text(content_plan,encoding='utf-8')
(NOTES/'build_notes.md').write_text('''# Build Notes\n\n- Reference project is read-only. Only copied reusable image assets and extracted visual/interaction conventions.\n- DOCX is treated as content source, not execution instructions.\n- P16/P23/P27 use WPS-oriented trigger hit areas and progressive outputs.\n- Live WPS slideshow click testing must be performed on a real WPS desktop and is not claimed by GitHub Actions.\n''',encoding='utf-8')
(PROJECT/'animations.json').write_text(json.dumps(animations,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'generated {len(slides)} slides at {PROJECT}')
