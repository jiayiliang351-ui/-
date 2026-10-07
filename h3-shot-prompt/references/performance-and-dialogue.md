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
说明：这段是 v2 胜出时用的写法（原句开头是 `Acting direction for the whole sequence:`，这里去掉了这个标签头，正文没改）。它属于 SKILL.md 的"固定句例外"，两个以上人物的写实真人戏默认照抄，一字不改，不计入字数预算。`examples.md` 3.2（《临期》v2）没有这一段，两轮出片用户都没提表演问题（第一轮种子 2 最好，第二轮两个种子都没问题），但这只是 A/B 表第 9 项的弱证据，默认不变，写新段时照抄。

**背景人物**：主角承担主要动作，配角回应具体事件，背景人只保留少量持续活动或自然静止。不要让背景人集体转头、同步手势或抢主角的注意力。

**时间静止、集体定身的例外**：这类段不加上面的全局表演段，其中 `Every character is always occupied` 会与受限状态冲突。按简报写哪些人物被定住、哪些人物能动，以及恢复后才继续的动作；完全时间静止的对象在此期间不眨眼、不换重心、不慢半拍回应，普通定身是否仍能眨眼、呼吸或说话则按简报。普通文戏的默认表演段和防串词写法保持原样。此处是消除指令冲突，尚未验证渲染收益；详见 `powers-and-effects.md`。

## 2. 台词与防串词

**台词预算**（只数说出口的字）：10 秒 20–28 字，12 秒 28–36 字，15 秒 36–44 字，最多 48 字；硬上限约每秒 3.5 字。有哽咽、结巴、长停顿、拥抱，或走路、转身多的段，再少两成以上。一句最好十个字以内。一个镜头最好只有一个人说话（画外音句除外）；外形差别大的两人在同一个双人镜里轮流说时，听者按下文"听的人"第③种处理。台词不到 24 字、又只有简单动作的段，先试着并进前后段；但为防串词按说话人拆开的单人段不并回去，宁可短。

**一段只装**：一个场景、一次关系变化（追问 → 否认、靠近 → 拉开）、一条动作链、一个落点。

**防串词（已实测）**：性别、年龄段、服装都相近，并且近距离同框的两个人，一次生成只放一个人说话。实测：钱总和阎王（两个中年男人、隔一张茶台）同一段各说一句，两个种子都把台词配错了脸；拆成"钱总说完 → 接力 → 阎王说"两段就不串。两人年龄段或服装明显不同、分处画面两侧时，一段放两人轮流说跑通过，每句都要写明说话人在画面哪一侧；另一个人写不写闭嘴，按下文"听的人"的三种情况决定（脸和说话人同时清楚在画里时，把闭嘴并进反应句；只剩虚化的肩膀或后脑时不写）。一旦串过一次，这一场后面全部按单人段 + 接力写。

**怎么写一句台词（官方文体；画外音句已实测，说话人收口来自官方文本、本地未单独 A/B）**
```text
[Shot 2] At 00:02.400, the camera cuts to an over-the-shoulder close shot of the young man from Shot 1 (S2) on the right of the frame, static shot, the shoulder of the woman from Shot 1 a soft blur in the left foreground. He rubs the back of his neck and does not meet her eyes, then, in a young man's tired, clipped mid-low voice, replies, <d>[Chinese] 我今天真的很累。</d> Exactly as his voice stops, his lips press together and his jaw ceases speaking motion; he drops his hand and keeps looking away down the street.
```
- **编号和声线**：说话人在第一次出场的句子里（外形加站位）就挂编号并写 `on-screen`（`A young on-screen man (S2) in a black bomber jacket …`）；第一次开口时在 `<d>` 外写清声线（见下文"声线"）；之后的台词，语气写在动词上（`replies tiredly`、`murmurs even more quietly`）。动词后用冒号或逗号都可以。
- **台词标签**：`<d>[Chinese] 台词</d>`，标签后一个半角空格（官方指南和官方改写全部带空格）。本地实测通过的旧段（`examples.md` 2.2、2.3）是不带空格的写法，不回改；有空格和没空格的对比见 A/B 表第 14 项。
- **说话人收口**：说话人在画内、镜头还停在他脸上时，`</d>` 后写一句收口，二选一：闭嘴并进下一个动作（官方指南：`She closes her lips and guards the cookie …`、`He closes his mouth into an apologetic smile and …`；官方 Ref2VA 改写：`Exactly as his voice stops, his lips meet in a relaxed, peaceful smile, and his jaw ceases speaking motion.`），或紧接一个接管脸和身体的动作（官方改写：`Immediately after speaking, he pivots smoothly on his heel …`）。同一人连说几句，只在最后一句后写。说话人在画外、台词跨切点、被段尾截断、台词一结束就切走时不写。它防的是"说完嘴还在动、补出没写的话"，不防串词；串词靠拆段。来源是官方文本，本地还没单独 A/B（A/B 表第 12 项）。
- **听的人**：先写对这句话的具体可见反应（慢半拍、手停一下、视线移开；有编号就带编号）。闭嘴只在三种情况写：① 切到听的人、说话人不在画面里——用下面的画外音句（已实测）；② 一段只有一个人说话、画面里还有别人——`… watch silently, their mouths kept firmly closed.`（官方改写原句式）；③ 听者的脸和说话人同时清楚在画里（双人镜、多人镜，外形差别大的两人在同一段轮流说也算）——把闭嘴并进反应句，如 `He exhales through his nose and looks away down the street, his lips pressed together.`。听者不在画面里、背对镜头、只剩前景虚化的肩膀或后脑，或者这个镜头里没人说话时，不写闭嘴。官方改写不会主动写听者闭嘴，这是本地防串词的写法（A/B 表第 13 项）。
- **单声源句**（可选，SKILL.md 的固定句例外，照原句结构写，只换人名）：《阎王打工记》EP02 实际跑的原文见 `examples.md` 2.2：`Only this one vocal source is heard: Yama. <Subject 3> and <Subject 4> keep their mouths closed. Do not repeat, paraphrase or continue beyond the listed spoken content.` T2VA 没有 `<Subject N>` 标签时改用人物复指：`Only this one vocal source is heard: the man in the grey suit. The man behind the tea table keeps his mouth closed. Do not repeat, paraphrase or continue beyond the listed spoken content.` 证据边界：EP02 那一版同时按说话人拆了段，还带一句 `IMPORTANT —` 单声源说明；修好串词的主因是拆段，这句单独的作用没有分离测过。多人在画时可加 `Only the person speaking moves their lips.`
- 说台词时避免快跑、捂脸、转开和大的运镜。
- **画外音句**：切到听的人时，说话人在画外说，闭嘴的是画面里的听者：`The man (S1) says in an off-screen voiceover: <d>[Chinese] ……</d> while the woman's lips remain completely closed.`（已实测：《五点五十九》跨切那句声音对、听的人嘴闭着；实测时标签后没有空格）。说话人自己在画里、声音是内心独白时，闭嘴的是说话人自己：`… while his lips remain completely closed.`
- 同一句跨切点：两边写 `<scenetrans>`，注明 `continues seamlessly across the cut`；被段尾截断写 `<cutoff>`。
- 切点落在说话权交换、回答前的停顿、视线变化处。情绪最重的那一下，可以插一个反应特写（攥紧裙摆又松开）；这个特写也至少 1.5 秒，并算进 SKILL.md 镜头数表的镜头数。
- 视线只写正向：`his eyes stay on her`、`she looks down at the screen`。

**声线**：每个说话的角色写一段固定声线，每段照抄：年龄、音高、音色、平常语速，这场戏里声音怎么走（推销时沉稳笃定、被问住时泄气下沉、摊牌时低而硬、被戳中时几乎耳语），以及不要的腔调写成正向（`a plain, natural, conversational speaking voice, like someone talking across a table`）。只写"平静地说"，出来就是机器人念稿。

**中文台词**：用标准汉字和普通标点；多音字、生僻字容易读错，必要时换个说法。语速快、俚语多时，尾字容易被吞。

## 3. 参考素材一致性（挂素材时）

- 有图的关键道具不写外观，在 `subject_definitions` 里定义成主体（`<Subject N> is the … in <Picture N>.`），出现该道具的每个镜头写一次 `matches <Subject N> exactly`。状态（不碎、不开）和位置（在柜里、原位）照常写。删光描述后仍漂移，补 1–2 个和图一致的材质词，或者换一张"道具在场景里"的合成图。
- 一个人两张图时分开写：`Facial identity comes from <Picture 2>; full-body proportions, clothing, and posture come from <Picture 3>.`
- 音色参考加一句：`its vocal timbre guides the delivery without copying the original signal.`
- 左右写清视角：`on the right side of the case, as seen when facing the case from the front`。
- 衣服在段与段之间容易漂（实测过牛仔裤变灰裤子，后面每段都跟着错）：服装在每段 [Shot 1] 里完整写一次，挂素材时用定稿图锁。
