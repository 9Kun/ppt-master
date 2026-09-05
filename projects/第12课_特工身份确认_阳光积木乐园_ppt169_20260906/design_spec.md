<!-- ppt-master-schema: design-spec/v1 -->
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
| Chapter number | 180 |
| Section title | 56 |
| Counter display | 70 |

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

#### Slide 01 - 特工身份确认

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 特工身份确认
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 02 - 今天的任务路线

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 今天的任务路线
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 03 - 复习抢答规则

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答规则
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 04 - 复习抢答_1_2

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答_1_2
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 05 - 复习抢答_3_4

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答_3_4
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 06 - 复习抢答_5_6

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答_5_6
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 07 - 复习抢答_7_8

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答_7_8
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 08 - 复习抢答_9_10

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 复习抢答_9_10
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 09 - 任务启动

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 任务启动
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 10 - 新知精学

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 新知精学
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 11 - while像值班守卫

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: while像值班守卫
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 12 - 计数防止不停

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 计数防止不停
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 13 - break提前下车

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: break提前下车
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 14 - continue跳过本轮

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: continue跳过本轮
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 15 - for和while怎么选

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: for和while怎么选
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 16 - 练习A_数到3停

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 练习A_数到3停
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 17 - 易错_漏掉计数增加

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 易错_漏掉计数增加
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 18 - 本课选择题_1_2

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 本课选择题_1_2
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 19 - 本课选择题_3_4

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 本课选择题_3_4
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 20 - 本课选择题_5_6

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 本课选择题_5_6
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 21 - 本课选择题_7_8

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 本课选择题_7_8
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 22 - break实战

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: break实战
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 23 - 练习B_答对就break

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 练习B_答对就break
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 24 - break执行路径

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: break执行路径
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 25 - 微项目三次口令门

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 微项目三次口令门
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 26 - 三次口令门代码拆解

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 三次口令门代码拆解
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 27 - 三次口令门_运行验证

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 三次口令门_运行验证
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 28 - continue位置很重要

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: continue位置很重要
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 29 - 项目实施步骤

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 项目实施步骤
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 30 - 作品验收与展示

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 作品验收与展示
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 31 - 常见问题与处理

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 常见问题与处理
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。

#### Slide 32 - 离堂小结

- **Audience move**: 从等待教师讲解 → 明确本页任务并能口头说明或现场操作。
- **Relationships**: 本页信息按“任务/问题 → 示例或选择 → 结论/反馈”的教学顺序组织。
- **Composition**: 单一课堂动作居中展开，保持阳光积木乐园的大圆角卡片与清晰主次。
- **Title**: 离堂小结
- **Core message**: 围绕本课 while、计数、break、continue 与三次口令门推进一个明确学习动作。
- **Content**: 以 DOCX 教纲对应知识、练习、代码或运行结果为唯一课程内容来源。


## X. Speaker Notes Requirements

- **Generation**: disabled
