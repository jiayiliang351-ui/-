---
name: "h3-shot-prompt"
description: "为本地部署的开源 MiniMax H3（只有 H3-Base，没有官方 Context-IR 改写层）写写实真人 AI 剧的分镜提示词：对话戏、安静戏、动作戏、多段接力。按官方 Context-IR 的文体输出 T2VA/I2VA/FL2VA/L2VA 三段式或 Ref2VA 六段式，可再输出 V7.3 导播台 JSON。写《纸引》《阎王打工记》等项目某一段、把剧情变成 H3 提示词、或出片后按病症改提示词时使用。"
---

# H3 分镜提示词（本地 H3-Base 版）

## 先弄懂一件事：你在替官方 Context-IR 干活

官方 H3 是三段流水线：**Context-IR（闭源改写系统）→ H3-Base（开源，本地跑的就是它）→ Regenerate-2K（闭源）**。官方 README 原话：Context-IR "is critical to the quality of the final output"。

在海螺、fal、官方 API 上，用户随手写的提示词会先被 Context-IR 改写成一份固定文体的英文文档，再交给 H3-Base。**别人分享的"好提示词"，多数是改写之前的原文**；你本地跑，写什么就原样进 H3-Base。所以照抄别人的写法、或者堆规则，在本地都会走样。

本 skill 的产出必须**长得像 Context-IR 的产出**（官方原样示例见 `references/examples.md`）：
- 英文连续散文，按播放顺序从第一帧写到最后一帧；
- 每一句都是看得见或听得见的东西，读起来像有人看完成片后写下的描述；
- 不写给人看的规则、指令、强调、禁令、状态标签。

**可观察测试（写完每句都过一遍）：** 这句话能不能出自"看完视频的人写的描述"？
| ❌ 不像描述 | ✅ 改成描述 |
|---|---|
| `IMPORTANT — he must not touch the cup.` | `His hand stops a few centimetres short of the cup and stays there.` |
| `(flame: OUT)` | `The flame on his tail is gone; a thin curl of smoke rises from the charred tip.` |
| `Never swap sides.` | `She stays on the left of the frame, he on the right.`（每个镜头陈述一次） |
| `She is sad.` | `Her eyes redden; she blinks once and keeps looking ahead.` |
| `WHIP PAN. He SLAMS the table.` | `The camera pans right with large amplitude at fast speed as he slams his palm on the table.` |
| `Line lands about 2.80–3.90s.` | 删掉；台词位置靠镜头切点和动作先后来定 |

意图和情绪可以写，但要挂在看得见的行为上：`he keeps his eyes on the chopsticks, as if to keep the thanks casual`。

## 工作流程（每段都走）

1. **确认输入**：哪个项目（只读 `references/projects/` 里对应那张卡）、时长、模式（有无首帧、尾帧、参考素材）、一句话剧情（原因 → 动作 → 结果，原因要在画面里看得见）、台词逐字、谁说。缺了会改变结果的才问，其余按常理补。
2. **可行性检查**：对照 `references/physics-and-action.md` 第 1 节"H3 做不好的事"。命中就改设计（换景别、拆段、只拍接触前后、用插入特写），不要靠多写字硬扛。
3. **定时长和切点**：用下面的合法时长表；切点严格递增，每个镜头至少 1.5 秒，最后一个切点离结尾至少 1.5 秒。
4. **定镜头数**：按下表。给每个镜头写一句中文"这一镜新增什么信息"（主体、空间、状态、视角或时间），写不出来就合并成运镜。
5. **写正文**：按下文"文体"。写实真人戏默认叠加"电影感底座"和"活人感"。
6. **自查**：能运行代码时，把提示词存成文件，跑 `python3 scripts/lint_prompt.py 文件 --seconds 10`，修掉所有 ERROR、看过所有 WARN；然后按文末清单过一遍脚本查不了的部分（物理、表演、可行性）。
7. **交付**：提示词放在代码块里；代码块外用一行中文写"本段开头继承什么 / 结尾交给下一段什么"（手里拿着什么、谁在哪、门开没开）。

## 时长、镜头数、字数

**合法时长**（24 fps，帧数满足 n % 17 == 5；导播台填整数秒，实际按这张表出片）：

`5.17 · 5.88 · 6.58 · 7.29 · 8.00 · 8.71 · 9.42 · 10.13 · 10.83 · 11.54 · 12.25 · 12.96 · 13.67 · 14.38 · 15.08`

只有 8 秒是整数。导播台填 10 秒，实际出 10.13 秒；填 15 秒，实际出 15.08 秒。所有切点都要小于实际时长。

| 时长 | 对话戏 | 安静戏 | 动作戏 |
|---|---|---|---|
| 5–8 秒 | 1–2 镜 | 1 镜 | 2–3 镜 |
| 10 秒 | 2–3 镜 | 1 镜 | 3–4 镜 |
| 15 秒 | 3–5 镜 | 1–2 镜 | 4–6 镜 |

官方改写结果平均每段 2–4 个镜头。8 秒切 6 刀这种密度离训练分布太远，只在"一打多爽片"里用（见 `physics-and-action.md`）。

**正文字数**（`integrated_multimodal_description` 或 `detailed_description`）：单镜头、简单段 150–300 个英文词；多镜头、复杂段 350–500 词；台词多或挂素材多的段可到 600 词左右。字数要花在画面和声音上：画风、光线合计不超过五分之一，规则说明为零。写得太短也是常见的失败。

**台词预算**（只数说出口的中文字）：10 秒 20–28 字，12 秒 28–36 字，15 秒 36–44 字，上限 48 字；硬上限约每秒 3.5 字。有哽咽、长停顿、走路转身多的段，再少两成以上。一句最好十个字以内。

## 文体：正文怎么写

**[Shot 1]**（不带时间戳）依次写：画风一两句 → 场景和光源 → 在场的人（外形、在画面哪一侧、手里拿着什么）→ 第一个动作。在场人数用陈述句写明：`Only the two of them are in the room.`

**后续镜头**：`[Shot N] At 00:04.500, the camera cuts to a close-up of ...`，然后简短复指人物（`the man in the grey suit from Shot 1`），交代他在哪一侧，再写动作。

**动作**：一个镜头只有一个主动作，外加最多一个反应。用先后词串起来（`first … a beat later … only then …`，`as …`，`until …`）。每个物理动作写全"起因 → 用力 → 对方或物体的反应 → 落定"，例如 `the wing catches him mid-stride; he is knocked sideways, rolls once on the wet stone and slides to a stop`。细节见 `references/physics-and-action.md`。

**运镜**：写成镜头里的一句自然英文，类型 + 幅度 + 速度（只在有意义时写幅度、速度）：`The camera pushes in with small amplitude at slow speed toward her hands.` 运镜要有动机：谁的动作或视线带着镜头走、揭示什么、停在什么构图。

**台词**：
- 说话人第一次出现时，在 `<d>` 外面写清身份、音色、语气和编号：`The middle-aged man with a low, rough voice (S1) says: <d>[Chinese]那我帮你扔。</d>`
- `<d>` 里面只放台词原文，逐字照抄。
- 说完写闭嘴：`As his line ends, his lips close and his jaw stops moving.`
- 听的人写看得见的反应，并写 `her lips stay closed`。
- 画外音固定句式：`… says in an off-screen voiceover: <d>[Chinese]……</d> while the woman's lips remain completely closed.`（已实测不串词）
- 防串词规则见 `references/performance-and-dialogue.md`。

**跨镜状态**：要一路记住的东西（火还着不着、手里还攥着什么、谁已经离开），在每个相关镜头里用一句陈述写出来，不写括号标签。

**结尾**：最后一秒没有新动作，写清停在什么状态（人在哪、看哪、手里有什么），只有烟、光、雨这类东西还在动。

**语言和符号**：结构部分全用英文和半角符号（逗号、引号、括号、冒号）。中文只出现在 `<d>` 台词和画面里真实可见的文字里。中文全角标点、弯引号混进结构部分会改变分词，标记词会失效。

## 输出格式

| 手上有什么 | 模式 | 写法 |
|---|---|---|
| 只有文字 | T2VA | 三段式 |
| 一张图当第一帧（含上一段末帧接力） | I2VA | 首帧对齐句 + 三段式 |
| 首帧 + 尾帧 | FL2VA | 首尾帧对齐句 + 三段式，默认单镜头 |
| 一张图当最后一帧 | L2VA | 尾帧对齐句 + 三段式 |
| 角色图、场景图、声音参考 | Ref2VA | 六段式 |

三段式：
```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```
- `overall_soundscape`：1–4 句连续英文，写环境声、动作声、呼吸等；台词不重复写在这里；和画面同步的关键声音写进对应镜头。
- `non_diegetic_music`：1–3 句，写乐器、速度、力度变化；没有配乐写 `N/A`。

对齐句（逐字照抄，只换数字）、Ref2VA 六段式、标签和标记词，见 `references/official-format.md`。导播台 JSON 见 `references/pipeline-and-settings.md`。

## 写实真人戏的默认层（已实测）

- **电影感底座**：每段开头照抄，再接一句本场光源。见 `references/cinematography.md`。
- **活人感**：一人行动、一人慢半拍反应；隐藏目的；用大动作盖住小动作；情绪写先后过程；每镜小动作不超过 2 个。见 `references/performance-and-dialogue.md`。
- **防串词**：长得像、挨得近的两个人，一次生成只让一个人说话，用接力拆段。

## 出片后怎么改

先按 `references/troubleshooting.md` 的病症表找原因。原则：
1. **先排除提示词以外的原因**：时长填错、步数和 CFG 不对、种子太少（每版至少 2–3 个种子）。
2. **一次只改一处**，另存新版本（v2、v3…），不覆盖旧版。
3. **先删后加**：先看能不能删掉一个多余的事件、镜头或描述来解决，最后才加字。
4. 串词不靠加字修，直接按说话人拆段。

## 写完自查

1. 每一句都过了"可观察测试"：没有 `IMPORTANT`、`FORBIDDEN`、`must`、`never`、括号状态标签、全大写标签、台词落点秒数。
2. 模式选对；I2VA/FL2VA/L2VA 的第一行是对齐句，后面空一行。
3. 时长取自合法时长表；`[Shot 1]` 没有时间戳；切点严格递增，每镜至少 1.5 秒，全部小于实际时长。
4. 镜头数在表内，每个镜头都带来新信息。
5. 每个镜头一个主动作；物理动作写了"起因 → 用力 → 反应 → 落定"；命中"H3 做不好的事"的地方已经改了设计。
6. 在场人数、左右站位、手里的道具在 [Shot 1] 写明，在相关镜头里重复陈述。
7. 台词逐字、在预算内；说话人有编号和声线；说完写了闭嘴；听的人写了反应和闭嘴；相像的两人没有在同一段里各说一句。
8. 写实真人戏：开头是电影感底座 + 本场光源；表演写成可见行为和先后过程。
9. 结构部分全英文、半角符号；中文只在 `<d>` 和画面文字里。
10. 正文字数在预算内，画风和光线不超过五分之一。
11. 最后一秒没有新动作，结尾状态写清楚，下一段能接上。
12. Ref2VA：六段齐全、顺序对；标签定义一次、全文一致；summary 有任务前缀；retention 用固定标记词、不写 `(Sx)`。

## 参考文件

| 文件 | 什么时候读 |
|---|---|
| `references/official-format.md` | 每次都读：对齐句、切点、运镜词表、台词标记、Ref2VA 六段式 |
| `references/examples.md` | 第一次用、或拿不准文体时：官方改写原样示例 + 你本地跑通的范例 + 新写法 A/B 对照 |
| `references/physics-and-action.md` | 有动作、接触、打斗、道具操作时 |
| `references/performance-and-dialogue.md` | 有人物表演、台词时 |
| `references/cinematography.md` | 写实真人戏的电影感底座、光、色、运镜动机 |
| `references/pipeline-and-settings.md` | 接力、首帧流程、导播台 JSON、采样设置、A/B 方法 |
| `references/troubleshooting.md` | 出片后按病症修改 |
| `references/projects/zhiyin.md` | 写《纸引》时 |
| `references/projects/yanwang.md` | 写《阎王打工记》时 |
| `scripts/lint_prompt.py` | 写完后跑：查规则词、括号标签、全角符号、切点、时长、台词字数、Ref2VA 标签和标记词 |
