# 示例

三类示例，用途不同：
1. **官方改写原样示例**：H3-Base 训练时见过的就是这种文体。拿不准怎么写时，先读这一节，照它的语气和句式写；字数、声音段长度和配乐按 SKILL.md 的预算和默认来。官方示例里这些不照学：配乐情绪词（`mournful`、`heartwarming`、`joyful`）和配乐渐强、1.2 那种约 530 词的单镜头长段、1.3 只有一句的声音段。
2. **你本地跑通的范例**：内容和结构验证过。它们是旧文体（带 `IMPORTANT`、括号标签、按秒列声音），照抄内容思路，不照抄这些写法。
3. **本地验证过的新文体范例**：快剪动作（《纸引》）和多节拍文戏（《临期》）各一段，和旧版同种子对比、本地出片验证过，内容和写法都可以学。

---

## 1. 官方改写原样示例

来源：`github.com/MiniMax-AI/MiniMax-H3` 的 README 复现脚本和官方 skill。这些是 Context-IR 改写后、直接送进 H3-Base 的文本。

注意它们的共同点：
- 全是连续的描述性英文，没有一句规则或强调；
- 按时间顺序写，用 `Early in the clip`、`As the clip progresses`、`Throughout the remainder of the clip`、`Suddenly`、`As … fades` 交代先后；
- 物理过程写全：`The sheer spatial force violently jolts the bridge, causing the captain to stagger slightly forward, her shoulders tensing as she braces herself`；
- 后面的镜头复指前面的人：`the captain from Shot 1`、`the young man in the dark-grey hoodie from Shot 1`；
- 台词前写声线，台词后写收口：闭嘴并进下一个动作（`He closes his mouth into an apologetic smile and strokes the dog's thick white fur.`），或紧接一个动作（官方指南 I2VA 示例 `… says: <d>[English] I get off at the next station.</d> She folds the letter along its existing crease.`；`official-calibration.md` 的 office_two_speakers `Immediately after speaking, he pivots smoothly on his heel …`）；
- 一段 1–3 个镜头（1.1、1.3 和 1.4 的 T2VA 是多镜头；1.2 和 1.4 的 FL2VA、L2VA 是单镜头）。
- 台词标签后有一个空格：`<d>[English] I get off at the next station.</d>`。

用官方接口改写的本项目 8 条测试需求在 `official-calibration.md`，和本节一起作参照。

### 1.1 T2VA，10 秒，2 个镜头（无台词，物理冲击）

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot, pushing in slowly. In the cavernous, dimly lit bridge of a starship, sleek metallic consoles with glowing amber displays flank a massive, curved observation window. A female captain, in her late 40s with an athletic build and short silver-streaked black hair, stands in the center midground. She wears a structured, high-collared dark navy military tunic with silver chest insignias. Her back is to the camera, silhouetted against the cool, ambient starlight pouring through the thick glass. She stands perfectly still with her hands clasped tightly behind her back. Outside the window, a massive armada of jagged, dark grey dreadnoughts hovers in tight formation against a deep purple space nebula. The fleet's massive rear thrusters begin to glow with an intense, escalating bright blue light. [Shot 2] At 00:04.500, the camera cuts to a close-up of the captain's face and shakes strongly. The brilliant blue-white light from the fleet's gathering energy reflects vividly in her dark eyes. Suddenly, a blinding white flash floods through the window, completely washing out the background as the fleet jumps to hyperspace. The sheer spatial force violently jolts the bridge, causing the captain from Shot 1 to stagger slightly forward, her shoulders tensing as she visibly braces herself against the physical tremors. As the intense white light fades abruptly, leaving only the dim, empty expanse of the purple nebula reflected on her starkly lit skin, her jaw clenches, and she slowly closes her eyes in the newly emptied space.

overall_soundscape: A low, resonant hum of the ship's ambient life support systems serves as the baseline, soon drowned out by an audible, escalating, high-pitched electronic whine as the fleet outside charges its hyperdrives. A massive, deafening, bass-heavy boom and sharp crackle erupts during the blinding flash, accompanied by the loud metallic creaking, rattling, and deep thuds of the bridge's bulkheads vibrating under immense physical stress. The intense roaring impact then cuts abruptly back to a hollow, echoing room tone, leaving only the faint, steady hum of the isolated bridge.

non_diegetic_music: Cinematic space-opera orchestral score, slow tempo, featuring a solitary, mournful French horn melody over deep, sustained string dissonances that build rapidly in volume and intensity, swelling to a massive orchestral peak before snapping immediately into silence right after the jump.
```

### 1.2 I2VA，8 秒，单镜头（静止机位 + 焦点转移 + 多人小动作）

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] This is a live-action, cinematic shot with a shallow depth of field. The camera holds a perfectly static shot throughout the entire eight-second duration, capturing a cozy family gathering in a traditional Japanese dining room. The scene opens with a large, intricately patterned blue and white ceramic bowl of ramen in the immediate foreground, rendered in crisp, sharp focus. The bowl sits on a smooth, polished long wooden table. Inside the bowl, a rich, oily golden-brown broth surrounds yellow wavy noodles, topped with two thick, round slices of chashu pork featuring visible fat marbling and a distinct spiral meat pattern. A generous mound of freshly chopped, bright green scallions rests in the center, and a crisp, dark green rectangular sheet of nori seaweed is tucked into the right edge. To the left of the bowl, a pair of light brown wooden chopsticks rests horizontally on a small, dark rectangular chopstick rest, near a small cylindrical ceramic teacup with blue painted patterns. On the right side of the table, a spherical paper lantern with a ribbed bamboo frame sits on a black wooden base. In the background, a large family of seven is gathered around the table, initially appearing as a soft, blurred presence. Behind them, traditional Japanese sliding shoji screens with wooden lattice frames are open, revealing a bright outdoor scene with lush green trees. Early in the clip, the thick, white steam rising from the hot ramen broth immediately intensifies, billowing upwards in thick, swirling clouds that dance continuously above the bowl. As the clip progresses into the middle seconds, the camera maintains its static position while the focus begins a deliberate, smooth shift deeper into the room. The foreground ramen bowl, its vibrant ingredients, and the rising steam gradually soften into a hazy, out-of-focus blur. Simultaneously, the family members in the background come into sharp, detailed clarity. The heavy steam continues to rise from the foreground, creating a dynamic, translucent veil between the camera and the family. With the focus now firmly locked on the background, the vibrant family dinner comes alive. The man in the dark navy blue long-sleeved shirt on the left leans forward, his mouth moving animatedly in a silent exchange. The young girl in the crisp white short-sleeved t-shirt beside him smiles brightly, looking toward the center of the table. The woman on the far left, wearing a soft light blue long-sleeved blouse, turns her head slightly, smiling gently. Across the table, the woman in the light grey button-down shirt smiles broadly, her eyes crinkling, as she rests her hands near her plate. The woman in the dark grey top further back uses her wooden chopsticks to pick up a small piece of food from a central ceramic dish filled with bright red pickled vegetables. The woman in the center back in the light grey sweater smiles gently, her hands clasped softly in front of her, observing the interaction. Throughout the remainder of the clip, the family continues their lively physical interaction, their mouths moving in continuous, silent cadences of conversation, while the thick, white steam from the blurred ramen bowl in the foreground never stops rising, adding a comforting atmosphere to the warm gathering.

overall_soundscape: The soundscape begins with a quiet room tone mixed with the faint, airy rustle of the thick steam billowing from the hot ramen bowl in the foreground, accompanied by the subtle, continuous hissing and bubbling of the rich broth. As the visual focus shifts deeper into the room, the physical sounds of the bustling family dinner become dominant in the foreground. The clear, sharp clinking of ceramic bowls and wooden chopsticks touching plates is clearly heard as the family members reach for food. This is followed by the faint, muffled thud of a cup being set down on the smooth wooden table, and the subtle, rhythmic rustle of cotton and wool clothing as the family members lean forward and gesture, perfectly capturing the lively, physical atmosphere of the shared meal.

non_diegetic_music: A gentle, heartwarming acoustic guitar melody plays softly in the background, accompanied by the subtle, resonant notes of a traditional Japanese koto. The music maintains a slow, comforting tempo that enhances the cozy, nostalgic, and joyful atmosphere of the family gathering.
```

### 1.3 Ref2VA，3 个镜头，两人对话（官方 skill 的完整示例）

```text
subject_definitions:
<Subject 1> is the coffee-shop environment in <Picture 1>, featuring an exposed brick wall, an orange tufted sofa with patterned pillows, a neon sign, and a wooden coffee table.
<Subject 2> is the fluffy white Samoyed in <Picture 2>, <Picture 3>, and <Picture 4>, with thick white fur, pointed ears, a dark nose, and a curved tail.
<Subject 3> is the young blonde woman in <Video 1>, with long blonde hair and a light-pink button-down shirt with rolled-up sleeves.
<Subject 4> is the young man in <Video 2>, with short wavy brown hair and a dark-grey hoodie with drawstrings.
<Audio 1> is the voice-timbre reference for <Subject 3> (S1), containing a spoken English vocal layer.

summary:
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. <Subject 4> enters with <Subject 2>, which lunges toward the cookie. The three-shot exchange uses <Audio 1> as the voice-timbre reference for <Subject 3> and ends with a canned audience laugh.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table are retained.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the Samoyed's thick white fur, pointed ears, dark nose, and curved tail are retained.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the blonde woman's identity, long hair, and light-pink shirt are retained.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the young man's short wavy brown hair and dark-grey hoodie are retained.
<Audio 1>: reference - its vocal timbre guides the dialogue delivery of <Subject 3> without copying the original signal.

detailed_description:
The target video uses a realistic multi-camera sitcom style with warm indoor lighting.
[Shot 1] A medium shot establishes <Subject 1>, the coffee shop with its exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table. <Subject 3> (S1), the young woman with long blonde hair and a light-pink button-down shirt with rolled-up sleeves, sits on the sofa holding a chocolate-chip cookie. From the left, <Subject 4>, the young man with short wavy brown hair and a dark-grey hoodie with drawstrings, enters holding the leash of <Subject 2>, the thick-furred white Samoyed with pointed ears, a dark nose, and a curved tail. The dog lunges toward the cookie and pulls the leash taut. <Subject 3> (S1) jerks her hand back and, using the clear youthful voice timbre referenced from <Audio 1>, exclaims with light annoyance, <d>[English] Hey! Watch your dog!</d> She closes her lips and guards the cookie while <Subject 4> pulls the dog back.
[Shot 2] At 00:03.000, the shot cuts to a close-up of <Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1, sitting beside <Subject 3> on the sofa and holding <Subject 2> securely in his arms. <Subject 4> (S2) says in a casual young male voice with a playful tone and an easy conversational pace, <d>[English] He just likes cookies more than me.</d> He closes his mouth into an apologetic smile and strokes the dog's thick white fur.
[Shot 3] At 00:05.000, the shot cuts to a close-up of <Subject 3> (S1), the blonde woman in the light-pink shirt from Shot 1. Her annoyance softens as she looks toward the Samoyed. <Subject 3> (S1) replies in the same clear youthful voice referenced from <Audio 1> with an amused cadence, <d>[English] Well, he has good taste at least.</d> She smiles and raises the cookie in a small toast-like gesture. A classic canned audience laugh begins immediately after the line and continues through the final frame.

overall_soundscape:
Soft indoor coffee-shop room tone continues throughout the scene.

non_diegetic_music:
N/A
```

### 1.4 官方指南里的短示例

T2VA：
```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters of a small street bakery before sunrise. The camera pushes in with small amplitude at slow speed as the middle-aged baker with a calm, slightly raspy voice (S1) places a fresh loaf on the wooden counter and says: <d>[English] First batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a close-up of steam rising from the sliced bread while the baker's final words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as trays clink softly inside the bakery. The doorbell rings once, followed by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo, joined by sparse upright-bass notes and a gentle fade at the end.
```

FL2VA，8 秒单镜头：
```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a rain-soaked cyclist begins in the position and framing established by Picture 1, holding a closed black umbrella beside a silver bicycle. The camera pulls out with small amplitude at slow speed as she releases the bicycle handle, raises the umbrella above her shoulder, and presses the runner upward until the canopy opens. Water rolls from the expanding fabric while she steps beneath it, rotates the handle into the final angle, and settles into the pose, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: Rain falls steadily on the pavement, followed by the metallic click of the umbrella runner and the soft snap of the canopy opening. Water drips from the bicycle frame as distant traffic passes.

non_diegetic_music: N/A
```

L2VA，单镜头：
```text
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a close shot begins with an intact drinking glass near the edge of a dark wooden table, while the same hand and sleeve visible in <Picture 1> approach from the right. The camera pushes in with small amplitude at slow speed as the fingertips strike the rim. The glass tips, falls, and hits the floor with a sharp impact; cracks spread through it as fragments slide outward. Toward the end, the moving pieces lose momentum and settle into the exact broken arrangement, hand position, camera angle, lighting, and final composition established by <Picture 1>.

overall_soundscape: Fingertips tap the glass before it scrapes across the tabletop, falls, and breaks with a sharp crash. Small fragments scatter and gradually stop sliding across the floor.

non_diegetic_music: A low electronic pulse at a slow tempo, ending immediately after the glass breaks.
```

---

## 2. 你本地跑通的范例（旧文体，学内容不学写法）

### 2.1 对话 + 走位，15 秒，5 个镜头（本地跑通）

用户要求"情侣吵架后各自往反方向走，男生全程在画面里，最后镜头弧形推到他右肩后，远处她越走越小、始终没回头"。不挂素材。学它的：台词只有 20 字（走路多）；第 3 镜的过肩构图和结尾同一个构图前后呼应；弧形绕拍时人站着不动；脚步声一起一停。新文体下，它的三条 `IMPORTANT` 应改写成各镜头里的陈述句。

```text
integrated_multimodal_description: [Shot 1] A live-action urban relationship drama, photoreal, 16:9, at night on a long, straight, empty tree-lined sidewalk in a quiet city. Mature plane trees line the street; tall sodium-vapor streetlamps stand evenly spaced along the sidewalk, each throwing a warm amber pool of light on the paving, with cool blue-cyan shadow between the pools; a few parked cars along the curb, low buildings with dark windows. 50mm lens, shallow depth of field, fine film grain, real skin texture with visible pores, no retouching. Handheld camera with a gentle breathing sway during the argument; smooth and slow in the last shot. Only these two people; no one else on the street.

Characters, fixed for the whole video:
The woman (S1): young woman, shoulder-length straight black hair, oatmeal-beige long wool coat over a cream turtleneck, black straight trousers, white sneakers, a small black leather shoulder bag on her left shoulder. Voice: a soft, low-mid young woman's voice, slightly husky, even and quiet; when hurt she gets quieter, not louder. No shouting, no crying out, no shrill or cutesy tone.
The man (S2): young man, short neat black hair, black bomber jacket over a grey hoodie, dark jeans, white sneakers, both hands empty. Voice: a young man's mid-low voice, tired and clipped, a little impatient, never shouting.
Staging: in every side view she is on frame LEFT and he is on frame RIGHT; never swap sides.

IMPORTANT — the man is in EVERY frame of the video. Every shot includes him, either his full figure or his shoulder and the back of his head in the foreground. There is no shot without him.
IMPORTANT — cause and effect, in this exact order: she accuses him → he makes an excuse and looks away → she says one quiet final line → SHE turns and walks away first, toward frame LEFT → he stands still for one beat, then walks three steps the opposite way, toward frame RIGHT → he stops and turns back to look at her → he stands still while she keeps walking away and never looks back.
IMPORTANT — once she starts walking she NEVER turns her head, never looks back, never slows down, never stops. Her eyes are wet but no tears fall. They never touch at any point.

[Shot 1] At 00:00.000, medium two-shot from the side under one streetlamp. She (frame LEFT) and he (frame RIGHT) stand facing each other about one step apart, in profile. Her right hand grips the strap of her shoulder bag. She looks straight at him, eyes glistening, voice low and steady. The woman (S1) says: <d>[Chinese]你每次都说下次。</d> Line lands about 0.50–1.60s. He exhales through his nose and looks away down the street. Gentle handheld sway, until about 2.40s.

[Shot 2] At 00:02.400, hard cut to an over-the-shoulder close shot of the man: her shoulder and black hair are a soft blur in the left foreground. He rubs the back of his neck with his right hand, not meeting her eyes, tired and impatient. The man (S2) says: <d>[Chinese]我今天真的很累。</d> Line lands about 2.80–3.90s. He drops his hand and keeps looking away, until about 4.60s.

[Shot 3] At 00:04.600, hard cut to the reverse: a close shot of her face over his shoulder — the back of his head and his shoulder in the black bomber jacket are a soft blur in the right foreground. Eyes wet, no tears fall; her voice goes quieter, not louder. The woman (S1) says: <d>[Chinese]那你回去休息吧。</d> Line lands about 5.00–6.20s. She holds his eyes for one beat, then lowers her gaze and turns her body away toward frame left, until about 7.40s.

[Shot 4] At 00:07.400, hard cut to a WIDE, LOCKED-OFF side view of the whole sidewalk, the streetlamps receding in a line. She WALKS AWAY toward frame LEFT at a steady, unhurried pace, back straight, not looking back. He stays still under the streetlamp for one beat, jaw tight, then turns and walks three steps toward frame RIGHT, STOPS, and turns his head and shoulders back to look down the sidewalk after her. The gap between them is now wide, until about 10.20s.

[Shot 5] At 00:10.200, hard cut to a medium close shot of the man from the front-right, three-quarter view of his face: he stands completely still, looking back down the sidewalk toward her, jaw tight, eyes fixed, lips pressed shut. Then the camera makes one slow, smooth ARC around his RIGHT side while gently PUSHING IN, keeping him in frame the whole time — from his three-quarter face, past his right profile, to directly behind his right shoulder. As the camera comes around, the long lamp-lit sidewalk opens up beyond him and her small figure appears far down it. By about 13.00s the camera settles close behind his right shoulder: the back of his head (short black hair) and his right shoulder in the black bomber jacket fill the right third of the frame in soft focus; beyond him, in focus, she keeps walking away, her back to the camera, the beige coat passing through one amber pool of light after another, getting smaller. She never turns, never looks back, never slows. He does not move, does not call out; only his hair and jacket stir slightly in the wind; his face, hair and clothes stay exactly the same as the camera circles him. The camera holds with a faint breathing sway until 15.08s; last frame: his blurred back of head in the foreground, her small figure still walking away in the distance.

overall_soundscape: (0.00s) Quiet late-night street: low hum of the sodium lamps, distant city traffic, a light wind in the plane-tree leaves. (0.50s) Her low, steady line. (1.80s) His short exhale through the nose. (2.80s) His tired, clipped reply; faint rustle of his jacket collar as he rubs his neck. (5.00s) Her quiet final line. (7.60s) Her footsteps begin — even, unhurried, receding. (8.40s) His three footsteps the other way. (9.60s) His footsteps stop; only her footsteps remain, getting fainter with distance. (12.00s) A car passes far away on another street; wind in the leaves. (15.08s) Her footsteps almost gone. No other voices.

non_diegetic_music: N/A
```

### 2.2 拆说话人防串词 + 电影感底座（《阎王打工记》EP02，10 秒，本地跑通、不串词）

前一段只有钱总说"他走了，三百多单活谁干？"，这一段接力接上，只有阎王说话，之后用灯、茶汽、念珠这些真实物件表现法力。学它的：单声源、焦段写进镜头、法力只拍物理后果、最后一个镜头落在对手的反应上。

```text
detailed_description:
Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores. Location light: a warm amber pool from the pendant lamp over the tea table, cold blue dusk from the window behind; faces half warm, half cool; deep walnut and charcoal tones.

The location is <Subject 1>. Behind the people is ONLY <Subject 1>: the long dark walnut tea table in the centre, a floor-to-ceiling window behind it with the dusk-blue city, a small bonsai pine on the left, a plain ink-wash scroll on the right, warm pendant light. There is no grey wall, no studio backdrop and no plain seamless background anywhere in the frame.

Yama, disguised as the new employee Yan Wang, is <Subject 2>, a small antique bronze-cased earbud in his LEFT ear. Voice: a deep, resonant male voice with an imperial cadence; when thrown off it cracks into strangled disbelief; anger stays deep, never shrill. No narrator tone. Here he speaks at a normal conversational volume, plainly and briskly. His voice moves with the scene: quiet and certain when he pitches, a flat, deflated drop when he is stuck, low and hard when he lays down his terms. Yama is restrained and intense: still body, few gestures, a heavy, steady gaze on the person he speaks to; what he feels shows in small things — a brow tightening, a jaw muscle, a slow breath.
Mr. Qian, the company boss, is <Subject 3>. His black ebony prayer beads match <Subject 7> exactly. Mr. Qian is calm and unhurried; the faintest polite smile that never reaches his eyes.
Xiao Zhang is <Subject 4>: heavy dark circles under puffy eyes, greyish sallow skin, messy hair, black-rimmed glasses, a wrinkled plaid shirt; haggard, exhausted and unsmiling. Xiao Zhang is haggard and unsmiling, but alive: tiny involuntary reactions show on him — his typing fingers pause for half a beat, he swallows, blinks slowly, his jaw tightens — and he never turns to look at Yama.
Staging, fixed for this scene and matching <Subject 5>: Yama stands in front of the tea table on frame LEFT; Mr. Qian sits behind the tea table on frame RIGHT; Xiao Zhang stands at the far RIGHT end of the table; the company seal and the red seal paste sit at the table's right front corner. Never swap sides.
All eyelines stay inside the scene: at each other, at screens, at props or down; the eyes stay off the lens.
Only this one vocal source is heard: Yama. <Subject 3> and <Subject 4> keep their mouths closed. Do not repeat, paraphrase or continue beyond the listed spoken content.
Tone: quiet power. Every sign of Yama's power is a real, physical change in the room, small and grounded, shown through objects and people's reactions.
The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.

Light: warm amber pool from the pendant lamp over the tea table, cold blue dusk from the window behind Mr. Qian; faces half warm, half cool; a thin curl of tea steam catching the light.
IMPORTANT — only Yama speaks in this video. Mr. Qian and Zhang keep their mouths closed the whole time. The room answers him with small, real, physical changes; nothing glows.

[Shot 1 · 0.00–1.20s] LOW-ANGLE MEDIUM, continuing exactly from the last frame: Yama on frame LEFT draws the vermilion brush, matching <Subject 6> exactly, from his jacket and SLAPS it flat on the tea table.

[Shot 2] At 00:01.200, hard cut to an 85mm CLOSE-UP of Yama, steady, his eyes on Mr. Qian. Yama (S1) says, low and level: <d>[Chinese]他的活本王干，一分钱不要。</d> Line lands about 1.50–3.71s.

[Shot 3 · 4.20–7.60s] Three quick inserts: the pendant lamp dims for a beat and comes back; the steam over Mr. Qian's teacup stops rising; the string of black prayer beads, matching <Subject 7> exactly, slips loose and the beads roll and click across the walnut.

[Shot 4 · 7.60–10.13s] CLOSE-UP of Mr. Qian looking down at the scattered beads; for the first time his calm holds perfectly still.

overall_soundscape:
(0.1s) A sharp CRACK of wood on wood. (1.5s) Yama, low. (4.2s) A low electrical hum drop; steam cut off; beads clicking and rolling across wood. (7.6s) Dead silence.
```

### 2.3 活人感 + 画外音 + 画面文字（《临期》段 04，15 秒，6 个镜头，用户反馈跑得不错）

学它的：隐藏目的（想道谢但不想尴尬 → 说成半句玩笑、眼睛看筷子）；画外台词配听者 `lips remain completely closed`；反应写成"慢半拍、手停一下、嘴角动一点、不回头"。第 3.2 节是同一段的新文体版，两轮出片验证过。

```text
integrated_multimodal_description: [Shot 1] Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores. Location light: flat cold-white fluorescent tubes inside the store, a warm amber glow from the hot-food cabinet, blue night light through the wet glass front as the rain thins; faces half cold white, half warm. Total runtime is exactly 15.08 seconds.
This continues directly from the previous segment. The same small unbranded 24-hour convenience store at 2 a.m. No logos or brand names anywhere.
Lao Xu: a delivery rider about 45, rain-flattened short hair, grey stubble, a sun-darkened tired face, a wet yellow rain jacket over a grey hoodie, a scuffed yellow helmet. Voice: a middle-aged man's low, rough voice, plain Mandarin, short and gruff; here it carries a dry half-joke, warm underneath.
Xiao Su: the night-shift clerk, a young woman about 22, dark hair in a low ponytail, a plain dark-green store vest over a white long-sleeve tee; she never speaks here.
Staging, fixed: the checkout counter is on frame RIGHT with Xiao Su behind it; the window counter and the door are on frame LEFT. Never swap sides.
Acting direction for the whole sequence: nobody stands idle or poses for the camera. Every character is always occupied with some small piece of business — handling an object, finishing a movement, glancing at something off-topic. In every exchange one character acts while the other reacts, and reactions arrive a beat late, the way real people respond while their attention is still somewhere else. Small involuntary gestures (swallowing, shifting weight, thumb rubbing an edge, a delayed look-up) matter more than polished facial expressions.
Hidden purposes: Lao Xu wants to thank her without making it awkward for either of them, so he turns it into a dry half-joke and keeps his eyes on his chopsticks. Xiao Su is pleased, but does not want to make anything of it, so she keeps working and does not turn around.
IMPORTANT — only Lao Xu speaks in this video, one line, heard while the camera is on Xiao Su. Xiao Su's lips stay completely closed the whole time.
The first image is a 50mm MEDIUM of Lao Xu at the window counter on frame LEFT: he snaps the disposable chopsticks apart and rubs them together to clear the splinters, his eyes on the chopsticks. (boxed meal: OPEN)

[Shot 2] At 00:02.200, the camera cuts to a 50mm MEDIUM of Xiao Su behind the counter on frame RIGHT, her back half-turned, stacking cartons. Lao Xu (S1) says in an off-screen voiceover: <d>[Chinese]那我帮你扔。</d> Line lands about 2.60–3.80s, while Xiao Su's lips remain completely closed. A beat after the line her hands pause; one corner of her mouth lifts a fraction; she does not turn around, and goes back to the cartons.

[Shot 3] At 00:05.000, the camera cuts to an 85mm CLOSE-UP of Lao Xu eating his first mouthful fast, steam rising from the box, his eyes on the food.

[Shot 4] At 00:07.600, the camera cuts to a 35mm WIDE through the glass front from inside: outside, the rain thins to a drizzle and stops; drops still run down the glass. In the foreground on frame LEFT, Lao Xu stands, closes the empty box and pulls on his yellow helmet. (helmet: ON HEAD)

[Shot 5] At 00:10.000, the camera cuts to a 50mm MEDIUM at the door on frame LEFT: Lao Xu pushes the door half open, stops, and without looking back taps the glass twice with one knuckle toward the counter.

[Shot 6] At 00:11.600, the camera cuts to an 85mm CLOSE-UP of Xiao Su behind the counter on frame RIGHT: a beat late, without looking up from the cartons, she nods once. The camera holds a static shot with a faint handheld breath. No new action in the last second; only the door chime still fading and the drops on the glass. Last frame at 15.08s: Xiao Su alone behind the counter, the empty window counter soft behind her on the left. (Lao Xu: GONE)

overall_soundscape: (0.0s) Wooden chopsticks snapping apart and rubbed together; rain on the glass. (2.6s) Lao Xu's line. (3.9s) Cartons stacked behind the counter. (5.0s) Quick eating, a plastic box lid tapping. (7.6s) The rain thinning to drips; a stool pushed back; a helmet strap clicking. (10.0s) The door opening, two light knuckle taps on glass. (11.6s) The door chime fading, a scooter starting outside and pulling away, dripping water.

non_diegetic_music: Sparse solo piano at a slow tempo enters at about 5.0 seconds, very quiet under the ambience, adds a single sustained low note when the rain stops, and fades out after the second knuckle tap.
```

---

## 3. 本地验证过的新文体范例（2026-10-07 两轮出片）

这两段是新文体，和旧版同种子对比、在本地出片验证过，内容和写法都可以学。它们没有完全照现行规则写（《临期》v2 照抄校准前写的 skill 版；《纸引》v2 写的时候复指出处、切镜句写景别和运镜状态、字数上限这些规则已经在 SKILL.md 里，但没有照做），不一致的地方在各节列出来，写新段时按 SKILL.md。

### 3.1 《纸引》EP1-06 快剪动作：扑水被截、踩灭尾火（8 秒 6 镜，第二轮两个种子都没问题）

学它的：
- 一个动作节拍一镜：冲刺 → 起跳被扫开 → 爬起再冲 → 插入特写踩灭 → 被拽停 → 余波。每镜 1.0–1.3 秒，第一镜 1.5 秒，最后一镜 1.8 秒。
- 交互放在 1.3 秒的第 2 镜：这一镜从冲刺的最后一步和起跳开始，在空中被翅膀扫开，摔回画面左边。两个种子都没有先停顿。
- 每个切镜写小老虎往画面右边跑；水盆出现的每个镜头写它在画面右边缘的木凳上；插入特写写尾巴拖向画面左边；后续镜头写 `from the same side`，机位不跳到动作线另一侧。两个种子方向都没翻，水盆都没漂。
- 声音段 3 句，配乐 N/A。

和旧版比：旧版（`tools/context_ir/old_versions/zhiyin_ep1_06.txt`）同样 6 镜、同样切点，第一轮最好，但写的是全大写运镜、`[Shot N · 时间]` 镜头头、`(flame: ON)` 括号标签和按秒列的声音，切到灭火特写方向翻了，水盆也漂。v2 换成新文体，补了方向和水盆位置；另外还改了这些：删了第 2 镜的快甩（`WHIP PAN`）和 `front paws reaching`，加了 `At the top of the leap` 和 `between him and the basin`；第 4 镜从急推特写（`SNAP-ZOOM ECU`）改成静止特写（插入特写保持静止，见 `physics-and-action.md` 第 3A 节）；删了第 3 镜的 `Without stopping` 和第 6 镜的 `A beat of stillness`，第 6 镜改成鹤女先抬爪、小老虎后坐下；声音段加了每步的铃声；字数多了约 30%。所以 v2 的结果是整包结果，方向不翻不能只归给每镜写方向。第一轮的 4 镜新文体版（`tools/context_ir/skill_versions/zhiyin_ep1_06.txt`）不如 6 镜，不再作范例。

和现行规则不一致、写新段时按 SKILL.md 的地方：后续镜头复指没带出处（第 2、3、6 镜的 `the cub`、第 5 镜的 `The cub's`、第 6 镜的 `The crane-woman`，应写 `the paper tiger cub from Shot 1`、`the crane-woman from Shot 2`；第 2、3 镜的水盆是动作对象，也应写 `the bronze basin from Shot 1`；只有第 5 镜给鹤女写了 `from Shot 2`，所以 lint 不报）；第 2 镜的切镜句没写景别（`a side tracking shot`），第 3、5 镜没写运镜状态（`a low-angle medium shot from the same side`）；固定段（画风开头）以外约 478 词，超过多镜头 450 词的上限；第 1 镜（画风开头以外）约 106 词、第 2 镜约 115 词、第 6 镜约 76 词，超过快剪每镜 40–70 词。lint 对这几处都不报 WARN。

```text
integrated_multimodal_description: [Shot 1] Photoreal cinematic, 16:9. A vast dark hall of an ancient Chinese paper-effigy shop on a rainy night: black wooden pillars, wet stone floor, white paper lotus lanterns hanging from the beams, white paper horses standing in the shadows. Warm orange light from an iron fire brazier at the back left, cold blue rain light from the open doorway at the back. All creatures are real handmade paper craft: stiff folded paper with visible fibres, brush-ink lines and burnt edges; they bend only at the joints. Film grain. A low tracking shot at paw height follows a small tiger cub made of stiff white folded paper — black brush-painted stripes, torn red paper ribbons at his neck and wrists, a tiny bronze bell at his throat, one amber ink-painted eye and one blank white paper eye — as he sprints on all fours across the wet stone toward the right of the frame, toward a black bronze water basin on a low wooden stool at the right edge of the frame. A small flame burns on the very tip of his tail and streams out behind him toward the left like a lit fuse.

[Shot 2] At 00:01.500, the camera cuts to a side tracking shot at the same low height, the cub still racing toward the right of the frame, the basin on its stool at the right edge. He leaps for the basin. At the top of the leap, a tall paper crane-woman — long thin beak, spiky white paper crown, layered white paper robes trimmed in red, one snow-white wing and one charred black wing — steps in from the right between him and the basin and sweeps her white wing across his path. The wing slams into him in mid-air; white paper feathers and ash burst, and he tumbles back to the left across the wet stone.

[Shot 3] At 00:02.800, the camera cuts to a low-angle medium shot from the same side, the cub on the left of the frame, his tail flame still burning. He scrambles up, claws skidding on the wet stone, and lunges again toward the basin at the right edge of the frame; the camera shakes slightly as he launches.

[Shot 4] At 00:04.000, the camera cuts to a static extreme close-up of his burning tail tip on the stone, trailing toward the left of the frame. A thin white bird claw comes down hard on the tip and pins it flat; sparks and black paper ash burst out from under the claw, and the flame is crushed out in one blow.

[Shot 5] At 00:05.000, the camera cuts to a low-angle medium shot from the same side. The cub's lunge toward the right stops short: his stiff paper body jerks taut and the bell at his throat jolts once. The crane-woman from Shot 2 stands bent over him, her claw pinning his tail to the stone on the left; the basin stays on its stool at the right edge of the frame.

[Shot 6] At 00:06.200, the camera cuts to a wider shot from the same side, slowly pulling out. The crane-woman lifts her claw and folds her white wing. The cub sits on the wet stone, looks back toward the left at his charred tail tip, where a thin curl of smoke rises, then looks at the basin at the right edge of the frame and stays where he is. Only the smoke and the brazier light keep moving.

overall_soundscape: Steady rain beyond the open doorway and the soft crackle of the brazier fill the hall. Small paper paws patter fast on wet stone and the tiny bell rings with each stride; a heavy paper wing whumps and a light paper body skids across the floor. Sparks hiss and crackle sharply as the claw comes down, followed by a single jolt of the bell and the thin hiss of rising smoke.

non_diegetic_music: N/A
```

### 3.2 《临期》段 04（15 秒 6 镜，第一轮 skill 版种子 2 最好，第二轮 v2 两个种子都没问题）

学它的：
- 一个节拍一镜：拿筷子 → 画外台词配听者反应 → 吃饭 → 雨停起身戴头盔 → 推门敲玻璃 → 点头余波。
- 隐藏目的写进行为（`keeping his eyes on the food, as if to keep his thanks casual`、`as if she would rather not make anything of it`），反应慢半拍、手停一下、嘴角动一点、不回头。
- 画外台词句配听者 `lips remain completely closed`。
- 细小物件写成已经完成的状态：拿起已经掰开的筷子，不写掰、搓（第一轮 skill 版正文和声音段都写了掰开、搓，段 10 筷子变形；v2 把这两句都改成已经掰开、只碰饭盒，同种子不再变形。声音段里也不要留掰、搓）。
- 没有全局表演段，两轮出片用户都没提表演问题（A/B 表第 9 项的弱证据，默认仍保留表演段）。

和现行规则不一致、写新段时按 SKILL.md 的地方：台词标签后没有空格（`<d>[Chinese]那我帮你扔。</d>`，A/B 表第 14 项）；后续镜头没有用 `from Shot N` 复指；`with no logos or brand names anywhere`、`he says nothing` 是否定写法；配乐里的 `at about 5 seconds` 是片内秒数，lint 会对这四处报 WARN。下面几处 lint 查不到：说话人老徐在第 1 镜第一次出场时没挂 `(S1)` 和 `on-screen`；第 1 镜的构图句（`A 50mm medium shot shows Lao Xu`）放在场景句后面，只有景别，没写运镜状态；第 2–5 镜的切镜句只写了景别，没写运镜状态；固定段（底座和光源句）以外约 472 词，超过多镜头 450 词的上限。

```text
integrated_multimodal_description: [Shot 1] Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores. Location light: flat cold-white fluorescent tubes inside the store, a warm amber glow from the hot-food cabinet, blue night light through the wet glass front as the rain thins; faces half cold white, half warm. A small unbranded 24-hour convenience store at 2 a.m., with no logos or brand names anywhere. The checkout counter is on the right of the frame and the window counter and glass door are on the left. Only two people are in the store. A 50mm medium shot shows Lao Xu at the window counter on the left: a delivery rider about 45, rain-flattened short hair, grey stubble, a sun-darkened tired face, a wet yellow rain jacket over a grey hoodie, his scuffed yellow helmet on the counter beside an open boxed meal. He picks up a pair of already-split wooden chopsticks lying beside the open box, keeping his eyes on the food, as if to keep his thanks casual.

[Shot 2] At 00:02.200, the camera cuts to a 50mm medium shot of Xiao Su behind the checkout counter on the right: a young woman about 22, dark hair in a low ponytail, a plain dark-green store vest over a white long-sleeve tee. Her back is half turned as she stacks cartons on a shelf. Lao Xu, a middle-aged man with a low, rough voice in plain Mandarin, short and gruff, a dry half-joke with warmth underneath (S1), says in an off-screen voiceover: <d>[Chinese]那我帮你扔。</d> while Xiao Su's lips remain completely closed. A beat after the line her hands pause on a carton; one corner of her mouth lifts a fraction; she does not turn around, and goes back to stacking, as if she would rather not make anything of it.

[Shot 3] At 00:05.000, the camera cuts to an 85mm close-up of Lao Xu at the window counter on the left, eating his first mouthful fast, steam rising from the box, his eyes on the food. His mouth is busy chewing and he says nothing.

[Shot 4] At 00:07.600, the camera cuts to a 35mm wide shot from inside the store toward the glass front. Outside, the rain thins to a drizzle and stops, while drops still run down the glass. In the foreground on the left, Lao Xu stands, closes the empty box and pulls on his yellow helmet, clicking the strap shut under his chin.

[Shot 5] At 00:10.000, the camera cuts to a 50mm medium shot at the glass door on the left. Lao Xu, helmet on, pushes the door half open, stops, and without looking back taps the glass twice with one knuckle toward the counter.

[Shot 6] At 00:11.600, the camera cuts to an 85mm close-up of Xiao Su behind the counter on the right. A beat after the taps, without looking up from the cartons, she nods once. The camera holds a static shot with a faint handheld breath. For the rest of the shot she does not move again; only the door chime fades and drops slide down the glass, and the window counter on the left behind her stands empty now that Lao Xu has gone.

overall_soundscape: Rain patters on the glass front over a low fluorescent hum and thins to slow drips as the scene goes on. Wooden chopsticks click lightly against the plastic box, a plastic box lid taps, a stool scrapes back and a helmet strap clicks shut. Two light knuckle taps on glass are followed by the door chime fading and a scooter starting outside and pulling away.

non_diegetic_music: Sparse solo piano at a slow tempo enters at about 5 seconds, very quiet under the ambience, adds a single sustained low note when the rain stops, and fades out after the second knuckle tap.
```
