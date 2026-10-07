# 动作与物理

H3 不会算物理，它是按"见过的视频长什么样"来画。物理对不对，取决于两件事：动作本身是不是它见得多、画得稳的那一类；提示词有没有把物理过程写成一串看得见的先后变化。研究上，PhyT2V（CVPR 2025）先让大模型找出场景里涉及的物理规律，再把它写进提示词，物理正确率提高了约 2.3 倍。本节就是这件事的手工版。

## 1. H3 做不好的事（先绕开，再动笔）

评测和本地实测里反复出问题的：

| 难点 | 常见病 | 绕开的办法 |
|---|---|---|
| 两个人在同一个全身画面里精确接触（擒拿、拥抱、扶起、递东西） | 穿模、手粘在一起、多出一只手 | 接触那一下给特写（只拍手和物件）；或者拍接触前和接触后两镜，把接触藏在切点里；或者停在"将触未触" |
| 快速大幅动作（打斗、翻滚、摔倒） | 脸糊、肢体变形、动作发飘 | 景别拉近到半身、一个镜头一个动作；力量感交给镜头（甩、推近）和后果（碎片、灰、震动） |
| 被打飞、倒地、爬起这类受力动作 | 无重量、像被线吊着 | 只拍"一顿""被拽住""踉跄半步"；被打中的一方用碎掉、炸开、猛地停住来表现 |
| 手部操作小物件（系扣、写字、拿杯子、点烟） | 手指数量不对、物件变形 | 物件大一点、动作慢一点、镜头近一点；一个镜头只操作一个物件 |
| 多人同时做不同的事 | 动作互相干扰、有人突然消失 | 一个镜头只有一个人在做主动作，其他人静止或只做重复的小动作 |
| 一个镜头里塞好几个动作 | 顺序错乱、动作被跳过 | 一镜一条主动作链（同一个人、同一个目的、一步接一步）；不在一个镜头里并行第二条链，多了就拆镜头或拆段 |
| 遮挡后重新出现、快速穿过前景 | 身份和服装变掉 | 避免；需要时在出现后再复述一次外形 |
| 远景里的人脸、远景里的字 | 768p 下糊成一片 | 要看清就推近 |

## 2. 物理怎么写

**先列物理清单（写之前在脑子里过，不写进提示词）**：这一段里谁有重量、谁碰到谁、碰的是什么材质、力往哪个方向、动完之后怎么停下来。然后把每一条写成看得见的结果。

**四步写法：起因 → 用力 → 反应 → 落定**
```text
He plants his palm on the desk and pushes himself up; the desk shifts a centimetre with a dry scrape, the teacup on it trembles once and settles, and he stands still with his weight on both feet.
```

**常用的物理细节（每个接触选一两个，不要堆）**
- 重量：`his wrist and forearm show the load of the pistol`、`the bag drags her shoulder down`、`she steps heel-first, her weight landing on the front foot`
- 接触点：`his fingertips press into the paper and it buckles`、`the chair legs scrape across the tiles`
- 材质反应：纸会折、皱、撕而不会拉伸；布料被拉紧、起褶、慢半拍落下；水会晃、溅、顺着表面流；木头会震、会响；玻璃会裂纹从接触点散开
- 惯性和衰减：`the swinging lamp slows over three swings and stops`、`the rolling bead loses speed and stops against the teapot`
- 环境一起动：风同时吹动头发、衣角和灰尘，方向一致；人走过时水洼起波纹
- 落定：`settles`、`comes to rest`、`stops against`、`holds its new shape`

**接触戏怎么写得有分量**（官方改写的写法，四步之内补细节；本地还没出片验证，见 `pipeline-and-settings.md` A/B 表第 18 项）：
- **起因**带时机词：`Just as his fingertips graze the paper, …`。没交代原因的物理变化，补一个看得见的起因（官方把"念珠散开"写成 `the string holding the black prayer beads from Shot 1 snaps without warning`）。
- **用力**：主动方先整个身体动，再接触（`lunges forward`）；每个接触最多一个力度或突然副词（`forcefully`、`abruptly`、`sharply`）。入画的全身大景别里不用 `violently`，免得动作过猛、肢体变形。
- **反应**：既写接触点，也写受力方上游的身体（`The young man's shoulders tense sharply as his forward momentum is halted.`、`Jerked to a sudden halt by his pinned tail, …`）。快的接触放在插入特写里时（只拍手和物件，看不到肩膀），上游身体的反应写在紧接的下一镜里。
- **僵持**（有就写）：写持续受力——指节发白、手背青筋、呼吸声（`the older man's knuckles turning pale`）；手抖最多写 `a faint tremor`，不写 `tremble visibly`。
- **落定或抽离**：落定照常写；"在对方没松的手下面滑出"（`slowly sliding out from under the older man's unyielding grip`）只在只拍手和物件的特写里慢速写，配摩擦声。
- 快的接触那一下仍按第 3A 节只放在插入特写里，不学官方在双人中近景里写擒腕。常用结构：中景写起因（伸手）→ 插入特写写接触（只拍手和桌面，`holding a static shot`）→ 切回中景写受力方的身体反应、僵持和抽离。插入特写保持静止，接触的冲击感交给声音和下一镜的身体反应。

**方向跟着力走**：横砍碎片往侧面飞，下砸往下塌，撞墙裂纹从接触点散开，被推的人往推的方向退。

**速度要写明**：H3 容易把惊吓、碰撞拍成慢动作。写 `in real time`、`at once`、`a sudden full-body flinch`；真要慢动作才写 `in slow motion`，而且全段只用一次。

**写不了的物理就别写**：精确的数字（推 37 厘米）、复杂的连锁反应（多米诺式五步因果）、流体的细节形状，模型都接不住。写一个最主要的后果就够。

## 3. 动作戏设计

### A. 一对一，或有剧情的冲突（真人剧最常用）

- 快的接触（踩、刺、砍、扇耳光）只放在一个特写镜头里，接触那一下配一个可见反馈（火星、灰、布料一甩、桌面一震）。普通触碰不凭空生火花。
- 慢的接触（拥抱、搀扶、递东西）要么写完整过程，一步不跳：放下手里的东西 → 走近 → 伸手 → 对方先愣一下再回应；要么停在"将触未触"。
- 每次交锋至少改变一样东西：位置、高度、方向、谁占上风。写清结果状态：人停在哪、哪只手还握着什么。
- 武器和能力只用参考图里有的或用户指定的，没有就徒手，不凭称号（"剑客"）补武器。能力写清从身体哪里发出、往哪去、碰到什么、怎么消散。
- 情绪升级时镜头晃动也升级：开头 `the camera shakes slightly`，最激烈那一下 `shakes strongly`。晃动写在中景、反应镜头上；接触的插入特写保持静止。

### B. 一打多（爽片）

这套骨架来自线上平台的高分案例，那些案例经过了官方 Context-IR 和 2K 重生成。本地 768p 直接跑，切得太密会乱，所以 15 秒最多 6 个镜头：

| 时间 | 运镜 | 这一段干什么 |
|---|---|---|
| 0–2.0s | 俯拍甩到仰拍 | 登场、落地、武器亮起，还不打 |
| 2.0–4.5s | 低角度从背后跟拍 | 冲进敌群，第一击，前排敌人碎掉 |
| 4.5–7.0s | 侧面跟拍，同一镜里快速推近到眼睛、面具或枪口的特写（不切） | 跃起砸地，地面炸开；推近到特写 |
| 7.0–9.5s | 侧面跟拍，一个镜头（不拆成两三个角度的快切：拆开后每镜不到 1.5 秒，全段也会超过 6 个镜头） | 原地连击，每一下都有敌人碎掉 |
| 9.5–11.5s | 静止特写 | 一拍静：轻轻一碰，没反应，然后一击，全场同时碎 |
| 11.5–15.08s | 弧形绕拍后拉远 | 终结：主角自己的手做一个动作，全屏特效炸开，慢慢停在主角身上 |

配套：敌人一碰就碎成灰、墨、火星、纸屑，不演被打飞；主角尽量不露正脸（面具、兜帽、背影）；终结手势写清是主角自己的手（`raises his own right hand`）；环绕只在最后一段用；声音在 9.5 秒左右突然安静。

### C. 安静戏（一镜到底）

适用：一个人，或两个人但不接触；没有打斗。动作主要交给镜头（由远推近、贴脸后拉远、对焦虚实变化）。人只做几个小动作，但要有一个小事件：触发 → 反应 → 余波（画外有动静 → 一怔、偷瞄 → 松口气但头没转回来）。整段是一条主动作链，按时间先后写，最后停在一个定住的瞬间。

写法要点（参照 `official-calibration.md` 的 quiet_shen_fire）：
- 首句写景别和整段运镜（`a medium shot, the camera slowly pushes in toward …`）；写实真人戏放在底座和光源之后的第一句构图句。
- 触发可以用 `Suddenly, …` 开头；先后用事件锚定（`Suddenly`、`Once …`、`a beat later`），或用官方用过的 `Early in the shot`、`Toward the end`。不写片内秒数。
- 反应链保留"眼先动、头慢半拍"的明确时间差（`her eyes move first, sliding toward the sound; only a beat later does her head turn a fraction`），写一两句都可以。
- 运镜终点挂在最后一个从句上（`as the camera closes in on the flickering flames and her profile`），同时写清人停在什么状态。
- 画外声音的方位按简报写，不挪进画面（官方把"画外"的窸窣改成了 `the dark corner behind her`，不学）；手里道具的状态前后一致。
- 声音里写一处由动作引起的环境反馈，地面材质按项目卡（《纸引》大殿是湿石地，不是木地板），绑在反应链里已有的动作上（受惊后重心落回脚跟时的一下摩擦）；反应链里没有碰到地面的动作时，这个反馈可以不写，不要为它新加动作。再写人物的呼吸。配乐写 `N/A`。

## 4. 通用技巧

- **先拍结果，再揭原因**：神秘的东西先让观众看到它造成的动静（纸片自己一颤），下一镜再露出它是什么。
- **跨切镜的动作写明是延续**：`continuing the same movement from Shot 2, she is still holding her head`，而不是重新开始一个已经坐好的状态。
- **镜头绕人转时，人站着不动**：想换到某人背后看出去，让他站定，镜头沿一侧弧形推到肩后；或者他自己整个转身背对镜头。
- **两人往相反方向走**：每个镜头写明谁往画面左、谁往画面右，`the gap between them keeps growing`。
- **必须不动的东西写成状态**：`the car sits in park with the handbrake on and its wheels still`。
- **要某人全程在画面里**：在对方的镜头里用过肩构图（虚着的肩膀和后脑勺在前景）。

## 5. 句子库（照着改）

```text
He lunges for the basin, front claws skidding on the wet stone.
The wing catches him mid-stride; he is knocked sideways, rolls once and slides to a stop.
A thin claw comes down hard on the burning tip and pins it flat; sparks and black ash burst out from under it and the flame is crushed out.
His stiff paper body jerks taut and the bell at his throat jolts once.
She sets the cup down first, then reaches across the table; her fingertips stop just short of his hand.
He takes half a step forward, heel first in the soft dirt, and a small puff of dust drifts and thins.
The door swings shut behind her, bounces once against the frame and clicks closed.
The beads scatter across the walnut tabletop, roll, slow down and stop one by one against the teapot.
（插入特写）Just as his fingertips graze the paper, a thick hand clamps down on his wrist and forcefully presses it flat against the tabletop.
（切回中景）At the cut, the young man's shoulders tense sharply as his forward momentum is halted.
The string holding the black prayer beads from Shot 1 snaps without warning, and the beads scatter across the walnut.
The two hands hold there against each other, the older man's knuckles turning pale, both men breathing hard through the nose.
```
