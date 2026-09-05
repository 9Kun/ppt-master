<!-- ppt-master-schema: spec-lock/v1 -->
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
- chapter_number: 180
- section_title: 56
- counter_display: 70

## icons
- library: none
- inventory: none

## images
- teacher-mascot: images/daxian_teacher_mascot_halfbody_v1.png | source=user | crop=no-crop
- route-background: images/bg_three_act_blocks_v1.png | source=user | crop=adaptive
- chapter-background: images/bg_new_knowledge_portal_v1.png | source=user | crop=adaptive

## page_rhythm
- P01: anchor
- P02: anchor
- P03: breathing
- P04: dense
- P05: dense
- P06: dense
- P07: dense
- P08: dense
- P09: anchor
- P10: anchor
- P11: breathing
- P12: dense
- P13: dense
- P14: dense
- P15: breathing
- P16: dense
- P17: dense
- P18: dense
- P19: dense
- P20: dense
- P21: dense
- P22: anchor
- P23: dense
- P24: breathing
- P25: anchor
- P26: dense
- P27: dense
- P28: dense
- P29: dense
- P30: breathing
- P31: dense
- P32: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
- 不使用 opacity="0" (user)
- 不使用 fill="none" 作为交互命中区域 (user)
