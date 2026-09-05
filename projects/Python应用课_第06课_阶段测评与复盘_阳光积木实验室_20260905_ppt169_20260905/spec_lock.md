<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 已完成 Python turtle 前 5 课的小学阶段学习者与陪同家长
- objective: 通过现场测评、命令实验和微项目，让学生能综合已有 turtle 命令、解释三个新增命令，并按小步测试流程完成可展示的小红花作品。
- core_message: 复盘不是背命令，而是把已经学会的积木重新组合，做出一朵真正属于自己的小红花。
- consumption_mode: presentation

## mode
- mode: custom
- mode_references: instructional
- mode_behavior: 以复习闯关、新命令小实验、分段练习、微项目装配、展示复盘为教学骨架；每个新命令先看用途，再看代码，再运行验证，题目始终先思考后揭晓。

## visual_style
- visual_style: custom
- visual_style_references: soft-rounded, paper-cut
- visual_style_behavior: 大圆角卡片、胶囊页签、浅层阴影和奶油留白构成阳光积木实验室；章节页使用切纸舞台和大编号，代码页统一为三色圆点编辑器与深色终端，控制装饰密度并保留投影清晰度。

## colors
- background: #FFFDF5
- secondary_bg: #EAF5FF
- primary: #2E9BFF
- accent: #FF9F1C
- secondary_accent: #FF6FA5
- body_text: #203044
- secondary_text: #60758A
- divider: #CFE5F8
- surface: #FFFFFF
- terminal: #17243A
- success: #22C55E

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: YouYuan, Microsoft YaHei, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- code_family: Consolas, Courier New, monospace
- body: 30
- title: 46
- subtitle: 34
- annotation: 20
- chapter: 60
- code: 20
- compact_code: 12.5
- footer: 16
- card_heading: 28
- chapter_number: 176
- answer_emphasis: 36
- micro_label: 23
- compact_body: 24
- route_label: 25
- display_heading: 40
- section_heading: 42
- hero_heading: 54

## icons
- library: tabler-filled
- inventory: tabler-filled/code-circle, tabler-filled/book, tabler-filled/alert-triangle, tabler-filled/bulb, tabler-filled/device-desktop, tabler-filled/puzzle, tabler-filled/list-check, tabler-filled/star, tabler-filled/home, tabler-filled/school, tabler-filled/check, tabler-filled/eye, tabler-filled/palette, tabler-filled/flower, tabler-filled/player-play, tabler-filled/device-floppy

## images
- teacher-mascot: images/ref08_daxian_teacher_mascot_halfbody_v1.png | source=user | crop=no-crop
- route-background: images/ref08_bg_route_blocks_v1.png | source=user | crop=adaptive
- turtle-new-commands: images/mascot_turtle_new_commands_v2.png | source=generated | crop=no-crop
- turtle-flower-workshop: images/mascot_turtle_flower_workshop_v2.png | source=generated | crop=no-crop

## page_rhythm
- P01: anchor
- P02: dense
- P03: anchor
- P04: breathing
- P05: dense
- P06: dense
- P07: dense
- P08: dense
- P09: dense
- P10: dense
- P11: anchor
- P12: dense
- P13: breathing
- P14: dense
- P15: dense
- P16: dense
- P17: dense
- P18: dense
- P19: anchor
- P20: dense
- P21: dense
- P22: breathing
- P23: dense
- P24: dense
- P25: dense
- P26: dense
- P27: breathing
- P28: dense
- P29: dense
- P30: breathing
- P31: dense
- P32: dense
- P33: dense
- P34: dense
- P35: dense
- P36: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
- “参考项目只用于提炼和复用艺术风格、页面结构与交互机制，严禁修改或覆盖参考项目。” (user)
- “不允许进入页面时直接显示最终输出” (user)
- “不允许所有动画对象在初始画面叠加显示” (user)
