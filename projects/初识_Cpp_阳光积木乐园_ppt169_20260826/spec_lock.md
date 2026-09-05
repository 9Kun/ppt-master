<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 8–12 岁零基础孩子与陪同家长
- objective: 通过现场互动教学让孩子解释五要素并独立用 cout 输出文字、计算结果与图案，同时让家长掌握课后陪练清单。
- core_message: C++ 没那么神秘——一行 cout 就能让电脑说话、算结果、画图案，编程像搭积木一样好玩。
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: instructional
- mode_behavior: 以三幕课为骨架，将每个知识单元组织为看见任务、拆开零件、跟做验证、独立闯关、回顾迁移；标题说明学习动作，大仙老师负责路标，复用控制台作为一致实验站。

## visual_style
- visual_style: custom
- visual_style_references: soft-rounded, paper-cut
- visual_style_behavior: 大圆角卡片、胶囊页签、浅层阴影与舒适留白构成数字积木界面；切纸式层叠、哑光纹理和积木轨道提供跨页身份，代码框统一为白色圆角三点终端，页面用大色带、超大编号和不对称主舞台变化节奏。

## colors
- background: #FFFDF5
- secondary_bg: #EAF5FF
- primary: #2E9BFF
- accent: #FF9F1C
- secondary_accent: #FF6FA5
- body_text: #203044
- surface: #FFFFFF
- terminal: #17243A
- divider: #CFE5F8
- success: #22C55E
- image_rendering: custom
- image_rendering_references: vector-illustration, paper-cut
- image_rendering_behavior: 使用面向四年级孩子的现代二维教育动画比例、圆润可缩放的人物轮廓与克制分层；大仙老师采用约 3.5 头身感的大头半身构图，头部与眼睛明显放大但保持成人教师身份，日常偏严肃着装，透明背景，颜色服从演示文稿角色色。

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: YouYuan, Microsoft YaHei, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- code_family: Consolas, Courier New, monospace
- body: 24
- title: 44
- subtitle: 32
- annotation: 18
- chapter: 58
- code: 22
- footer: 14
- card_heading: 28
- chapter_number: 190
- answer_emphasis: 38
- pattern_display: 54

## icons
- library: tabler-filled
- inventory: tabler-filled/code-circle, tabler-filled/book, tabler-filled/alert-triangle, tabler-filled/bulb, tabler-filled/device-desktop, tabler-filled/puzzle, tabler-filled/list-check, tabler-filled/star, tabler-filled/calculator, tabler-filled/home, tabler-filled/school, tabler-filled/device-speaker, tabler-filled/check

## images
- teacher-mascot: images/daxian_teacher_mascot_halfbody_v1.png | source=ai | pattern=#A2-01 transparent sticker; enlarged face and gesture anchor the right edge or lower corner and interact with native speech bubbles | crop=no-crop
- p02-background: images/bg_three_act_blocks_v1.png | source=ai | pattern=full bleed behind native cards with a light warm wash | crop=adaptive
- p03-background: images/bg_new_knowledge_portal_v1.png | source=ai | pattern=full bleed; native title and steps remain editable above image | crop=adaptive
- devcpp-icon: images/devcpp_real_icon.png | source=user | pattern=contain inside the main tool card | crop=no-crop
- devcpp-new-file: images/devcpp_new_file_ai_v1.png | source=ai | pattern=contain inside rounded screenshot frame; native numbered callouts overlay | crop=no-crop
- devcpp-hello-code: images/devcpp_hello_code_ai_v1.png | source=ai | pattern=contain inside rounded screenshot frame; exact code labels remain native | crop=no-crop
- devcpp-compile-success: images/devcpp_compile_success_ai_v1.png | source=ai | pattern=contain inside rounded screenshot frame; native callouts mark save/compile/run | crop=no-crop
- hello-terminal: images/hello_world_terminal_real.png | source=user | pattern=contain inside dark rounded frame | crop=no-crop

## page_rhythm
- P01: anchor
- P02: dense
- P03: breathing
- P04: anchor
- P05: anchor
- P06: dense
- P07: dense
- P08: dense
- P09: breathing
- P10: dense
- P11: anchor
- P12: dense
- P13: dense
- P14: dense
- P15: dense
- P16: dense
- P17: dense
- P18: anchor
- P19: dense
- P20: anchor
- P21: dense
- P22: dense
- P23: dense
- P24: dense
- P25: dense
- P26: dense
- P27: anchor
- P28: dense
- P29: dense
- P30: dense
- P31: dense
- P32: breathing
- P33: dense
- P34: anchor
- P35: dense
- P36: dense
- P37: breathing
- P38: dense
- P39: dense
- P40: dense
- P41: breathing
- P42: dense
- P43: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
