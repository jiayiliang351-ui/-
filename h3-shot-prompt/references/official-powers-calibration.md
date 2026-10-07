# 官方异能改写原文（12 条 T2VA）

来源：仓库 `tools/context_ir/powers/cases.json` 与 `results/{case_id}.json` 中的 `task.content.prompt`。2026-10-07 从已保存的成功响应复制，每个需求一次采样；没有新调用 API，没有参考图输入，没有渲染。下方英文正文逐字保留，包含原文的瑕疵；`powers-and-effects.md` 是如何有条件使用它们的说明。

## 阅读前先核对

- 官方输出只证明一次改写怎样写，不证明 H3 的画质、物理、身份或音画表现。已有第二轮出片规则优先按各自证据使用，不因新样本少切就改快剪表。
- 字数按原分析脚本的英文词计数；`[Shot N]` 只数显式标签。`awaken_xianxia` 虽只有 `[Shot 1]`，正文在 00:07.500 转到面部特写，不能当一镜到底；`blast_xianxia` 的后续镜头头未用明确切镜动词，`onevsmany_xianxia` 的末镜也没有明确切镜句。
- 12 条中 10 条 `non_diegetic_music` 不是 `N/A`（例外是 `telekinesis_urban`、`timestop_urban`）；这些简报均未要求配乐。保留原文用于核对，写新段不跟着自加配乐。
- `timestop_urban` 静止期间新增衣料、碰杯和液体声音，与简报“只有他的脚步声”不一致。`telekinesis_urban` 声音也超出简报列出的三类声源，写新段先守原声音限制。
- `element_urban` 松开双手前没交代杯子已放稳。`timestop_xianxia` 左手触发、左臂抱孩子、放手解除之间的占用不清；拨偏箭写向上，结尾又把它与整批箭一同写进地面，轨迹与落点的衔接需要核对。新写时补动作连接，不能盲抄。
- `awaken_urban` 简报只定住身边雨滴，正文基本保留局部范围，但声音把雨声整体切掉，范围需要核对；`MWS` 等缩写不照学。
- 发光、隐形、悬浮、结束状态按原需求分别处理；原文里的自加细节、配乐、强副词、无对白人物的 S 编号、缺镜头标签或重复否定不自动升级为规则。

## 用例目录

- [blast_urban](#blast_urban) — 8 秒
- [blast_xianxia](#blast_xianxia) — 8 秒
- [telekinesis_urban](#telekinesis_urban) — 10 秒
- [telekinesis_xianxia](#telekinesis_xianxia) — 10 秒
- [element_urban](#element_urban) — 8 秒
- [element_xianxia](#element_xianxia) — 8 秒
- [awaken_urban](#awaken_urban) — 10 秒
- [awaken_xianxia](#awaken_xianxia) — 10 秒
- [timestop_urban](#timestop_urban) — 15 秒
- [timestop_xianxia](#timestop_xianxia) — 15 秒
- [onevsmany_urban](#onevsmany_urban) — 15 秒
- [onevsmany_xianxia](#onevsmany_xianxia) — 15 秒

## blast_urban

名义时长：8 秒；比例：16:9。

简报原文：

写实都市异能短剧，深夜废弃地下停车场，日光灯管一半坏了，水泥柱和积水。年轻女人（短发、黑色机车夹克、牛仔裤）站在画面左边，对面画面右边一个拿铁棍的光头打手朝她冲过来。她右手掌心向前，掌心里先亮起一小团蓝白色的光，光越聚越亮，照亮她的脸和夹克；她一推，一道蓝白能量波射出去，打中打手胸口，打手整个人往后飞，撞上他身后的水泥柱，柱子裂开、灰尘落下，铁棍当啷掉在积水里。她手心的光熄灭，手微微发抖。没有台词。动作要有重量，能量要有来源、轨迹、命中和消散。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot, the camera executes a slow push in on the tense standoff. The setting is a desolate, abandoned underground parking lot at midnight, where half the overhead fluorescent tubes are broken, leaving heavy shadows among thick concrete pillars and large water puddles on the cracked floor. On the left midground stands a young woman (short dark hair, slim build, black leather motorcycle jacket, dark denim jeans). On the right, a burly, bald thug in a grimy tank top clutches a rusted iron rod. The thug aggressively rushes toward her, splashing heavy boots through a puddle. The woman stands her ground, raising her right hand with her palm facing forward. A concentrated, swirling orb of blue-white light suddenly ignites in her palm, rapidly intensifying and casting a brilliant, glowing illumination across her sharp facial features and the dark folds of her leather jacket. She steps into a low stance and thrusts her palm forward, launching a blazing blue-white energy wave toward the right. [Shot 2] At 00:03.500, the camera cuts to a medium shot, executing a fast tracking shot following the energy wave from Shot 1. The glowing blue-white beam strikes the bald thug from Shot 1 squarely in the chest. The sheer kinetic force lifts him off his feet, hurling him violently backward through the air. He slams heavily into a thick concrete pillar in the background. Deep cracks instantly web across the grey cement upon the heavy impact, sending a cascade of white dust and small debris falling over his slumping shoulders. His grip goes slack, and the rusted iron rod slips from his hand, tumbling downward out of frame. [Shot 3] At 00:06.000, the shot transitions to a close-up, with a static shot focused on the extended right arm of the young woman from Shot 1. The intense blue-white glow lingering in her open palm flickers and completely extinguishes, plunging her hand back into the dim, moody ambient lighting of the broken fluorescents. Her fingers twitch, and her entire hand trembles visibly from the intense physical exertion, while in the softly out-of-focus background, the iron rod from Shot 2 splashes heavily into a dark puddle.
overall_soundscape: The scene opens with the loud, rhythmic splashing of heavy footsteps charging through shallow water, layered beneath the low, electrical hum and sporadic crackle of failing fluorescent lights. A sharp, high-pitched electrical whine surges loudly in the foreground as the energy orb ignites, snapping into a heavy, concussive boom when the wave fires. This transitions into a brutal, resonant thud as the body slams into solid concrete, accompanied by the dry, gritty crack of splitting rock and the patter of falling debris. The sequence closes with a sharp metallic clang that immediately gives way to a distinct, wet splash as the iron rod hits the puddle, leaving only a quiet, breathy ambient hum.
non_diegetic_music: Heavy, pulsing electronic bass synthesizer, fast tempo, driving a sudden, aggressive crescendo that abruptly cuts out into total musical silence upon the heavy physical impact.
```

## blast_xianxia

名义时长：8 秒；比例：16:9。

简报原文：

写实古风仙侠，清晨山门前的长石阶，云雾缭绕，两侧古松。白衣青年剑修（束发、白色交领长袍、腰间佩剑未出鞘）站在台阶上方画面左边，一个黑衣蒙面刺客从画面右边台阶下方持刀扑上来。剑修并起右手食指中指，指尖凝出一道金色剑气，抬手一划，金色剑气呈弧形飞出，斩在刺客刀身上，刀断成两截，刺客被冲得滚下台阶，剑气余势削断台阶旁一截松枝，松针簌簌落下。剑修收指，衣袖还在飘。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, a wide shot capturing a weathered stone staircase at a mountain gate during dawn, enveloped in thick, swirling white mist with ancient, gnarled pine trees standing on both sides. A young male swordsman (S1) in a crisp white cross-collared robe with his hair tied in a neat topknot stands mid-staircase on the left, his hand resting on the hilt of a sheathed sword at his waist. From the lower-right foreground, a masked assassin in a tight-fitting black tactical outfit lunges upward with a steel curved blade, the camera using a Static Shot to frame the tense confrontation. [Shot 2] At 00:03.200, the camera tilts slightly upward to follow the swordsman (S1) as he brings his right index and middle fingers together, conjuring a brilliant, razor-sharp golden sword aura. He swipes his hand forward, and the golden energy arcs through the air, colliding with the assassin's blade, snapping the steel in two with a sharp metallic crack. [Shot 3] At 00:05.500, the camera executes a slight Pedestal Down to track the impact as the masked assassin, disarmed and off-balance, tumbles backward down the stone stairs. The golden energy, continuing its trajectory, shears off a thick branch of the ancient pine on the right, causing a flurry of green pine needles to drift slowly into the misty air while the swordsman (S1) lowers his hand, his white sleeves fluttering gently in the mountain breeze.
overall_soundscape: The ambient sound of a soft mountain breeze whistling through the pine needles is heard throughout, layered with the rhythmic, heavy thud of the assassin's boots hitting the stone stairs. The intense crack of metal snapping provides a sharp, high-frequency sound, followed by the soft, rustling hiss of pine needles falling onto the stone steps.
non_diegetic_music: A solo, low-register bamboo flute plays a slow, sustained melody, accompanied by a subtle, rhythmic strike of a wooden temple block that sets a tense, martial atmosphere.
```

## telekinesis_urban

名义时长：10 秒；比例：16:9。

简报原文：

写实都市异能短剧，傍晚老旧出租屋的厨房，暖黄灯光，窗外是城市黄昏。十七岁左右的少年（瘦、灰色连帽衫）坐在餐桌前画面右边，盯着桌上画面左边的一只装了半杯水的玻璃杯。不要任何发光特效。杯子先轻轻颤动，水面起细纹，然后杯子贴着桌面慢慢滑向他，再离开桌面浮起一指高，悬在空中微微晃。少年额头冒汗，一滴鼻血流到上唇。他一松劲，杯子落回桌面，水溅出一点。只有冰箱嗡嗡声、杯底摩擦桌面声和他的呼吸声。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium shot, the camera pushes in slowly. A skinny, approximately seventeen-year-old boy sits in the right midground of an old, cramped kitchen, wearing a faded grey cotton hoodie. On the left side of a scratched wooden dining table sits a plain glass half-filled with clear water. The scene is illuminated by a bare, warm yellow overhead bulb casting stark shadows, while the muted orange and blue of city twilight is visible through a dirty window in the background. The boy stares intensely at the glass, leaning his torso forward. The glass gently trembles on the wood, and fine, rapidly vibrating ripples form on the surface of the water inside. [Shot 2] At 00:03.500, the camera cuts to a close-up on the table surface, holding a static shot. The glass from Shot 1 slowly slides across the wooden tabletop from left to right, drawn toward the boy. It then smoothly lifts a finger's width off the table, hovering in mid-air and shaking slightly under the warm yellow light, completely devoid of any glowing visual effects. [Shot 3] At 00:07.200, the camera cuts to a tight close-up of the boy from Shot 1, tilting down slightly as he reacts. Heavy beads of sweat glisten on his forehead. A single, dark red drop of blood flows from his nose down to his upper lip. He suddenly exhales and slumps his shoulders, his facial muscles relaxing as he loses his intense focus. Immediately, the hovering glass drops back down into the lower edge of the frame, hitting the tabletop and splashing a small amount of water over the rim onto the wood.
overall_soundscape: A continuous, low-pitched mechanical hum of an old refrigerator sets the ambient room tone. Pronounced, heavy nasal breathing from the boy is clearly heard in the foreground, growing slightly more strained before releasing in a sharp, audible exhalation. A distinct, gritty scraping sound of glass sliding against a wooden surface is clearly heard, concluding with a loud, sharp clack and a tiny wet splash when the glass drops back to the table.
non_diegetic_music: N/A
```

## telekinesis_xianxia

名义时长：10 秒；比例：16:9。

简报原文：

写实古风仙侠，秋天竹林里的小院，地上落满枯黄竹叶，院门在画面右边。白发老道（灰色道袍、木簪、清瘦）站在院子中间偏左，背着一只手。他抬起另一只手的两根手指，满地竹叶慢慢离地，悬浮到膝盖高，静静停在空中微微打转；他手指往院门一指，所有竹叶像一阵风一样朝画面右边的院门涌出去，院门被吹得吱呀一声晃开。没有发光特效，力量只靠竹叶和风表现。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot from a neutral angle, the camera holds a static shot on an autumn bamboo forest courtyard. The rustic ground is thickly carpeted with dry, yellow bamboo leaves, and a weathered wooden courtyard door stands closed on the right side of the frame. In the center-left of the yard, a thin old Daoist stands upright with his left hand resting casually behind his back. He appears elderly with an aged face and long white hair secured by a simple wooden hairpin, wearing a loose, flowing gray cotton robe. Soft, diffused autumn daylight filters through the unseen bamboo canopy above, casting dappled, natural shadows across the yard. The Daoist slowly raises his right arm, extending his index and middle fingers toward the sky. In response to his physical gesture, the dry yellow leaves across the entire ground gently lift into the air. They hover suspended at knee height, quietly swirling and rotating on invisible currents while the man's expression remains entirely calm. He abruptly flicks his wrist, pointing his two extended fingers sharply toward the courtyard door on the right. Instantly, the hovering mass of leaves surges forward like a powerful gust of wind, rushing in a dense yellow stream toward the right side of the frame. The heavy, fast-moving wave of leaves blasts into the wooden door, forcing it to swing violently outward on its hinges. The old Daoist stands perfectly still in his original posture as the remaining leaves flutter wildly through the suddenly opened doorway.
overall_soundscape: Gentle ambient breeze rustling through tall bamboo stalks, seamlessly transitioning into a pronounced, dry crinkling and crisp, continuous rustle as hundreds of dry leaves lift off the dirt. A sharp, loud whoosh of rushing wind suddenly erupts in the foreground, followed by the intense, sweeping clatter of dry leaves hurtling rapidly through the air. The soundscape culminates in a loud, hollow wooden bang and an audible, high-pitched creak of old hinges as the heavy courtyard door forcefully swings open, trailing off into a soft, settling flutter of scattered leaves.
non_diegetic_music: Subtle, slow-tempo ambient score featuring a single, sustained low string drone that gradually swells in volume and texture, creating a sense of invisible rising pressure, and abruptly cutting to absolute silence the moment the door blasts open.
```

## element_urban

名义时长：8 秒；比例：16:9。

简报原文：

写实都市异能短剧，冬夜便利店窗边的高脚桌，冷白日光灯，窗外下雪。年轻女人（长直发、米色毛衣）双手捧着一杯热咖啡，热气往上飘，她心事重重。特写她的手和杯子：她的手指不自觉收紧，一层白霜从她指尖接触杯壁的地方向外蔓延，爬满纸杯，热气消失，咖啡表面结成一层冰，杯壁发出细小的咔咔声。她猛地松手，低头看自己的手掌，掌心也覆着一层薄霜。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium shot, the camera slowly pushes in. A young woman with long, straight black hair, wearing a thick beige knit sweater, sits at a high wooden table by a convenience store window. Harsh, cool white fluorescent overhead lights illuminate the interior, contrasting with the dark winter night and gently falling snow visible outside the large glass pane. The woman holds a white paper coffee cup with both her hands, thick steam visibly rising from the brim. She stares blankly downward, her shoulders slumped with a heavy, preoccupied expression. [Shot 2] At 00:03.500, the camera cuts to a close-up of the woman's hands and the paper cup from Shot 1. In a static shot, her pale fingers involuntarily tighten their grip, squeezing the cup slightly. Instantly, a delicate web of crystalline white frost blooms outward from the exact points where her fingertips press against the paper, rapidly crawling across the entire surface of the cup. The rising steam abruptly vanishes, and the dark liquid coffee visible near the edge instantly glazes over into a solid, cloudy layer of ice. [Shot 3] At 00:06.000, the camera cuts to a medium close-up of the woman as it tilts down slightly. She jerks her hands away from the cup with a sudden, panicked start, her eyes widening in shock. She immediately turns her right hand palm-up, staring intently down at her own skin, where a thin, shimmering layer of delicate white frost now completely coats her palm under the sterile fluorescent glare.
overall_soundscape: The continuous, low electrical hum of a convenience store refrigerator establishes the room tone, alongside the faint, muffled whistling of winter wind outside the window. As the freeze begins, a distinct, rapid crackling and crisp popping sound of ice forming dominates the foreground, paired with a sharp, subtle sizzle as the hot steam is suddenly extinguished. A sudden, sharp rustle of thick knit fabric and a quick, audible gasp are clearly heard as the woman violently jerks her hands away from the cup.
non_diegetic_music: Slow tempo, a subtle ambient synthesizer drone paired with sparse, echoing high-register piano keystrokes that build a quiet, eerie tension, featuring no percussion.
```

## element_xianxia

名义时长：8 秒；比例：16:9。

简报原文：

写实古风仙侠，夜里漆黑的山洞，只有洞口透进一点冷蓝月光。年轻女修（黑发高马尾、深紫色窄袖劲装）盘腿坐在画面中间，抬起右手。她食指和拇指之间先跳出几丝细小的紫白色电弧，噼啪作响，电光照亮她半边脸和洞壁；电弧越来越密，在她五指之间来回跳，她的发梢和鬓边碎发因为静电微微飘起。她猛地握拳，电光一下灭掉，洞里只剩月光和一缕焦味的白烟。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, a medium close-up pushing in slowly on a young female cultivator seated cross-legged in the center of a pitch-black, rugged stone cave. The setting is shrouded in darkness, illuminated only by a sliver of cold blue moonlight angling in from the unseen cave entrance on the left, casting deep shadows across the jagged, damp rock walls behind her. The young woman has a slender build, a calm expression, and long jet-black hair tied in a tight high ponytail. She wears a dark purple, tight-sleeved martial outfit made of textured woven fabric, accented with dark leather bracers. As the camera physically pushes in, she slowly raises her right hand to chest height. Suddenly, tiny, vivid purple-white electrical arcs leap between her index finger and thumb. The bright, concentrated purple electricity acts as a dynamic local light source, sharply illuminating the right half of her face and the rough cave wall behind her while casting dancing shadows. The electrical arcs grow visibly denser, jumping rapidly back and forth across all five of her spread fingers. The intense static electricity causes the tips of her ponytail and the loose stray hairs at her temples to float and flutter upwards in the charged air. With a swift, forceful motion, her jaw clenches slightly and she snaps her hand into a tight fist. The intense electric light extinguishes instantly, plunging the cave back into the dim, cold blue moonlight, as a thin wisp of translucent white smoke curls upward from her tightly clenched knuckles and dissipates into the dark cave air.
overall_soundscape: A hollow, low-frequency wind blowing through the cave establishes the quiet, eerie ambient room tone, followed by the distinct, sharp crackles and snaps of high-voltage electricity as the sparks ignite. The electrical sizzle rapidly grows into a loud, aggressive buzz in the foreground, culminating in a sharp, percussive pop as the woman clenches her fist, immediately giving way to a faint, airy hiss from the resulting smoke and the return of the hollow cave wind.
non_diegetic_music: A low, sustained electronic bass drone with a slow tempo builds subtle tension underneath the action, abruptly cutting to complete silence the moment the electric sparks are extinguished.
```

## awaken_urban

名义时长：10 秒；比例：16:9。

简报原文：

写实都市异能短剧，雨夜高楼天台，远处城市霓虹。年轻男人（湿透的白衬衫、黑西裤，嘴角有血）被逼到天台边的护栏前，背对画面右边的护栏；三个打手在画面左边慢慢围上来。他低着头喘气，咬紧牙关，再抬头时瞳孔泛起一圈淡金色的光；他身边的雨滴在半空中停住，在他周围悬停成一个球形的空隙，他的湿衬衫下摆和头发被一股看不见的气流吹得往后飘。打手们停住脚步，往后退了半步。表情不要夸张，克制。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, a MWS of a rain-swept urban skyscraper rooftop at night, with the blurred neon glow of the city skyline visible in the deep background. A young man (S1) with short, dark, wet hair, wearing a drenched white button-down shirt and black dress trousers, stands trapped against the edge of a metallic rooftop railing on the right, his lower lip split and stained with a dark trickle of blood. Three tall men in dark trench coats (the hitmen) slowly close in from the left, their figures partially obscured by the heavy downpour. The camera tracks the man (S1) as he leans heavily against the railing, head bowed, shoulders heaving with audible, labored breaths. [Shot 2] At 00:04.200, the camera cuts to a close-up of the man (S1) as he suddenly jerks his head upward, his gaze intensifying as a ring of pale, ethereal gold light pulses within his irises. The camera holds a static shot as the falling raindrops around him abruptly freeze in mid-air, suspending in a perfect spherical void around his body, while an unseen pressure causes his wet shirt hem and damp hair to flare backward as if caught in a sudden, powerful updraft. [Shot 3] At 00:07.500, the camera cuts to a medium shot framing the hitmen, who stop in their tracks and instinctively recoil, stepping backward with wide, wary eyes, their hands raised slightly in confusion as they stare at the anomalous air currents emanating from the man (S1) in the foreground.
overall_soundscape: The scene is dominated by the relentless, heavy thrum of rain against the concrete rooftop and metal railings, punctuated by the distinct, rhythmic splatters of water hitting fabric. As the man (S1) breathes, his wet, raspy gasps are clearly audible over the rain, followed by a sudden, jarring cessation of rain-impact sounds when the suspension effect occurs, leaving only a low-frequency, hum-like air pressure sound. The hitmen's footsteps on the wet gravelly surface are crisp and heavy, followed by the distinct, frantic squeak of leather soles sliding against the wet roof as they scramble backward.
non_diegetic_music: A slow, pulsing cinematic score featuring deep, sustained synth pads and a ticking metallic percussion that accelerates slightly in tempo as the man's eyes glow.
```

## awaken_xianxia

名义时长：10 秒；比例：16:9。

简报原文：

写实古风仙侠，悬崖边的石台上，云海翻涌，黄昏。年轻女子（白色素衣、长发披散）闭眼盘坐闭关。她周身的空气开始流动，淡白色的灵气像薄雾一样绕着她慢慢旋转，越转越快，她的长发和衣袖被带得飘起来；身下石台从她身边开始裂开细纹，碎石子微微弹起。最后灵气猛地收回她体内，四周一静，她睁开眼，瞳孔里一闪青色微光随即消失，头发和衣袖缓缓落下。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium full shot at eye level on a rugged stone platform overlooking a vast, rolling sea of clouds at dusk. A young woman (S1) with pale skin and long, flowing black hair worn loose, dressed in simple white linen robes, sits in a cross-legged meditative pose with her eyes firmly closed. The camera holds a static shot as thin, translucent wisps of white spiritual energy begin to emanate from the air around her, slowly orbiting her body. As the energy intensity increases, the camera begins a slow push in, capturing her hair and the wide sleeves of her robe beginning to flutter violently in the turbulent air. The stone platform beneath her begins to develop spiderweb-like cracks, with small pebbles visibly vibrating and jumping off the surface. At 00:07.500, the camera abruptly transitions to a tight close-up on her face, capturing the exact moment the white energy violently collapses inward into her body. A sudden silence falls, she snaps her eyes open, and a fleeting, intense cyan glow flickers deep within her irises before vanishing instantly. The fabric of her robe and her hair lose their tension and descend softly back against her frame in the settling air.
overall_soundscape: The constant, low-frequency roar of wind rushing through the canyon dominates the background. As the spiritual energy intensifies, a high-pitched, metallic shimmering sound grows in volume, layered with the distinct clatter of small stones hitting the hard, uneven rock surface. The moment the energy is absorbed, all ambient wind and vibration sounds are abruptly silenced, leaving only a faint, hollow atmospheric reverb.
non_diegetic_music: A low, sustained drone of a traditional Chinese bamboo flute (dizi) plays at a very slow, meditative tempo, accompanied by a single, deep resonant bass note from a guqin that swells in volume until the final silence.
```

## timestop_urban

名义时长：15 秒；比例：16:9。

简报原文：

写实都市异能短剧，白天繁忙的十字路口，行人很多，车流，鸽子。年轻男人（黑色长风衣、短发）站在斑马线中间，他打了一个响指，一切瞬间静止：行人停在半步、鸽子停在半空翅膀张开、喷泉的水柱凝固、一个外卖员手里滑落的咖啡杯停在半空，咖啡溅出的液滴也悬在空中。只有他能动，他在静止的人群中穿行，镜头一镜到底跟着他。他走到外卖员面前，把悬空的咖啡杯取下来，放回外卖员手里，再打一个响指，一切恢复运动，外卖员一愣，看着手里的杯子。全片一个镜头。静止时环境声全部消失，只有他的脚步声。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium tracking shot, the camera follows a young man with short black hair wearing a long black trench coat and dark trousers as he stops in the middle of a bustling, sunlit city crosswalk. The wide intersection is densely packed with moving cars and pedestrians in everyday casual clothing, while several gray pigeons flutter near the edges of the asphalt. The young man raises his right hand and sharply snaps his fingers. Instantly, the entire scene freezes. Pedestrians are locked mid-stride, a pigeon hangs suspended in mid-air with its wings fully spread, and the white water columns of a stone plaza fountain in the background solidify into motionless pillars. The camera steadily tracks the young man as he calmly weaves through the completely immobilized crowd, acting as the sole moving figure in the environment. He approaches a male food delivery rider wearing a bright yellow uniform jacket and a white safety helmet, who is frozen in a slightly pitched-forward posture. A white paper coffee cup hangs motionless in mid-air just below the rider's outstretched hand, surrounded by glossy brown droplets of splashing coffee permanently suspended in space. The young man smoothly reaches out, plucks the floating cup from the air, and firmly places it back into the rider's waiting grasp. He then turns his head slightly and snaps his fingers a second time. Immediately, the frozen world bursts back into chaotic motion. Pedestrians resume walking, the pigeon darts away, and the fountain splashes dynamically onto the stone. The delivery rider jerks his shoulders in surprise, blinking rapidly as he stares down at the perfectly intact coffee cup in his hand, while the young man continues walking away through the crossing.
overall_soundscape: The scene opens with a loud, chaotic urban ambience of rumbling car engines, distant honking, and the overlapping patter of dozens of footsteps. A sharp, distinct finger snap cuts through the noise, instantly followed by an absolute drop into ambient silence. In this sudden vacuum, only the pronounced, rhythmic clack of the young man's hard-soled shoes on the asphalt and the heavy fabric rustle of his trench coat are clearly heard in the foreground. A soft paper tap and subtle liquid squelch sound as he handles the suspended coffee cup. A second crisp finger snap occurs, immediately triggering the loud, rushing return of roaring traffic, splashing fountain water, and bustling crowd murmurs.
non_diegetic_music: N/A
```

## timestop_xianxia

名义时长：15 秒；比例：16:9。

简报原文：

写实古风仙侠，古镇集市的青石街，两边是摊位和灯笼，行人惊慌四散。一阵黑色羽箭从画面右上方的屋顶射向街心，街心有一个摔倒的小男孩。青衣女侠（高马尾、青色劲装、背着长剑）从画面左边冲出，抬起左手，时间凝住：所有箭停在半空，四散的人群停在奔跑的姿势，灯笼停在摇晃到一半的角度，扬起的尘土悬着不落。她在悬停的箭之间穿过，伸手把一支正对着小男孩的箭拨偏，把小男孩抱到街边，再放下手，时间恢复，所有箭钉进空地。一镜到底。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, a wide tracking shot captures the chaotic expanse of an ancient Chinese market street paved with uneven bluestone blocks, flanked by wooden vendor stalls and brightly glowing red paper lanterns. Fleeing villagers in coarse earth-toned linen Hanfu scatter in panic, kicking up thick clouds of yellowish dust. A dense volley of black-feathered arrows with heavy iron tips streaks diagonally from a grey-tiled roof in the upper right frame, raining directly toward the center of the street. In the dead center of the bluestone path, a little boy, around five years old in a simple beige tunic, trips over a spilled bamboo basket of apples, falling flat onto the stone and bracing for impact. Instantly, a young female martial artist in cyan dashes into the frame from the left midground. She has sharp, focused facial features, long black hair tied in a high wind-blown ponytail, and wears a form-fitting cyan martial arts outfit with silver leather bracers, carrying a long straight sword strapped across her back. She halts her sprint, digging her boots into the ground, and thrusts her left hand forward with her palm facing out. The camera pushes in slightly as time instantly freezes: the deadly black arrows hover completely motionless in mid-air just feet above the ground; the panicked pedestrians are locked in awkward mid-stride running postures with their mouths open in frozen screams; the glowing red lanterns hang suspended at a sharp forty-five-degree angle from their wooden eaves; and the thick, swirling dust kicked up by the crowd floats perfectly still, suspended like tiny golden particles. The camera smoothly tracks the woman as she calmly weaves her way through the deadly matrix of floating arrows. She reaches out with her bare right hand and lightly pushes the side of a black arrow that is pointed squarely at the frozen boy's head, visibly deflecting its trajectory upward. Without pausing, she scoops the rigid little boy into her left arm, holding him securely against her chest, and briskly steps out of the impact zone, carrying him to the safety of a sturdy wooden stall on the right edge of the street. The camera pans right to follow her as she gently sets the boy down behind a wooden pillar and sharply lowers her left hand. The moment her arm drops, time snaps back to normal speed. The deflected arrow and the entire black volley instantly resume their lethal velocity, slamming violently into the now-empty bluestone paving where the boy had just been lying, burying their iron tips deep into the stone as the crowd's frantic scattering continues around them.
overall_soundscape: The scene opens with a chaotic din of loud, overlapping screams, frantic running footsteps on hollow wooden boards and solid stone, and the sharp, aerodynamic whoosh of a massive arrow volley slicing through the air. A sudden, massive sub-bass boom reverberates, immediately followed by an absolute, unnatural vacuum of silence as time freezes. Within this dead silence, only the crisp rustle of the martial artist's thick cyan cotton clothing and the subtle leather creak of her boots are clearly heard as she steps forward, accompanied by a faint, metallic clink as her finger taps the hovering iron arrowhead. As she drops her hand, the deafening chaos instantly snaps back with a violent whoosh, culminating in the loud, rapid-fire clack, crack, and grinding crunch of dozens of iron arrowheads aggressively shattering into the hard bluestone pavement, overlapping with the resumed, panicked shrieks of the fleeing crowd.
non_diegetic_music: Aggressive, high-tempo traditional Chinese percussion featuring massive taiko-style drum strikes that abruptly cuts off into a deep, sustained, tense electronic bass drone during the time freeze, creating a feeling of weightless suspension, before exploding back into a rapid, thunderous rhythmic onslaught the second time resumes.
```

## onevsmany_urban

名义时长：15 秒；比例：16:9。

简报原文：

写实都市异能爽片，夜里空旷的地下车库，日光灯，几辆车。主角（三十岁男人，黑色高领毛衣、灰色长大衣）站在中间，六个拿刀和棍的打手从四面围上来。他先徒手接住第一个打手的棍子反手撂倒；第二个人扑来时他抬手，一股看不见的念力把对方连人带刀推飞，撞在车门上，车门凹陷、警报响；剩下的人一起冲上来，他双手往下一压，周围地面一圈积水和灰尘炸开，几个人同时被压倒在地。最后他理了理大衣，车库灯管一根根闪烁。快节奏，多镜头。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot, the camera trucks right across a dim, damp underground parking garage at night, characterized by concrete pillars, parked cars in the background, and cool, pale overhead fluorescent lighting that casts stark shadows. An on-screen 30-year-old male protagonist stands calmly in the center, wearing a black turtleneck and a long, tailored gray wool overcoat. Six male thugs in dark street clothes, gripping steel pipes and combat knives, form a tight, hostile circle around him. A thug in a black hoodie steps forward, swinging a heavy metal club. The protagonist swiftly raises his bare hand, catching the club mid-swing, and uses a fluid backhand motion to violently throw the attacker down onto the wet concrete. [Shot 2] At 00:03.500, the camera cuts to a medium shot and pulls out as a second thug from Shot 1, wearing a brown leather jacket, lunges forward with a gleaming silver knife. The protagonist from Shot 1 fluidly turns and raises his open right palm toward the attacker. Without physical contact, an invisible kinetic force instantly halts the thug's momentum, throwing him and his knife violently backward through the air. [Shot 3] At 00:06.500, the camera cuts to a close-up and pans left to follow the airborne thug from Shot 2. He slams brutally into the side door of a parked silver sedan. The metal door visibly caves inward with a deep dent upon impact, and the car's amber hazard lights immediately begin flashing. [Shot 4] At 00:09.500, the camera cuts to a wide shot and holds a static shot as the remaining four thugs from Shot 1 simultaneously sprint toward the center from the edges of the frame. The protagonist from Shot 1 sharply thrusts both hands downward toward the floor. A violent, perfectly circular shockwave erupts from the ground at his feet, blasting a ring of stagnant puddle water and pale dust outward. The invisible downward pressure instantly flattens all four rushing thugs face-first onto the wet concrete in unison. [Shot 5] At 00:12.500, the camera cuts to a medium shot and tilts up to reframe the protagonist from Shot 1. He stands perfectly still amidst the fallen bodies, lifting his hands to smoothly adjust the lapels of his gray overcoat. Above him, the long white fluorescent tubes bolted to the concrete ceiling sputter and flicker out one by one, casting erratic strobing flashes over his stoic face.
overall_soundscape: The scene opens with the low, echoing ambient hum of the underground garage, interrupted by the swift, audible whoosh of a swinging club and a sharp smack of a barehanded catch, ending in a loud thud of a body hitting wet concrete. A deep, resonant bass boom signals the telekinetic blast, immediately followed by a loud, violent crash of metal caving in as a body strikes a car door, triggering the shrill, rhythmic blaring of a car alarm in the background. A sharp, explosive splash of water and the loud, synchronized clatter of multiple bodies slamming into the ground follow the downward strike. The clip concludes with the crisp, distinct rustle of heavy wool fabric, paired with the sharp, erratic electrical crackle and buzz of failing fluorescent lights.
non_diegetic_music: Driving electronic synth-bass, fast tempo, featuring heavy industrial percussion beats, which abruptly drops out at the final moment, leaving only a single, low-frequency sustained drone.
```

## onevsmany_xianxia

名义时长：15 秒；比例：16:9。

简报原文：

写实古风仙侠爽片，月夜竹林，风吹竹叶。白衣剑修（束发、白色长袍）站在竹林空地中间，背后的长剑还在鞘里。十几个黑衣刺客从竹林四周跃出围攻。他不拔剑，只一抬手，背后长剑自己出鞘飞上半空，剑身泛着冷白微光；他手指一引，飞剑在刺客之间穿梭，挑飞刀剑、斩断竹子，被斩断的竹子成片倒下；最后飞剑在空中一分为九，九道剑影环绕着他旋转，刺客们全部倒地或后退。飞剑回鞘，竹叶慢慢落下。快节奏，多镜头。没有台词。

官方改写原文：

```text
integrated_multimodal_description: [Shot 1] Cinematic, a medium-wide shot pushes in on a moonlit bamboo forest filled with low-lying silver mist. A tall, lean cultivator stands perfectly still in the center of the clearing, his long black hair tied up in a jade guan. He wears a flowing white silk hanfu that flutters in the night breeze, and a silver-scabbarded longsword rests vertically across his back. The cold, directional moonlight casts sharp shadows as over a dozen black-clad assassins, wearing dark cloth masks and wielding dark steel curved blades, suddenly leap into the frame from the peripheral bamboo grove to surround him. The cultivator does not reach for his weapon; instead, he calmly raises his right hand, extending two fingers forward. [Shot 2] At 00:03.200, the camera cuts to a close-up and tilts up rapidly behind his right shoulder. Without any physical contact, the longsword bursts upward out of the scabbard on the cultivator's back, emitting a piercing, cold white glow. The radiant blade streaks straight up into the night sky, trailing a ribbon of luminescent energy. [Shot 3] At 00:05.800, the camera cuts to a wide framing and tracks the glowing sword's rapid movement across the clearing. The cultivator from Shot 1 sweeps his extended fingers sharply left and right. Guided by his gesture, the glowing sword violently darts among the leaping assassins, throwing off bright orange sparks as it knocks their dark blades away. The flying weapon swiftly slices horizontally through the thick green trunks of the surrounding bamboo trees, causing the severed upper halves to collapse and crash heavily onto the forest floor. [Shot 4] At 00:09.500, the camera cuts to a medium shot and arcs around the cultivator. Hovering steadily in the air at his eye level, the single glowing longsword instantly multiplies, splitting into nine translucent white sword shadows. These nine ethereal blades spin violently in a tight, protective halo around him, generating an immense kinetic gust that blows the surrounding assassins completely off their feet, sending them tumbling backward into the dirt. [Shot 5] At 00:12.600, the camera holds a static medium close-up on the cultivator's upper back. The nine sword shadows merge seamlessly back into one solid blade, which plunges straight down into the scabbard with a decisive physical lock. The cool blue moonlight illuminates dozens of severed green bamboo leaves as they drift slowly down through the frame, settling around his serene silhouette.
overall_soundscape: The soundscape opens with audible howling wind rustling through bamboo leaves, followed by the loud, rapid flapping of heavy fabric as the assassins leap. A sharp, resonant metallic slide is clearly heard as the sword shoots from its scabbard, transitioning immediately into a continuous, high-pitched magical hum. Loud, aggressive clangs of steel striking steel ring out in the foreground, interspersed with the distinct, violent cracking of snapping wood and the pronounced, heavy thuds of massive bamboo trunks crashing to the earth. A dominant, oscillating whoosh sweeps through the sound field as the swords spin rapidly, ending with multiple heavy thuds of bodies hitting the dirt, and a final, loud metallic clack as the blade locks back into its sheath.
non_diegetic_music: A fast-paced, dramatic orchestral score driven by heavy taiko drums and urgent staccato strings, featuring a soaring, aggressive solo erhu melody that builds in tempo and dynamic intensity before abruptly cutting to complete silence at the final sword lock.
```
