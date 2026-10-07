---
name: "h3-action-prompt-design"
description: "h3-shot-prompt 的补充手册：H3 提示词涉及挂素材六段式、空间方向与门、手和道具、粤语对白、本地帧长、latent 接力、车辆擦身，或出片后按病症查修法时查这里。写法本身以 h3-shot-prompt 为准。"
---

# H3 补充手册（实测规矩）

**先用 `h3-shot-prompt` 写。** 分镜、镜头头、运镜、动作、状态标签、台词预算、范例，都以它为准。这本手册只放它没写到、又在本地渲染里验证过的规矩，按主题查，用不到的章节不读。

两者冲突时听 `h3-shot-prompt`。下面这些旧规矩已经作废，不要再用：
- 不再要求 `detailed_description` 写满 350–500 词。那是官方指南的建议范围，但快剪范例 1、4 都更短，照样跑通；字数跟着镜头走，安静戏可以写满。绝不为凑字数加事件、道具或规则。
- `[Shot N · 1.5–2.8s]` 镜头头、`(flame: ON)` `(3 remaining)` 这类状态标签、大写运镜和动词、`IMPORTANT —` 段、对话戏里的 `hard cut to`，都可以写进提示词。
- 运镜不强制官方词表（`Push In with small amplitude at slow speed`）。它仍然可用，适合安静戏；快剪用大写运镜。
- 旧的整段模板（1v1、1vN、追逐、跑酷、写实）和 `ANCHORS LOCKED / RED LINES / END STATE` 那一套格式全部作废。

仍然不能进提示词的：内部编号（镜头 ID、P1、FAN_A、声线代号）、给人看的制作备注（"后期处理""为了接力"）、LoRA 触发词之外的工作流说明。

---

## 1. 挂素材：六段式怎么写

只在挂了图、视频或音频时用；不挂素材就用 `integrated_multimodal_description` 三段式。六段顺序固定：
`subject_definitions / summary / retention_analysis / detailed_description / overall_soundscape / non_diegetic_music`，每段标题单独一行，段间空一行。`detailed_description` 里的镜头照 `h3-shot-prompt` 写。

### subject_definitions

一行一个主体：它是谁（或是什么地方、什么道具）、来自哪张图、看得见的外形。
`<Subject 1> is Ajie, the young working-class man in a faded T-shirt and flip-flops, shown in {{ref:R02_...}}. The image sets his face, hairstyle, build and clothing; pose, expression, framing and background follow the description.`

- 同一个人、地方或道具的几张图合成**一个**主体：`shown in {{ref:A}} (lamp on) and {{ref:B}} (lamp off)`。一个人两个标签，就会多出一个人。
- **每张图只干一件事，写明它提供什么、不提供什么。** 角色卡：`The image supplies identity, hair, proportions and costume only; its backdrop, standing pose and portrait camera are not reproduced, and it is not a first frame.`
- **挂上的素材必须在文字里用到。** 接了线却没提的图照样进模型，模型自己决定拿它干什么。原生 ComfyUI 里标签顺序等于接线顺序（`<Picture 1>` 就是 `ref_image_0`）；参考节点没真正接上会悄悄退回文生视频，看日志确认参考数。
- **纯色底的角色卡会把背景带进片子**，场景变成影棚。要同时挂场景图做单独的主体，镜头里写：`Behind them is ONLY <Subject N>: [三个具体特征]. There is no grey wall, no studio backdrop and no plain seamless background anywhere in the frame.`
- **手、鞋、道具的插入特写不要挂角色卡。** 实测：挂了完整人物又只拍不露脸的局部，出了半透明的重影。
- **关键道具**指向图，不要描述造型；它出现的每个镜头都写 `matches <Subject N> exactly`，只留状态和位置词（完好、在玻璃柜里、同样大小）。道具走样时先删描述词；还走样，再加一两个和图一致的材质词，或者做一张道具摆在场景里的参考图。
- **临时状态不是改设计**："车灯亮着、手刹拉起"写成那辆车的状态。
- **参考图的状态要和剧情此刻一致**（灯开关、门还是墙、白天黑夜、天气、损坏）。唯一可用的图对不上时，在主体行加一句"In this shot its lamp is off"，并告诉用户。
- 画面文字用英文双引号逐字写出（`a plate reading "6"`），没写出来的字会变成乱码。
- 首帧、尾帧、关键帧这类具体画面单独一行：`{{ref:X}} is the first frame of [Shot 1], showing ...`，任务类型用 `keyframe completion`。
- 脸来自一张图、身体和服装来自另一张时，在同一行写明，每个 ref 仍只出现一次。外形用摄影词，不用气质形容词（空灵、甜美）。

锁定程度写在主体行里：

| 锁定 | 主体行写 | retention 标记 |
|---|---|---|
| 全锁 | 脸、发型、身形、服装都来自图 | `fully_preserved` |
| 锁脸，服装按文字 | 脸和发型来自图，服装来自描述 | `partially_preserved` |
| 服装有自己的图 | 脸来自人物卡；服装逐项对照它自己的图（剪裁、颜色、长度、鞋袜、印字） | 服装 `fully_preserved` |

### summary 和 retention_analysis

- summary：`[reference generation] The target video shows <Subject 1> ...`，一小段说**画面上发生什么**。不写片段编号、剪辑说明，只用已定义的标签。任务类型可用 ` + ` 组合：`reference generation`、`keyframe completion`、`video editing`、`video continuation`、`audio reuse`、`audio reference`。导播台的 latent 接力**不是** `video continuation`，那个只用于输入里本身有参考视频的情况。
- retention：`<Subject N> (appears in [Shot 1], [Shot 2]): <标记> - <保留的具体特征>`。只对照这个主体行定义的角色判断：换姿势、换表情、有新动作不算丢失，角色脸发型身形服装都在就是 `fully_preserved`。
  - `partially_preserved`：换装、脸始终不露、场景图的灯/门/天色和此刻不同。
  - `attribute_transfer`：特征转到另一个可辨认的东西上（同款的另一只箱子）。
  - `weak_reference`：只借风格、构图、氛围；本段看不见的主体也勉强用它，但更好的做法是在这段禁用那个素材。
  - 音频只用 `fully_copy / partially_copy / reference / weak_reference`。
  - retention 里不写 `(S1)` 这类说话人编号。
- 只借音色的声线参考：`Use it only to guide vocal timbre and delivery; do not copy it into the final soundtrack.` 参考音频里原来的话不能出现在片子里。

### 导播台 JSON 里的素材

- `{{ref:别名}}` 原样保留，只出现在 `subject_definitions`，每个启用的素材出现一次，保持原顺序。不增删、不改名、不改路径；不动 id、seed、时长、接力开关、`disabledAssetIds`。
- 自己写素材条目时，字段要全：`id, alias, kind, path, enabled: true, fixed, fixedOrder, shotIds: [], includeVideoAudio, durationSeconds, audioDurationSeconds, fingerprint`。缺 `enabled` 会被当成禁用，报"未找到或已禁用素材"。别名不含空格和花括号，最好纯 ASCII。`path` 相对 ComfyUI 的 `input/`，本机 Windows 路径在云端 GPU 上读不到。
- `resume` 只在整个 Plan 的 hash 不变时跳过已完成的镜头，改任何一镜都会全部重跑。没改的镜头保持 seed 和分辨率，每次测试换新的 `runId`。

---

## 2. 本地帧长

本地工作流把秒换成帧：`max(5, round(秒 × 24))`，再向上取到 17k+5。实际片长比填的数长：

| 填 | 帧 | 实际 |
|---|---|---|
| 4 s | 107 | 4.46 s |
| 5 s | 124 | 5.17 s |
| 6 s | 158 | 6.58 s |
| 7 s | 175 | 7.29 s |
| 8 s | 192 | 8.00 s |
| 9 s | 226 | 9.42 s |
| 10 s | 243 | 10.13 s |
| 11 s | 277 | 11.54 s |
| 12 s | 294 | 12.25 s |
| 13 s | 328 | 13.67 s |
| 14 s | 345 | 14.38 s |
| 15 s | 362 | 15.08 s |

- 时间点、summary、对齐句都按实际长度写，最后一个镜头要把多出来的时间填满。只有 8 秒正好对上。
- 事件都挤在前半段时，尾巴会僵住（第三方测得尾段运动量掉到全片平均的 0.46，正常片是 0.55–0.94）。最后一秒没有新动作，但烟、光、衣摆、环境声还在动。
- 单次生成不超过 15 秒。

---

## 3. 空间、方向和站位

### 空间设定（只在规划里用，不进提示词）

一个地点被两段以上用到，就先定下来，之后每段都照它写：

| 项 | 例子 |
|---|---|
| 布局 | 床靠左墙、窗在床上方；传菜口在餐厅后方 |
| 层级和连接 | 店在街角对着大门；家在七楼 |
| 固定机位 | "卡座机位：厨房在右后，街门在左"；"楼梯口机位：上行楼梯在画左" |
| 轴线和行进方向 | 隔桌对话 A 永远在画左；回家永远往画右走 |
| 光源 | 早上窗光从画右来；每层楼梯口一盏黄灯 |
| 尺度 | 层高约 2.5 米，桌高约 75 厘米，巷宽约 3 米 |
| 固定道具 | 只有一张凳子，在门牌"7"下面 |
| 住处和路线 | 他家在左侧楼梯最上面；店离大门两个门面 |
| 状态变化 | 第 15 段起门变成墙；第 8 段后灯坏了 |

《纸引》大殿的固定位置已经写在 `h3-shot-prompt` 的项目卡里，以那里为准。

### 每一段都要做到

- **方向写出来，不靠暗示。** 上楼下楼、进门出门、朝镜头还是背离、走哪个出口，都要写；画左画右推不出上下和里外。上楼到平台，先露头和肩。一串灯按什么顺序亮也要写。
- **轴线**：一场对话里每个人待在 180 度线同一侧；同一条路线跨段保持同一个画面方向。反打会左右互换，要重写门、出口、楼梯在哪边。
- **视线高度**：站着的人看坐着的人是俯视，坐着的人抬脸；司机视角在座椅高度。
- **尺度写成实际距离**，模型爱把东西压扁：风扇在躺着的人上方整整一个身长、柜台齐腰、车隔两条车道。相隔远的两样东西要用够宽的景别；硬塞进一个特写，房间就被压缩了。
- **大全之后的近景，把背景重写一遍**：用全景里的具体东西（墙色、招牌或门牌号、窗、灯），留够头顶空间放关键标志，景深适中。只写 "shallow depth of field, soft bokeh" 会让模型自己编一个黑背景。
- **同类东西多个时说清是哪一个**："他自己那层楼梯口、头顶那盏灯"。
- **两人戏左右锁定**：第一个镜头定下，之后每个镜头用同一句重复（范例 2、5 的写法）。镜子和玻璃里的倒影除外，出现时说明。单人戏写明没有左右规则，免得套用系列模板。
- **挤的构图写死人数**：`Exactly 2 distinct people are represented in this crop. No extra body, duplicate face or mirror double enters.`
- **画框边缘用身体部位说**："画框下缘止于她胸口"。必须完整的道具：`the WHOLE television, with a margin around it`，屏幕内容写具体。
- **模型想填的空，用真东西填。** 空的前景总被编出家具或人时，把场景里真有的东西放到前景、隔着它拍。第三方实例：隔着茶几和果盘拍，床就不再凭空出现；"她必须躺在沙发上"这句话没用。
- **听的人半张脸表情不对**：从背后拍，只留后脑和一侧肩膀。
- **去掉难的物理**：车窗写成开着、没有玻璃，避开透明层里的反射。
- **狭小空间写清几何**："左舵车，司机在画左，镜头在副驾朝左前方，离她的脸 0.7–1.0 米，画右能看到空着的副驾"。

### 行为逻辑

每个角色每一段都要交代：从哪开始（位置、朝向、画面哪侧）→ 从哪来、往哪去（上下、里外、从画面哪侧进出）→ 每个动作的起因（看得见的声音、东西，或一句动机"想找人诉苦"）→ 谁在谁和谁之间（说挡路就站在路上，说挤过去就说从哪侧）→ 停在哪、什么状态。

- 画外角色给一个画面方向（"画外左侧有人在问"），同一组蒙太奇里方向不变，视线才对得上。
- 盯着看的镜头，写明在盯什么。认出某样东西，写明认出什么、从哪来，不点缺席角色的名字（"从八楼滚下来的垃圾"）。
- 没有起因的反应看起来是乱来的：补起因，或者删掉反应。

---

## 4. 门和其他会动的固定物

实测：只写 "the door opens"，门和铁闸就会自己开。在写实故事里这就成了闹鬼。

- 门、闸、窗、抽屉、盖子、帘子，只在看得见的人动它时才动。一两句写完：谁、哪只手（两手都占着就用肩、胯、脚）、碰哪里（把手、门闩、链、铁条、门边）、往哪开（向里、向外到楼梯口、往画左）、开多大（一掌宽、一半、整个靠到墙上）、门和手停在哪。
  例："His right hand slides the gate's bolt back and shoves the gate outward; it swings toward screen-left and stops against the landing wall."
- 不写不及物的门："the door opens""the door bangs open""as the door opens"。
- 从门后开，就露门边的一只手或一侧肩膀。
- 不能动的门在可能动的那一刻写状态："the door stays shut""the door itself does not move"。门后有声音、链子响、敲门、钥匙打不开时尤其要写。
- 开场就开着的门写清怎么开着："its gate stands propped fully open against the wall for the day"。
- 声音放在手动之后（门闩一响、锁舌一扣、铰链吱呀）。
- 在空间设定里定好每扇门往哪边开、铰链在哪侧、几层（里面木门外面铁闸：从里面先开木门，再拉闩开闸）。必须看得清的门牌挂在墙或门框上，不挂在会转走的门扇上。
- 同理：灯只在有触发时亮（脚步、咳嗽、开关、定时），道具只在手里动。纸扎"自己动"是《纸引》的有意设计，照项目卡写，先拍动静再露真身。

---

## 5. 手和道具

- **身体的左右不是画面的左右。** 面朝镜头的人，右手在画左；背对镜头，右手在画右。手碰画面某侧的东西（扶手、门、墙）时两个都写，并且对上："his right hand, on the left of frame, closes on the rail"。
- **道具账**：几个、谁的、哪只手、什么状态（拿着、放下、开、关、掉了）。拿着东西的手不是空手：要去抓扶手，先写放下或松开。
- 有风险的动作时重复道具和手："he steps back once; the same bag stays in his left hand."
- 一个镜头里只写一样要一路跟住的东西时，用 `h3-shot-prompt` 的括号标签；多样东西就逐镜重复。
- 持续状态（伤、湿、脏、灯、门、碎片）除非画面里有可见原因，否则不重置。之后还要行动的角色不能用终结动词（碎了、化了），杂兵除外。

---

## 6. 对白和粤语

台词预算、声线段、每镜一句、`Line lands about …` 的写法看 `h3-shot-prompt`。这里只补标注格式和粤语。

- 台词原样放进 `<d>[语言] ...</d>`，写真正的语言：粤语写 `[Cantonese]`，不用 `[Chinese]`。`<d>` 里只放语言标签和台词，完整句子带句末标点；被打断的保留省略号。
- 说话人编号每段从 S1 重新编，按开口顺序；画外的声音也给编号。同一人的第二句也要标。挂素材时写成 `<Subject 2> (S1), at screen-left, says flatly ..., <d>[Cantonese] 喂，借借。</d>`；不挂素材写 `The woman (S1) says:`。
- 画面里有两人以上时，写说话人在画面哪侧。听的人露脸时写明嘴闭着，反应放在眼睛、呼吸、喉咙、手上。多人段加一句 "Only the person speaking moves their lips."
- **一次生成尽量只有一个声源。** 第三方实例：一次生成里几个人说话会串台，模型还会补没写的回话。必须两人时，台词隔开，每次都写听的人闭嘴。单人说话时，台词后接：`Only this one vocal source is heard. <Subject 3>'s mouth stays closed. Do not repeat, paraphrase or continue beyond the listed spoken content.` 再写嘴在什么时候闭上（按台词结束或实际片长）。
- 说台词时避免快跑、捂脸、转开和大的运镜；说完写 `closes his mouth naturally`，再接下一个动作。
- 旁白用固定说法 `says in an off-screen voiceover`，`</d>` 后面紧跟一句画面里的人嘴闭着。
- 跨剪辑点的台词两头都用 `<scenetrans>`，并说明声音跨过剪辑点延续；被片尾截断的用 `<cutoff>`。
- 要强锁声线，可以给每个角色挂参考音频（`<Audio N>`，最多三个），绑到它的 S 编号。
- H3 自己出的环境底噪很少：在 `overall_soundscape` 写明每段沉默下面垫什么环境声；系列片后期每场铺一条环境声。
- **粤语**：
  - 用香港繁体和口语字（嘅 咗 喺 冇 啲 嚟 佢哋 唔該 鎖匙 黐線）。书面语或普通话说法会把发音拉向普通话。
  - 语气词用对（喎 反驳，㗎 断言，吖嘛 "本来就是"，啦 催促）。唔該 谢服务，多謝 谢礼物。数字写"三十"不写"卅"。
  - 粤语不在 H3 官方稳定支持的 11 种语言里（阿拉伯、中、英、法、德、意、日、韩、葡、俄、西）。整集开跑前，每个主要声线先跑一段试口型和发音。

---

## 7. latent 接力和跨段衔接

- 接力的几段，环境那一句一字不改地照抄。要换空间（更宽的路、新房间），在前一段就交代好；后一段写了不同的空间，会在交接处跳到新地点。
- 后一段从前一段的最后一帧开始，开场位置必须等于前一段的**实际**结束位置。接力开着却要求另一个起始位置，出过重复的人。多镜头快剪段：前一段最后一个镜头的构图和人的状态，就是后一段第一个镜头的起点。
- 接力关着时，新生成往往从静止开始，连续动作会像停了一下。连续动作用接力。
- 接力链上每一段都要挂身份参考图，否则身份会越漂越远。
- 用上一段尾帧当下一段首帧（I2VA/FL2VA）会累积漂移：第三方实例到第五段母亲已经不像了，烧进画面的字幕也被带下去。解决办法是每段独立挂 2–4 张参考。
- **不要从空画面开始一段**（人走出去了、门关上了），下一个进来的人会被编一张脸。
- 只约束首帧时，坐着的人会自己站起来；首尾都约束才坐得住。
- 真实尾帧会带上模糊、字幕、闭眼、出画；"稳定尾帧"（结尾附近最清楚的一帧）干净但不是精确结尾。每个项目选一种，并让最后一个动作落定，下一段开头才不会抖。
- 漂移明显时断链，用只靠参考图生成的一段重建锚点。不设固定的接力段数上限。

---

## 8. 两种特殊动作

**连续行走、长距离移动**
- 用侧跟拍，镜头跟着步速走，人保持在画面中间。固定机位加"走到画面左三分之一"这种目标，和真实步速冲突，模型会让她停下、走过头，或者多出一个她。
- 全段一个步速。不写会让人停下的词：stop、pause、wait、hesitate、slow、small steps、in place、stands。危险区域里"小步走"读起来像在等危险。
- 走路时手上的动作（重拨电话、看手机）写 "in stride"。
- `h3-shot-prompt` 范例 5 是"两人往反方向走"的跑通写法，优先照它。

**车辆和行人擦身、撞上**
- 车沿镜头轴线从纵深开向镜头，行人在车和镜头之间，写明车直冲着她。留了车道或偏移，模型就会让车拐开、擦过去。
- 用位置锚定相遇，不用秒数："When the truck reaches her, she is still in the middle of the road on the stripes, the far kerb several strides ahead." 路要够宽，并在接力的前一段就交代路宽。
- 车还在全速、车头占满画面时切黑。要求看到碰撞，模型会让车在人前面刹住。
- 车写成没有品牌的普通车，光滑无标的车头和空白车牌，避免出现像品牌的标志和乱码车牌。

---

## 9. 本地生成：否定、negativePrompt、LoRA

- **本地没有改写器。** 官方 App/API 会先用 H3-Context-IR 把输入整理成结构化格式，所以那里写自然语言、`[0s-2s]` 时间码、"no push in, no cuts" 这类短否定都行。本地 ComfyUI 模型读到的就是你写的字。
- **本地正向里写"没有 X"也算提到 X。** 第三方实例："no subtitles"反而招来了字幕。改成写结束状态、写出所有该有的东西；全项目只留一句文字防护：`The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.`，以及紧跟在 "ONLY <场景>" 后面的那句背景排除。
  - `h3-shot-prompt` 的 `FORBIDDEN:` 用于出片后针对一个具体毛病的修补（和一条正向的 `IMPORTANT` 配对），效果以实测为准；不要一开始就堆 FORBIDDEN 清单。
- 不在正向里点缺席的角色或东西（这镜没有阿婆就别写"no granny"），写 "nobody else is in frame"。
- **negativePrompt**：H3 权重是 CFG 蒸馏的，没有原生负向输入，只有工作流加了 NAG 这类节点才起作用。V7.3 导播台（`BasicGuider`）没接，就留空，防护全写成正向句。接了的话写短而具体的几项。
- **LoRA 触发词和效果 embedding** 放在描述正文里（`detailed_description` 或 `integrated_multimodal_description`），不放在最后一段后面，否则会被当成配乐说明。触发词原样写，不让模型改写。
  - 武术 LoRA（Jojocodex wushu）：触发词 `wushu_action`，强度 0.5，写成 `wushu_action, [谁] + [具体招式和力] + [场景/镜头]`。
  - 写实 LoRA（fal）：`r34l1sm` 放最前面，强度 1.0，想轻一点 0.6–0.8。
  - MiniMax 自带 10 个效果 embedding（`minimaxh3_art_is_explosion` `_blooming_flowers` `_bullet_time` `_dark_magic` `_fire_breath` `_four_seasons` `_kiss_camera` `_spiral_ascent` `_storm_magic` `_truman_show`）。放进 `ComfyUI/models/embeddings/`，写成 ` embedding:minimaxh3_bullet_time`：小写、前面有空格、名字后没有句号，否则会被悄悄丢掉。只有全开或不开，改措辞调不了强度。
- **加速 LoRA**：larryvrh v4 强度 1.0，6–8 步，simple 调度器；4 步糊快动作，超过 8 步过锐。加速 LoRA 在 1344×768 训练，直接出 1920×1088 会偏软，1080p 用后期放大。
- 打戏 LoRA、文戏高配流程、多跑几个种子：见 `h3-shot-prompt`"提示词以外"一节。
- 每次改配置后看日志：有些设置会悄悄关掉缓存或换成别的注意力后端。

---

## 10. 纸扎和定格质感

《纸引》的画风底座、角色插句、纸扎规则都在 `h3-shot-prompt` 的项目卡里，照抄那里的。这里只补官方纸艺 skill 的几条，挑用得上的：
- 分层：前景遮挡物（纸叶、门框、帘子）、中景是主要动作、背景有视差和小纸机关在动，不是一张静止的平面。
- 材质写成正向状态：`matte cardstock with visible fibres and cut edges, soft contact shadows between layers`，本地不要列一串禁止的画风。
- 动作：小步、短停、轻微回弹、铰链关节、纸张落定。镜头像拍微缩舞台：慢推、横移出视差、定住的中景、微距；避开快速穿越、360 环绕、液态变形（一打多的终结段按 `h3-shot-prompt` 骨架例外）。
- 声音只放在看得见的动作上：翻纸、剪纸、卡片滑动、木头轻响、关节咔哒。

---

## 11. 出片后按病症查

先按 `h3-shot-prompt` 的规矩改：一次只针对一个问题加一条 `IMPORTANT`（需要时配一句 `FORBIDDEN`），其他文字一字不动，另存新版本。改法查这张表：

| 病症 | 改法 |
|---|---|
| 门、闸、抽屉自己动 | 写出人、手、接触点、方向、幅度、结束位置（第 4 节） |
| 背景变成灰色影棚 | 挂场景图做主体；"Behind them is ONLY <场景>: …"（第 1 节） |
| 空前景里凭空冒出家具或人 | 把场景里真有的东西放到前景隔着拍；加字没用 |
| 近景背景变成黑的、陌生的 | 用全景的具体特征重写背景，景深适中（第 3 节） |
| 不露脸的局部特写出了半透明重影 | 这镜不挂角色卡 |
| 道具越画越走样 | 删描述词，写 `matches <Subject N> exactly`（第 1 节） |
| 听的人半张脸表情不对 | 从背后拍 |
| 说话人朝错方向 | 写画面左右加视线目标；"never addresses the camera" |
| 串台、多出没写的回话 | 一个声源；"Only this one vocal source is heard…"（第 6 节） |
| 走路的人停下、走过头、变成两个 | 侧跟拍，删掉停顿类的词（第 8 节） |
| 车拐开或在人前刹住 | 车沿镜头轴线，位置锚定，全速切黑（第 8 节） |
| 接力段开头多出一个人、跳到别处 | 起始位置等于上一段实际结尾；环境句照抄（第 7 节） |
| 身份沿接力链漂移 | 每段挂参考；断链重建锚点 |
| 尾巴僵住 | 事件往后排，最后一秒留余动和环境声（第 2 节） |
| 写了"没有字幕"却出了字幕 | 删掉否定句，只留那一句统一的文字防护（第 9 节） |
| 受惊反应变成慢动作 | 写"瞬间、全身一颤、绝对不慢" |
| 多一只手、手指弯错 | 随机问题，换种子重跑一次 |

渲染没看过之前，不说画面、口型或连戏"没问题"。