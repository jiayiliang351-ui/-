---
name: "h3-shot-prompt"
description: "为本地部署的开源 MiniMax H3（只有 H3-Base，没有官方 Context-IR 改写层）写写实真人 AI 剧的分镜提示词：对话戏、安静戏、动作戏、多段接力。按官方 Context-IR 的文体输出 T2VA/I2VA/FL2VA/L2VA 三段式或 Ref2VA 六段式，可再输出 V7.3 导播台 JSON。写《纸引》《阎王打工记》等项目某一段、把剧情变成 H3 提示词、或出片后按病症改提示词时使用。"
---

# H3 分镜提示词（本地 H3-Base 版）

## 先弄懂一件事：你在替官方 Context-IR 干活

官方 H3 是三段流水线：**Context-IR（闭源改写系统）→ H3-Base（开源，本地跑的就是它）→ Regenerate-2K（闭源）**。官方 README 原话：Context-IR "is critical to the quality of the final output"。

在海螺、fal、官方 API 上，用户随手写的提示词会先被 Context-IR 改写成一份固定文体的英文文档，再交给 H3-Base。**别人分享的"好提示词"，多数是改写之前的原文**；你本地跑，写什么就原样进 H3-Base。所以照抄别人的写法、或者堆规则，在本地都会走样。

本 skill 的产出必须**长得像 Context-IR 的产出**（官方原样示例见 `references/examples.md` 第 1 节，用官方接口改写的本项目测试需求见 `references/official-calibration.md`）：
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
| `with no logos or brand names anywhere` | `its shelves stocked with plain, generic packaging`（写画面里实际有什么） |
| `Line lands about 2.80–3.90s.` / `By about 13 seconds` | 删掉；台词和动作的位置靠切点和先后来定 |

- 意图和情绪可以写，但要挂在看得见的行为上：`he keeps his eyes on the chopsticks, as if to keep the thanks casual`。
- **否定分两种**：修饰动作方式的否定可以写（官方原句 `walks away, never looking back`、`Without lifting his head, he …`、`though she does not turn around`），最好同句再给一个正向状态；点名不存在的东西（`no X`、`nobody`、`nothing`）不写——本地实测写 `no subtitles` 反而招来了字幕。简报里"没有/不要 X"：物件和特效改写成正向的具体外观；"没有配乐"写 `N/A`；"没有台词"什么都不写。

**固定句例外**：下面几句是本地实测过、或官方原文的固定句，照抄原文，不改写，也不仿写新的同类句子；它们不受可观察测试约束：
1. 电影感底座（`references/cinematography.md` 第 1 节）和项目卡的画风开头（项目卡写明的删句例外照项目卡，如《纸引》没有纸扎角色的段删掉 creatures 那一句）；
2. 全局表演段（`references/performance-and-dialogue.md` 第 1 节）；
3. 单声源句（同文件第 2 节，单人说话的段可选用；只换人名，或用该节给出的 T2VA 人物复指版），以及可选的 `Only the person speaking moves their lips.`；
4. 字幕防护句 `The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.`；
5. 挂纯色底角色卡时的背景句（EP02 实测原文是 `Behind the people is ONLY <Subject 1>: …`，`Behind them is ONLY …` 是等价写法），和挤构图的人数句（见 `h3-action-prompt-design` 第 1、3 节）。

本场光源句不是固定句：每场新写，一句、约 30 词以内，也要过可观察测试。

## 工作流程（每段都走）

1. **确认输入**：哪个项目（只读 `references/projects/` 里对应那张卡）、时长、模式（有无首帧、尾帧、参考素材）、一句话剧情（原因 → 动作 → 结果，原因要在画面里看得见）、台词逐字、谁说。缺了会改变结果的才问，其余按常理补。每个项目第一次写时，问一次配乐是后期统一加还是每段自带（见下文"输出格式"）。
2. **可行性检查**：对照 `references/physics-and-action.md` 第 1 节"H3 做不好的事"。命中就改设计（换景别、拆段、只拍接触前后、用插入特写），不要靠多写字硬扛。
3. **定时长和切点**：用下面的合法时长表；切点严格递增，每个镜头至少 1.5 秒，最后一个切点离结尾至少 1.5 秒。切点优先放在节拍边界上：换说话人、从起因切到后果的插入、从后果切到反应脸、两次交锋之间、从一个段落切到下一个段落（对话 → 离场）。同一个人一条连续的动作（爬起 → 再冲）不在中间切。
4. **定镜头数**：按下表。给每个镜头写一句中文"这一镜新增什么信息"（主体、空间、状态、视角或时间），写不出来就合并。只想换距离或视角时，用有动机的运镜代替切镜（跟着视线横摇、弧形绕到肩后）。
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
| 10 秒 | 1–3 镜 | 1 镜 | 2–4 镜 |
| 11–14 秒 | 1–4 镜 | 1–2 镜 | 2–5 镜 |
| 15 秒 | 1–5 镜 | 1–2 镜 | 3–6 镜 |

- 官方改写每段 1–3 个镜头，平均约 2 个，第一镜通常占全长的四成到一半（`examples.md` 第 1 节和 `official-calibration.md` 的 8 条；两条 15 秒的校准分别只用了 2 个和 1 个镜头）。时长变长不等于要多切；表里的数是上限范围，节拍允许时取下半段。
- 只有一两句台词、其余是小动作的段，按对话戏一栏，优先取下半段（15 秒 2–3 镜），听的人用有动机的运镜带出来（官方：`The camera pans slowly rightward to follow his gaze toward the cashier`），不另切。
- 对话戏取 1 镜，只适用于单人说话，或外形差别大的两人在双人镜里轮流说（见"台词"）。
- 本地跑通的旧范例（`examples.md` 2.1–2.3）是 4–6 镜的旧密度：2.2 第 1 镜只有 1.2 秒，2.2、2.3 的镜头数也超出对话戏一栏。它们只作 A/B 表第 8 项的对照，不照抄密度。新写的段按上表来，每镜至少 1.5 秒；一打多爽片按 `physics-and-action.md` 第 3B 节。

**正文字数**（`integrated_multimodal_description` 或 `detailed_description`）：照抄的固定段不计入预算——电影感底座（约 105 词）、全局表演段（约 75 词）、字幕防护句、项目卡的画风开头；本场光源句（约 30 词）也不计入。固定段以外：
- T2VA / I2VA / FL2VA / L2VA：单镜头、简单段 150–300 个英文词，一般写 150–220；多镜头 250–450 词，一般写 250–320；台词多的段（3 句以上或 24 个字以上）上限 550 词左右。范围的上限是天花板，不是目标：官方改写平均约 275 词，这还包括了场景、光线和画风。
- Ref2VA：按官方指南 350–500 词；单镜头不因此缩短。

超预算时先减镜头（合并没有新信息的镜头，用有动机的运镜代替切镜），再删陈设清单和重复的外形描写；切镜句里的景别、运镜状态、左右站位保留。固定段以外，镜头里再写画风、光线的句子合计不超过这部分的五分之一（底座已经管了画风，镜头里只补这一镜看得见的光）；规则说明为零。写得太短也是常见的失败。lint 报的词数包含固定段，套了底座、光源句和表演段的段会比上面的数多约 200–230 词，超过 650 词的 WARN 看过即可。

**台词预算**（只数说出口的中文字）：10 秒 20–28 字，12 秒 28–36 字，15 秒 36–44 字，上限 48 字；硬上限约每秒 3.5 字。有哽咽、长停顿、走路转身多的段，再少两成以上。一句最好十个字以内。

## 文体：正文怎么写

**[Shot 1]**（不带时间戳）依次写：
1. 画风：写实真人戏照抄电影感底座整段，再接一句本场光源；项目卡有自己的画风开头的照抄项目卡（《纸引》的开头已经写了火盆和门口的光，不再接光源句）；其他题材写一两句（`Photoreal cinematic, 16:9, …`）。
2. 第一句构图句：紧接画风，写清景别和运镜状态，并带出场景（`A 50mm medium two-shot, holding a static shot with a faint handheld breath, looks across a quiet night sidewalk …`；单人安静戏可以直接带出人物：`In a medium shot, the camera slowly pushes in toward …`）。官方改写 8/8 条第一句就有景别。
3. 场景陈设：只写这一段会用到、或交代空间的几样，不列清单。
4. 在场的人：外形、在画面哪一侧、手里拿着什么。会说话的人在这一句就挂编号并写 `on-screen`：`A young on-screen woman (S1) with shoulder-length black hair … stands on the left of the frame.` 在场人数写一句短的陈述（`Only the two of them are in the room.`，或先写空间再写人数 `empty desks stretch into the background; only the two of them are here`）。
5. 两人以上的写实真人戏：照抄全局表演段；不要字幕时接字幕防护句。
6. 第一个动作。

**后续镜头**：`[Shot N] At 00:04.500, the camera cuts to an extreme close-up of the hands on the table, holding a static shot.` 切镜句里同时写景别和运镜状态，运镜状态写短的就行（`static shot`、`pushing in slowly`、`holding steady`）；`with a faint handheld breath` 这类长写法只在第一句构图句里用一次（底座已经写了手持）。然后：
- 前面出现过的人、动物、关键道具，在这个镜头第一次提到时写 `<短外形或身份> from Shot N`：`the paper tiger from Shot 1`、`the black prayer beads from Shot 1`、`the young man from Shot 1 (S1)`。每个镜头 1–2 处，先给人物；道具只在它是这一镜动作的对象时写；同一句只写一次；门、柜台、窗这类布景不用。Ref2VA 写成 `<Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1`。
- 切镜后至少交代一次左右站位（`visible as an out-of-focus silhouette in the right foreground`）。

**动作**：一个镜头只有一条主动作链，外加最多一个反应。一条链指同一个人、同一个目的、一步接一步的动作（提壶 → 倒茶 → 放壶 → 推杯）；同一个镜头里不并行第二条链。一镜到底的安静戏就是一条链：触发 → 反应 → 余波。用先后词串起来（`first … a beat later … only then …`，`as …`，`until …`）。每个物理动作写全"起因 → 用力 → 对方或物体的反应 → 落定"，例如 `the wing catches him mid-stride; he is knocked sideways, rolls once on the wet stone and slides to a stop`。接触戏的写法（力度副词、受力方的身体反应、僵持）见 `references/physics-and-action.md` 第 2 节。

**运镜**：写成镜头里的一句自然英文。官方指南的"类型 + 幅度 + 速度"（`The camera pushes in with small amplitude at slow speed toward her hands.`）和 Context-IR 常用的副词式（`pushing in slowly`、`pans slowly rightward`）都可以。运镜要有动机：谁的动作或视线带着镜头走、揭示什么、停在什么构图。景别写全称，可以用 Title Case（`Medium Close-Up`），不写缩写（`MCU`）。

**台词**：
- `<d>` 里面只放语言标签和台词原文，标签后一个半角空格，台词逐字照抄：`<d>[Chinese] 那我帮你扔。</d>`。
- 第一次开口时，在 `<d>` 外写清声线：年龄、音高、音色、语速、这场戏里声音怎么走（见 `references/performance-and-dialogue.md`）。之后的台词，语气写在动词上：`replies tiredly`、`murmurs even more quietly`、`says in a low, steady voice`。动词后用冒号或逗号都可以。
- **说话人收口**：说话人在画内、镜头还停在他脸上时，`</d>` 后写一句收口，二选一：闭嘴并进下一个动作（`She closes her lips and guards the cookie …`；`Exactly as his voice stops, his lips meet in a tired half-smile, and his jaw ceases speaking motion; he drops his hand.`），或紧接一个接管脸和身体的动作（`Immediately after speaking, he pivots on his heel …`）。同一人连说几句，只在最后一句后写。说话人在画外（用画外音句）、台词跨切点（`<scenetrans>`）、被段尾截断（`<cutoff>`）、台词一结束就切走时不写。它防的是"说完嘴还在动、补出没写的话"，不防串词。来源是官方文本，本地还没单独 A/B（A/B 表第 12 项）。
- **听的人**：先写对这句话看得见的反应（慢半拍、手停一下、视线移开；有编号就带编号：`The man (S2) breaks eye contact, …`）。只在三种情况再写嘴闭着：① 切到听的人、说话人不在画面里——用画外音句；② 一段只有一个人说话、画面里还有别人——`… watch silently, their mouths kept firmly closed.`；③ 听者的脸和说话人同时清楚在画里——把闭嘴并进反应句（`…, his lips pressed together.`）。听者不在画面里、背对镜头、只剩前景虚化的肩膀或后脑，或者这个镜头里没人说话时，不写闭嘴。
- **画外音句**（已实测不串词）：`… (S1) says in an off-screen voiceover: <d>[Chinese] ……</d> while the woman's lips remain completely closed.`——闭嘴的是画面里的听者。说话人自己在画里、声音是内心独白时，写 `while his lips remain completely closed`。
- 防串词：性别、年龄段、服装都相近，并且近距离同框的两个人（实测：钱总和阎王隔一张茶台），一段只让一个人说话，按说话人拆段。年龄段或服装明显不同、分处画面两侧的两个人，可以在同一段轮流说，每句写清说话人在哪一侧。闭嘴句代替不了拆段。细则见 `references/performance-and-dialogue.md`。

**跨镜状态**：要一路记住的东西（火还着不着、手里还攥着什么、谁已经离开），在每个相关镜头里用一句陈述写出来，不写括号标签。

**结尾**：最后一秒不开始新动作（不新起身、不新开口、不新伸手拿东西）。已经开始、本来就该持续的动作（走远、车开远、镜头慢推），用同样的速度延续到最后一帧。定格可以单独成句（`Toward the end, …`），也可以挂在最后一个动作的从句里（`…, freezing completely motionless as a thin wisp of smoke rises from behind him`）。要接力的段，必须写清最后的状态：人在哪、看哪、手里有什么、还在往哪个方向走。除此之外只有烟、光、雨、衣摆这类东西还在动。不写片内秒数。

**语言和符号**：结构部分全用英文和半角符号（逗号、引号、括号、冒号）。中文只出现在 `<d>` 台词和画面里真实可见的文字里。中文全角标点、弯引号混进结构部分会改变分词，标记词会失效。

## 输出格式

| 手上有什么 | 模式 | 写法 |
|---|---|---|
| 只有文字 | T2VA | 三段式 |
| 一张图当第一帧（含上一段末帧接力） | I2VA | 首帧对齐句 + 三段式。有人物、要跨段保持长相时，同时挂身份图，改用 Ref2VA `[keyframe completion + reference generation]` |
| 首帧 + 尾帧 | FL2VA | 首尾帧对齐句 + 三段式，默认单镜头 |
| 一张图当最后一帧 | L2VA | 尾帧对齐句 + 三段式 |
| 角色图、场景图、声音参考 | Ref2VA | 六段式 |

三段式：
```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```
- `overall_soundscape`：2–4 句连续英文，一般 50–100 词。第 1 句写环境底噪（可以用 `establishes the …` 收住）；后面每句把一两个关键动作声绑到看得见的动作上（`as the man rubs his neck`、`At the cut, …`），写清材质和接触面（`flesh and bone hit the solid wooden table`）；最关键的 1–2 个声音加一个显著词（`clearly heard`、`distinct`、`sharp`）。有台词的段，显著词只给没有台词的时刻；呼吸、喘息只写给说话人，或放在没有台词的时刻。台词不重复写在这里。
- `non_diegetic_music`：接力剧集默认写 `N/A`（每段各自生成配乐，段与段接缝会跳）。用户要每段自带配乐、或简报要求配乐时，1–3 句，照官方的克制写法：单件乐器或低频铺底、`slow tempo`、明写克制（`stays quiet under the foreground sounds, without any swell`），进入时机挂在画面事件上（`begins the moment the rain noise subsides`）；按官方指南不写情绪词。同一场戏的多段用同一句。简报写了"没有配乐"或"只有某某声"、一镜到底的安静戏、纯动作拟音段，写 `N/A`。

对齐句（逐字照抄，只换数字）、Ref2VA 六段式、标签和标记词，见 `references/official-format.md`。导播台 JSON 见 `references/pipeline-and-settings.md`。

## 写实真人戏的默认层（已实测）

- **电影感底座**：每段开头照抄，再接一句本场光源。见 `references/cinematography.md`。项目卡有自己的画风开头时（《纸引》），用项目卡那段代替底座，两段不叠加；项目卡写明套用底座的（《阎王打工记》）照常用底座。
- **活人感**：有两个以上人物的段，在人物和站位之后、第一个动作之前，照抄全局表演段（`Nobody stands idle or poses for the camera. …`，一字不改）。镜头里再写：一人行动、一人慢半拍反应；隐藏目的；用大动作盖住小动作；情绪写先后过程；每镜小动作不超过 2 个。见 `references/performance-and-dialogue.md`。
- **防串词**：性别、年龄段、服装都相近并且近距离同框的两个人，一次生成只让一个人说话，用接力拆段。

## 出片后怎么改

先按 `references/troubleshooting.md` 的病症表找原因。原则：
1. **先排除提示词以外的原因**：时长填错、步数和 CFG 不对、种子太少（每版至少 2–3 个种子）。
2. **一次只改一处**，另存新版本（v2、v3…），不覆盖旧版。
3. **先删后加**：先看能不能删掉一个多余的事件、镜头或描述来解决，最后才加字。
4. 串词不靠加字修，直接按说话人拆段。

## 写完自查

1. 除"固定句例外"列出的句子外，每一句都过了"可观察测试"：没有 `IMPORTANT`、`FORBIDDEN`、`must`、命令式 `do not` / `NEVER`、括号状态标签、全大写标签、片内秒数；没有点名不存在的东西（`no X`）。修饰动作方式的否定（`never looking back`）可以有。
2. 模式选对；I2VA/FL2VA/L2VA 的第一行是对齐句，后面空一行。
3. 时长取自合法时长表；`[Shot 1]` 没有时间戳；切点严格递增，每镜至少 1.5 秒，全部小于实际时长；切点在节拍边界上。
4. 镜头数在表内，每个镜头都带来新信息；每个切镜句写了景别和运镜状态。
5. 每个镜头一条主动作链；物理动作写了"起因 → 用力 → 反应 → 落定"；命中"H3 做不好的事"的地方已经改了设计。
6. 在场人数、左右站位、手里的道具在 [Shot 1] 写明；后续镜头第一次提到前面出现过的人和道具时写了 `from Shot N`；切镜后交代了一次左右站位。
7. 台词逐字、在预算内，`<d>[语言] ` 标签后有空格；说话人第一次出场就挂了编号和 `on-screen`，第一次开口写了声线；画内说话人说完写了收口（闭嘴，或紧接的动作）；听的人写了反应，三种情况下写了闭嘴，看不到脸的听者和没人说话的镜头没写；相像的两人没有在同一段里各说一句。
8. 写实真人戏：开头是电影感底座 + 本场光源（《纸引》用项目卡画风开头）；两人以上的段有全局表演段；表演写成可见行为和先后过程。
9. 结构部分全英文、半角符号；中文只在 `<d>` 和画面文字里。
10. 固定段以外的字数在预算内；固定段以外的画风和光线不超过这部分的五分之一；`overall_soundscape` 2–4 句，关键声音绑在动作上。
11. 最后一秒没有开始新动作（已经在进行的走远、慢推可以延续）；结尾状态写清楚，下一段能接上。
12. Ref2VA：六段齐全、顺序对；标签定义一次、全文一致；summary 有任务前缀；retention 用固定标记词、不写 `(Sx)`。

## 参考文件

| 文件 | 什么时候读 |
|---|---|
| `references/official-format.md` | 每次都读：对齐句、切点、运镜词表、台词标记、Ref2VA 六段式 |
| `references/examples.md` | 第一次用、或拿不准文体时：官方改写原样示例 + 你本地跑通的范例 + 新写法 A/B 对照 |
| `references/official-calibration.md` | 用官方接口改写的本项目测试需求（对话、动作、安静戏、接触、手部道具各有一条），找最接近的一条参照 |
| `references/physics-and-action.md` | 有动作、接触、打斗、道具操作时 |
| `references/performance-and-dialogue.md` | 有人物表演、台词时 |
| `references/cinematography.md` | 写实真人戏的电影感底座、光、色、运镜动机 |
| `references/pipeline-and-settings.md` | 接力、首帧流程、导播台 JSON、采样设置、A/B 方法 |
| `references/troubleshooting.md` | 出片后按病症修改 |
| `references/projects/zhiyin.md` | 写《纸引》时 |
| `references/projects/yanwang.md` | 写《阎王打工记》时 |
| `scripts/lint_prompt.py` | 写完后跑：查规则词、括号标签、全角符号、台词标签空格、切点、时长、`from Shot` 复指、台词字数、Ref2VA 标签和标记词 |

配套 skill：`h3-action-prompt-design`（补充手册：挂素材细则、空间方向、门、手和道具、粤语、接力、车辆、LoRA 触发词）；`h3-director-json-review`（整份导播台 JSON 的审查、批量重写和校验）。
