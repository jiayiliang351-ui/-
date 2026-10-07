# 表演与台词

## 1. 活人感（写实真人戏默认用，已实测）

来源：小佟的「活人感 skill」。实测：《五点五十九》v2 对 v1 同种子，v2 全面胜出（人不呆、反应有先后、表情不夸张、更有故事感）；《临期》温情戏也跑得好。人物看着假，多半不是脸不够真，而是**人太闲、演得太用力**。

**表演公式**
- 单人：人物 + 正在做的小事 + 下意识反应 + 情绪落点。
- 多人：不要每个人都演。**一人行动，另一人反应，反应慢半拍**，因为真人的注意力还留在别处。

**反向表演三技巧（情绪藏起来，不演出来）**
1. **先给隐藏目的，再给情绪。** 只写"他很紧张"，模型按最大幅度演。写成 `nervous, but doesn't want the visitor to notice`，模型才走克制路线。
2. **用大动作盖住小动作。** 紧张时去端水杯，尴尬时整理衣服，难过时转身收拾东西。眼神闪躲、手指发紧藏在大动作里面。
3. **情绪写先后过程。** 不写最终状态（"他笑了"），写 `first … a beat later … only then …`。

正反对照：
```text
反面：She is nervous and glances around, then smiles.
正面：She is nervous about the inspection, but doesn't want the visitor to notice. She turns back to the desk and starts stacking files to busy herself; her thumb keeps rubbing the folder's edge, and only after a beat do her shoulders settle.
```

**用量与程度**
- 每镜小动作 1–2 个。成片台词说不利索时，先砍插在台词中间的分心动作。
- 程度词决定真假：`a fraction` / `faintest` / `almost imperceptibly` / `a beat late`。
- 不堆表情词（brows knitted、eyes pleading）。表情挂在动作和反应链上。
- "憔悴、没笑容"不等于没表情：`haggard and unsmiling, but alive: his typing fingers pause for half a beat, he swallows, blinks slowly`。整段写"面无表情、只说台词"，成片就是木头人。

**全局表演指导（已实测有效的一段，写在角色和站位之后、第一个动作之前）**
```text
Nobody stands idle or poses for the camera. Every character is always occupied with some small piece of business — handling an object, finishing a movement, glancing at something off-topic. In every exchange one character acts while the other reacts, and reactions arrive a beat late, the way real people respond while their attention is still somewhere else. Small involuntary gestures (swallowing, shifting weight, thumb rubbing an edge, a delayed look-up) matter more than polished facial expressions.
```
说明：这段是 v2 胜出时用的写法（原句开头是 `Acting direction for the whole sequence:`，这里去掉了这个标签头，正文没改）。新文体的 A/B 里会试"去掉这段、把内容全写进镜头"的版本，结果出来前继续用它。

**背景人物**：主角承担主要动作，配角回应具体事件，背景人只保留少量持续活动或自然静止。不要让背景人集体转头、同步手势或抢主角的注意力。

## 2. 台词与防串词

**台词预算**（只数说出口的字）：10 秒 20–28 字，12 秒 28–36 字，15 秒 36–44 字，最多 48 字；硬上限约每秒 3.5 字。有哽咽、结巴、长停顿、拥抱，或走路、转身多的段，再少两成以上。一句最好十个字以内，一个镜头只有一个人说话。台词不到 24 字、又只有简单动作的段，先试着并进前后段。

**一段只装**：一个场景、一次关系变化（追问 → 否认、靠近 → 拉开）、一条动作链、一个落点。

**防串词（已实测）**：长得像、挨得近的两个人，一次生成只放一个人说话。实测：钱总和阎王（两个中年男人、隔一张茶台）同一段各说一句，两个种子都把台词配错了脸；拆成"钱总说完 → 接力 → 阎王说"两段就不串。两人外形、位置差别大时，一段放两人轮流说跑通过，但每句都要写明说话人在画面哪一侧、另一个人嘴闭着。一旦串过一次，这一场后面全部按单人段 + 接力写。

**怎么写一句台词（官方文体 + 实测句式）**
```text
[Shot 2] At 00:02.400, the camera cuts to an over-the-shoulder close shot of the man on the right of the frame, her shoulder a soft blur in the left foreground. He rubs the back of his neck and does not meet her eyes. The young man with a tired, clipped mid-low voice (S2) says: <d>[Chinese]我今天真的很累。</d> As the line ends his lips close and his jaw stops moving; he drops his hand and keeps looking away down the street.
```
- 说话人第一次出现：身份 + 音色 + 语气 + 编号，都在 `<d>` 外。
- 说完写闭嘴（`his lips close and his jaw stops moving`），否则嘴容易一直动。
- 听的人：写对这句话的具体反应，写 `her lips stay closed`。
- 单人说话的段，台词后可以接这句实测有效的单声源句（《阎王打工记》EP02 不串词，虽然是指令式写法，照样保留）：`Only this one vocal source is heard. <Subject 3>'s mouth stays closed. Do not repeat, paraphrase or continue beyond the listed spoken content.` 多人在画时加一句 `Only the person speaking moves their lips.`
- 说台词时避免快跑、捂脸、转开和大的运镜。
- 切到听的人时，说话人在画外说：`The man (S1) says in an off-screen voiceover: <d>[Chinese]……</d> while the woman's lips remain completely closed.`（已实测：《五点五十九》跨切那句声音对、听的人嘴闭着）
- 同一句跨切点：两边写 `<scenetrans>`，注明 `continues seamlessly across the cut`；被段尾截断写 `<cutoff>`。
- 切点落在说话权交换、回答前的停顿、视线变化处。情绪最重的那一下，可以插一个不到 1.5 秒的特写（攥紧裙摆又松开）。
- 视线只写正向：`his eyes stay on her`、`she looks down at the screen`。

**声线**：每个说话的角色写一段固定声线，每段照抄：年龄、音高、音色、平常语速，这场戏里声音怎么走（推销时沉稳笃定、被问住时泄气下沉、摊牌时低而硬、被戳中时几乎耳语），以及不要的腔调写成正向（`a plain, natural speaking voice, not a broadcaster's tone`）。只写"平静地说"，出来就是机器人念稿。

**中文台词**：用标准汉字和普通标点；多音字、生僻字容易读错，必要时换个说法。语速快、俚语多时，尾字容易被吞。

## 3. 参考素材一致性（挂素材时）

- 有图的关键道具不写外观，在 `subject_definitions` 里定义成主体（`<Subject N> is the … in <Picture N>.`），出现该道具的每个镜头写一次 `matches <Subject N> exactly`。状态（不碎、不开）和位置（在柜里、原位）照常写。删光描述后仍漂移，补 1–2 个和图一致的材质词，或者换一张"道具在场景里"的合成图。
- 一个人两张图时分开写：`Facial identity comes from <Picture 2>; full-body proportions, clothing, and posture come from <Picture 3>.`
- 音色参考加一句：`its vocal timbre guides the delivery without copying the original signal.`
- 左右写清视角：`on the right side of the case, as seen when facing the case from the front`。
- 衣服在段与段之间容易漂（实测过牛仔裤变灰裤子，后面每段都跟着错）：服装在每段 [Shot 1] 里完整写一次，挂素材时用定稿图锁。
