from pathlib import Path

project = Path('projects/第12课_特工身份确认_阳光积木乐园_ppt169_20260906')
svg_dir = project / 'svg_output'
stems = [p.stem for p in sorted(svg_dir.glob('*.svg'))]
assert len(stems) == 32, len(stems)

roster=[]
for i, stem in enumerate(stems, 1):
    name = stem.split('_',1)[1] if '_' in stem else stem
    roster.append(f'''#### Slide {i:02d} - {name}\n\n- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。\n- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。\n- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。\n- **Title**: {name}\n- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。\n- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。\n''')

outline='\n'.join(roster)
design=f'''<!-- ppt-master-schema: design-spec/v1 -->
# 第12课 · 特工身份确认 · 阳光积木乐园 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 第12课 · 特工身份确认 · 阳光积木乐园 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 32 |
| Primary Language | zh-CN |
| Target Audience | 8–12 岁小学阶段 Python 学习者，以及需要看懂课堂结构的家长。 |
| Communication Intent | 以“小小特工任务中心”为故事壳，按复习→新知→示例→运行验证→练习→微项目→总结的顺序教授 while、计数变量、break、continue 与 for/while 对比。 |
| Desired Audience Outcome | 学生能解释 while、break、continue 的作用，能保证循环最终停止，并完成最多三次、空白不计次、正确可提前结束的口令验证器。 |
| Core Message / Ask / Action | 条件成立就重复；计数让循环有机会停止；成功可 break；空白可 continue。 |
| Delivery Context | 教师现场投影授课，包含点击揭晓答案、切换运行案例、点击运行并观察终端输出。 |
| Artifact Afterlife | 作为学生课后复习、家长回看课堂结构和教师再次授课的可复用课件。 |
| Reading Mode | balanced |
| Content Strategy | 严格以第12课 DOCX 教纲为内容来源；参考 C++ 项目仅复用阳光积木乐园的视觉语言、页面节奏与交互机制，不复用其知识内容或页数。 |
| Design Style | 阳光积木乐园 / 阳光积木实验室：大圆角积木卡、胶囊页签、亮蓝橙粉配色、奶油暖底与深色终端。 |
| AI Image Acquisition Path | not applicable — reuse existing project-local reference assets only |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | disabled — user requires project notes directory, not presenter speaker notes |
| Custom Animations | enabled — click reveal plus WPS-oriented task/run trigger sequences |
| Narration Audio | disabled — no narration requested |
| Created Date | 2026-09-06 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 40 px safe margin |
| Content Area | 1200 × 640 within x=40–1240, y=40–680 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional
- **Mode Behavior**: 以课堂任务推进为骨架，每页只承担一个学习动作；代码需要验证时统一进入控制台实验站。
- **Visual style**: custom
- **Visual Style References**: soft-rounded, paper-cut
- **Visual Style Behavior**: 大圆角卡片、胶囊页签、积木步骤块、克制的分层纸感；代码框统一三色圆点，终端统一深蓝黑。
- **Theme**: 小小特工任务中心里的阳光积木实验室。
- **Tone**: 明亮、可靠、有互动感，儿童友好但不低幼。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFDF5 | 全局暖白背景 |
| Secondary background | #EAF5FF | 浅蓝解释与分区卡 |
| Primary | #2E9BFF | 标题、导航、主任务 |
| Accent | #FF9F1C | 课堂动作、运行与重点 |
| Secondary accent | #FF6FA5 | 思考、易错、揭晓 |
| Body text | #203044 | 正文 |
| Secondary text | #7A8A9B | 页脚、辅助说明 |
| Divider | #CFE5F8 | 卡片边界与轻分隔 |
| Success | #22C55E | 正确、完成、成功状态 |
| Terminal | #17243A | 终端背景 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 圆润、课堂亲和 | YouYuan | Arial Rounded MT Bold | Microsoft YaHei, sans-serif |
| Body | 清晰、中性、投影易读 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽、字符可辨 | Consolas | Consolas | Microsoft YaHei, monospace |

- **Title stack**: YouYuan, Microsoft YaHei, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, Microsoft YaHei, monospace

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 38 |
| Subtitle | 26 |
| Annotation | 18 |
| Code | 18 |
| Footer | 14 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 标题/任务 → 主内容 → 反馈/结论。
- **Composition tendency**: 概念页以不对称大卡片为主；练习页留出明确的题目与揭晓区；运行页固定左代码右终端。
- **Cross-page continuity**: 蓝橙粉绿任务色、圆角、三色代码窗圆点、深色终端贯穿全套。
- **Spacing posture**: variable by page rhythm。
- **Spacing anchors**: page margin 40 px; block gap 24 px; column gutter 24 px; corner radius 30 px; body leading 1.35×。

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| daxian_teacher_mascot_halfbody_v1.png | 1144 × 1430 | 0.80 | 封面教师卡通形象 | Existing | transparent sticker | no-crop | user | Existing | copied from read-only style reference project | none | hero_page |
| bg_three_act_blocks_v1.png | 1672 × 941 | 1.78 | 任务路线背景 | Existing | full-page atmosphere | adaptive | user | Existing | copied from read-only style reference project | none | content_page |
| bg_new_knowledge_portal_v1.png | 1672 × 941 | 1.78 | 章节开启背景 | Existing | full-page atmosphere | adaptive | user | Existing | copied from read-only style reference project | none | section_page |

## IX. Content Outline

### Part 1: 第12课 · 特工身份确认

{outline}

## X. Speaker Notes Requirements

- **Generation**: disabled
'''
(project/'design_spec.md').write_text(design,encoding='utf-8')

rhythms=[]
anchors={1,2,9,10,22,25,32}
breathing={3,11,15,24,30}
for i in range(1,33):
    r='anchor' if i in anchors else 'breathing' if i in breathing else 'dense'
    rhythms.append(f'- P{i:02d}: {r}')
lock=f'''<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 8–12岁小学阶段 Python 学习者与陪同家长
- objective: 学生能解释并使用 while、计数、break、continue，完成最多三次且空白不计次的口令验证器。
- core_message: 条件成立就重复；计数保证停止；成功 break；空白 continue。
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: instructional
- mode_behavior: 以任务驱动的课堂递进组织内容，运行验证统一进入控制台实验站。

## visual_style
- visual_style: custom
- visual_style_references: soft-rounded, paper-cut
- visual_style_behavior: 复用阳光积木乐园的大圆角、胶囊、明亮积木色与克制纸感；代码和终端保持统一实验台结构。

## colors
- background: #FFFDF5
- secondary_bg: #EAF5FF
- primary: #2E9BFF
- accent: #FF9F1C
- secondary_accent: #FF6FA5
- success: #22C55E
- body_text: #203044
- secondary_text: #7A8A9B
- terminal: #17243A
- divider: #CFE5F8

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

## icons
- library: none
- inventory: none

## images
- teacher-mascot: images/daxian_teacher_mascot_halfbody_v1.png | source=user | crop=no-crop
- route-background: images/bg_three_act_blocks_v1.png | source=user | crop=adaptive
- chapter-background: images/bg_new_knowledge_portal_v1.png | source=user | crop=adaptive

## page_rhythm
{chr(10).join(rhythms)}

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
- 不使用 opacity="0" (user)
- 不使用 fill="none" 作为交互命中区域 (user)
'''
(project/'spec_lock.md').write_text(lock,encoding='utf-8')
print('schema artifacts rewritten')
