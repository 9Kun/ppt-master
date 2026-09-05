#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path
from xml.etree import ElementTree as ET

PROJECT = Path("projects/Python应用课_第06课_阶段测评与复盘_阳光积木实验室_20260905_ppt169_20260905")
SVG_OUT = PROJECT / "svg_output"
SVG_FINAL = PROJECT / "svg_final"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

TOUCHED = {
    "06_热身1-2_起步命令.svg",
    "07_热身3-4_重复动作.svg",
    "08_热身5-6_位置导航.svg",
    "09_热身7-8_颜色填充.svg",
    "10_热身9-10_背景与圆.svg",
    "13_新命令小实验.svg",
    "15_显示与隐藏海龟.svg",
    "23_选择题1-2.svg",
    "24_选择题3-4.svg",
    "25_选择题5-6.svg",
    "26_选择题7-8.svg",
    "30_微项目装配站.svg",
    "35_三个常见问题.svg",
}

QUESTION_PAGES = {
    "23_选择题1-2.svg": [(1, "A", ["hideturtle() 只隐藏海龟图标，", "已经画好的图形会保留。"]), (2, "B", ["showturtle() 用来重新显示", "海龟图标。"])],
    "24_选择题3-4.svg": [(3, "A", ["screen.title(\"…\") 用来修改", "绘图窗口标题。"]), (4, "C", ["一圈 360° ÷ 6 片花瓣，", "每次应转 60°。"])],
    "25_选择题5-6.svg": [(5, "A", ["隐藏海龟能让最终作品更干净，", "也不会遮住图形。"]), (6, "D", ["turtle 中 270° 指向下方，", "适合画向下的花茎。"])],
    "26_选择题7-8.svg": [(7, "B", ["一次只改一处再运行，", "最容易发现是哪一步出错。"]), (8, "B", ["本课目标是综合多个命令，", "完成一幅可展示的小红花作品。"])],
}


def q(tag: str) -> str:
    return f"{{{NS}}}{tag}"


def parse_page(name: str):
    path = SVG_OUT / name
    tree = ET.parse(path)
    return path, tree, tree.getroot()


def find_id(root: ET.Element, element_id: str) -> ET.Element:
    for el in root.iter():
        if el.get("id") == element_id:
            return el
    raise RuntimeError(f"missing id={element_id}")


def write_page(path: Path, tree: ET.ElementTree) -> None:
    tree.write(path, encoding="utf-8", xml_declaration=False)


def set_tspan_x(text_el: ET.Element, x: str) -> None:
    for child in list(text_el):
        if child.tag == q("tspan"):
            child.set("x", x)


def overlay_warmup_answers() -> None:
    for name in sorted([n for n in TOUCHED if n[:2] in {"06", "07", "08", "09", "10"}]):
        path, tree, root = parse_page(name)
        for n, base_x in [(1, 76), (2, 678)]:
            group = find_id(root, f"answer-q{n}")
            rects = [el for el in list(group) if el.tag == q("rect")]
            texts = [el for el in list(group) if el.tag == q("text")]
            if not rects or len(texts) < 2:
                raise RuntimeError(f"unexpected answer group structure in {name} q{n}")
            rect = rects[0]
            rect.attrib.update({
                "x": str(base_x), "y": "360", "width": "526", "height": "112", "rx": "22",
                "fill": "#E9FBEF", "stroke": "#22C55E", "stroke-width": "2",
            })
            answer_text, why_text = texts[0], texts[1]
            answer_text.attrib.update({"x": str(base_x + 20), "y": "399", "font-size": "20", "fill": "#22C55E"})
            set_tspan_x(answer_text, str(base_x + 20))
            why_text.attrib.update({"x": str(base_x + 20), "y": "432", "font-size": "15", "fill": "#203044"})
            set_tspan_x(why_text, str(base_x + 20))
        write_page(path, tree)


def replace_scene_with_image(name: str, group_id: str, image_name: str) -> None:
    path, tree, root = parse_page(name)
    group = find_id(root, group_id)
    for child in list(group):
        group.remove(child)
    image = ET.SubElement(group, q("image"))
    image.attrib.update({
        "href": f"../images/{image_name}",
        "x": "990", "y": "204", "width": "240", "height": "312",
        "preserveAspectRatio": "xMidYMid meet",
    })
    write_page(path, tree)


def flower_group(group: ET.Element, cx: float, cy: float, show_cursor: bool) -> None:
    for child in list(group):
        group.remove(child)
    group.set("opacity", "1")
    # Stem first so petals sit above it.
    ET.SubElement(group, q("line"), {
        "x1": str(cx), "y1": str(cy + 34), "x2": str(cx), "y2": str(cy + 112),
        "stroke": "#22C55E", "stroke-width": "8", "stroke-linecap": "round",
    })
    petal_centers = [
        (cx, cy - 48), (cx + 42, cy - 24), (cx + 42, cy + 24),
        (cx, cy + 48), (cx - 42, cy + 24), (cx - 42, cy - 24),
    ]
    for px, py in petal_centers:
        ET.SubElement(group, q("circle"), {
            "cx": str(px), "cy": str(py), "r": "34", "fill": "#FFB9D0",
            "stroke": "#FF6FA5", "stroke-width": "3",
        })
    ET.SubElement(group, q("circle"), {
        "cx": str(cx), "cy": str(cy), "r": "24", "fill": "#FFE26A",
        "stroke": "#FF9F1C", "stroke-width": "3",
    })
    if show_cursor:
        # Tiny equilateral triangle: turtle cursor, intentionally simple.
        tx, ty, side = cx + 91, cy + 12, 24.0
        h = side * (3 ** 0.5) / 2
        points = f"{tx},{ty - 2*h/3} {tx - side/2},{ty + h/3} {tx + side/2},{ty + h/3}"
        ET.SubElement(group, q("polygon"), {
            "points": points, "fill": "#22C55E", "stroke": "#168A43", "stroke-width": "2",
        })


def revise_p15() -> None:
    name = "15_显示与隐藏海龟.svg"
    path, tree, root = parse_page(name)
    flower_group(find_id(root, "scene-decoration-p15-01"), 330, 300, True)
    flower_group(find_id(root, "scene-decoration-p15-02"), 952, 300, False)
    write_page(path, tree)


def revise_choice_states() -> None:
    rows = {"A": 300, "B": 358, "C": 416, "D": 474}
    for name, questions in QUESTION_PAGES.items():
        path, tree, root = parse_page(name)
        for qnum, correct, explanation_lines in questions:
            base_x = 76 if qnum % 2 == 1 else 678
            group = find_id(root, f"state-q{qnum}")
            for child in list(group):
                group.remove(child)
            for letter, y in rows.items():
                is_correct = letter == correct
                ET.SubElement(group, q("rect"), {
                    "x": str(base_x), "y": str(y), "width": "526", "height": "48", "rx": "16",
                    "fill": "#E9FBEF" if is_correct else "#FFE2ED",
                    "fill-opacity": "0.78",
                    "stroke": "#22C55E" if is_correct else "#FF6FA5",
                    "stroke-width": "2",
                })
            ex_x = base_x + 174
            ET.SubElement(group, q("rect"), {
                "x": str(ex_x), "y": "530", "width": "352", "height": "70", "rx": "18",
                "fill": "#FFF7E8", "stroke": "#FF9F1C", "stroke-width": "2",
            })
            txt = ET.SubElement(group, q("text"), {
                "x": str(ex_x + 18), "y": "556", "font-family": "Microsoft YaHei, Arial, sans-serif",
                "font-size": "15", "font-weight": "600", "fill": "#203044", "text-anchor": "start",
            })
            first = ET.SubElement(txt, q("tspan"), {"x": str(ex_x + 18), "dy": "0"})
            first.text = f"解析：{explanation_lines[0]}"
            second = ET.SubElement(txt, q("tspan"), {"x": str(ex_x + 18), "dy": "22"})
            second.text = explanation_lines[1]
        write_page(path, tree)


def txt(parent, x, y, text, size, fill="#203044", weight="400", anchor="start", family="Microsoft YaHei, Arial, sans-serif"):
    el = ET.SubElement(parent, q("text"), {
        "x": str(x), "y": str(y), "font-family": family, "font-size": str(size),
        "font-weight": str(weight), "fill": fill, "text-anchor": anchor,
    })
    el.text = text
    return el


def revise_p35() -> None:
    root = ET.Element(q("svg"), {
        "viewBox": "0 0 1280 720", "data-pptx-page-role": "content",
        "font-family": "Microsoft YaHei, Arial, sans-serif",
    })
    ET.SubElement(root, q("rect"), {"x":"0","y":"0","width":"1280","height":"720","rx":"0","fill":"#FFFDF5","id":"page-bg"})
    ET.SubElement(root, q("circle"), {"cx":"1210","cy":"35","r":"66","fill":"#EAF5FF","opacity":"0.9"})
    ET.SubElement(root, q("circle"), {"cx":"1250","cy":"95","r":"26","fill":"#FFE2ED","opacity":"0.9"})
    ET.SubElement(root, q("rect"), {"x":"34","y":"28","width":"16","height":"54","rx":"8","fill":"#FF9F1C"})
    txt(root, 64, 70, "卡住时，先查这三处", 40, weight="700", family="YouYuan, Microsoft YaHei, sans-serif")
    txt(root, 66, 100, "先检查最可能的原因，不要删掉全部重来", 17, fill="#60758A")
    ET.SubElement(root, q("rect"), {"x":"1000","y":"34","width":"210","height":"42","rx":"21","fill":"#EAF5FF"})
    txt(root, 1105, 62, "海龟修理站", 16, fill="#2E9BFF", weight="700", anchor="middle")
    ET.SubElement(root, q("rect"), {"x":"48","y":"655","width":"128","height":"42","rx":"21","fill":"#FFF2DC"})
    txt(root, 112, 683, "P35", 15, fill="#FF9F1C", weight="700", anchor="middle")

    cards = [
        (48,  "#EAF5FF", "#2E9BFF", "问题 1", "花瓣重复填充很慢", "使用 speed(0)", 1),
        (442, "#FFF2DC", "#FF9F1C", "问题 2", "花茎方向错误", "检查 setheading(270)", 2),
        (836, "#FFE2ED", "#FF6FA5", "问题 3", "作品代码较长", "回到半成品，逐段运行", 3),
    ]
    for x, tint, accent, badge, problem, fix, idx in cards:
        cx = x + 185
        ET.SubElement(root, q("rect"), {"x":str(x),"y":"138","width":"370","height":"482","rx":"30","fill":"#FFFFFF","stroke":"#CFE5F8","stroke-width":"2"})
        ET.SubElement(root, q("rect"), {"x":str(x),"y":"138","width":"370","height":"10","rx":"5","fill":accent})
        ET.SubElement(root, q("rect"), {"x":str(x+24),"y":"166","width":"120","height":"42","rx":"21","fill":tint})
        txt(root, x+84, 194, badge, 16, fill=accent, weight="700", anchor="middle")
        ET.SubElement(root, q("circle"), {"cx":str(cx),"cy":"292","r":"72","fill":tint})
        if idx == 1:
            # speedometer / fast-run symbol
            ET.SubElement(root, q("path"), {"d":f"M {cx-42} 310 A 46 46 0 0 1 {cx+42} 310", "fill":"none","stroke":accent,"stroke-width":"8","stroke-linecap":"round"})
            ET.SubElement(root, q("line"), {"x1":str(cx),"y1":"310","x2":str(cx+30),"y2":"278","stroke":accent,"stroke-width":"7","stroke-linecap":"round"})
            ET.SubElement(root, q("circle"), {"cx":str(cx),"cy":"310","r":"8","fill":accent})
        elif idx == 2:
            ET.SubElement(root, q("circle"), {"cx":str(cx),"cy":"292","r":"42","fill":"#FFFFFF","stroke":accent,"stroke-width":"4"})
            ET.SubElement(root, q("line"), {"x1":str(cx),"y1":"260","x2":str(cx),"y2":"315","stroke":accent,"stroke-width":"7","stroke-linecap":"round"})
            ET.SubElement(root, q("polygon"), {"points":f"{cx-14},307 {cx+14},307 {cx},326", "fill":accent})
        else:
            for yy, ww in [(266,88),(290,110),(314,72)]:
                ET.SubElement(root, q("rect"), {"x":str(cx-ww/2),"y":str(yy),"width":str(ww),"height":"12","rx":"6","fill":accent})
        txt(root, cx, 390, problem, 24, weight="700", anchor="middle")
        ET.SubElement(root, q("rect"), {"x":str(x+24),"y":"428","width":"154","height":"44","rx":"22","fill":"#FFF2DC"})
        txt(root, x+101, 457, "点击看修复", 16, fill="#FF9F1C", weight="700", anchor="middle")
        hit = ET.SubElement(root, q("g"), {"id":f"reveal-fix{idx}-hit","data-pptx-role":"decoration","data-pptx-bounds":"0 0 1280 720"})
        ET.SubElement(hit, q("rect"), {"x":str(x+24),"y":"428","width":"154","height":"44","rx":"22","fill":"#FFFFFF","opacity":"0.001"})
        g = ET.SubElement(root, q("g"), {"id":f"fix-{idx}","data-pptx-role":"decoration","data-pptx-bounds":"0 0 1280 720"})
        ET.SubElement(g, q("rect"), {"x":str(x+24),"y":"492","width":"322","height":"96","rx":"20","fill":"#E9FBEF","stroke":"#22C55E","stroke-width":"2"})
        txt(g, cx, 531, "修复建议", 15, fill="#22C55E", weight="700", anchor="middle")
        txt(g, cx, 566, fix, 17, fill="#203044", weight="700", anchor="middle")
    txt(root, 1220, 684, "阳光积木实验室 · 一次只做清楚一件事", 14, fill="#60758A", anchor="end")
    ET.ElementTree(root).write(SVG_OUT / "35_三个常见问题.svg", encoding="utf-8", xml_declaration=False)


def ensure_image_locks() -> None:
    design_path = PROJECT / "design_spec.md"
    design = design_path.read_text(encoding="utf-8")
    marker = "| ref08_bg_route_blocks_v1.png | 1672 × 941 | 1.78 | 本课路线的柔和积木背景 | full-page background | 全幅铺底，四关卡沿中轴排列 | adaptive | user | Existing | 从用户指定第08课项目只读复制，不复用原课程文字 | none | full_page |"
    rows = [
        "| mascot_turtle_new_commands_v2.png | 1122 × 1402 | 0.80 | P13 新命令实验主题角色 | transparent character illustration | 右侧完整显示，放大镜与无字命令牌保持可见 | no-crop | ai | Existing | 项目既有 AI 生成透明角色图，无文字与水印 | none | content_page |",
        "| mascot_turtle_flower_workshop_v2.png | 1122 × 1402 | 0.80 | P30 微项目装配主题角色 | transparent character illustration | 右侧完整显示海龟、工作台和积木花 | no-crop | ai | Existing | 项目既有 AI 生成透明角色图，无文字与水印 | none | content_page |",
    ]
    if rows[0] not in design:
        design = design.replace(marker, marker + "\n" + "\n".join(rows))
        design_path.write_text(design, encoding="utf-8")

    lock_path = PROJECT / "spec_lock.md"
    lock = lock_path.read_text(encoding="utf-8")
    anchor = "- route-background: images/ref08_bg_route_blocks_v1.png | source=user | crop=adaptive"
    lock_rows = [
        "- p13-new-command-mascot: images/mascot_turtle_new_commands_v2.png | source=ai | crop=no-crop",
        "- p30-flower-workshop-mascot: images/mascot_turtle_flower_workshop_v2.png | source=ai | crop=no-crop",
    ]
    if lock_rows[0] not in lock:
        lock = lock.replace(anchor, anchor + "\n" + "\n".join(lock_rows))
        lock_path.write_text(lock, encoding="utf-8")


def sync_touched_to_final() -> None:
    SVG_FINAL.mkdir(parents=True, exist_ok=True)
    for name in TOUCHED:
        shutil.copy2(SVG_OUT / name, SVG_FINAL / name)


def main() -> None:
    overlay_warmup_answers()
    replace_scene_with_image("13_新命令小实验.svg", "scene-decoration-p13-01", "mascot_turtle_new_commands_v2.png")
    revise_p15()
    revise_choice_states()
    replace_scene_with_image("30_微项目装配站.svg", "scene-decoration-p30-01", "mascot_turtle_flower_workshop_v2.png")
    revise_p35()
    ensure_image_locks()
    sync_touched_to_final()
    print("Lesson06 visual revision round 2 applied")
    print("Touched pages:", ", ".join(sorted(TOUCHED)))


if __name__ == "__main__":
    main()
