<!-- ppt-master-schema: design-spec/v1 -->
# Python应用课 第05课_多彩画笔大师 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Python应用课 第05课 · 多彩画笔大师 · 彩色徽章工坊 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 23 |
| Primary Language | zh-CN |
| Target Audience | 已完成 Turtle 前四课、会使用坐标移动和基础绘图命令的小学中年级儿童，以及需要快速掌握课堂目标与陪练方法的家长。 |
| Communication Intent | 用项目式课堂带孩子复习坐标与移动前置知识，依次理解画笔色、填充色、背景色、线宽、填充顺序与 circle 参数；每个重要知识都先观察、再写代码、再运行验证，最后完成一枚可个性化展示的双层彩色徽章。 |
| Desired Audience Outcome | 孩子能解释 pencolor、fillcolor、color 的区别，正确使用 begin_fill 与 end_fill 包住封闭图形代码，能调整 bgcolor、pensize/width、circle 的半径和 extent，并独立补全、运行、检查双层彩色徽章作品。 |
| Core Message / Ask / Action | 先选颜色和线宽，再把完整封闭图形夹在 begin_fill 与 end_fill 之间——代码就能把普通线条变成可展示的彩色徽章。 |
| Delivery Context | 主要用于教师现场投影、点击揭晓、WPS 放映交互与学生同步编程的 120 分钟课堂；次要用于孩子课后复习和家长按验收清单陪练。 |
| Artifact Afterlife | 作为第 5 课课堂主课件、教师讲稿、学生课后复习材料，并作为后续 Turtle 项目课的系列化视觉与交互基线。 |
| Reading Mode | balanced |
| Content Strategy | 以指定教案为唯一课程事实来源，保留 10 道第 4 课知识抢答、8 道本课选择题、三段运行验证和最终微型 PBL；允许为儿童理解重组页面节奏，但不引入教案未讲授的命令或几何推导。 |
| Design Style | 彩色徽章工坊：继承参考项目的阳光积木实验室、大圆角积木卡、胶囊导航、纸切层次、高对比代码终端和 WPS 控制台；跨页母题改为调色盘、画笔色带、同心徽章与颜色轨迹。 |
| AI Image Acquisition Path | not applicable — 本课使用本机 SVG 矢量绘制、渐变、纸切积木和代码画布，不新增 AI 图片 |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 用户明确要求生成教师讲稿 notes |
| Custom Animations | enabled — 用户明确要求知识揭晓、选择题揭晓、任务按钮、代码切换、运行状态、逐字输出和逐步绘图；交互页采用 WPS 模式 |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-08-30 |

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
- **Mode Behavior**: 以“复习前置知识 → 看见颜色差异 → 拆解命令 → 运行观察 → 选择判断 → 补全作品 → 展示验收”为教学骨架；每页承担一个学习动作，三次控制台运行分别验证彩色圆、填充正方形和双层徽章。
- **Visual style**: custom
- **Visual Style References**: soft-rounded, paper-cut
- **Visual Style Behavior**: soft-rounded 提供大圆角卡、胶囊导航、舒适留白和浅层抬升；paper-cut 提供像彩纸叠放一样的色块、徽章圆片和任务舞台。代码框统一为白色圆角外壳、三色窗口点和 Consolas；终端统一深蓝底。三张控制台维持“①选任务 → ②看代码 → ③运行 → ④看结果”，按钮上方使用直接根命中区。
- **Theme**: “彩色徽章工坊”跨页母题——蓝橙粉绿色带像画笔轨迹穿过页面；同心圆徽章从空心轮廓逐步增加边框色、填充色和背景色；页签与进度节点像调色盘色块。
- **Tone**: 明亮、清楚、可信、有动手感；儿童友好但不幼儿化，家长可快速扫描目标、步骤和验收标准。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFDF5 | 全局暖白背景；封面使用 #FFFCF1→#FFEFCB 渐变 |
| Secondary background | #EAF5FF | 解释区、画布外壳、家长提示 |
| Primary | #2E9BFF | 标题、导航、代码主线、主按钮 |
| Accent | #FF9F1C | 课堂动作、运行按钮、关键参数 |
| Secondary accent | #FF6FA5 | 思考题、易错提示、填充色强调 |
| Body text | #203044 | 正文与代码外说明 |
| Surface | #FFFFFF | 内容卡、代码编辑器、任务卡 |
| Terminal | #17243A | 终端输出区 |
| Divider | #CFE5F8 | 分隔线、网格和轨迹辅助 |
| Success | #22C55E | 正确答案、完成状态、验收通过 |
| Light orange | #FFF2DC | 参数与操作提示 |
| Light pink | #FFE2ED | 填充与错误提示 |
| Light green | #E9FBEF | 正确解析与完成提示 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 圆润、开口大、课堂亲和 | YouYuan | Arial Rounded MT Bold | Microsoft YaHei, sans-serif |
| Body | 清晰、中性、投影易读 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽、能区分 1/l、0/O、引号和括号 | Consolas | Consolas | Courier New, monospace |

- **Title stack**: YouYuan, Microsoft YaHei, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, Courier New, monospace
- **Role rationale**: Code 在语法卡、编辑器和终端中跨页复现，固定 Consolas 保证半角符号与缩进清楚可辨。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Annotation | 18 |
| Chapter | 58 |
| Code | 20 |
| Footer | 14 |
| Card heading | 28 |
| Answer emphasis | 36 |
| Console title | 40 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上标题或题号色块建立入口，右上课堂环节胶囊标记进度；代码与运行结果保持明显主次，一页只突出一个动作。
- **Composition tendency**: 概念页采用比喻图与准确技术解释并置；练习页用代码卡＋结果画布；控制台页固定为顶部任务按钮、左侧编辑器、右上画布、右下终端与状态区。
- **Cross-page continuity**: 画笔色带、调色盘圆点和同心徽章轮廓反复出现但不过度装饰；P11、P18、P20 保持同构控制台与稳定顶层组命名。
- **Spacing posture**: 封面、项目启动和离堂页留白充足；抢答、选择题与控制台页信息较密；所有页面遵守 40 px 安全边距。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/palette | 颜色、调色盘、课程主题 |
| tabler-filled/pencil | 画笔、写代码、修改参数 |
| tabler-filled/flask-2 | 命令实验站、运行验证 |
| tabler-filled/code-circle | 代码与程序 |
| tabler-filled/book | 复习与知识讲解 |
| tabler-filled/bulb | 思考题、口诀和提示 |
| tabler-filled/alert-triangle | 易错警示 |
| tabler-filled/puzzle | 选择题与补全挑战 |
| tabler-filled/list-check | 任务卡与验收清单 |
| tabler-filled/circle-check | 正确答案与完成状态 |
| tabler-filled/check | 正确项与验收通过 |
| tabler-filled/star | 闯关鼓励和作品亮点 |
| tabler-filled/flag | 课堂终点 |
| tabler-filled/trophy | 作品展示 |
| tabler-filled/device-desktop | Turtle 图形窗口 |
| tabler-filled/player-play | 运行程序按钮 |
| tabler-filled/keyboard | 输入代码 |
| tabler-filled/eye | 观察运行结果 |
| tabler-filled/school | 课堂环节导航 |
| tabler-filled/writing | 跟着写和补一补 |
| tabler-filled/heart | 友善建议与课间休息 |
| tabler-filled/home | 课后回看 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## IX. Content Outline

### Part 0: 开场与课堂航线

#### Slide 01 - 封面：多彩画笔大师

- **Audience move**: 从“今天又要画图”到期待亲手把黑白轮廓变成彩色徽章。
- **Layout**: 暖黄渐变舞台；左侧标题与三枚能力胶囊，右侧大型双层徽章由蓝色边框、黄色外圈、橙色内圈构成；画笔色带从代码卡流向徽章。
- **Title**: 多彩画笔大师
- **Core message**: 让边框、填充、背景和线宽一起工作，普通图形就能变成作品。
- **Content**: 眉标“Python 应用课 · 第 05 课”；主题阶段“神奇海龟小画家”；副题“给海龟岛的徽章加上颜色、粗线和填充”；能力胶囊“会配色 / 会填充 / 会改参数”。
- **Cover impact**: 绑定钩子“把一条普通黑线升级成一枚有边框、有填充色的彩色徽章”，用从空心圆到双层徽章的视觉转变表现。
- **Motion suggestion**: 空心轮廓先出现，边框色、外圈填充、内圈填充按作品层级依次进入。

#### Slide 02 - 两小时彩色探险航线

- **Audience move**: 从只看到课程标题到理解四个主要环节和 120 分钟时间分配。
- **Layout**: 四段横向色带像调色盘路径，依次连接到终点徽章；中部大卡显示四阶段，底部放课间休息提示与家长陪练句式。
- **Title**: 两小时彩色探险航线
- **Core message**: 15 分钟复习、45 分钟讲解、20 分钟选择题、40 分钟拓展编程，四关合计 120 分钟。
- **Content**: ①课前复习·知识抢答 15 分钟；②本课知识讲解 45 分钟；③本课选择题练习 20 分钟（65–75 分钟课间休息）；④拓展应用·编写并运行代码 40 分钟。家长提示：“每运行一次，都请孩子说出改了什么、结果为什么变。”
- **Motion suggestion**: 四段色带从左到右依次亮起，终点徽章最后完成。

### Part 1: 课前复习 · 第4课知识抢答

#### Slide 03 - 第4课知识抢答（1–5）

- **Audience move**: 从课前状态回到坐标与移动知识，敢于用短句口答。
- **Layout**: 五张横向题卡；初始只见问题和中性问号胶囊，点击后绿色答案胶囊与“为什么”解析同步出现。
- **Title**: 第4课知识抢答 · 1–5
- **Core message**: 坐标、goto 和 penup 是今天定位彩色图形的前置本领。
- **Content**: 1 屏幕中心坐标是什么？答案 `(0,0)`，解析“中心点的 x 和 y 都是 0”；2 x 正数通常向哪边？答案“向右”，解析“x 轴从中心向右增大”；3 y 正数通常向哪边？答案“向上”，解析“y 轴从中心向上增大”；4 goto 需要几个坐标数字？答案“两个，x 和 y”，解析“先写横向位置，再写纵向位置”；5 移动不留线要先做什么？答案 `penup()`，解析“抬起画笔后移动不会留下轨迹”。
- **Motion suggestion**: 每次点击揭晓一题，答案与解析同一拍出现。

#### Slide 04 - 第4课知识抢答（6–10）

- **Audience move**: 从回忆单个命令到能说出方向、标记与上节课作品。
- **Layout**: 与 P03 同构；底部最后出现“抢答小冠军”鼓励条。
- **Title**: 第4课知识抢答 · 6–10
- **Core message**: 回原点、改朝向、画标记和画圆弧，都是今天布置徽章的基础。
- **Content**: 6 `home()` 有什么作用？答案“回到中心原点”，解析“让海龟回到 `(0,0)`”；7 `setheading(90)` 让海龟朝哪边？答案“向上”，解析“90 度对应屏幕上方”；8 `dot()` 适合画什么？答案“实心圆点或地点标记”，解析“它能快速画出一个实心标记”；9 `circle()` 适合画什么？答案“圆或圆弧”，解析“本课还会给圆加粗线和填充”；10 上节课的微项目是什么？答案“海龟岛藏宝图”，解析“坐标和标记帮助我们完成了藏宝图”。
- **Motion suggestion**: 五题逐次揭晓；冠军条最后出现。

### Part 2: 本课知识讲解

#### Slide 05 - 项目启动：海龟岛彩色徽章

- **Audience move**: 从复习状态进入项目情境，明确最终作品和验收方向。
- **Layout**: 左侧驱动问题与黑白/彩色徽章对比，右侧最终成果卡与任务路线；建议文件名放在深色代码胶囊。
- **Title**: 项目启动 · 海龟岛彩色徽章
- **Core message**: 今天要让徽章有边框、有填充、有背景，还能通过改参数变出自己的版本。
- **Content**: 驱动问题“怎样给海龟岛的徽章加上颜色、粗线和填充？”；最终成果“一枚有边框、有填充色的双层彩色徽章”；重点命令 `color()` / `pencolor()` / `fillcolor()` / `begin_fill()` / `end_fill()` / `bgcolor()` / `pensize()` / `width()` / `circle()`；文件名 `lesson05_color_badge.py`。
- **Motion suggestion**: 黑白徽章先出现，彩色层与三张任务卡逐次进入。

#### Slide 06 - 三位颜色管理员

- **Audience move**: 从“颜色命令都一样”到能区分线条、内部和一次设置两者。
- **Layout**: 三张并列角色卡：线条管理员、填充管理员、双管家；下方放准确语法与一个小圆示意。
- **Title**: 三位颜色管理员
- **Core message**: `pencolor` 管边框，`fillcolor` 管里面，`color` 可以一次设置两者。
- **Content**: `t.pencolor("blue")` 设置线条颜色；`t.fillcolor("yellow")` 设置图形内部颜色；`t.color("red", "pink")` 第一个颜色是边框、第二个颜色是填充。课堂颜色词仅使用 red、blue、green、yellow、pink、orange。
- **Motion suggestion**: 三张角色卡依次亮起；最后出现“边框在前，填充在后”口诀。

#### Slide 07 - 填充三明治

- **Audience move**: 从记住两个命令到理解它们必须包住完整的封闭图形代码。
- **Layout**: 中央三层三明治：上层 `begin_fill()`、中层“完整封闭图形代码”、下层 `end_fill()`；右侧给正方形代码和闭合箭头。
- **Title**: 填充三明治
- **Core message**: 先开始填充，再画完整封闭图形，最后结束填充；顺序不能乱。
- **Content**: 比喻“begin_fill 是上面一片面包，完整图形代码是夹心，end_fill 是下面一片面包”；技术事实“填充区域来自两条命令之间绘制并闭合的路径”；易错提醒“少了 end_fill 或图形没有闭合，填充可能不完整”。
- **Motion suggestion**: 上层、夹心、下层按顺序进入；闭合箭头最后绕一圈。

#### Slide 08 - 背景和画笔粗细

- **Audience move**: 从只会改变图形颜色到会同时设置画布背景和线条粗细。
- **Layout**: 左侧背景舞台 `screen.bgcolor("lightyellow")`，右侧两支不同粗细画笔对比 `width(6)` 与 `pensize(3)`；底部准确结论卡。
- **Title**: 背景和画笔粗细
- **Core message**: `bgcolor` 改画布背景，`width` 和 `pensize` 都能改变线宽。
- **Content**: `screen = turtle.Screen()` 后用 `screen.bgcolor("lightyellow")`；`t.width(6)` 和 `t.pensize(6)` 作用相同，括号里是一个简单数字；线宽数字越大，线条越粗。
- **Motion suggestion**: 背景先换色，再让细线与粗线对比出现。

#### Slide 09 - circle 的两个数字

- **Audience move**: 从只会画圆到能读懂半径和 extent 的作用。
- **Layout**: 左侧整圆 `circle(60)`，右侧半圆 `circle(60,180)`，中间用两枚参数胶囊解释；不做几何推导。
- **Title**: circle 的两个数字
- **Core message**: 第一个数字主要表示半径；第二个数字 180 让海龟只画半圆。
- **Content**: `t.circle(60)` 画半径 60 的圆；`t.circle(60, 180)` 画同半径的半圆；本课只修改半径和 180，不讲几何原理。
- **Motion suggestion**: 整圆按路径画出，再切换为半圆并高亮 180。

#### Slide 10 - 练习A：彩色圆

- **Audience move**: 从读单条命令到能看懂一段完整程序并准备亲手输入。
- **Layout**: 左侧任务与 8 行代码卡，右侧淡黄色画布＋蓝色粗线圆；每行旁边用短标签说明作用。
- **Title**: 练习 A · 彩色圆
- **Core message**: 先创建画布与海龟，再设置背景、画笔色和线宽，最后画圆。
- **Content**: 代码 `import turtle`；`screen = turtle.Screen()`；`screen.bgcolor("lightyellow")`；`t = turtle.Turtle()`；`t.pencolor("blue")`；`t.width(6)`；`t.circle(70)`；`turtle.done()`。学生改一改：把 `width(6)` 换成 `pensize(3)`，比较线条粗细。
- **Motion suggestion**: 代码按逻辑分组揭示；运行结果最后出现。

#### Slide 11 - 交互控制台：彩色圆实验站

- **Audience move**: 从看懂代码到主动切换参数、点击运行并用结果解释差异。
- **Layout**: 复用参考控制台：顶部两个任务按钮“蓝色粗线圆 / 粉色细线圆”；左侧完整代码；右上画布逐段绘圆；右下终端逐字输出；状态区从“点击运行”到“绘制中”再到“作品完成”。
- **Title**: 彩色圆实验站
- **Core message**: 只改颜色和线宽，圆的轮廓就会呈现不同效果。
- **Content**: 任务 1：`pencolor("blue")`＋`width(6)`＋`circle(70)`；任务 2：`pencolor("pink")`＋`pensize(3)`＋`circle(70)`。运行前不显示圆；运行时将圆拆为 4 段依次绘制，终端逐字打印“蓝色粗线圆完成！”或“粉色细线圆完成！”。
- **Motion suggestion**: 任务按钮切换代码并重置旧画布/旧输出；运行按钮触发状态、四段圆弧、逐字输出和完成状态；允许反复点击。

### Part 3: 本课选择题练习

#### Slide 12 - 选择题 1–2

- **Audience move**: 从听讲到独立识别线条色与填充色命令。
- **Layout**: 左右双题卡；初始选项统一浅色，点击后正确项变绿并同步出现解析。
- **Title**: 选择闯关 · 第 1–2 题
- **Core message**: 线条颜色用 `pencolor`，内部颜色用 `fillcolor`。
- **Content**: 题1“设置画笔线条颜色可用？”A `pencolor()`（正确）B `range()` C `input()` D `type()`；解析“pencolor 专门设置线条颜色”。题2“设置填充颜色可用？”A `forward()` B `fillcolor()`（正确）C `home()` D `print()`；解析“fillcolor 设置封闭图形内部颜色”。
- **Motion suggestion**: 两次点击分别揭晓两题，正确颜色与解析同拍出现。

#### Slide 13 - 选择题 3–4

- **Audience move**: 从认识填充命令到判断正确的开始和结束位置。
- **Layout**: 双题卡，同 P12。
- **Title**: 选择闯关 · 第 3–4 题
- **Core message**: `begin_fill` 在画图前，`end_fill` 在封闭图形完成后。
- **Content**: 题3“开始填充前使用？”A `end_fill()` B `begin_fill()`（正确）C `penup()` D `done()`；解析“begin_fill 标记填充路径开始”。题4“完成封闭图形后使用？”A `end_fill()`（正确）B `begin_fill()` C `left()` D `setx()`；解析“end_fill 结束路径并显示填充”。
- **Motion suggestion**: 两题分别揭晓。

#### Slide 14 - 选择题 5–6

- **Audience move**: 从认命令到理解背景与线宽参数。
- **Layout**: 双题卡；题 6 旁放细线/粗线小图。
- **Title**: 选择闯关 · 第 5–6 题
- **Core message**: `bgcolor` 改画布背景，`pensize(6)` 表示线宽为 6。
- **Content**: 题5“设置背景颜色可用？”A `screen.bgcolor()`（正确）B `t.forward()` C `t.range()` D `print()`；解析“bgcolor 属于画布 Screen”。题6“`t.pensize(6)` 表示？”A 画6次 B 线宽为6（正确）C 走6步 D 转6度；解析“pensize 控制画笔粗细，不控制次数、距离或角度”。
- **Motion suggestion**: 两题分别揭晓。

#### Slide 15 - 选择题 7–8

- **Audience move**: 从读参数到能判断 circle 半径和填充三明治顺序。
- **Layout**: 双题卡；题 8 用三层小三明治辅助记忆。
- **Title**: 选择闯关 · 第 7–8 题
- **Core message**: `circle(50)` 的 50 主要是半径；填充必须“开始—画图—结束”。
- **Content**: 题7“`t.circle(50)` 中的 50 主要表示？”A 半径（正确）B 颜色 C 速度 D 名字；解析“circle 第一个参数控制圆的半径”。题8“填充代码正确顺序是？”A 画图-开始-结束 B 开始-画图-结束（正确）C 结束-画图-开始 D 开始-结束-画图；解析“填充命令必须包住完整封闭图形代码”。
- **Motion suggestion**: 两题分别揭晓，题 8 解析与三层顺序同拍出现。

#### Slide 16 - 课间休息

- **Audience move**: 从连续学习切换到有序休息，养成保存与返回后先运行的习惯。
- **Layout**: 中央大卡三步提醒，右侧调色盘计时器；留白充分。
- **Title**: 课间休息 · 10 分钟
- **Core message**: 先保存、再休息、回来先运行已有代码。
- **Content**: ①保存当前 `.py` 文件；②活动眼睛和手指；③返回后先运行一次已有代码，再继续修改。
- **Motion suggestion**: 三步依次出现，计时器最后亮起。

### Part 4: 拓展应用 · 编写并运行代码

#### Slide 17 - 练习B：填充正方形

- **Audience move**: 从会画彩色轮廓到能把填充三明治放进完整正方形程序。
- **Layout**: 左侧代码卡突出 `color("red", "pink")`、`begin_fill()`、循环和 `end_fill()`；右侧正方形从边框到粉色内部逐步完成。
- **Title**: 练习 B · 填充正方形
- **Core message**: `begin_fill` 在循环前，`end_fill` 在四条边闭合后。
- **Content**: 代码 `import turtle`；`t = turtle.Turtle()`；`t.color("red", "pink")`；`t.begin_fill()`；`for i in range(4):`；缩进 `t.forward(100)`、`t.right(90)`；`t.end_fill()`；`turtle.done()`。学生改一改：修改边框色、填充色和边长。
- **Motion suggestion**: 四条边逐次绘制，闭合后填充色出现。

#### Slide 18 - 交互控制台：填充正方形

- **Audience move**: 从读代码到通过运行对比理解颜色参数与边长变化。
- **Layout**: 顶部两个任务按钮“红边粉心 100 / 蓝边黄心 80”；左侧代码；右上画布逐边绘制并在闭合后填充；右下终端逐字输出。
- **Title**: 填充正方形实验站
- **Core message**: 边框色、填充色和边长都能改，但填充三明治顺序不变。
- **Content**: 任务 1：`color("red", "pink")`、边长 100；任务 2：`color("blue", "yellow")`、边长 80。点击运行后依次画四条边，闭合后显示填充，终端打印“填充正方形完成！”。
- **Motion suggestion**: WPS 任务按钮切换代码与运行按钮并清空旧状态；运行按钮触发四边绘制、填充、逐字输出和完成状态；可重复点击。

#### Slide 19 - 微项目：双层彩色徽章

- **Audience move**: 从完成单个填充图形到理解双层徽章的作品目标、步骤和学生需要修改的部分。
- **Layout**: 左侧四步任务卡“背景→外圈→移动→内圈”，中央半成品代码把颜色和半径标为可修改，右侧验收预览。
- **Title**: 微项目 · 海龟岛彩色徽章
- **Core message**: 两个填充圆叠在同一画布上，配合背景、线宽和位置，就能组成双层徽章。
- **Content**: 作品目标：淡蓝背景、黄色外圈、橙色内圈、清楚边框；输入是颜色卡、半径与 `goto` 的 y 数字；处理是按“设置→开始填充→画圆→结束填充”完成两圈；输出是双层彩色徽章。半成品代码保留 TODO：选择两组颜色；内圈半径在 50/65/75 中选择；若位置不理想只改 `goto(0, y)` 的 y。
- **Motion suggestion**: 四步任务卡沿徽章层级依次亮起，TODO 位置最后高亮。

#### Slide 20 - 交互控制台：徽章工坊

- **Audience move**: 从计划作品到点击运行、观察外圈与内圈依次完成，并对比个性化参数。
- **Layout**: 顶部两个任务按钮“经典徽章 100/65 / 我的徽章 100/50”；左侧完整代码；右上画布先绘并填外圈，再移动并绘内圈；右下终端分两行逐字/逐行打印；状态完成后显示“徽章完成”。
- **Title**: 海龟岛徽章工坊
- **Core message**: 每一层都要完成自己的填充三明治；参数变化必须对应徽章内圈大小变化。
- **Content**: 经典版：背景 `lightblue`，外圈 `navy/yellow` 半径 100，内圈 `red/orange` 半径 65；个性版：外圈不变，内圈半径 50。终端第一行“外圈完成”，第二行“内圈完成”，最后状态“作品完成！”。
- **Motion suggestion**: 任务按钮切换代码并重置旧输出与图形；运行后状态变“绘制中”，外圈 4 段绘制＋填充，内圈 4 段绘制＋填充，终端逐行输出，最后显示完成状态；支持反复点击。

#### Slide 21 - 代码挑战：补一补，再创造

- **Audience move**: 从观看标准答案到真正补全代码、做出自己的配色与尺寸决策。
- **Layout**: 左侧半成品代码留 5 个空位，右侧三档挑战卡“基础 / 进阶 / 创意”，底部运行验收路径。
- **Title**: 代码挑战 · 补一补，再创造
- **Core message**: 作品不是抄出来的——补全关键命令，再选择自己的颜色和半径。
- **Content**: 空位 1 背景色；空位 2 外圈 `begin_fill()`；空位 3 外圈 `end_fill()`；空位 4 内圈颜色；空位 5 内圈半径。基础版补对命令；进阶版修改两组颜色；创意版把内圈半径改为 50 或 75，并只在需要时调整 goto 的 y。运行路径“补代码→保存→运行→看图形→按清单修正”。
- **Motion suggestion**: 五个空位逐次高亮，三档挑战最后出现。

#### Slide 22 - 海龟修理站

- **Audience move**: 从遇错就求助到能按清单检查拼写、顺序、闭合和位置。
- **Layout**: 四张 2×2 易错卡，初始显示现象，点击后同步出现粉色原因和绿色修复；底部自救口诀。
- **Title**: 易错警示 · 海龟修理站
- **Core message**: 先看拼写，再看填充顺序和图形闭合，最后再调位置参数。
- **Content**: ①颜色名称拼错：只从颜色卡复制；② begin/end 位置颠倒：固定“开始—完整图形—结束”；③图形未封闭导致填充异常：检查循环次数和转角；④内圈位置不理想：只改 goto 的 y 数字，先不同时改多个参数。口诀“拼写对、顺序对、图形闭合、一次只改一个参数”。
- **Motion suggestion**: 四卡逐次揭晓，口诀最后出现。

#### Slide 23 - 作品验收、展示与离堂小结

- **Audience move**: 从“程序能跑”到会按标准验收、用完整句式展示并复述今天的本领。
- **Layout**: 左侧三项验收清单，中间作品展示句式深色卡，右侧三句离堂收获和回家任务；终点徽章盖章。
- **Title**: 作品验收 · 彩色徽章发布会
- **Core message**: 至少两种颜色、填充完整、背景或不同线宽至少一项——达标就能发布作品。
- **Content**: 验收：□至少使用两种颜色；□填充图形完整，没有漏掉 `end_fill()`；□包含背景或不同线宽中的至少一项。展示句式：“我的作品是……；我使用了……命令；我修改了……；下一次我想……”。同伴只提一条友善建议，关注颜色是否清楚、图形是否完整。离堂句：“今天我学会了画笔颜色；我完成了一枚有边框、有填充色的彩色徽章；下次报错先检查拼写、符号和缩进。”
- **Closing impact**: 绑定行动“回家把内圈半径换一个数字，做第二枚徽章并讲给家人听为什么变了”。
- **Motion suggestion**: 三项验收逐条亮起，展示句式进入，终点徽章最后盖章。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 逐页依据最终 SVG 编写；包含教师话术、课堂提问、停顿点、点击顺序、控制台运行顺序、课间提醒、错误现场处理、家长陪练提示与作品展示管理；比喻旁必须给出准确技术事实，不添加教案之外的几何推导或命令。
- **Total duration**: 120 minutes
- **Notes style**: 互动式、耐心、短句化；先让孩子预测，再点击验证，再说“为什么”。
- **Presentation purpose**: instruct, engage, practice, verify, and hand off a child-friendly coding project
