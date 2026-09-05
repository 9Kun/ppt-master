<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 已完成 Turtle 前四课的小学中年级儿童与陪同家长
- objective: 让孩子理解颜色、线宽、填充顺序与 circle 参数，独立补全、运行并展示一枚双层彩色徽章，家长能按验收清单陪练。
- core_message: 先选颜色和线宽，再把完整封闭图形夹在 begin_fill 与 end_fill 之间——代码就能把普通线条变成彩色徽章。
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: instructional
- mode_behavior: 以复习前置知识、看见颜色差异、拆解命令、运行观察、选择判断、补全作品和展示验收为教学骨架；每页承担一个学习动作，三次控制台分别验证彩色圆、填充正方形和双层徽章。

## visual_style
- visual_style: custom
- visual_style_references: soft-rounded, paper-cut
- visual_style_behavior: 大圆角卡、胶囊导航、舒适留白和浅层抬升构成统一积木界面；彩纸式色块、调色盘圆点、画笔色带与同心徽章提供纸切层次；代码框统一白色圆角外壳、三色窗口点和 Consolas，终端统一深蓝底；P11/P18/P20 维持顶部任务按钮、左侧编辑器、右上画布、右下终端与直接根点击命中区。

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
- light_orange: #FFF2DC
- light_pink: #FFE2ED
- light_green: #E9FBEF

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
- code: 20
- footer: 14
- card_heading: 28
- answer_emphasis: 36
- console_title: 40

## icons
- library: tabler-filled
- inventory: tabler-filled/palette, tabler-filled/pencil, tabler-filled/flask-2, tabler-filled/code-circle, tabler-filled/book, tabler-filled/bulb, tabler-filled/alert-triangle, tabler-filled/puzzle, tabler-filled/list-check, tabler-filled/circle-check, tabler-filled/check, tabler-filled/star, tabler-filled/flag, tabler-filled/trophy, tabler-filled/device-desktop, tabler-filled/player-play, tabler-filled/keyboard, tabler-filled/eye, tabler-filled/school, tabler-filled/writing, tabler-filled/heart, tabler-filled/home

## page_rhythm
- P01: anchor
- P02: dense
- P03: dense
- P04: dense
- P05: anchor
- P06: dense
- P07: dense
- P08: dense
- P09: breathing
- P10: dense
- P11: dense
- P12: dense
- P13: dense
- P14: dense
- P15: dense
- P16: breathing
- P17: dense
- P18: dense
- P19: dense
- P20: dense
- P21: dense
- P22: dense
- P23: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
