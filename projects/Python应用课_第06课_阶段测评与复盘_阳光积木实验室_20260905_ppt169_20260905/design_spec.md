<!-- ppt-master-schema: design-spec/v1 -->
# Python应用课·第06课·阶段测评与复盘 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Python应用课·第06课·阶段测评与复盘·阳光积木实验室 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 36 |
| Primary Language | zh-CN |
| Target Audience | 已完成 Python turtle 前 5 课的小学阶段学习者，以及需要了解课堂进度与陪练方法的家长。 |
| Communication Intent | 用阶段测评回忆 turtle 核心命令，再教授显示/隐藏海龟与窗口标题，随后通过三次运行验证和微型 PBL，把花瓣、花心、花茎组合成可展示、可署名的小红花作品。 |
| Desired Audience Outcome | 学生能完成抢答与选择题，解释新增命令，按“运行基础版—只改一处—再运行—保存”完成并展示作品。 |
| Core Message / Ask / Action | 复盘不是背命令，而是把已经学会的积木重新组合，做出一朵真正属于自己的小红花。 |
| Delivery Context | 主要用于 120 分钟主讲人现场投影、点击揭晓和代码运行演示；次要用于课后复习与家长查看学习结构。 |
| Artifact Afterlife | 作为阶段测评、课堂演示、作品验收与课后复习材料重复使用。 |
| Reading Mode | presentation |
| Content Strategy | 严格覆盖 DOCX 的章节、题目、答案、代码、运行结果与顺序；按投影节奏把连续题目合并为双题页，但每题仍独立揭晓。参考项目只提供视觉语言、页面结构与交互机制。 |
| Design Style | 阳光积木实验室：大圆角积木卡、胶囊导航、纸艺层次、明亮课堂色与统一交互控制台。 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default, supporting a presenter-led 120-minute lesson |
| Custom Animations | enabled — explicit user request for button-triggered tasks, answer reveals, code switching and progressive output |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-05 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 48 px safe margin |
| Content Area | 1184 × 624 within x=48–1232, y=48–672 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional
- **Mode Behavior**: 以“复习闯关—新命令小实验—分段练习—微项目组装—展示复盘”为教学骨架；每个新命令先看用途，再看代码，再运行验证，题目始终先思考后揭晓。
- **Visual style**: custom
- **Visual Style References**: soft-rounded, paper-cut
- **Visual Style Behavior**: 延续参考项目的阳光积木语言：大圆角卡片、胶囊页签、浅层阴影、奶油留白和蓝橙粉绿积木；章节页使用切纸舞台和大编号，代码页使用统一三色圆点编辑器与深色终端，避免机械卡片矩阵。
- **Theme**: “小红花装配实验室”跨页母题：四盒彩色命令积木沿实验轨道逐步拼成花瓣、花心、花茎和完整作品。
- **Tone**: 明亮、耐心、有挑战感；适合儿童投影阅读，也让家长快速理解学习目标和验收标准。

### AI Image Strategy

- **Purpose**: 仅为 P13 和 P30 生成新的透明角色插画，替换旧海龟送花图；不生成整页背景或带文字的信息图。
- **Style anchor**: 以原有海龟角色作为风格参考，保持圆润三维玩具黏土质感、绿色海龟主体和蓝橙粉配色，但重新设计姿势、道具与教学情境。
- **P13 scene**: 海龟实验员佩戴护目镜，手持放大镜和三块无字命令牌，表达“观察新命令并马上实验”。
- **P30 scene**: 海龟工匠在小工作台上拼装六瓣积木花，表达“把代码零件组合成完整作品”。
- **Constraints**: PNG 透明背景；角色和关键道具完整；无文字、Logo、水印、额外人物或复杂场景；使用 `preserveAspectRatio="xMidYMid meet"` 完整显示。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFDF5 | 全局奶油底色 |
| Secondary background | #EAF5FF | 说明区与轻量分区 |
| Primary | #2E9BFF | 标题、主路径、主要按钮 |
| Accent | #FF9F1C | 任务、步骤、运行状态 |
| Secondary accent | #FF6FA5 | 花瓣、思考题、错误提示 |
| Body text | #203044 | 正文与代码说明 |
| Secondary text | #60758A | 注释、提示与页脚 |
| Divider | #CFE5F8 | 轻分隔线与边框 |
| Surface | #FFFFFF | 卡片和代码外壳 |
| Terminal | #17243A | 终端与运行窗口 |
| Success | #22C55E | 正确、完成与验收通过 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 圆润、亲和、课堂清楚 | YouYuan | Arial Rounded MT Bold | Microsoft YaHei, sans-serif |
| Body | 中性、投影易读 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽、字符辨识清楚 | Consolas | Consolas | Courier New, monospace |

- **Title stack**: YouYuan, Microsoft YaHei, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, Courier New, monospace
- **Role rationale**: 代码跨多页重复出现，固定使用 Consolas；标题继续采用参考项目的幼圆风格。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 30 |
| Title | 46 |
| Subtitle | 34 |
| Annotation | 20 |
| Chapter | 60 |
| Code | 20 |
| Compact code | 12.5 |
| Footer | 16 |
| Card heading | 28 |
| Chapter number | 176 |
| Answer emphasis | 36 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 标题给出当前学习动作，主舞台承载题目、代码或作品，底部用一句检查口令收束。
- **Composition tendency**: 章节页以大编号和舞台切换节奏；题目页使用双区独立揭晓；代码运行页完全沿用统一控制台心智模型。
- **Cross-page continuity**: 四盒彩卡、花朵零件、实验轨道、老师提示气泡反复出现；控制台的按钮、代码区、终端与状态区位置保持一致。
- **Spacing posture**: 依据 anchor / dense / breathing 节奏变化，互动页信息密度较高，章节与休息页保留大面积留白。
- **Spacing anchors**: page margin 48 px; block gap 24 px; column gutter 28 px; corner radius 28 px; body leading 42 px.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/code-circle | 代码、控制台、程序任务 |
| tabler-filled/book | 复习、规则、课堂小结 |
| tabler-filled/alert-triangle | 易错提醒 |
| tabler-filled/bulb | 思考与提示 |
| tabler-filled/device-desktop | 窗口、运行与观察结果 |
| tabler-filled/puzzle | 命令组合与工具箱 |
| tabler-filled/list-check | 检查清单与验收 |
| tabler-filled/star | 测评关卡与完成奖励 |
| tabler-filled/home | 回到中心 home() |
| tabler-filled/school | 课堂目标与路线 |
| tabler-filled/check | 正确答案与完成状态 |
| tabler-filled/eye | showturtle() |
| tabler-filled/palette | 颜色与个性化 |
| tabler-filled/flower | 小红花作品 |
| tabler-filled/player-play | 运行程序 |
| tabler-filled/device-floppy | 保存文件 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ref08_daxian_teacher_mascot_halfbody_v1.png | 1097 × 1434 | 0.76 | 封面右侧老师舞台 | transparent character cutout | 完整显示于右侧圆角舞台 | no-crop | user | Existing | 从用户指定第08课项目只读复制，只复用人物图片 | none | hero_page |
| ref08_bg_route_blocks_v1.png | 1672 × 941 | 1.78 | 本课路线的柔和积木背景 | full-page background | 全幅铺底，四关卡沿中轴排列 | adaptive | user | Existing | 从用户指定第08课项目只读复制，不复用原课程文字 | none | full_page |
| mascot_turtle_new_commands_v2.png | 1122 × 1402 | 0.80 | P13 新命令实验右侧海龟实验员 | transparent character cutout | 右侧圆形舞台内完整显示 | no-crop | ai | generated | 项目内既有 AI 生成透明角色图 | none | content |
| mascot_turtle_flower_workshop_v2.png | 1122 × 1402 | 0.80 | P30 微项目装配右侧海龟工匠 | transparent character cutout | 右侧圆形舞台内完整显示 | no-crop | ai | generated | 项目内既有 AI 生成透明角色图 | none | content |

## IX. Content Outline

### Part 0: 开场与路线

#### Slide 01 - 阶段测评与复盘
- **Audience move**: 从“要考试”转为期待用旧命令完成新作品。
- **Relationships**: 复习、实验、作品三项能力按课程进程递进。
- **Layout**: 复用第08课封面框架：左侧标题、三枚能力积木与文件运行卡，右侧老师圆角舞台；全部文字与任务替换为本课内容。
- **Title**: 阶段测评与复盘
- **Core message**: 把五课学过的积木重新组合，送出一朵会旋转的彩色花。
- **Content**: 主题“神奇海龟小画家” · 驱动问题 · 最终成果 `lesson06_red_flower.py`。
- **Images**: 老师形象完整显示。
- **Cover impact**: 绑定钩子“10 题热身 + 3 次实验 + 1 朵作品”。

#### Slide 02 - 今天的 120 分钟
- **Audience move**: 从课程标题到看清时间、章节和终点。
- **Relationships**: 抢答→项目启动→新知→练习A→选择题→休息→练习B→微项目→展示→小结。
- **Layout**: 复用第08课路线框架与背景素材：四个错落关卡、曲线连接、终点旗和课堂提示；阶段名称与时间全部来自本课教纲。
- **Title**: 今天的 120 分钟
- **Core message**: 每个阶段都有“想一想—做一做—验一验”。
- **Content**: 0–12 复习 · 12–20 启动 · 20–65 学与练 · 65–75 休息 · 75–120 项目与展示。

#### Slide 03 - 今天要带走什么
- **Audience move**: 从知道流程到理解学习目标和验收标准。
- **Relationships**: 三个目标共同支撑最终作品。
- **Layout**: 复用第08课三列两行卡片网格：上排三个学习目标，下排两项可观察表现与通关标准；不出现第08课知识内容。
- **Title**: 今天要带走什么
- **Core message**: 会综合、会新增命令、会按清单修改作品。
- **Content**: 综合移动/转向/循环/坐标/颜色/填充 · 认识 showturtle/hideturtle/title · 完成并展示作品。

### Part 1: 课前复习

#### Slide 04 - ① 十题热身赛
- **Audience move**: 从准备状态进入快速回忆。
- **Relationships**: 10 题按基础命令、循环位置、颜色填充分组。
- **Layout**: 复用第08课三列两行卡片网格，把旧命令分成五盒并保留一张热身玩法卡；只作为抢答前的知识地图。
- **Title**: ① 十题热身赛
- **Core message**: 先口答，再揭晓；答错不扣分，马上修正。
- **Content**: 手势或小白板抢答 · 每题约 40 秒 · 同桌可互助。

#### Slide 05 - 抢答规则
- **Audience move**: 从想抢答到知道怎样参与和复盘。
- **Relationships**: 听题→独立想→亮答案→口头修正。
- **Layout**: 四步环形轨道，最后连接“星星不扣分”。
- **Title**: 先想，再亮答案
- **Core message**: 快不是唯一目标，能说出为什么才算过关。
- **Content**: 口答/手势/小白板 · 同桌互助 · 答错立即修正。

#### Slide 06 - 热身 1–2
- **Audience move**: 从模糊记忆到说出导入与前进命令。
- **Relationships**: 两题并列且独立揭晓。
- **Title**: 热身 1–2 · 起步命令
- **Core message**: 模块先导入，海龟再前进。
- **Content**: 1 导入海龟模块怎么写？答案 `import turtle`。2 向前走用什么命令？答案 `forward()`。
- **Motion suggestion**: 两题初始只显示问题；各自点击后出现绿色答案与一句解释。

#### Slide 07 - 热身 3–4
- **Audience move**: 从会看循环到能指出重复结构与次数位置。
- **Relationships**: for 循环包含 range() 次数设置。
- **Title**: 热身 3–4 · 重复动作
- **Core message**: `for` 负责重复，`range()` 告诉它重复几次。
- **Content**: 3 重复动作使用什么结构？答案 for 循环。4 循环次数写在哪里？答案 range() 中。
- **Motion suggestion**: 分别点击揭晓；第二题揭晓后用包含关系连接两答案。

#### Slide 08 - 热身 5–6
- **Audience move**: 从记得位置命令到区分指定坐标与回中心。
- **Relationships**: goto()/setpos() 与 home() 形成目的地对比。
- **Title**: 热身 5–6 · 位置导航
- **Core message**: 一个去指定坐标，一个回到中心。
- **Content**: 5 移动到指定坐标用什么？`goto()` 或 `setpos()`。6 回到中心用什么？`home()`。
- **Motion suggestion**: 揭晓时分别点亮坐标旗与中心点。

#### Slide 09 - 热身 7–8
- **Audience move**: 从会改颜色到复述填充的开始与结束。
- **Relationships**: 线条颜色与封闭区域填充是装饰工具的两个层级。
- **Title**: 热身 7–8 · 颜色与填充
- **Core message**: `pencolor()/color()` 管颜色，`begin_fill()/end_fill()` 成对使用。
- **Content**: 7 设置线条颜色命令。8 开始和结束填充命令。
- **Motion suggestion**: 各自点击揭晓；填充答案成对同时出现。

#### Slide 10 - 热身 9–10
- **Audience move**: 从回忆背景与圆形命令到完成十题复盘。
- **Relationships**: 背景属于 Screen，圆属于 Turtle 绘制动作。
- **Title**: 热身 9–10 · 背景与圆
- **Core message**: `Screen().bgcolor()` 管舞台，`circle()` 画圆。
- **Content**: 9 设置背景色用什么？10 画圆常用什么命令？
- **Motion suggestion**: 两题独立揭晓；最后出现“10/10 热身完成”。

### Part 2: 项目启动与新知

#### Slide 11 - 项目启动：送你一朵小红花
- **Audience move**: 从答题切换到为同学创作作品。
- **Relationships**: 驱动问题连接花瓣、花心、花茎与署名展示。
- **Layout**: 柔和积木背景上，一朵大花由三块零件拼成，老师提出挑战。
- **Title**: 送你一朵小红花
- **Core message**: 怎样综合使用海龟命令，画一朵会旋转的彩色花？
- **Content**: 最终成果：可展示、可署名的小红花单元作品。
- **Images**: 使用积木背景与老师形象。

#### Slide 12 - 成功标准先看清
- **Audience move**: 从想做作品到知道怎样算完成。
- **Relationships**: 能运行、三部分完整、能说出修改点共同构成验收。
- **Title**: 做完，还要能讲出来
- **Core message**: 作品不是“看起来差不多”，而是能运行、够完整、说得清。
- **Content**: □ 基础版完整运行 · □ 花瓣/花心/花茎齐全 · □ 指出自己修改的一处。

#### Slide 13 - ② 新命令小实验
- **Audience move**: 从项目目标进入三个新增技能。
- **Relationships**: 显示/隐藏海龟、设置窗口标题、测试修改按教学顺序递进。
- **Layout**: 左侧三块实验任务卡，右侧使用新生成的“放大镜海龟与无字命令牌”透明角色插画。
- **Title**: ② 新命令小实验
- **Core message**: 每讲一个命令，马上运行一次。
- **Content**: showturtle() / hideturtle() · screen.title() · 小步测试。

#### Slide 14 - 四盒命令工具箱
- **Audience move**: 从零散命令到按作用分类。
- **Relationships**: 移动、重复、位置、装饰四类并列，共同服务作品。
- **Title**: 把命令放回四盒彩卡
- **Core message**: 想不起来命令时，先问“我现在要做哪一类动作？”
- **Content**: 移动 forward/left · 重复 for/range · 位置 goto/home/setheading · 装饰 color/fill/bgcolor。

#### Slide 15 - 显示与隐藏海龟
- **Audience move**: 从看见绘图光标到理解作品完成后可隐藏它。
- **Relationships**: showturtle() 与 hideturtle() 形成可逆对比。
- **Title**: 小海龟：上场 / 退场
- **Core message**: 显示方便观察，完成后隐藏让作品更整洁。
- **Content**: `t.showturtle()` 显示 · `t.hideturtle()` 隐藏 · 隐藏不会删除图形。

#### Slide 16 - 交互控制台：海龟上场与退场
- **Audience move**: 从理解用途到点击运行比较两段代码。
- **Relationships**: 两个任务共享同一实验流程，运行结果形成对比。
- **Title**: 海龟显隐实验站
- **Core message**: 选任务、看代码、运行、观察状态变化。
- **Content**: 任务 A 显示海龟；任务 B 隐藏海龟；短状态逐字符输出。
- **Motion suggestion**: WPS 任务切换重置旧代码和旧输出；运行后“运行中…”→逐字输出→完成状态。

#### Slide 17 - 给窗口起名字
- **Audience move**: 从会画图到知道如何给作品舞台命名。
- **Relationships**: Screen 对象拥有 title 方法，标题文字作为参数。
- **Title**: `screen.title()` 给画展挂牌
- **Core message**: `screen.title("小红花画展")` 会改变图形窗口标题。
- **Content**: 先创建 `screen = turtle.Screen()` · 再调用 `screen.title(...)` · 标题不画在画布内部。

#### Slide 18 - 交互控制台：三个窗口标题
- **Audience move**: 从看懂语法到切换并运行三个标题示例。
- **Relationships**: 三个任务只替换字符串参数，代码结构保持不变。
- **Title**: 窗口标题实验站
- **Core message**: 只改双引号里的文字，就能给作品换名字。
- **Content**: 小红花画展 / 我的海龟作品 / 送你一朵花；逐字符显示设置结果。
- **Motion suggestion**: 三任务按钮切换代码；每个运行按钮独立触发状态与逐字输出。

#### Slide 19 - 安全修改四步法
- **Audience move**: 从想一次改很多到采用可定位问题的小步迭代。
- **Relationships**: 运行基础版→只改一处→再运行→保存为顺序关系。
- **Title**: 一次只改一处
- **Core message**: 小步修改，更容易发现哪一步出了问题。
- **Content**: ①运行基础版 ②只改一处 ③再次运行 ④确认后保存。
- **Motion suggestion**: 四步依次揭示，结论“不要一次改很多处”最后出现。

### Part 3: 动手练习 A 与选择题

#### Slide 20 - 练习 A：六片花瓣
- **Audience move**: 从单个命令到读懂循环绘制花瓣的完整结构。
- **Relationships**: 设置颜色→循环 6 次→填充圆→左转 60°构成顺序。
- **Title**: 练习 A · 用循环画花瓣
- **Core message**: 6 次 × 60° = 一整圈，先不要改这两个数字。
- **Content**: 完整花瓣代码 · 运行结果“6 个粉色圆形花瓣围成一朵花” · 可改 orange/yellow/purple。

#### Slide 21 - 交互控制台：花瓣换色
- **Audience move**: 从阅读代码到运行三个颜色任务并观察花瓣预览。
- **Relationships**: 三任务共享 range(6)/left(60)，只对比颜色参数。
- **Title**: 花瓣颜色实验站
- **Core message**: 只改颜色，不动次数与角度。
- **Content**: 粉色基础版 / 橙色版 / 紫色版；输出按行显示“开始绘制→6片花瓣→完成”。
- **Motion suggestion**: 任务切换隐藏旧代码、旧输出和旧花朵预览；运行后逐行显示状态并揭示对应花朵。

#### Slide 22 - ③ 八题选择挑战
- **Audience move**: 从跟着写转为用手势独立判断。
- **Relationships**: 新命令、角度方向、测试方法、课程目标四组递进。
- **Layout**: 超大“03”与 A/B/C/D 四枚按钮积木，右侧老师举起选择牌。
- **Title**: ③ 八题选择挑战
- **Core message**: 先选 A/B/C/D，再点击揭晓；错题马上回到代码验证。
- **Content**: 每页两题，各题独立揭晓。

#### Slide 23 - 选择题 1–2
- **Audience move**: 从记忆名称到区分隐藏与显示。
- **Relationships**: 两题互为反向命令对比。
- **Title**: 选择题 1–2 · 显示还是隐藏
- **Core message**: `hideturtle()` 隐藏，`showturtle()` 显示。
- **Content**: 题1 隐藏海龟：A 正确。题2 重新显示：B 正确；保留全部 A/B/C/D 选项和解析。
- **Motion suggestion**: 每题点击后只显示本题正确色、错误色与解析。

#### Slide 24 - 选择题 3–4
- **Audience move**: 从识别标题命令到计算花瓣转角。
- **Relationships**: 标题方法与 6×60° 两题独立。
- **Title**: 选择题 3–4 · 标题与转角
- **Core message**: `screen.title()` 设置标题；6 片花瓣每次左转 60°。
- **Content**: 题3 答案 A；题4 答案 C；完整选项与解析。
- **Motion suggestion**: 两题独立揭晓，角度题揭晓后显示一圈 360°。

#### Slide 25 - 选择题 5–6
- **Audience move**: 从知道隐藏作用到判断花茎向下的方向角。
- **Relationships**: 作品整洁与方向控制两题独立。
- **Title**: 选择题 5–6 · 整洁与方向
- **Core message**: 隐藏图标不会删图；270° 通常朝下。
- **Content**: 题5 答案 A；题6 答案 D；完整选项与解析。
- **Motion suggestion**: 每题先投票，揭晓时显示正确答案和方向箭头。

#### Slide 26 - 选择题 7–8
- **Audience move**: 从选方法到说出本课真正目标。
- **Relationships**: 小步测试是完成综合作品的方法。
- **Title**: 选择题 7–8 · 方法与目标
- **Core message**: 每次改一处再运行，最终用综合命令完成作品。
- **Content**: 题7 答案 B；题8 答案 B；完整选项与解析。
- **Motion suggestion**: 两题独立揭晓；最后出现“8/8 挑战完成”。

#### Slide 27 - 课间保存站
- **Audience move**: 从连续练习切换到休息并保护进度。
- **Relationships**: 保存→休息眼睛和手指→回来先运行一次。
- **Title**: 保存好，再休息 10 分钟
- **Core message**: 文件名只用英文、数字和下划线：`lesson06_red_flower.py`。
- **Content**: Ctrl+S · 活动眼睛与手指 · 返回后先运行已有代码。

### Part 4: 练习 B 与微项目

#### Slide 28 - 练习 B：花心和花茎
- **Audience move**: 从花瓣扩展到花心、方向和粗线条。
- **Relationships**: dot 花心→setheading(270) 向下→pensize/pencolor→forward 花茎。
- **Title**: 练习 B · 花心 + 花茎
- **Core message**: 先点花心，再把方向设为 270° 向下画花茎。
- **Content**: 完整练习 B 代码 · 运行结果 · 可把 140 改为 100 或 180。

#### Slide 29 - 交互控制台：花茎长度
- **Audience move**: 从看懂代码到运行比较三种长度。
- **Relationships**: 100/140/180 三任务只改变 forward 参数。
- **Title**: 花茎长度实验站
- **Core message**: 只改一个数字，就能比较作品变化。
- **Content**: 短 / 标准 / 长三任务；输出逐行显示“方向 270°→长度→完成”。
- **Motion suggestion**: 切换代码和运行按钮；运行时逐行输出并显示对应长度预览。

#### Slide 30 - ④ 微项目装配站
- **Audience move**: 从两个小程序切换到组合完整作品。
- **Relationships**: 花瓣、花心、花茎、背景标题、隐藏海龟按装配顺序连接。
- **Layout**: 左侧三步装配清单，右侧使用新生成的“海龟在工作台拼装积木花”透明角色插画。
- **Title**: ④ 微项目 · 送你一朵小红花
- **Core message**: 不从空白重写，使用半成品逐段组合。
- **Content**: 基础版先成功 · 有余力再个性化。

#### Slide 31 - 完整作品代码地图
- **Audience move**: 从长代码压力转为看懂五个可管理的代码区块。
- **Relationships**: 窗口设置→创建海龟→花瓣循环→花心花茎→隐藏并结束。
- **Title**: 长代码，也是一块块拼起来的
- **Core message**: 每段只负责一件事，出错就回到对应区块检查。
- **Content**: 完整微项目代码，分为 5 个彩色区块；标记可改背景、花瓣色、花茎长、标题。

#### Slide 32 - 交互控制台：完整作品
- **Audience move**: 从代码地图到选择版本、运行并观察完整作品结果。
- **Relationships**: 基础版、暖色版、署名版共享结构，只改变 1–2 项。
- **Title**: 小红花作品实验站
- **Core message**: 先跑通基础版，再做一两个自己的修改。
- **Content**: 基础版 / 暖色花瓣版 / 自定义标题版；逐行状态与完整花朵预览。
- **Motion suggestion**: 三任务按钮；任务切换重置旧代码、旧输出与旧预览；运行逐行打印“窗口→花瓣→花心花茎→隐藏海龟→完成”。

#### Slide 33 - 五步完成桌面画展
- **Audience move**: 从看到成品到按可执行步骤完成自己的版本。
- **Relationships**: 分类复习→运行两个小程序→组合测试→修改 1–2 项→展示说明。
- **Title**: 从基础版走到个人作品
- **Core message**: 每一步完成后再走下一步。
- **Content**: DOCX 项目实施步骤 1–5。
- **Motion suggestion**: 五步沿路径依次出现，终点旗最后出现。

### Part 5: 展示、排错与离堂

#### Slide 34 - 作品验收与同伴建议
- **Audience move**: 从完成作品到能自检并友善表达建议。
- **Relationships**: 三项验收决定是否完成，四句展示句式支持表达。
- **Title**: 画展开始：检查，再分享
- **Core message**: 每人只提一条具体、友善、能行动的建议。
- **Content**: 三项验收框 · “我的作品是…/我使用了…/我修改了…/下一次我想…”。

#### Slide 35 - 三个常见问题
- **Audience move**: 从遇到混乱到知道第一步检查哪里。
- **Relationships**: 慢→speed(0)；方向错→setheading(270)；代码长→回到半成品逐段运行。
- **Title**: 卡住时，先查这三处
- **Core message**: 先检查最可能的原因，不要删掉全部重来。
- **Content**: 花瓣填充慢 · 花茎方向错误 · 作品代码较长；对应处理方法。
- **Motion suggestion**: 先显示问题，点击后依次揭晓处理方法，正确处理用绿色。

#### Slide 36 - 离堂小结
- **Audience move**: 从课堂结束到能口头复述命令、作品和排错动作。
- **Relationships**: 一个命令、一个作品、一个排错行动构成离堂表达。
- **Layout**: 三块能力积木汇聚为一朵小红花，老师在右侧挥手。
- **Title**: 今天，我把旧积木拼成了新作品
- **Core message**: 下次遇到报错，先检查拼写、符号和缩进。
- **Content**: “我会用的 1 个命令…” · “我完成的 1 个作品…” · “我下次先检查…”。
- **Closing impact**: 绑定行动“保存 `lesson06_red_flower.py`，向同伴说出自己修改的一处”。
- **Images**: 老师形象完整显示。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 逐页依据最终 SVG 编写，包含教师话术、点击提示、等待学生作答的停顿点、代码运行预期和分层支架；仅使用 DOCX 教学内容，不执行其中的操作性文本。
- **Total duration**: 120 minutes including a 10-minute break
- **Notes style**: 互动式、耐心、短句优先，先让学生回答再点击揭晓。
- **Presentation purpose**: 教学、阶段测评、作品实践与课后复习
