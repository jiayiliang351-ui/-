# 官方格式（摘自 MiniMax 官方 h3-prompt-writing skill）

来源：`github.com/MiniMax-AI/MiniMax-H3` 的 `skills/h3-prompt-writing/references/base-en.txt` 和 `ref-en.txt`。这是 H3-Base 训练时见过的文体，字段名、对齐句、标签、标记词一律照抄。

## 1. 模式与结构

| 模式 | 第一行 | 主字段 |
|---|---|---|
| T2VA | 没有对齐句，直接写三段 | `integrated_multimodal_description` |
| I2VA | 首帧对齐句 | 同上 |
| FL2VA | 首尾帧对齐句 | 同上 |
| L2VA | 尾帧对齐句 | 同上 |
| Ref2VA | 没有对齐句，直接写六段 | `detailed_description` |

本地 ComfyUI：T2V/I2V 模板走 FL2VA 权重（T2VA/I2VA/FL2VA/L2VA 都用它），R2V 模板走 Ref2VA 权重。

## 2. 对齐句（必须是第一行，后面空一行）

I2VA：
```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

FL2VA（注意这句里 Picture/Shot 不带尖括号和方括号，照抄）：
```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.
```

L2VA：
```text
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.
```

- `N` = 真正的最后一个镜头编号，单镜头就是 1。
- `S.SS` = 两位小数。官方说是"有效时长"，本 skill 用本地实际帧长：8 秒写 `8.00`，10 秒写 `10.13`，15 秒写 `15.08`。（开源复刻项目 open-h3-ir 主张写名义时长 `10.00`，两种写法还没对比过，见 `pipeline-and-settings.md` 的 A/B 表。）

## 3. 三种关键帧模式的正文顺序

| 模式 | 顺序 | 要点 |
|---|---|---|
| I2VA | 首帧锚点 → 动作开始 → 连续发展 → 结果或反应 | [Shot 1] 先复述图里已有的画风、人物、构图、场景，再写下一个动作；身份、服装、颜色、道具、位置关系保持一致。可以多镜头 |
| FL2VA | 首帧状态 → 看得见的中间变化 → 差距逐步收窄 → 尾帧状态 | 默认单镜头。写"怎么从 A 走到 B"，不要把两张图各描述一遍；结尾写 `settles into the pose, spacing, lighting and composition established by Picture 2` |
| L2VA | 合理的前一状态 → 明确的动作和过渡 → 最后一镜逐步收拢 → 落到尾帧 | 图只锚定最后一刻，开头自己推一个能接上的状态 |

## 4. 镜头与切点

- `[Shot 1]` 不带时间戳。T2VA 和关键帧模式下，画风和起始构图紧跟在 `[Shot 1]` 后面写；Ref2VA 下，画风用一两句英文写在 `[Shot 1]` 之前（写实真人戏是电影感底座整段加本场光源，见 SKILL.md）。
- 后续镜头：`[Shot N] At MM:SS.mmm, the camera cuts to …`，时间严格递增，小于实际时长。
- 切镜动词：`the camera cuts to` / `the shot cuts to` / `the shot transitions to` / `the shot changes to` / `the shot switches to`。叠化、淡入淡出、划像只在明确需要时用。
- 切镜要带来新信息（主体、空间、状态、视角或时间）。只改距离或一点角度时，用运镜，不切。

## 5. 运镜：类型 + 幅度 + 速度

| 类型 | 含义 |
|---|---|
| `Zoom In / Zoom Out` | 变焦，机身不动 |
| `Push In / Pull Out` | 机身前后移动 |
| `Pan Left / Pan Right` | 原地水平转 |
| `Truck Left / Truck Right` | 机身水平平移 |
| `Tilt Up / Tilt Down` | 原地上下转 |
| `Pedestal Up / Pedestal Down` | 机身整体升降 |
| `Arc Shot` | 绕主体弧形运动 |
| `Tracking Shot` | 跟随移动的主体 |
| `Static Shot` | 机位和镜头都不动 |
| `Shake Slightly / Shake Strongly` | 轻微 / 强烈晃动 |
| `POV` | 主观视角 |
| `Roll Clockwise / Roll Counterclockwise` | 绕镜头轴旋转 |

幅度：`with small amplitude` / `with large amplitude`。速度：`at slow speed` / `at fast speed`。中等幅度、正常速度省略。

写成句子里的动作，不在句尾堆标签：
```text
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

旧写法对照（旧 skill 的大写词 → 官方句子）：
| 旧写法 | 官方写法 |
|---|---|
| `WHIP PAN` | `the camera pans right with large amplitude at fast speed` |
| `SNAP-ZOOM ECU` | `the camera zooms in with large amplitude at fast speed to an extreme close-up of …` |
| `DOLLY-IN` / `DOLLY-OUT` | `the camera pushes in / pulls out (at slow speed)` |
| `SIDE TRACKING` | `a tracking shot follows … from the side` |
| `LOW-ANGLE … TRACKING` | `a low-angle tracking shot follows …` |
| `360 ORBIT` | `the camera makes an arc shot with large amplitude around …` |
| `LOCKED-OFF` | `the camera holds a static shot` |
| 手持轻晃 | `the camera shakes slightly` |

## 6. 说话人与台词

- 会出声的角色用固定编号 `(S1)`、`(S2)`，按实际开口先后编；整段不变；不出声的角色不编号。多人齐声用 `(S1,S2)`。
- 第一次出现时写清身份：角色类型、年龄、性别、是否在画内、音高、音色、语速、口音。身份、编号、动作、语气都写在 `<d>` 外面。官方改写的习惯是在人物第一次出场的句子里就挂编号，并写 `on-screen`：`A young on-screen woman (S1) with shoulder-length straight black hair … stands on the left side of the frame.`
- `<d>` 里只放语言标签和台词原文，标签后一个半角空格，逐字照抄，不翻译、不改标点：`<d>[Chinese] 你每次都说下次。</d>`（官方指南原文 `<d>[English] I get off at the next station.</d>` 带空格；官方改写 7/7 句带空格。）
- 说话动词后用冒号（官方指南 T2VA 示例 `says: <d>`）或逗号（官方 Ref2VA 示例和 Context-IR 改写 `says, <d>`）都可以。
- 画外音固定句式：`<d>` 后紧跟一句"画面里那个人嘴闭着"（官方原文：state that the corresponding on-screen character's lips remain closed）。说话人自己在画里、声音是内心独白或旁白时，闭嘴的是说话人自己：
```text
The man (S1) says in an off-screen voiceover: <d>[Chinese] ……</d> while his lips remain completely closed.
```
说话人在画外、画面切到听的人身上时，闭嘴的是听的人（本地已实测，《五点五十九》段 03）：
```text
The man (S1) says in an off-screen voiceover: <d>[Chinese] ……</d> while the woman's lips remain completely closed.
```
- 同一句台词跨切点：两边都写 `<scenetrans>`，并写明 `continues seamlessly across the cut`（也可用 `continues uninterrupted into the next shot` / `carries over from the previous shot` / `remains audible across the transition`）。
- 被段尾截断的台词写 `<cutoff>`。
- 官方文本里的说完收口：官方 Ref2VA 改写（README 复现脚本）`Exactly as his voice stops, his lips meet in a relaxed, peaceful smile, and his jaw ceases speaking motion.`；官方指南饼干示例 `She closes her lips and guards the cookie …`、`He closes his mouth into an apologetic smile and …`。2026-10-07 的 8 条 T2VA 校准改写里，7 句台词后都没写说话人闭嘴，而是接听者的反应、切走，或 `Immediately after speaking, …` 这样的紧接动作。本 skill 的用法见 SKILL.md"说话人收口"。

## 7. 画面文字

画面里真实可见的字（招牌、屏幕、标签），用英文半角双引号逐字写，不翻译：`A red neon sign reading "营业中" glows above the doorway.` 768p 下远景里的小字看不清，要字清楚就给一个静止的插入特写。

## 8. 两个声音字段

- `overall_soundscape`：官方规定 1–4 句连续英文，写整段的环境声、动作声、非语言人声（风、雨、脚步、衣料、撞击、呼吸、笑）。台词、唱歌、角色听得见的音乐写在正文里，这里不重复。只有用户明确要求全程无声时才写 `N/A`。官方改写的实际写法偏长（8 条校准平均约 87 词，多为 3–4 句）：第 1 句写环境底噪，后面每句把关键动作声绑到看得见的动作上；本 skill 的具体要求见 SKILL.md"输出格式"。
- `non_diegetic_music`：1–3 句，只有观众听得见的配乐；写乐器、速度、节奏、力度变化，官方指南要求不写抽象情绪词（官方改写自己常违反，不照学）。收音机、现场演奏这类角色听得见的音乐写进正文。没有配乐写 `N/A`。官方改写在简报没提配乐时常自己加一段克制的配乐；接力剧集的默认做法见 SKILL.md"输出格式"。

## 9. Ref2VA 六段式

顺序：`subject_definitions` → `summary` → `retention_analysis` → `detailed_description` → `overall_soundscape` → `non_diegetic_music`。六段全英文，只有 `<d>` 里的台词和画面文字保留原语言。

**四类标签**
| 标签 | 用途 |
|---|---|
| `<Subject N>` | 可复用的可见内容：人、动物、物件、场景、服装、道具、特效、风格、动作 |
| `<Picture N>` | 图片本身当具体帧用（首帧、关键帧、尾帧、构图锚点、分镜参考） |
| `<Video N>` | 整段视频关系：被编辑的源视频、续写起点、运镜和剪辑节奏参考 |
| `<Audio N>` | 音频：复制、音色参考、节奏参考 |

- 图片只用来定义角色或场景时，不单列 `<Picture N>`，写进对应 `<Subject N>`：`<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue cardigan, and a thin silver necklace.`
- 一个角色来自多个素材时分开写清：`<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.`
- `<Video N>` 和 `<Audio N>` 各自编号，序号不代表配对。标签一旦定义，六段里含义不变；summary 里不新增标签。
- 声音参考：`<Audio 1> is the voice-timbre reference for <Subject 1> (S1).`（`(Sx)` 沿用正文里的开口顺序）
- 导播台的 `{{ref:别名}}` 只是挂素材的占位符，展开后模型看到的必须是上面四类标签。标签写错（`<Image 1>`、`<Ref 1>`）、挂了素材正文却没提、编号和挂载顺序对不上，模型都会认错素材。

**summary**：一段英文，以方括号任务前缀开头，多种关系用 ` + ` 连接，不重复：
- `keyframe completion`：图当具体帧
- `reference generation`：图、视频、音频只做生成参考
- `video editing`：直接修改源视频
- `video continuation`：从源视频继续往下拍
- `audio reuse`：直接复用音频信号
- `audio reference`：只参考音色、节奏、风格

常用：角色图 + 场景图 + 声音参考 → `[reference generation + audio reference]`；再加首帧图 → `[keyframe completion + reference generation + audio reference]`。

**retention_analysis**：每个标签一行，不写 `(Sx)`。
- 可见内容：`fully_preserved` / `partially_preserved` / `attribute_transfer` / `weak_reference`
- 音频：`fully_copy` / `partially_copy` / `reference` / `weak_reference`
- 格式：`<Subject 1> (appears in [Shot 1], [Shot 3]): fully_preserved - …`；`<Picture 2> ([Shot 1] first frame): fully_preserved - …`；`<Audio 1>: reference - …`
- 剧情里新加的动作和背景不算"保留度下降"，不要因此降级。

**detailed_description**：画风一两句写在 `[Shot 1]` 前（写实真人戏是电影感底座整段）；每个镜头写清构图、主体外形和位置、环境和光、动作和状态变化、运镜、声音、参考内容在哪里出现。生成任务一般 350–500 个英文词，台词多的段以装下完整台词为先。重要的 `<Subject N>` 第一次清楚出现时，写它的参考特征、画面位置和当前动作；之后沿用同一标签。说话的参考角色写成 `<Subject 2> (S1) turns toward the woman and says, <d>[Chinese] ……</d>`。后续镜头复指写成 `<Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1`（官方示例写法）。

关键帧锚点的自然写法：`the shot begins from <Picture 1>` / `the shot's keyframe corresponds to <Picture 2>` / `the shot ends on <Picture 3>`。
