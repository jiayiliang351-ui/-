# H3 异能样本独立证据审查

日期：2026-10-07。审查对象：`h3-calibration/tools/context_ir/powers/cases.json` 的原始简报、`results/<case_id>.prompt.txt` 的官方改写，以及审前 H3 skill 三件套。

## 证据边界与版本

- 这是文本忠实度与规则适用边界审查。没有调用网络、API 或渲染，没有读取 baseline/candidate 测试输出，没有修改仓库或已安装 skill。
- 官方改写能证明“该次改写使用了这种描述”，不能证明本地 H3-Base 能准确生成，更不能证明画面、声音、物理、剪辑或身份保持已经通过验收。
- 审查进行时父任务正在更新工作树。为避免把新修订当成旧规则，本文 skill 引用固定到仓库 Git HEAD `0ccc1d7f5b0aec48fc2c0e21d90ed5ff2c5d9c48`。本文给出的 skill 行号均为这个审前版本，不承诺对应修改后的工作树行号。可以用 `git show <该提交>:<文件>` 核对。
- 已独立比对上述提交中的 15 份三件套文件与 `D:/Codex/Users/Administrator/.codex/skills/` 对应文件：以 `utf-8-sig` 解码并统一换行后内容全部相等。此前看到的文件 SHA256 差异不能作为语义版本差异；正在修改的工作树另当别论。
- 下面逐条列出原始 case_id。采用的是固定选题样本，不是随机抽样；本文不据此宣称成功率或普遍优劣。某类只有都市、仙侠各一个样本，尤其不宜推出硬性镜头数或必备特效。

## 总体判断

最值得吸收的是“把指定的异能写成可观察的变化过程”，以及给现有写实规则增加明确的适用边界。现有文体、状态延续、可见因果、道具账和声音随事件变化已经能支撑这些需求，不需要另造一套堆满强制词的提示词格式。

最需要防止的是把降难方案当成改剧情权限：把打飞改为踉跄、把真人打手改成碎灰、给念力开的门补一只手、给时间静止的人群补小动作、为了镜头数表拆开用户指定的一镜到底。这些是规则适用问题；本次文本不能回答哪种拍法实际更稳。

官方输出也必须过简报忠实度检查。例如 `blast_xianxia` 改了站位高度，`telekinesis_xianxia` 加重了开门力度，`awaken_urban` 加重了打手反应，`timestop_urban` 加了静止期间额外声源，`onevsmany_urban` 把闪烁改成逐根熄灭。不能因其来自官方就把这些变化收成默认规则。

## 逐条审查

所有官方文件下文路径前缀均为 `tools/context_ir/powers/results/`；官方三段式的正文、声音、配乐分别位于文件第 1、2、3 行。原简报位于 `tools/context_ir/powers/cases.json` 对应 `id` 的 `text` 字段。

### 1. `blast_urban`：都市掌心能量波

**意图、声音与结尾。** 发光起点、向右发射、命中胸口、后飞撞柱、柱裂落灰、铁棍落水、掌心熄灭与手抖均保留。原简报未规定配乐，官方增添电子配乐应作为可选创作提案。没有台词不等于禁止呼吸或拟音。结尾没有被改成角色摆姿势或敌人消散。

原简报逐字：
> 她一推，一道蓝白能量波射出去，打中打手胸口，打手整个人往后飞，撞上他身后的水泥柱，柱子裂开、灰尘落下，铁棍当啷掉在积水里。她手心的光熄灭，手微微发抖。

官方逐字（`blast_urban.prompt.txt:1`）：
> The sheer kinetic force lifts him off his feet, hurling him violently backward through the air. He slams heavily into a thick concrete pillar in the background.

> The intense blue-white glow lingering in her open palm flickers and completely extinguishes, plunging her hand back into the dim, moody ambient lighting of the broken fluorescents.

> Her fingers twitch, and her entire hand trembles visibly from the intense physical exertion, while in the softly out-of-focus background, the iron rod from Shot 2 splashes heavily into a dark puddle.

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:13`）：
> | 被打飞、倒地、爬起这类受力动作 | 无重量、像被线吊着 | 只拍"一顿""被拽住""踉跄半步"；被打中的一方用碎掉、炸开、猛地停住来表现 |

skill 逐字（同文件 `:61`）：
> - 武器和能力只用参考图里有的或用户指定的，没有就徒手，不凭称号（"剑客"）补武器。能力写清从身体哪里发出、往哪去、碰到什么、怎么消散。

**条件建议与冲突。** 第二条已提供有效的能量链框架。可以补上“源点照亮附近材质；命中后写被命中物的反馈；熄灭后恢复原光源”，但仅适用于用户指定发光的能力。第一条不能用于删掉此次指定的打飞撞柱；可改景别、分解命中与撞击，不能静默换结果。官方 `trembles visibly` 也不应当作为通用力度模板，简报仍要求“微微发抖”。

### 2. `blast_xianxia`：指尖剑气、断刀与余势

**意图、声音与结尾。** 剑仍在鞘里，金色剑气断刀、刺客滚下阶梯、余势断枝、松针落下、收指袖飘均保留。站位从“台阶上方”变为“台阶中部”，这是空间设定偏移。笛子、木鱼式敲击是新增配乐，简报没有授权其成为必备设计。

原简报逐字：
> 站在台阶上方画面左边

官方逐字（`blast_xianxia.prompt.txt:1`）：
> A young male swordsman (S1) in a crisp white cross-collared robe with his hair tied in a neat topknot stands mid-staircase on the left, his hand resting on the hilt of a sheathed sword at his waist.

> He swipes his hand forward, and the golden energy arcs through the air, colliding with the assassin's blade, snapping the steel in two with a sharp metallic crack.

> The golden energy, continuing its trajectory, shears off a thick branch of the ancient pine on the right, causing a flurry of green pine needles to drift slowly into the misty air while the swordsman (S1) lowers his hand, his white sleeves fluttering gently in the mountain breeze.

skill 逐字（`h3-action-prompt-design/SKILL.md:125`）：
> - **方向写出来，不靠暗示。** 上楼下楼、进门出门、朝镜头还是背离、走哪个出口，都要写；画左画右推不出上下和里外。上楼到平台，先露头和肩。一串灯按什么顺序亮也要写。

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:13`）：
> | 被打飞、倒地、爬起这类受力动作 | 无重量、像被线吊着 | 只拍"一顿""被拽住""踉跄半步"；被打中的一方用碎掉、炸开、猛地停住来表现 |

**条件建议与冲突。** “余势”需要写明是同一道剑气继续原轨迹，不重新生成第二道攻击；保留武器未出鞘状态。空间规则本来就应拦住 `mid-staircase` 的漂移，不能把它收成范例站位。滚下台阶是用户明确指定的结果，不应被上述受力降难规则改成踉跄。断刀属于指定武器变化，也不能套用“细小物件写成已经完成”而省掉关键命中。

### 3. `telekinesis_urban`：无光念力、杯子与身体代价

**意图、声音与结尾。** 杯颤—水纹—沿桌面滑动—离桌一指—悬浮—出汗鼻血—松劲落杯的主链保留，且配乐为 `N/A`。但原简报的声音是封闭列表，官方又加入落桌 `clack` 和 `wet splash`；即使这些声音在现实中合理，严格执行“只有”时也应单独标为扩写，不能自动视为合规。

原简报逐字：
> 不要任何发光特效。

> 只有冰箱嗡嗡声、杯底摩擦桌面声和他的呼吸声。

官方逐字（`telekinesis_urban.prompt.txt:1`）：
> It then smoothly lifts a finger's width off the table, hovering in mid-air and shaking slightly under the warm yellow light, completely devoid of any glowing visual effects.

官方逐字（同文件 `:2`）：
> A distinct, gritty scraping sound of glass sliding against a wooden surface is clearly heard, concluding with a loud, sharp clack and a tiny wet splash when the glass drops back to the table.

skill 逐字（`h3-action-prompt-design/SKILL.md:161`）：
> - 同理：灯只在有触发时亮（脚步、咳嗽、开关、定时），道具只在手里动。纸扎"自己动"是《纸引》的有意设计，照项目卡写，先拍动静再露真身。

skill 逐字（`h3-shot-prompt/SKILL.md:31`，原句内片段）：
> 简报里"没有/不要 X"：物件和特效改写成正向的具体外观；"没有配乐"写 `N/A`；"没有台词"什么都不写。

skill 逐字（同文件 `:143`，原句内片段）：
> 简报写了"没有配乐"或"只有某某声"、一镜到底的安静戏、纯动作拟音段，写 `N/A`。

**条件建议与冲突。** 可以学习以桌面接触、水纹、位移、离桌高度和施力者生理代价表现不可见力量。不要把官方的否定短语照抄成通用例外：现有正向外观写法可保留，但不能因此补发光。真正需要修的是“道具只在手里动”的适用范围，念力受控物不应补手。声音封闭列表不仅要禁配乐，还要约束新增拟音。

### 4. `telekinesis_xianxia`：竹叶群体悬浮、风推院门

**意图、声音与结尾。** 手指触发—叶片抬到膝高—向右涌动—门打开的主链保留，没有额外可见光。门从“吱呀一声晃开”强化为暴力向外撞开，声音也加入 `loud, hollow wooden bang`；力度和开门方向是官方扩写。持续低弦乐同样是新增选项。结尾增加叶片继续穿过门口，可作为同一事件余波，不需要新能力。

原简报逐字：
> 所有竹叶像一阵风一样朝画面右边的院门涌出去，院门被吹得吱呀一声晃开。

官方逐字（`telekinesis_xianxia.prompt.txt:1`）：
> The heavy, fast-moving wave of leaves blasts into the wooden door, forcing it to swing violently outward on its hinges.

官方逐字（同文件 `:2`）：
> The soundscape culminates in a loud, hollow wooden bang and an audible, high-pitched creak of old hinges as the heavy courtyard door forcefully swings open, trailing off into a soft, settling flutter of scattered leaves.

skill 逐字（`h3-action-prompt-design/SKILL.md:153`）：
> - 门、闸、窗、抽屉、盖子、帘子，只在看得见的人动它时才动。一两句写完：谁、哪只手（两手都占着就用肩、胯、脚）、碰哪里（把手、门闩、链、铁条、门边）、往哪开（向里、向外到楼梯口、往画左）、开多大（一掌宽、一半、整个靠到墙上）、门和手停在哪。

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:37`）：
> - 环境一起动：风同时吹动头发、衣角和灰尘，方向一致；人走过时水洼起波纹

**条件建议与冲突。** 无形力量可以由一组同方向叶片运动和门的铰链反馈显现，保留“方向、幅度、终点”规则；“必须可见的人碰门”要限定于普通人力开门。叶群受同一施力事件控制，不等于若干人物各做独立动作。不能学习 `violently` 作为念力强度默认值，应回到简报的“晃开”。

### 5. `element_urban`：接触传霜、液体相变

**意图、声音与结尾。** 霜从手指接触处向外蔓延、纸杯结霜、热气消失、咖啡表面结冰、松手看掌心均保留。官方只明确展示右掌，而原文是“手掌”，不宜武断判成剧情错误。新增吸气声属于非台词，简报没有封闭声源列表；新增配乐仍是可选扩写。松手后杯子是否已经落在桌面，官方没有写清，应补状态而非凭空加摔杯。

官方逐字（`element_urban.prompt.txt:1`）：
> Instantly, a delicate web of crystalline white frost blooms outward from the exact points where her fingertips press against the paper, rapidly crawling across the entire surface of the cup.

> The rising steam abruptly vanishes, and the dark liquid coffee visible near the edge instantly glazes over into a solid, cloudy layer of ice.

> She immediately turns her right hand palm-up, staring intently down at her own skin, where a thin, shimmering layer of delicate white frost now completely coats her palm under the sterile fluorescent glare.

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:35`）：
> - 材质反应：纸会折、皱、撕而不会拉伸；布料被拉紧、起褶、慢半拍落下；水会晃、溅、顺着表面流；木头会震、会响；玻璃会裂纹从接触点散开

skill 逐字（`h3-action-prompt-design/SKILL.md:168`）：
> - **道具账**：几个、谁的、哪只手、什么状态（拿着、放下、开、关、掉了）。拿着东西的手不是空手：要去抓扶手，先写放下或松开。

**条件建议与冲突。** 材质规律用于基底、接触和余波，不能否定用户指定的相变。此处适合补“变化从何处开始、沿什么表面扩展、改变到何种最终状态”；不强行套能量投射的外部轨迹、命中目标或消散模板。道具账已能发现松手后的杯子归属问题，无须另立复杂规则。

### 6. `element_xianxia`：手部电弧、局部照明与熄灭

**意图、声音与结尾。** 右手、指间紫白电弧、变密、五指跳动、发梢静电、握拳熄灭、恢复月光与白烟的主链保留。焦味没有被写成画面可见对象；烟的可见描述适合本地文体。官方增添洞风、密集电流嗡鸣与电子低音，未违反“无台词”，但不是简报要求的唯一声音方案。

官方逐字（`element_xianxia.prompt.txt:1`）：
> The bright, concentrated purple electricity acts as a dynamic local light source, sharply illuminating the right half of her face and the rough cave wall behind her while casting dancing shadows.

> The intense electric light extinguishes instantly, plunging the cave back into the dim, cold blue moonlight, as a thin wisp of translucent white smoke curls upward from her tightly clenched knuckles and dissipates into the dark cave air.

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:61`，原句内片段）：
> 能力写清从身体哪里发出、往哪去、碰到什么、怎么消散。

skill 逐字（`h3-shot-prompt/references/cinematography.md:19`）：
> - 光写三件事：从哪来、软还是硬、落在哪里看得见（`a warm amber pool from the pendant lamp over the tea table, cold blue dusk from the window behind; faces half warm, half cool`）。

**条件建议与冲突。** 现有光源规则可直接用于发光异能；结束应写出能力照明退出后剩下的既有环境光。电弧属于局部受控效果，没有外部攻击目标，“碰到什么”不能作为所有能力的硬性字段，否则会擅自补攻击、爆炸或受害者。电光照亮场景也不能推广到无光念力。

### 7. `awaken_urban`：局部停雨与克制觉醒

**意图、声音与结尾。** 困在右侧护栏、三打手从左靠近、金色瞳圈、球状悬停雨滴、衣发后飘均保留。克制退半步被扩写成大眼、举手困惑和慌乱后撤；咬牙在正文中缺失。声音把雨滴停住写成雨落声骤停，但视觉只指定局部球形区域，不能据此默认整个城市或整个天台的雨声消失。

原简报逐字：
> 打手们停住脚步，往后退了半步。表情不要夸张，克制。

官方逐字（`awaken_urban.prompt.txt:1`）：
> [Shot 3] At 00:07.500, the camera cuts to a medium shot framing the hitmen, who stop in their tracks and instinctively recoil, stepping backward with wide, wary eyes, their hands raised slightly in confusion as they stare at the anomalous air currents emanating from the man (S1) in the foreground.

官方逐字（同文件 `:2`，原句内片段）：
> followed by a sudden, jarring cessation of rain-impact sounds when the suspension effect occurs, leaving only a low-frequency, hum-like air pressure sound.

> The hitmen's footsteps on the wet gravelly surface are crisp and heavy, followed by the distinct, frantic squeak of leather soles sliding against the wet roof as they scramble backward.

skill 逐字（`h3-shot-prompt/references/performance-and-dialogue.md:24`）：
> - 程度词决定真假：`a fraction` / `faintest` / `almost imperceptibly` / `a beat late`。

skill 逐字（`h3-action-prompt-design/SKILL.md:171`）：
> - 持续状态（伤、湿、脏、灯、门、碎片）除非画面里有可见原因，否则不重置。之后还要行动的角色不能用终结动词（碎了、化了），杂兵除外。

**条件建议与冲突。** 觉醒可以按“身体触发—能力显现—局部环境反应—他人反应”组织，不需要命中敌人。作用范围和声场范围分别核对；停住某一区域的雨滴，不自动推导出全场静音。克制表演规则应保留，官方的 `scramble backward` 不适合这个原简报。持续湿衣、血迹与站位也不应被觉醒特效重置。

### 8. `awaken_xianxia`：灵气收束、静场与恢复

**意图、声音与结尾。** 环绕灵气加速、衣发飘起、石台裂纹、碎石弹跳、能量回收、睁眼青光即逝、衣发落回均保留。金属闪响、笛与琴低音是新增声音层；“四周一静”在声音中被表达为环境风和振动停止，仍留混响，不等于数码绝对零声。

官方逐字（`awaken_xianxia.prompt.txt:1`）：
> At 00:07.500, the camera abruptly transitions to a tight close-up on her face, capturing the exact moment the white energy violently collapses inward into her body.

> A sudden silence falls, she snaps her eyes open, and a fleeting, intense cyan glow flickers deep within her irises before vanishing instantly.

> The fabric of her robe and her hair lose their tension and descend softly back against her frame in the settling air.

官方逐字（同文件 `:2`）：
> The moment the energy is absorbed, all ambient wind and vibration sounds are abruptly silenced, leaving only a faint, hollow atmospheric reverb.

skill 逐字（`h3-action-prompt-design/SKILL.md:98`，原句内片段）：
> 最后一秒没有新动作，但烟、光、衣摆、环境声还在动。

skill 逐字（`h3-director-json-review/SKILL.md:117`）：
> | 尾巴和长度 | 时间点用的是实际片长吗？最后一秒还有余动和环境声吗？ |

**条件建议与冲突。** 主动能量回收与衣发缓慢落回属于能力结束与余波，不应另加一个新事件。用户指定静场时，尾段“必须还有环境声”不能覆盖它；可以保留可见衣发余动。此样本正文虽然只有 `[Shot 1]` 标签，却在 `00:07.500` 写了 `abruptly transitions to a tight close-up`，实际含转场。不能用标签数宣称官方对该需求采用真正一镜到底，也不能把缺标签学成格式。

### 9. `timestop_urban`：单镜头冻结世界、仅主角行动

**意图、声音与结尾。** 一镜到底、响指冻结、静止人群/鸽/喷泉/杯滴、取杯归还、再响指恢复、外卖员吃惊均保留。官方额外让主角继续走远。严格按“静止时只有脚步声”，衣料声、纸杯轻敲与液体声是明确声源扩写；`N/A` 配乐是正确保留。边界响指属于启动/解除事件，应和冻结期间持续声源分开写。

原简报逐字：
> 全片一个镜头。静止时环境声全部消失，只有他的脚步声。

官方逐字（`timestop_urban.prompt.txt:1`）：
> The camera steadily tracks the young man as he calmly weaves through the completely immobilized crowd, acting as the sole moving figure in the environment.

> The delivery rider jerks his shoulders in surprise, blinking rapidly as he stares down at the perfectly intact coffee cup in his hand, while the young man continues walking away through the crossing.

官方逐字（同文件 `:2`）：
> In this sudden vacuum, only the pronounced, rhythmic clack of the young man's hard-soled shoes on the asphalt and the heavy fabric rustle of his trench coat are clearly heard in the foreground.

> A soft paper tap and subtle liquid squelch sound as he handles the suspended coffee cup.

skill 逐字（`h3-shot-prompt/references/performance-and-dialogue.md:30`，固定段内片段）：
> Every character is always occupied with some small piece of business — handling an object, finishing a movement, glancing at something off-topic.

skill 逐字（`h3-shot-prompt/SKILL.md:98`）：
> 5. 两人以上的写实真人戏：照抄全局表演段；不要字幕时接字幕防护句。

**条件建议与冲突。** 时间静止必须区分“保持哪种姿态的冻结对象”“能行动的主体”“被主体接触后可移动的物件”“恢复触发”。固定活人感段给“每个人”安排持续小动作，与冻结人群直接冲突，应整段免套而不是在其后再堆禁令。声音是封闭列表时，后文不应添普通拟音，即便物件确实被触碰。结尾若外卖员反应是指定落点，新增走远不能挤掉这一信息。

### 10. `timestop_xianxia`：箭雨冻结、单镜头救人

**意图、声音与结尾。** 箭从右上屋顶射出、左侧女侠左掌触发、箭/人/灯/尘静止、右手拨箭、抱孩子转移、落掌恢复、箭击空地均在正文出现。一镜到底保留。官方补了小男孩被苹果篮绊倒、向上拨箭、右侧摊柱、抱起后放下孩子等细节；可作为可核对的空间设计，不能反推原简报必需有篮子或固定 45 度灯笼。简报没有封闭声音列表，不能把都市案例的“只留脚步”推广到这里。

官方逐字（`timestop_xianxia.prompt.txt:1`）：
> The camera smoothly tracks the woman as she calmly weaves her way through the deadly matrix of floating arrows.

> She reaches out with her bare right hand and lightly pushes the side of a black arrow that is pointed squarely at the frozen boy's head, visibly deflecting its trajectory upward.

> Without pausing, she scoops the rigid little boy into her left arm, holding him securely against her chest, and briskly steps out of the impact zone, carrying him to the safety of a sturdy wooden stall on the right edge of the street.

> The camera pans right to follow her as she gently sets the boy down behind a wooden pillar and sharply lowers her left hand.

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:11`）：
> | 两个人在同一个全身画面里精确接触（擒拿、拥抱、扶起、递东西） | 穿模、手粘在一起、多出一只手 | 接触那一下给特写（只拍手和物件）；或者拍接触前和接触后两镜，把接触藏在切点里；或者停在"将触未触" |

skill 逐字（`h3-shot-prompt/SKILL.md:106`，原句内片段）：
> 一个镜头只有一条主动作链，外加最多一个反应。一条链指同一个人、同一个目的、一步接一步的动作（提壶 → 倒茶 → 放壶 → 推杯）；同一个镜头里不并行第二条链。

skill 逐字（`h3-action-prompt-design/SKILL.md:168`）：
> - **道具账**：几个、谁的、哪只手、什么状态（拿着、放下、开、关、掉了）。拿着东西的手不是空手：要去抓扶手，先写放下或松开。

**条件建议与冲突。** 女侠“进场—定时—拨箭—抱走—解除”可以视为同一救人目的的连续主链，环境集体恢复是同一触发的反馈，不自动成为需要拆镜的第二独立人物链。精确接触风险要提示，但不能强行两镜或停在将触未触，从而丢掉救人完成与一镜到底。左手既负责冻结触发又参与抱孩子，需核对解除手势和持抱状态；官方未明确“只要左掌姿态变化就解除”，因此这里只能判为控制姿态需要澄清的歧义，不能断言已经逻辑矛盾。

### 11. `onevsmany_urban`：真人打手、无光念力与同时压倒

**意图、声音与结尾。** 六名打手按第一人、第二人、剩余四人的状态推进；接棍撂倒、念力推飞撞车、车凹警报、下压群倒和理衣均保留。最后“灯管一根根闪烁”被写成逐根闪烁后熄灭，是结束状态改变。官方配乐和爆发低音属于新增声音选择，车警报是原简报已指定的事件声。

原简报逐字：
> 最后他理了理大衣，车库灯管一根根闪烁。

官方逐字（`onevsmany_urban.prompt.txt:1`）：
> Without physical contact, an invisible kinetic force instantly halts the thug's momentum, throwing him and his knife violently backward through the air.

> The invisible downward pressure instantly flattens all four rushing thugs face-first onto the wet concrete in unison.

> Above him, the long white fluorescent tubes bolted to the concrete ceiling sputter and flicker out one by one, casting erratic strobing flashes over his stoic face.

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:86`）：
> 配套：敌人一碰就碎成灰、墨、火星、纸屑，不演被打飞；主角尽量不露正脸（面具、兜帽、背影）；终结手势写清是主角自己的手（`raises his own right hand`）；环绕只在最后一段用；声音在 9.5 秒左右突然安静。

skill 逐字（同文件 `:18`）：
> | 多人同时做不同的事 | 动作互相干扰、有人突然消失 | 一个镜头只有一个人在做主动作，其他人静止或只做重复的小动作 |

**条件建议与冲突。** 群体同时压倒是同一次下压的集体后果，与多人各做独立主动作不同，应允许。打手仍是有身体和位置的真人，不能用一打多模板把他改成灰、遮住主角脸或强制 9.5 秒静音。保留“六人—已倒一人—飞出一人—剩四人”的数量账。灯光跨镜状态应按简报保留闪烁，不能学习 `flicker out` 作为自动结束。

### 12. `onevsmany_xianxia`：御剑、分影与回鞘

**意图、声音与结尾。** 主角不亲手拔剑、剑自行出鞘、指引穿梭、挑飞刀剑与断竹、分为九影环绕、刺客失去攻势、回鞘、落叶均保留。官方补出“九影合回实体剑”使数量回收更清楚，适合条件建议。冷白微光被强化为刺眼光和拖尾，九影生成强阵风把刺客全部吹飞，也是幅度/机制扩写；不能作为所有御剑需求的默认特效。

原简报逐字：
> 剑身泛着冷白微光

> 九道剑影环绕着他旋转，刺客们全部倒地或后退。

官方逐字（`onevsmany_xianxia.prompt.txt:1`）：
> Without any physical contact, the longsword bursts upward out of the scabbard on the cultivator's back, emitting a piercing, cold white glow.

> The radiant blade streaks straight up into the night sky, trailing a ribbon of luminescent energy.

> These nine ethereal blades spin violently in a tight, protective halo around him, generating an immense kinetic gust that blows the surrounding assassins completely off their feet, sending them tumbling backward into the dirt.

> The nine sword shadows merge seamlessly back into one solid blade, which plunges straight down into the scabbard with a decisive physical lock.

skill 逐字（`h3-action-prompt-design/SKILL.md:161`）：
> - 同理：灯只在有触发时亮（脚步、咳嗽、开关、定时），道具只在手里动。纸扎"自己动"是《纸引》的有意设计，照项目卡写，先拍动静再露真身。

skill 逐字（同文件 `:170`）：
> - 要一路跟住的东西，在每个相关镜头里用一句陈述重复（`the same bag is still in his left hand`），不用括号标签。

skill 逐字（`h3-shot-prompt/references/physics-and-action.md:86`，原句内片段）：
> 敌人一碰就碎成灰、墨、火星、纸屑，不演被打飞

**条件建议与冲突。** 御剑应写明遥控触发、剑从何处出鞘、与手势关系、穿梭造成什么材料反馈、实体剑/剑影数量与回鞘终态。需要免除“道具只在手里动”，同时保留“同一柄剑”的身份与状态账。九影是指定变化，不能误报成随机重复；再合回一柄是回鞘前的合理衔接，但不要擅自把数量扩成更多实体剑。真人刺客也不应改成碎灰。普通人力物理规律不能要求飞剑必须被人手抓住。

## 最值得补充的少量条件规则

下列是本次文本比较支持的边界建议，不是已经验证本地渲染收益的新硬规则。

1. **先锁定简报承诺，再降难。** 用户指定的能力类型、命中结果、人数、光效有无、声音限制、结束状态与一镜到底优先于通用骨架。风险用景别、信息顺序和可见反馈控制；确需改变剧情时在提示词之外提出替代方案。对应 `blast_urban`、`blast_xianxia`、`timestop_xianxia`、`onevsmany_urban`、`onevsmany_xianxia` 的上述逐字证据。
2. **能力按可观察变化分支描述。** 投射型写源点—传播—命中—材料/身体反馈—消退；无光遥控写触发—物体位置/高度/姿态变化—落定，不补光；元素变化写接触起点—传播—终态；觉醒写自身变化—作用范围—环境响应—收束，不强加受害者。对应 `blast_urban`、`telekinesis_urban`、`telekinesis_xianxia`、`element_urban`、`element_xianxia`、`awaken_urban`、`awaken_xianxia`。
3. **冻结与同因群体反馈是明确例外。** 时间静止区分谁能动、冻结对象的姿态、可操作物件与恢复触发；冻结人群免套“每人始终小动作”。同一次施力造成多人同时倒下或环境同时恢复，不等于多条互相竞争的独立主动作链。对应 `timestop_urban`、`timestop_xianxia`、`onevsmany_urban`。
4. **声音按阶段与许可范围写。** 常态—触发—能力持续—解除分别核对。写“只有某某声”就按封闭声源列表检查拟音和配乐；指定静场时免除尾巴必须有环境声的默认。局部能力不自动等于全场静音。对应 `telekinesis_urban`、`timestop_urban`、`awaken_urban`、`awaken_xianxia`。已有 `non_diegetic_music: N/A` 规则应保留，但它本身不足以约束额外拟音。
5. **能力结束也要交账。** 剑/影、人数、手中物、灯光、破损与衣发状态逐镜延续；“闪烁”不能自动改“熄灭”，“微光”不能自动升级为强光拖尾，“晃开”不能自动升级为撞开。对应 `telekinesis_xianxia`、`element_urban`、`onevsmany_urban`、`onevsmany_xianxia`。这些首先是忠实度检查，不需要为每个词增设一条泛化限制。

## 不应从本次样本推出的结论

- 不能说官方少镜头在本地更稳、某个秒数必然最好、特写一定胜过全身、能量轨迹已经正确、群体攻击已经可用。本文没有渲染证据。
- 不能废除现有快剪经验或默认电影感底座；这批文本没有和它们做受控视觉比较。只应处理其覆盖明确简报的边界。
- 不能把 `violently`、强光、拖尾、敌人全飞、低频冲击声、配乐骤停当成异能必备。本文逐条已经指出它们有时来自官方扩写而非原简报。
- 不能把所有“没有”都照官方译文写成负向句。无光念力需要保留语义；本地具体措辞仍应尊重既有的正向可观察描述策略，效果需后续验证。
- 不能按 `[Shot N]` 标签直接统计实际镜头，尤其是 `awaken_xianxia` 的未标号转场；也不能把缺失标号当作可推广文体。

## 验证记录

已运行自动子串校对：74 处块引用全部能在对应源文本中逐字匹配，覆盖上述 12 个 case_id，未发现引用不匹配。skill 核对对象为上述固定 Git 提交，避免父任务正在修改的工作树影响引用。报告内技能行号也按审前提交复核。校对只证明引文存在，不证明本文推断或渲染质量。
