<!-- ppt-master-schema: design-spec/v1 -->
# 初识 C++ · 阳光积木乐园 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 初识 C++ · 阳光积木乐园 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 43 |
| Primary Language | zh-CN |
| Target Audience | 8–12 岁零基础孩子，以及陪同学习、需要理解课堂结构与课后练习清单的家长。 |
| Communication Intent | 以教学为主线：先认识 C++ 与开发环境，再通过“让电脑说话—输出多行—输出计算结果—输出星号图案”逐步掌握 cout；穿插思考题、易错警示与练习，让家长同步看懂每阶段目标和陪练方法。 |
| Desired Audience Outcome | 孩子能用比喻解释头文件、命名空间、main、cout、return 0 五要素，并独立用 cout 输出文字、计算结果和星号图案；家长能依据编程题清单陪练并判断常见错误。 |
| Core Message / Ask / Action | C++ 没那么神秘——一行 cout 就能让电脑说话、算结果、画图案，编程像搭积木一样好玩。 |
| Delivery Context | 主要用于主讲人现场投影授课并点击讲解；次要用于孩子课后复习、家长回看课堂结构与练习清单。 |
| Artifact Afterlife | 作为孩子课后复习材料、家长陪练指南和后续 C++ 入门课程的可复用课堂课件。 |
| Reading Mode | balanced |
| Content Strategy | 保留 43 页页码、三幕教学骨架与全部核心知识点；严格按用户文件夹中 `xx.yy` 素材的页码与点击层级恢复教学节奏，并维持 P16/P23/P29/P33 对 P10 的完全复用。素材画面只作知识与交互参考，水印不进入成品。 |
| Design Style | 阳光积木实验室：大圆角积木卡、胶囊导航、层叠纸感与高对比代码终端。 |
| Formula Policy | text-only |
| AI Image Acquisition Path | host-native |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy confirmed by user |
| Custom Animations | enabled — user requested presenter-led click animation; reveal scope only, not all-motion auto-play |
| Narration Audio | disabled — final Stage-2 proactive policy confirmed by user |
| Created Date | 2026-08-26 |

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
- **Mode Behavior**: 以三幕课为骨架，将每个知识单元组织为“看见任务—拆开零件—跟做验证—独立闯关—回顾迁移”；标题直接说明学习动作，大仙老师负责提问、提醒与阶段路标，复用控制台作为一致的动手实验站。
- **Visual style**: custom
- **Visual Style References**: soft-rounded, paper-cut
- **Visual Style Behavior**: soft-rounded 负责大圆角卡片、胶囊页签、浅层阴影与舒适留白；paper-cut 负责积木块般的前后层次、切纸式章节舞台和少量哑光纹理。代码框统一为白色圆角终端卡与三色圆点，页面通过大色带、阶梯积木、超大编号和不对称主舞台改变节奏，避免重复卡片网格。
- **Theme**: “积木轨道”跨页母题——圆角积木砖组成从左上到右下的学习路径；章节页放大为舞台，内容页缩小为页签、进度块或步骤节点。
- **Tone**: 阳光、可信、清楚、有动手感；儿童友好但不幼儿化，家长信息始终可扫描。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFDF5 | 全局暖白底色；P01 使用 #FFFCF1→#FFEFCB 暖黄渐变，P02/P03 使用指定 AI 积木背景作为页级例外 |
| Secondary background | #EAF5FF | 解释区、家长提示区、轻量分区 |
| Primary | #2E9BFF | 标题、导航、核心步骤与主按钮 |
| Accent | #FF9F1C | 课堂动作、关卡编号、关键结果 |
| Secondary accent | #FF6FA5 | 思考题、易错提示、次级强调 |
| Body text | #203044 | 正文与主要代码外说明 |
| Surface | #FFFFFF | 卡片、代码框、控制台面板 |
| Terminal | #17243A | 终端预览与控制台深色屏幕 |
| Divider | #CFE5F8 | 轻分隔线、网格与路线辅助 |
| Success | #22C55E | 运行成功、正确答案与完成状态 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: vector-illustration, paper-cut
- **Visual**: 面向四年级孩子的现代二维教育动画角色：头身比例更卡通、轮廓更圆润，配合少量分层纸艺质感，在大屏与小角标中都能稳定识别。
- **Mood**: 像儿童科学馆的专业卡通导览老师：明快、亲切、可靠，但仍保持成人教师气质。
- **Image Rendering Behavior**: vector-illustration 负责略放大的头部与眼睛、圆润手脚、简洁可缩放的面部和姿态；paper-cut 负责克制的层叠纸边、哑光材质和柔和投影。保留人物身份辨识度与成人属性，采用约 5.5–6 头身的教育动画比例，日常偏严肃着装，避免幼儿化与写实时装插画感，透明背景，颜色服从演示文稿角色色。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 圆润、开口大、课堂亲和 | YouYuan | Arial Rounded MT Bold | Microsoft YaHei, sans-serif |
| Body | 清晰、中性、投影易读 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽、字符可辨 | Consolas | Consolas | Courier New, monospace |

- **Title stack**: YouYuan, Microsoft YaHei, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, Courier New, monospace
- **Role rationale**: Code 在多页反复出现，必须固定为 Consolas 以区分 `1/l`、`0/O`、半角符号与缩进。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Annotation | 18 |
| Chapter | 58 |
| Code | 22 |
| Footer | 14 |
| Card heading | 28 |
| Chapter number | 190 |
| Answer emphasis | 38 |
| Pattern display | 54 |

## V. Layout Principles

### Page Structure

- **Header area**: 左上为标题或题号积木块，右上为章节胶囊；章节页使用超大编号与场景式舞台。
- **Content area**: 每页只有一个主要学习动作；代码、终端、比喻图与练习区按信息权重形成不对称主次关系。
- **Footer area**: 页码与“孩子要会 / 家长陪练”简短标签按需出现，不与代码区争夺注意力。

### Spacing Specification

| Element | Current Project |
| --- | --- |
| Safe margin | 40 px |
| Content block gap | 24 px |
| Icon-text gap | 12 px |

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/code-circle | C++、代码框、程序结构 |
| tabler-filled/book | 新知、诗词与课后复习 |
| tabler-filled/alert-triangle | 易错警示与编译错误 |
| tabler-filled/bulb | 课堂思考与提示 |
| tabler-filled/device-desktop | 开发环境与运行结果 |
| tabler-filled/puzzle | 积木隐喻与五要素拼装 |
| tabler-filled/list-check | 练习清单与家长陪练 |
| tabler-filled/star | 图案工坊与闯关奖励 |
| tabler-filled/calculator | 运算表达式与计算结果 |
| tabler-filled/home | 房子图案与课后回看 |
| tabler-filled/school | 课堂目标与学习路线 |
| tabler-filled/device-speaker | cout“广播喇叭”比喻 |
| tabler-filled/check | 正确示例与完成状态 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| daxian_teacher_mascot_halfbody_v1.png | 1144 × 1430 | 0.80 | 面向四年级孩子的大仙老师半身串场吉祥物，复用于封面、章节、控制台与提示页 | AI-generated transparent character cutout | #A2-01 transparent sticker; enlarged face and gesture anchor the right edge or lower corner and interact with native speech bubbles | no-crop | ai | Generated | 以用户提供照片为身份参考；保留脸型、发型和温和神态，改为约 3.5 头身感的大头半身现代教育动画比例，眼睛与头部明显放大、轮廓更圆润；藏蓝休闲西装、白色圆领上衣，日常偏严肃，抬手讲解，成人教师属性，透明背景 | none | hero_page |
| bg_three_act_blocks_v1.png | 1672 × 941 | 1.78 | P02 三幕课的简约积木乐园背景 | AI-generated full-page background | full bleed behind native cards with a light warm wash | adaptive | ai | Generated | 暖奶油色留白中央，蓝橙粉积木与云朵只布置在边缘，不含文字 | none | full_page |
| bg_new_knowledge_portal_v1.png | 1672 × 941 | 1.78 | P03 新知精学章节背景 | AI-generated full-page background | full bleed; native title and steps remain editable above image | adaptive | ai | Generated | 暖奶油积木入口与蓝色拱门，左侧保留标题留白，不含文字 | none | full_page |
| devcpp_real_icon.png | 306 × 304 | 1.01 | P05 真实 Dev-C++ 图标 | user-provided raster icon | contain inside the main tool card | no-crop | user | Existing | 用户提供 `DEV C++.png` | none | content_page |
| devcpp_new_file_ai_v1.png | 1672 × 941 | 1.78 | P06 新建空白源文件的 Dev-C++ 界面 | AI-generated UI reconstruction | contain inside rounded screenshot frame; native numbered callouts overlay | no-crop | ai | Generated | 从零重构，无水印、无录屏条 | none | content_page |
| devcpp_hello_code_ai_v1.png | 1672 × 941 | 1.78 | P07 编写 Hello World 程序的 Dev-C++ 界面 | AI-generated UI reconstruction | contain inside rounded screenshot frame; exact code labels remain native | no-crop | ai | Generated | 从零重构，无水印 | none | content_page |
| devcpp_compile_success_ai_v1.png | 1672 × 941 | 1.78 | P08 保存与编译成功的 Dev-C++ 界面 | AI-generated UI reconstruction | contain inside rounded screenshot frame; native callouts mark save/compile/run | no-crop | ai | Generated | 从零重构，无水印 | none | content_page |
| hello_world_terminal_real.png | 1422 × 602 | 2.36 | P09 真实运行结果截图 | user-provided terminal screenshot | contain inside dark rounded frame | no-crop | user | Existing | 用户提供 `第九页运行结果图片.png` | none | content_page |

## IX. Content Outline

### Part 0: 开场与路线

#### Slide 01 - 初识 C++

- **Audience move**: 从“编程神秘”到期待亲手让电脑开口。
- **Layout**: #FFFCF1→#FFEFCB 暖黄渐变舞台上由蓝橙积木拼出 `cout` 轨道，右侧大仙老师大头半身透明吉祥物与电脑屏幕形成主视觉，标题占据最大留白区。
- **Title**: 初识 C++
- **Core message**: 一行 `cout`，就能让电脑说话、算结果、画图案。
- **Content**: 主标题；副标题“亲子 C++ 公开课”；主讲人“大仙老师”；三枚能力胶囊“说话 / 计算 / 画图”。
- **Images**: 使用 `daxian_teacher_mascot_halfbody_v1.png` 完整透明半身人物，不裁切；放大表情与手势并指向电脑与积木轨道。
- **Cover impact**: 绑定钩子“一行 cout 就能让电脑开口”，以代码积木进入屏幕、输出气泡离开屏幕的构图表现。
- **Motion suggestion**: 标题与老师保持在场；三枚能力积木按“说话→计算→画图”逐次进入，建立全课承诺。

#### Slide 02 - 今天的三幕课

- **Audience move**: 从只看到课程名称到理解整堂课的路线和终点。
- **Layout**: 一条由三段大积木组成的横向路线，孩子目标在上、家长陪练提示在下；每段形态不同而非三张等宽卡。
- **Title**: 今天的三幕课
- **Core message**: 新知精学 → 知识梳理 → 综合精练，每一步都能动手验证。
- **Content**: ① 新知精学：认识环境与 `cout`；② 知识梳理：记住五要素与输出规则；③ 综合精练：独立完成 8 道编程题。家长提示：“每幕结束，问孩子‘你能解释吗？你能自己写吗？’”。
- **Motion suggestion**: 路线从左向右依次亮起，最后出现“今天能做到”终点旗。

### Part 1: 新知精学

#### Slide 03 - ① 新知精学

- **Audience move**: 从路线总览进入第一幕并聚焦第一个可见成果。
- **Layout**: 蓝色切纸舞台与超大“01”，橙色积木台阶通向终端；大仙老师位于入口处。
- **Title**: ① 新知精学
- **Core message**: 先让电脑说出第一句话，再拆开它背后的积木。
- **Content**: 章节副句“认识环境 → 写下第一行 → 看见运行结果”。
- **Images**: 大仙老师吉祥物作为章节向导，不裁切。
- **Motion suggestion**: 章节编号先出现，随后三步路标依次进入。

#### Slide 04 - 任务：让电脑说 Hello World!

- **Audience move**: 从抽象认识 C++ 到拥有第一个明确任务。
- **Layout**: 左侧任务积木，右侧深色显示器；一句代码像蓝色积木插入屏幕，输出结果在屏幕内高亮。
- **Title**: Y2060 · 计算机输出
- **Core message**: 第一项任务只有一个：让屏幕显示 `Hello World!`。
- **Content**: 任务说明；目标输出 `Hello World!`；成功标准“文字完全一致、大小写一致、感叹号不丢”。
- **Motion suggestion**: 点击后代码积木进入屏幕，终端从空白变为显示结果。

#### Slide 05 - 我们在哪里写代码？

- **Audience move**: 从知道任务到认识需要的开发工具。
- **Layout**: 中央大电脑窗口，周围三块积木标注“写代码 / 编译 / 运行”；不复制旧软件标志为主视觉。
- **Title**: 开发环境：Dev-C++
- **Core message**: 开发环境把“写、检查、运行”三件事放在同一个地方。
- **Content**: “本课使用 Dev-C++ 5.11”；一句家长说明“它只是工具，核心技能是读懂和写出 C++ 代码”。

#### Slide 06 - 第一步：新建 C++ 文件

- **Audience move**: 从认识工具到能找到新建文件的入口。
- **Layout**: 原生 SVG 重绘简化版软件窗口，菜单、编辑区、信息区用编号气泡标记；右侧一条操作路线。
- **Title**: 1. 新建文件
- **Core message**: 先得到一张空白“代码纸”，再开始搭积木。
- **Content**: 操作路线“文件 → 新建 → 源代码”；家长提示“孩子能自己找到空白编辑区即可，不要求记住所有菜单”。
- **Motion suggestion**: 菜单入口、空白编辑区、光标按点击顺序被强调。

#### Slide 07 - 第二步：写下完整程序

- **Audience move**: 从空白编辑区到看到一份完整、可运行的最小程序。
- **Layout**: 左侧简化软件窗口，右侧大代码终端卡；五条彩色标注线对应五要素，但此页只整体认识，不展开解释。
- **Title**: 2. 编写代码
- **Core message**: 先完整照着搭好六行代码，再逐块理解它们的作用。
- **Content**: `#include <iostream>`；`using namespace std;`；`int main() {`；`cout << "Hello World!";`；`return 0;`；`}`。标注“工具箱 / 标准仓库 / 正门 / 广播喇叭 / 完成印章”。
- **Motion suggestion**: 五条标注按代码从上到下逐次出现。

#### Slide 08 - 第三步：保存、编译、运行

- **Audience move**: 从写完代码到理解程序为什么要先保存再运行。
- **Layout**: 三块相扣的积木步骤“保存 .cpp → 编译检查 → 运行观察”，下方为简化状态条。
- **Title**: 3. 保存与运行
- **Core message**: 文件名要以 `.cpp` 结尾；编译通过后，电脑才会执行程序。
- **Content**: 示例文件名 `hello.cpp`；解释“编译像搭积木前的质量检查”；状态示例“0 errors / 0 warnings”。
- **Motion suggestion**: 三块步骤按因果顺序连接，编译成功后运行按钮变为可用状态。

#### Slide 09 - 第一声：Hello World!

- **Audience move**: 从操作过程到获得第一次运行的成就感。
- **Layout**: 大面积深色终端居中，周围留白；左下小积木解释“输出内容”，右下解释“程序正常结束”。
- **Title**: 运行结果
- **Core message**: 终端显示 `Hello World!`，说明第一段程序成功运行。
- **Content**: 终端内容 `Hello World!`；`Process exited ... with return value 0`；“请按任意键继续”。只强调第一行与返回值 0 的意义。
- **Motion suggestion**: 终端光标闪烁后显示第一行，再出现绿色“运行成功”。

#### Slide 10 - 交互控制台 · 让电脑开口

- **Audience move**: 从观看结果到亲手切换三种程序、点击运行，并观察对应文字在终端中逐字符出现。
- **Layout**: 删除旧左侧品牌栏和三枚椭圆页签，改为全宽标题、三张横向任务卡，以及下方“代码编辑器—运行程序按钮—终端结果”的清晰实验路径。
- **Title**: Hello C++ World
- **Core message**: 选择任务、阅读 `cout`、点击“运行程序”，终端才会把文字一个一个打印出来。
- **Content**: 三个可点击选项为“运行示例代码 / 让电脑说中文 / ❤ 表白程序”，分别切换为 `cout << "Hello, World!";`、`cout << "你好，小小程序员！";`、`cout << "I ❤ Coding！";`。默认显示中文程序。状态栏初始提示“点击运行，让电脑开口说话!”，运行时显示“运行中...”，打印结束后显示“电脑说话了！！”。P16/P23/P29/P33 保持既有复用页面，不随本次 P10 单页改版联动。
- **Motion suggestion**: 三张任务卡和各自“运行程序”按钮均为 PowerPoint 原生触发形状；任务卡负责切换代码与按钮，运行按钮负责按约 0.12 秒节奏逐字符输出，并在输出结束时切换完成状态。

#### Slide 11 - 思考题：C++ 源程序扩展名

- **Audience move**: 从会保存文件到能识别 C++ 源程序最常用的扩展名。
- **Layout**: 左侧大题干与四个选项，右侧文件积木；点击后 `.cpp` 变绿并展开补充知识。
- **Title**: 思考题
- **Core message**: C++ 源代码文件通常使用 `.cpp` 扩展名。
- **Content**: 题目“C++ 编写的源程序扩展名是（ ）”；A `.cpp`；B `.doc`；C `.jpg`；D `.mp3`。答案 A。补充：`.cxx`、`.cc` 也可能用于 C++ 源文件，`.h` 常用于头文件。
- **Motion suggestion**: 先显示题目与四个选项；点击后 A 变绿，再出现解析与补充扩展名。

#### Slide 12 - 代码框架解析

- **Audience move**: 从识别 `cout` 到能用比喻解释完整程序的五个要素。
- **Layout**: 中央完整代码卡，五个不同形状积木围绕代码并以短线连接；大仙老师用一句话提醒“比喻帮助记忆，技术作用看小字”。
- **Title**: 代码框架解析
- **Core message**: 工具箱、标准仓库、正门、广播喇叭、完成印章，各司其职。
- **Content**: `#include <iostream>`＝引入输入输出功能的头文件（工具箱）；`using namespace std;`＝使用标准命名空间，可直接写 `cout`；`main`＝程序入口；`cout` 与 `<<`＝把内容送到屏幕，英文分号结束语句；`return 0`＝程序正常结束。明确“比喻帮助记忆，技术作用看说明”。
- **Motion suggestion**: 五个解释块按代码顺序逐次进入并高亮对应行。

#### Slide 13 - 选择判断：输入输出头文件

- **Audience move**: 从看见代码框架到能识别输入输出对应的头文件。
- **Layout**: 左侧题干与四个选项，右侧工具箱积木和代码框；答案揭示后 `<iostream>` 被高亮。
- **Title**: 选择判断
- **Core message**: 本课的输入输出功能来自头文件 `<iostream>`。
- **Content**: 题目“在 C++ 编程中，流输入输出对应的头文件是（ ）”；A `cstdio`；B `iostream`；C `algorithm`；D `cstring`。答案 B；解析：`iostream` 包含标准输入流 `cin` 和标准输出流 `cout`。
- **Motion suggestion**: 先投票；点击后 B 变绿，再把 `<iostream>` 积木放入工具箱位置。

#### Slide 14 - 选择判断：找出错误行

- **Audience move**: 从认识 `<iostream>` 到能在最小程序中定位头文件拼写错误。
- **Layout**: 左侧带行号的五行代码，右侧 A/B/C/D 四个行号选项；点击后第 1 行被粉色圈出并修复。
- **Title**: 选择判断
- **Core message**: 头文件名必须写成 `iostream`，少写一个字母就会编译失败。
- **Content**: 代码第 1 行为错误的 `#include <iostream>` 变体，题目问“其中有错误的代码行号是（ ）”；A 1；B 2；C 3；D 5。答案 A；修复为 `#include <iostream>`。
- **Motion suggestion**: 先显示代码与行号选项；点击后 A 变绿、错误位置放大，再出现正确拼写。

#### Slide 15 - cout 语句拆解

- **Audience move**: 从会认整行代码到能逐块解释 `cout << "Hello World!";`。
- **Layout**: 顶部一整行大代码，四条连接线落到“cout / << / 字符串 / ;”四个积木解释；底部保留思考题。
- **Title**: cout 语句
- **Core message**: `cout` 负责输出，`<<` 连接内容，双引号包住文字，英文分号结束语句。
- **Content**: `cout`＝console output 的缩写、命令电脑输出；`<<`＝连接需要显示的内容；`"Hello World!"`＝字符串，必须用英文双引号；`;`＝语句结束符。思考题：“如果把 `<<` 写成 `>>` 会怎样？”
- **Motion suggestion**: 先显示整行代码；四个解释按从左到右出现；思考题最后进入。

#### Slide 16 - 交互控制台 · 让电脑开口（复用）

- **Audience move**: 从新规则回到熟悉实验站并用同一操作路径练习。
- **Layout**: 完全复用 Slide 10 的所有可见组件、状态、图层、文本和动画顺序，不添加页码差异或新装饰。
- **Title**: Hello C++ World
- **Core message**: 熟悉的控制台让注意力集中在代码变化，而不是重新学习界面。
- **Content**: 与 Slide 10 完全一致。
- **Images**: 与 Slide 10 完全一致。
- **Motion suggestion**: 与 Slide 10 完全一致。

#### Slide 17 - 练习：输出指定短句

- **Audience move**: 从课堂示例到独立把题目文字放进字符串。
- **Layout**: 左侧 OJ 题目卡，右侧“读题→抄准→运行”三步条；答案点击后在下方代码卡出现。
- **Title**: N6713 · 短句输出
- **Core message**: 输出题先确认要显示的文字，再把它完整放进双引号。
- **Content**: N6713 要求输出英文短句 `thank you`；代码模板保留五要素，只补 `cout << "thank you";`；运行结果与题目逐字一致。
- **Motion suggestion**: 先给题目与空代码行；点击后填入字符串并显示终端结果。

#### Slide 18 - 练习：输出百分号

- **Audience move**: 从普通文字输出到确认 `%` 在字符串中可以直接显示。
- **Layout**: 超大 `%` 作为背景形状，前景为短题目和单行代码卡。
- **Title**: P1067 · 键盘输入和屏幕输出
- **Core message**: 题目要求的字母、数字、等号、百分号与逗号都要放进同一个字符串原样输出。
- **Content**: 目标输出 `a=10%,b=19%`；代码 `cout << "a=10%,b=19%" << endl;`；提醒百分号在本课的 `cout` 字符串中可直接写，英文标点不能换成中文标点。
- **Motion suggestion**: 点击后 `%` 从代码区“传送”到终端。

#### Slide 19 - 语法侦探

- **Audience move**: 从完成两道题到能主动检查一条 `cout` 是否正确。
- **Layout**: 四张“证据卡”围绕中央放大镜，点击答案后错误字符分别被标出。
- **Title**: 选择判断 · 输出 apple
- **Core message**: 输出字符串要同时检查 `cout`、`<<`、英文双引号和英文分号。
- **Content**: 题目“以下使用 cout 语句输出 apple，正确的是哪一项？”；A `cout << "apple";`；B `cout >> "apple";`；C `cout << apple;`；D `cout << "apple"`。答案 A；其余分别为方向符号错误、缺少字符串引号、缺少分号。
- **Motion suggestion**: 先投票；点击后正确卡片变绿，其他卡片依次显示错误原因。

#### Slide 20 - 思考：两条 cout 会输出什么？

- **Audience move**: 从单段输出到理解同一条语句可连续拼接多段内容。
- **Layout**: `cout` 喇叭在左，多块文字积木通过 `<<` 轨道串联到右侧终端。
- **Title**: 不换行拼接
- **Core message**: 两条 `cout` 都没有换行时，第二段内容会紧接在第一段后面。
- **Content**: `cout << "Welcome to C++!";` 与 `cout << "Coding is fun!";`；运行结果 `Welcome to C++!Coding is fun!`。明确“电脑不会自动换行”。
- **Motion suggestion**: 两条字符串依次沿轨道进入同一行终端；最后出现“没有换行”提示。

#### Slide 21 - 输出多行信息

- **Audience move**: 从发现两段内容粘在一起到会用 `endl` 让光标走到下一行。
- **Layout**: 左侧两条带 `endl` 的代码积木，右侧终端显示两行结果；底部用“回车积木”解释 `endl`。
- **Title**: 输出多行信息
- **Core message**: `endl` 是 end line 的缩写，放在输出链末尾可以换行。
- **Content**: `cout << "Welcome to C++!" << endl;`；`cout << "Coding is fun!" << endl;`；终端分两行显示。解释 `endl` 相当于输出后按一次回车。
- **Motion suggestion**: 先执行第一行并移动光标；再执行第二行；`endl` 回车积木最后被点亮。

#### Slide 22 - 多条信息，多行输出

- **Audience move**: 从理解换行符到能用多条 `cout` 组织多行内容。
- **Layout**: 左侧三条代码积木纵向排列，右侧终端每执行一条就新增一行。
- **Title**: 多条 cout 语句
- **Core message**: 每条 `cout` 负责一行，结构最直观、最适合初学者检查。
- **Content**: 一条连续输出链：`cout << "Hello World!" << endl << "123456" << endl << "你好世界!" << endl;`；说明多个内容可以连续写在一条 `cout` 中，每个输出内容用双引号包住，中间用 `<<` 连接。
- **Motion suggestion**: 代码与终端行一一对应、逐条揭示。

#### Slide 23 - 交互控制台 · 让电脑开口（复用）

- **Audience move**: 从换行规则回到熟悉控制台并准备多行诗词练习。
- **Layout**: 完全复用 Slide 10 的所有可见组件、状态、图层、文本和动画顺序。
- **Title**: Hello C++ World
- **Core message**: 同一个实验站承载不同练习，操作习惯保持不变。
- **Content**: 与 Slide 10 完全一致。
- **Images**: 与 Slide 10 完全一致。
- **Motion suggestion**: 与 Slide 10 完全一致。

#### Slide 24 - 练习：输出《静夜思》

- **Audience move**: 从三行示例到独立输出一首多行古诗。
- **Layout**: 左侧诗词排版卡，右侧代码终端；行与行之间用轻路线一一对应。
- **Title**: C5001 · 静夜思
- **Core message**: 一行诗对应一条 `cout`，标点和换行都要与题目一致。
- **Content**: 标题与四句诗；五条 `cout`（标题 + 四句）；终端预览。正文使用规范中文标点，代码字符串保持题目要求。
- **Motion suggestion**: 诗句与对应代码逐行配对出现，最后终端一次性显示完整结果。

#### Slide 25 - 易错警示（上）：字符双胞胎

- **Audience move**: 从能输出内容到意识到“看起来像”不代表编译器认为相同。
- **Layout**: 放大镜中心，两侧四组易混字符；下半区为中英文符号对比轨道，避免密集四列表格。
- **Title**: 常见编程错误 · 上
- **Core message**: 编译器逐字符检查，`l/1`、`O/0`、`;/:`、`*/x` 和中英文符号不能混用。
- **Content**: 眼睛与编译器容易认错的四组字符：小写 `l` vs 数字 `1`；大写 `O` vs 数字 `0`；分号 `;` vs 冒号 `:`；乘号 `*` vs 字母 `x`。逐组给出错误示例、正确示例与辨析技巧。
- **Motion suggestion**: 四组双胞胎逐组揭示；随后切换到中英文符号对比并高亮字宽差异。

#### Slide 26 - 易错警示（下）：配对与拼写

- **Audience move**: 从字符辨认到能系统检查括号、引号和关键单词。
- **Layout**: 左侧“配对迷宫”展示括号与转义引号；右侧“手抖拼写”四块纠错积木。
- **Title**: 常见编程错误 · 下
- **Core message**: 先检查成对符号，再检查关键单词，一个字符错也会让程序停下来。
- **Content**: 中英文符号对比：英文 `; , ( ) " "` 与中文 `； ， （ ） “ ”`；括号漏配；引号嵌套错误与正确写法 `cout << "He said \"Hello\"";`。
- **Motion suggestion**: 先让学生找错；点击后路径闭合并出现修复代码。

#### Slide 27 - 易错警示（末）：常见单词拼错

- **Audience move**: 从检查符号到能发现关键单词里一个字符的“手抖”错误。
- **Layout**: 四组“错误→正确”拼写积木沿检查路线排列，右下给出从上到下核对口诀。
- **Title**: 常见错误 · 单词拼错
- **Core message**: 关键单词只错一个字母，程序也可能无法编译。
- **Content**: `main` 写成 `mian`；`iostream` 写成 `i0stream`；`printf` 写成 `print`；`endl` 写成 `end1`。强调复制模板后逐行核对比凭记忆更可靠。
- **Motion suggestion**: 四个错误依次出现；点击后红色错字归位成绿色正确单词。

#### Slide 28 - 输出运算表达式

- **Audience move**: 从输出字符串过渡到区分“照抄文字”和“先计算再输出”。
- **Layout**: 左侧双引号展示盒输出 `3+5`，右侧数字积木通过加号合成为 `8`；底部用一条口诀收束。
- **Title**: 输出运算表达式
- **Core message**: 有双引号就原样显示；没有双引号就把表达式算出结果再输出。
- **Content**: `cout << "3+5";` → `3+5`；`cout << 3 + 5;` → `8`。双引号像“保鲜袋/展示盒”，包住的内容不会被当成算式计算。口诀“有引号照抄，没引号计算”。
- **Motion suggestion**: 先揭示左侧照抄，再揭示右侧计算，最后显示口诀。

#### Slide 29 - 交互控制台 · 让电脑开口（复用）

- **Audience move**: 从运算概念回到相同控制台并准备表达式练习。
- **Layout**: 完全复用 Slide 10 的所有可见组件、状态、图层、文本和动画顺序。
- **Title**: Hello C++ World
- **Core message**: 界面不变，只替换接下来要思考的代码内容。
- **Content**: 与 Slide 10 完全一致。
- **Images**: 与 Slide 10 完全一致。
- **Motion suggestion**: 与 Slide 10 完全一致。

#### Slide 30 - 三道小练习

- **Audience move**: 从对比示例到能把自然语言改写成 C++ 表达式。
- **Layout**: 三个不同形状的题目积木沿上升路线排列；答案区默认隐藏。
- **Title**: 输出运算表达式 · 小练习
- **Core message**: 先按数学顺序写表达式，再交给 `cout` 输出结果。
- **Content**: ① `7 - 2`；② `(8 + 3) * 2`；③ 连续输出 `1 + 2`、`3 * 4` 和 `2 * 2`。每题附“先想结果，再写代码”。
- **Motion suggestion**: 三题逐题进入；每次点击揭示表达式，不立即显示结果，给学生口算时间。

#### Slide 31 - 挑战：1234 × 5678

- **Audience move**: 从小算式到完成一条包含文字、计算与换行的组合输出。
- **Layout**: 上方题目与大结果积木，下方完整代码卡；字符串段和计算段用不同语法色连接。
- **Title**: Q3005 · 输出表达式的值
- **Core message**: 一条 `cout` 可以同时输出提示文字、计算结果和换行。
- **Content**: 目标 `1234 * 5678 = 7006652`；代码 `cout << "1234 * 5678 = " << 1234 * 5678 << endl;`；完整最小程序。
- **Motion suggestion**: 先显示题目，点击后出现结果，再拆解组合 `cout` 的三个输出段。

#### Slide 32 - 一行行 cout，就是画笔

- **Audience move**: 从数值计算切换到字符图案创作，并理解空格决定形状。
- **Layout**: 左侧多行代码像笔画堆叠，右侧星号图案在点阵纸上形成；橙色“画笔”轨迹连接两者。
- **Title**: 输出简单图案
- **Core message**: 每条 `cout` 画一行；星号和空格共同决定图案。
- **Content**: 三条极简示例从一颗星到三层形状；提醒“空格不可随意删除”。
- **Motion suggestion**: 代码每执行一行，右侧图案增加一层。

#### Slide 33 - 交互控制台 · 让电脑开口（复用）

- **Audience move**: 从画图原理回到相同控制台并准备图案闯关。
- **Layout**: 完全复用 Slide 10 的所有可见组件、状态、图层、文本和动画顺序。
- **Title**: Hello C++ World
- **Core message**: 控制台成为贯穿全课的固定实验站。
- **Content**: 与 Slide 10 完全一致。
- **Images**: 与 Slide 10 完全一致。
- **Motion suggestion**: 与 Slide 10 完全一致。

#### Slide 34 - 五星连珠

- **Audience move**: 从图案原理到独立完成第一个同一行图案。
- **Layout**: 五颗星号积木排成一线，代码卡和输出框上下呼应。
- **Title**: N6690 · 五星连珠
- **Core message**: 五个连续星号可以作为一个字符串一次输出。
- **Content**: 要求“同一行显示 5 个连续 `*`”；输出 `*****`；代码 `cout << "*****" << endl;`。
- **Motion suggestion**: 五颗星依次拼接，随后整体变成代码字符串并进入终端。

#### Slide 35 - 智慧树：先看目标图案

- **Audience move**: 从一行图案到观察多行图案的对齐规律。
- **Layout**: 左侧终端显示六行智慧树；右侧积木树把“树冠层数 / 每层星号 / 左侧空格 / 树干”拆成四个观察点。
- **Title**: C5002 · 智慧树
- **Core message**: 写代码前先数清每一行的星号和空格。
- **Content**: 完整六行目标图案；四项观察清单；家长提示“让孩子先用手指逐行数，再写代码”。
- **Motion suggestion**: 观察点按从上到下逐项高亮，对应终端中的一行或一组行。

#### Slide 36 - 智慧树：一行对应一条 cout

- **Audience move**: 从观察图案到能把六行目标逐行翻译成代码。
- **Layout**: 大代码卡占主位，右侧窄终端同步预览；每条代码与对应输出行同色连线。
- **Title**: C5002 · 智慧树代码
- **Core message**: 每一行图案都完整放进一个字符串，`endl` 负责走到下一行。
- **Content**: 六条 `cout` 代码，字符串中的空格完整保留；终端显示完整智慧树。
- **Motion suggestion**: 六条代码与六行输出成对逐次揭示，最后整体缩览确认对齐。

### Part 2: 知识梳理

#### Slide 37 - ② 知识梳理

- **Audience move**: 从大量动手例题切换到整理规则与词汇的阶段。
- **Layout**: 蓝色切纸舞台与超大“02”，五块程序积木围绕中央代码模板；大仙老师拿着检查清单。
- **Title**: ② 知识梳理
- **Core message**: 把刚才用过的代码，整理成以后可以反复使用的模板。
- **Content**: 章节副句“程序模板 / cout 规则 / 关键词词典”。
- **Images**: 大仙老师吉祥物作为整理向导，不裁切。
- **Motion suggestion**: 五块积木先散开，点击后归位成一份完整程序。

#### Slide 38 - 一张可复用的程序模板

- **Audience move**: 从零散记忆到获得一份可直接套用的最小程序模板。
- **Layout**: 左侧完整带注释代码卡，右侧 `cout` 五条规则清单；两区以积木卡扣连接。
- **Title**: 程序代码模板
- **Core message**: 保留固定框架，只替换 `cout` 中要输出的内容。
- **Content**: 六行最小程序及中文行尾注释；`cout` 规则：单行、输出并换行、多行、输出文字、输出计算结果。家长陪练提示“先让孩子口述五块作用，再遮住模板默写”。
- **Motion suggestion**: 模板五要素依次高亮；随后右侧五条 `cout` 规则逐条进入。

#### Slide 39 - 关键词词典（上）

- **Audience move**: 从会用模板到能解释前六个关键词的英文来源与作用。
- **Layout**: 六块词汇积木按两条路线排列，英文词根大、中文作用短；避免相同卡片矩阵，使用错位阶梯。
- **Title**: C++ 词汇积木 · 上
- **Core message**: 看懂英文词根，代码就不再像陌生符号。
- **Content**: include / iostream / using / namespace / std / main；每项含中文释义、词根拆分与一句作用。
- **Motion suggestion**: 每次点击点亮一个词根并拼出完整单词，按代码出现顺序推进。

#### Slide 40 - 关键词词典（下）

- **Audience move**: 从理解框架词汇到掌握输出与结束相关的四个关键词。
- **Layout**: 中央 `cout` 喇叭图，四个词汇环绕并连接到终端、换行、返回与整数入口。
- **Title**: C++ 词汇积木 · 下
- **Core message**: `cout`、`endl`、`return`、`int` 分别负责输出、换行、返回和整数类型。
- **Content**: 四个词汇的英文来源、中文作用与课堂比喻；强调 `cout` 更准确理解为标准输出对象，广播喇叭仅用于记忆。
- **Motion suggestion**: 四个词汇沿环形阅读路径依次进入并连接到对应功能。

### Part 3: 综合精练

#### Slide 41 - ③ 综合精练

- **Audience move**: 从整理知识切换到独立解决问题并建立课后行动感。
- **Layout**: 蓝色切纸舞台与超大“03”，橙色终点旗和任务清单形成通关场景；大仙老师做“出发”手势。
- **Title**: ③ 综合精练
- **Core message**: 现在不看示范，用同一套检查方法完成新的输出题。
- **Content**: 章节副句“读题 → 设计输出 → 写代码 → 运行检查”。
- **Images**: 大仙老师吉祥物作为闯关向导，不裁切。
- **Motion suggestion**: 四步任务路线逐段铺开，终点旗最后出现。

#### Slide 42 - 亲子编程题清单

- **Audience move**: 从课堂学习到获得可执行、可勾选的课后练习路线。
- **Layout**: 左侧 8 道题沿难度路径排列，右侧为“家长怎么陪”三步清单和通关徽章；每题有空复选框。
- **Title**: 综合精练 · 8 道编程题
- **Core message**: 先输出文字，再输出数字和图案；每题都用“读题—写代码—运行—找错”闭环。
- **Content**: N3113 废话上代码；N6648 输出英文单词；N6685 输出偶数；C5000 自我介绍；C5003 输出菱形；Q3008 雪花；Q3006 长方形；N6691 背诵诗词。家长陪练：只问检查问题、不直接报答案；让孩子口述五要素；每完成一题勾选并说明遇到的错误。
- **Motion suggestion**: 题目按“文字→数字→图案→综合”四组揭示，最后出现家长陪练三步法。

#### Slide 43 - 下节课再见

- **Audience move**: 从完成本课到能复述收获并愿意继续下一次编程挑战。
- **Layout**: 中央大屏显示结课句，三块能力积木从课程路线汇聚到屏幕；大仙老师在右侧挥手，底部保留一个明确复习行动。
- **Title**: 下节课再见
- **Core message**: 今天你已经能让电脑说话、算结果、画图案——回家完成第一道练习并讲给家长听。
- **Content**: 三项收获“会解释五要素 / 会写 cout / 会输出图案”；行动“今晚完成 N3113，并向家长讲一遍五要素”；结束语“编程像搭积木，下一块等你来拼”。
- **Images**: 大仙老师吉祥物完整显示，不裁切。
- **Closing impact**: 绑定行动“今晚完成 N3113，并向家长讲一遍五要素”，避免信息空白式致谢。
- **Motion suggestion**: 三项收获逐块汇聚，行动积木最后落在屏幕中央，老师挥手作为收束。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 逐页依据最终 SVG 编写；解释技术事实与儿童比喻的边界，包含课堂提问、点击提示、等待学生回答的停顿点和家长陪练补充，不添加源材料之外的技术结论。
- **Total duration**: 50–60 minutes
- **Notes style**: 互动式、耐心、先比喻后技术事实，使用适合 8–12 岁孩子的短句并照顾家长理解。
- **Presentation purpose**: instruct, engage, and hand off a practical parent-child practice plan
