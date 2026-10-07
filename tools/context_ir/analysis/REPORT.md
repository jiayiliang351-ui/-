# 官方改写对比报告

> 填写规则（给执行者）：
> 1. 只填事实。引用一律从 `analysis/side_by_side/<id>.md` 或 `analysis/sentences.md` **原样复制英文原句**，放在反引号里，不翻译、不改写、不总结。
> 2. 数字一律从 `analysis/features.md` 抄，不自己数。
> 3. 某项没有就写"无"。不要写"可能""大概"。
> 4. 每条用例一节，8 条都要填。最后填"跨用例统计"表。
> 5. 不要在这份报告里提改法，改法写进 `PROPOSALS.md`。


## 0. 运行信息

- 跑接口的日期：2026-10-07（Asia/Tokyo）
- 成功的用例数 / 总数：8 / 8
- 失败的用例和错误原文：本轮国内站新密钥无失败；此前其他密钥的 401、402 完整原文保存在 PROGRESS.md。
- token 用量合计（从 results/*.json 的 task.usage.total_tokens 相加）：68562

填写口径：英文引用从逐镜文件逐字抽取并核验；节拍按简报逗号、句号、分号原位切分，未写完整的要求记“否”。无台词、无配乐等否定要求按实际标签和字段核对，无对应句子写“无”。第 6 项逐行按所引原句判断，不跨行补足四步。情绪词沿用 analyze_ir.py 的 emotion 词表；L 等严格按模板的 features.md 命中数填表，不把关键词命中解释为语义证明。

---

## 用例：zhiyin_ep1_06（8 秒）

**1. 镜头数与切点**
- 官方：3 个，切点 3.20 5.50
- skill：4 个，切点 2.50 4.20 5.70
- codex（如有）：3 个，切点 2.00 4.50

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实电影感， | 是 | `[Shot 1] Cinematic, Medium Wide Shot at a low angle.` |
| 雨夜古代纸扎铺的大殿：黑木柱、湿石地、梁上挂白纸莲花灯， | 是 | `In the gloomy main hall of an ancient papercraft shop on a rainy night, the camera pans right, following the frantic movement of a small handmade papercraft tiger.`；`The highly textured set features black wooden pillars, a wet stone floor reflecting the ambient lighting, and white paper lotus lanterns hanging heavily from the overhead beams.` |
| 左后方铁火盆暖橙光， | 是 | `In the back-left midground, an iron brazier casts a warm orange glow, while cold blue rain light spills through the wide-open doors in the center background.` |
| 正后方敞开的大门透进冷蓝雨光。 | 是 | `In the back-left midground, an iron brazier casts a warm orange glow, while cold blue rain light spills through the wide-open doors in the center background.` |
| 所有角色都是真实的手工纸扎， | 是 | `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.`；`Suddenly, a tall, thin papercraft crane (with a long beak, a white paper crown, one pristine white wing, and one charred black wing) steps into the frame from the right.` |
| 硬纸、看得见纤维和墨线， | 是 | `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.` |
| 只在关节处弯。 | 是 | `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.` |
| 纸扎小老虎阿糊（白纸身、黑墨条纹、颈上小铜铃、一只琥珀墨眼一只空白纸眼）尾巴尖着着一小簇火， | 是 | `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.`；`A small cluster of real fire burns intensely on the tip of his tail.` |
| 四脚狂奔冲向右侧木凳上的黑铜水盆； | 是 | `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.`；`He charges toward a black bronze water basin resting on a wooden stool on the right side of the frame.` |
| 纸鹤婆婆（高瘦、长喙、白纸冠、一白一焦黑两只翅膀）从画右跨进来， | 是 | `Suddenly, a tall, thin papercraft crane (with a long beak, a white paper crown, one pristine white wing, and one charred black wing) steps into the frame from the right.` |
| 一翅膀把他扫开， | 是 | `The crane swings her charred wing, batting the tiger away.` |
| 他在湿石地上滚出去； | 是 | `He tumbles backward, rolling helplessly across the wet stone floor.` |
| 他爬起来再冲， | 是 | `The paper tiger from Shot 1 scrambles back onto his stiff paper feet, leans his weight forward, and lunges aggressively toward the basin again.` |
| 鹤婆一爪踩住他的尾巴尖， | 是 | `The tall crane from Shot 1 abruptly brings her large stiff claw down, violently stomping directly onto the burning tip of the tiger's tail.` |
| 火星和黑纸灰炸开， | 是 | `Bright orange sparks and thick black paper ash explode outward upon impact, instantly extinguishing the flame under the heavy claw.` |
| 火被踩灭； | 是 | `Bright orange sparks and thick black paper ash explode outward upon impact, instantly extinguishing the flame under the heavy claw.` |
| 他被拽住停下， | 是 | `Jerked to a sudden, jarring halt by his pinned tail, the paper tiger falls back into a seated position on the wet stone floor.` |
| 坐在地上回头看烧焦冒烟的尾巴， | 是 | `Jerked to a sudden, jarring halt by his pinned tail, the paper tiger falls back into a seated position on the wet stone floor.`；`He stiffly turns his head to look over his shoulder at his charred, smoking tail, his paper shoulders slumping slightly in defeat.` |
| 再看水盆， | 是 | `He then turns his head back forward to stare quietly at the out-of-focus water basin in the background, freezing completely motionless as a thin wisp of smoke rises from behind him.` |
| 不再动。 | 是 | `He then turns his head back forward to stare quietly at the out-of-focus water basin in the background, freezing completely motionless as a thin wisp of smoke rises from behind him.` |
| 没有台词， | 是 | 无 |
| 没有配乐。 | 是 | `N/A` |

官方额外加了、简报里没有的事件（原句）：`He stiffly turns his head to look over his shoulder at his charred, smoking tail, his paper shoulders slumping slightly in defeat.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：无
- 官方 `<d>` 原文：无

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, Medium Wide Shot at a low angle.`；`In the gloomy main hall of an ancient papercraft shop on a rainy night, the camera pans right, following the frantic movement of a small handmade papercraft tiger.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic, 16:9.`；`A vast dark hall of an ancient Chinese paper-effigy shop on a rainy night: black wooden pillars, wet stone floor, white paper lotus lanterns hanging from the beams, white paper horses standing in the shadows.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.`
- 这句里有几个外形特征（逐个列出）：6；`thick white paper`；`visible rough fibers`；`thick black ink stripes`；`small bronze bell on his neck`；`one amber ink eye`；`one blank paper eye`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `Bright orange sparks and thick black paper ash explode outward upon impact, instantly extinguishing the flame under the heavy claw.` | 是 | 是 | 是 | 是 |
| `Jerked to a sudden, jarring halt by his pinned tail, the paper tiger falls back into a seated position on the wet stone floor.` | 是 | 是 | 是 | 是 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`He stiffly turns his head to look over his shoulder at his charred, smoking tail, his paper shoulders slumping slightly in defeat.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：无

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：无
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：无

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, Medium Wide Shot at a low angle.`；`In the gloomy main hall of an ancient papercraft shop on a rainy night, the camera pans right, following the frantic movement of a small handmade papercraft tiger.`；`[Shot 2] At 00:03.200, the camera cuts to a Medium Close-Up and holds a static shot at floor level.`；`The paper tiger from Shot 1 scrambles back onto his stiff paper feet, leans his weight forward, and lunges aggressively toward the basin again.`；`The tall crane from Shot 1 abruptly brings her large stiff claw down, violently stomping directly onto the burning tip of the tiger's tail.`；`[Shot 3] At 00:05.500, the camera cuts to a Close-Up and pushes in slowly.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`while`；`Suddenly`；`then`；`as`

**11. 否定句**
无

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：4
- 官方 `non_diegetic_music` 原文：`N/A`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `The crane swings her charred wing, batting the tiger away.`
  - `Jerked to a sudden, jarring halt by his pinned tail, the paper tiger falls back into a seated position on the wet stone floor.`
  - `He stiffly turns his head to look over his shoulder at his charred, smoking tail, his paper shoulders slumping slightly in defeat.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `A vast dark hall of an ancient Chinese paper-effigy shop on a rainy night: black wooden pillars, wet stone floor, white paper lotus lanterns hanging from the beams, white paper horses standing in the shadows.`
  - `A low tracking shot at paw height follows a small tiger cub made of stiff white folded paper — black brush-painted stripes, torn red paper ribbons at his neck and wrists, a tiny bronze bell at his throat, one amber ink-painted eye and one blank white paper eye — as he sprints on all fours across the wet stone toward a black bronze water basin on a low wooden stool at the right of the hall.`
  - `A beat later she lifts the claw and folds her white wing against her side.`
---

## 用例：linqi_04（15 秒）

**1. 镜头数与切点**
- 官方：2 个，切点 8.50
- skill：6 个，切点 2.20 5.00 7.60 10.00 11.60
- codex（如有）：4 个，切点 2.00 5.50 10.50

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实真人温情短剧。 | 否 | `[Shot 1] Cinematic, MCU, static shot.` |
| 凌晨两点的小便利店（无品牌标识）， | 否 | `Inside a quiet, dimly lit convenience store at 2:00 AM, the delivery driver Lao Xu (S1), a 45-year-old man with matted, rain-dampened short hair, graying stubble, a deeply tanned face, and a sodden yellow plastic raincoat, sits at the left-hand windowsill.` |
| 外面的雨渐渐停了。 | 否 | `The scene opens with the distant, rhythmic patter of light rain fading into the background, accompanied by the sharp, audible snap of wooden chopsticks being separated. The clatter of plastic containers hitting the windowsill is followed by the soft, rhythmic rustle of cardboard boxes being stacked. As the delivery driver stands, the squeak of rubber soles on the floor and the muted thud of a helmet being picked up are clearly heard, ending with the sharp, metallic clinking of two distinct knuckle taps against the glass door.` |
| 外卖员老许（45岁左右， | 是 | `Inside a quiet, dimly lit convenience store at 2:00 AM, the delivery driver Lao Xu (S1), a 45-year-old man with matted, rain-dampened short hair, graying stubble, a deeply tanned face, and a sodden yellow plastic raincoat, sits at the left-hand windowsill.` |
| 雨淋塌的短发、胡茬、晒黑的疲惫脸、湿黄雨衣）在左边窗台吃店员小苏热给他的过期便当； | 否 | `Inside a quiet, dimly lit convenience store at 2:00 AM, the delivery driver Lao Xu (S1), a 45-year-old man with matted, rain-dampened short hair, graying stubble, a deeply tanned face, and a sodden yellow plastic raincoat, sits at the left-hand windowsill.`；`He holds a plastic container of bento and snaps apart a pair of white wooden chopsticks with a distinct click.` |
| 小苏（22岁， | 是 | `The camera pans slowly rightward to follow his gaze toward the cashier, where the store clerk Xiao Su (22), wearing a deep green vest over a simple white t-shirt with her hair in a low ponytail, stands with her back to him, organizing cardboard boxes on the counter.` |
| 低马尾， | 是 | `The camera pans slowly rightward to follow his gaze toward the cashier, where the store clerk Xiao Su (22), wearing a deep green vest over a simple white t-shirt with her hair in a low ponytail, stands with her back to him, organizing cardboard boxes on the counter.` |
| 深绿店员马甲）在右边收银台后背对着他码纸箱。 | 是 | `The camera pans slowly rightward to follow his gaze toward the cashier, where the store clerk Xiao Su (22), wearing a deep green vest over a simple white t-shirt with her hair in a low ponytail, stands with her back to him, organizing cardboard boxes on the counter.` |
| 老许掰开一次性筷子， | 是 | `He holds a plastic container of bento and snaps apart a pair of white wooden chopsticks with a distinct click.` |
| 眼睛看着筷子， | 否 | `The camera pans slowly rightward to follow his gaze toward the cashier, where the store clerk Xiao Su (22), wearing a deep green vest over a simple white t-shirt with her hair in a low ponytail, stands with her back to him, organizing cardboard boxes on the counter.` |
| 用半开玩笑的粗哑嗓音说：“那我帮你扔。 | 否 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| ”这句台词出现时镜头在小苏身上， | 否 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 小苏不说话， | 是 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 手停了一下， | 是 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 嘴角动了一点， | 是 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 没回头。 | 是 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 老许埋头快吃， | 否 | `Lao Xu (S1) finishes his meal quickly, sets the empty container down, and stands up to retrieve his yellow motorcycle helmet from the counter.` |
| 吃完戴上黄头盔走到门口， | 否 | `Lao Xu (S1) finishes his meal quickly, sets the empty container down, and stands up to retrieve his yellow motorcycle helmet from the counter.`；`He walks toward the store entrance, his heavy boots thudding softly on the tiled floor.` |
| 推开半扇门， | 否 | `As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.` |
| 没回头， | 否 | `As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.` |
| 用指节朝收银台方向敲了两下玻璃。 | 是 | `As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.` |
| 最后小苏没抬头， | 是 | `Xiao Su, still focused on her tasks and with her head bowed, gives a small, singular nod of acknowledgment without ever looking back.` |
| 点了一下头。 | 是 | `Xiao Su, still focused on her tasks and with her head bowed, gives a small, singular nod of acknowledgment without ever looking back.` |
| 整段只有老许这一句台词， | 是 | `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.` |
| 安静的钢琴在雨停时轻轻进来。 | 否 | `A solo, melancholic piano melody begins with soft, sustained chords the moment the rain noise subsides, maintaining a slow and steady tempo throughout the clip.` |

官方额外加了、简报里没有的事件（原句）：`As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：`那我帮你扔。` → 一致
- 官方 `<d>` 原文：`那我帮你扔。`

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, MCU, static shot.`；`Inside a quiet, dimly lit convenience store at 2:00 AM, the delivery driver Lao Xu (S1), a 45-year-old man with matted, rain-dampened short hair, graying stubble, a deeply tanned face, and a sodden yellow plastic raincoat, sits at the left-hand windowsill.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic live-action, 16:9.`；`Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`Inside a quiet, dimly lit convenience store at 2:00 AM, the delivery driver Lao Xu (S1), a 45-year-old man with matted, rain-dampened short hair, graying stubble, a deeply tanned face, and a sodden yellow plastic raincoat, sits at the left-hand windowsill.`
- 这句里有几个外形特征（逐个列出）：4；`matted, rain-dampened short hair`；`graying stubble`；`deeply tanned face`；`sodden yellow plastic raincoat`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `He holds a plastic container of bento and snaps apart a pair of white wooden chopsticks with a distinct click.` | 否 | 是 | 是 | 否 |
| `As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.` | 是 | 是 | 是 | 否 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：无

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：`Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：`Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, MCU, static shot.`；`The camera pans slowly rightward to follow his gaze toward the cashier, where the store clerk Xiao Su (22), wearing a deep green vest over a simple white t-shirt with her hair in a low ponytail, stands with her back to him, organizing cardboard boxes on the counter.`；`Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`；`[Shot 2] At 00:08.500, the camera cuts to a medium shot behind the counter.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`as`；`As`

**11. 否定句**
`Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`；`Xiao Su, still focused on her tasks and with her head bowed, gives a small, singular nod of acknowledgment without ever looking back.`

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：3
- 官方 `non_diegetic_music` 原文：`A solo, melancholic piano melody begins with soft, sustained chords the moment the rain noise subsides, maintaining a slow and steady tempo throughout the clip.`
- 是否含情绪词（抄 features.md 的 music_mood_words）：1

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `[Shot 1] Cinematic, MCU, static shot.`
  - `As he reaches the exit, he pushes the glass door open a crack, lets out a soft grunt, and raps his knuckles twice against the glass surface facing the register.`
  - `A solo, melancholic piano melody begins with soft, sustained chords the moment the rain noise subsides, maintaining a slow and steady tempo throughout the clip.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `He snaps a pair of disposable chopsticks apart and rubs them together to clear the splinters, keeping his eyes on the chopsticks, as if to keep his thanks casual.`
  - `In the foreground on the left, Lao Xu stands, closes the empty box and pulls on his yellow helmet, clicking the strap shut under his chin.`
  - `Rain patters on the glass front over a low fluorescent hum and thins to slow drips as the scene goes on. Wooden chopsticks snap apart and rub together, a plastic box lid taps, a stool scrapes back and a helmet strap clicks shut. Two light knuckle taps on glass are followed by the door chime fading and a scooter starting outside and pulling away.`
---

## 用例：yanwang_ep02（10 秒）

**1. 镜头数与切点**
- 官方：3 个，切点 5.20 8.00
- skill：4 个，切点 1.60 4.60 7.40
- codex（如有）：3 个，切点 2.00 6.00

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实职场奇幻剧， | 是 | `[Shot 1] Cinematic, medium shot, holding a Static Shot.` |
| 傍晚老板办公室：长胡桃木茶台， | 是 | `The scene is set in an executive office at dusk, anchored by a long walnut tea table in the midground.` |
| 身后落地窗外是冷蓝的城市黄昏， | 是 | `In the background, floor-to-ceiling windows reveal a cold blue city skyline, contrasting with the warm, directional glow of an amber pendant light hanging directly above the desk.` |
| 茶台上方一盏琥珀吊灯。 | 是 | `In the background, floor-to-ceiling windows reveal a cold blue city skyline, contrasting with the warm, directional glow of an amber pendant light hanging directly above the desk.` |
| 阎王（伪装成新员工， | 是 | `On the left side of the frame stands the King of Hell (S1), an on-screen middle-aged man disguised as a new employee, wearing a dark gray, slightly-too-small suit with a bronze earphone in his left ear.` |
| 深灰偏小西装， | 是 | `On the left side of the frame stands the King of Hell (S1), an on-screen middle-aged man disguised as a new employee, wearing a dark gray, slightly-too-small suit with a bronze earphone in his left ear.` |
| 左耳戴古铜耳机， | 是 | `On the left side of the frame stands the King of Hell (S1), an on-screen middle-aged man disguised as a new employee, wearing a dark gray, slightly-too-small suit with a bronze earphone in his left ear.` |
| 中年男人）站在茶台前画面左侧； | 是 | `On the left side of the frame stands the King of Hell (S1), an on-screen middle-aged man disguised as a new employee, wearing a dark gray, slightly-too-small suit with a bronze earphone in his left ear.` |
| 老板钱总（银灰背头、炭灰立领上衣、手上一串黑念珠）坐在茶台后画面右侧； | 是 | `On the right, Boss Qian—a man with silver-gray slicked-back hair and a charcoal gray mandarin-collar top—sits behind the desk, holding a string of black prayer beads.` |
| 疲惫的同事小张站在茶台最右端。 | 是 | `At the far right edge stands Xiao Zhang, a younger, exhausted-looking colleague with slumped shoulders.` |
| 阎王从西装里抽出一支朱笔拍在茶台上， | 是 | `The King of Hell (S1) reaches into his tight suit jacket, pulls out a traditional vermilion wooden brush, and slaps it forcefully onto the tea table.` |
| 看着钱总， | 是 | `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.` |
| 低沉平稳地说：“他的活本王干， | 是 | `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.` |
| 一分钱不要。 | 是 | `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.` |
| ”然后屋里发生真实的物理变化：吊灯暗了一下又亮， | 是 | `The amber light overhead suddenly dims, then abruptly brightens.` |
| 钱总茶杯上的热气停住， | 是 | `On the desk, the wisps of white steam rising from Boss Qian's ceramic teacup instantly freeze, hanging entirely motionless in mid-air.` |
| 念珠散开滚过桌面。 | 是 | `The beads violently burst apart, rolling and scattering chaotically across the smooth wooden surface.` |
| 最后停在钱总低头看念珠的脸上， | 是 | `[Shot 3] At 00:08.000, the shot transitions to a close-up of Boss Qian's face from Shot 1, using a Static Shot.`；`He slowly tilts his head down to look toward the scattered beads out of frame.` |
| 他第一次没了从容。 | 是 | `The confident composure he previously maintained completely vanishes; his eyes widen slightly and his jaw slackens as he processes the physically impossible events in front of him.` |
| 只有阎王说话， | 是 | `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.` |
| 其他人嘴闭着。 | 是 | `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.` |
| 不要特效光。 | 是 | 无 |

官方额外加了、简报里没有的事件（原句）：`In Boss Qian's resting hands, the string holding the black prayer beads from Shot 1 snaps without warning.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：`他的活本王干，一分钱不要。` → 一致
- 官方 `<d>` 原文：`他的活本王干，一分钱不要。`

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, medium shot, holding a Static Shot.`；`The scene is set in an executive office at dusk, anchored by a long walnut tea table in the midground.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic live-action, 16:9.`；`Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`On the left side of the frame stands the King of Hell (S1), an on-screen middle-aged man disguised as a new employee, wearing a dark gray, slightly-too-small suit with a bronze earphone in his left ear.`
- 这句里有几个外形特征（逐个列出）：2；`dark gray, slightly-too-small suit`；`bronze earphone in his left ear`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `The King of Hell (S1) reaches into his tight suit jacket, pulls out a traditional vermilion wooden brush, and slaps it forcefully onto the tea table.` | 否 | 是 | 是 | 否 |
| `The beads violently burst apart, rolling and scattering chaotically across the smooth wooden surface.` | 否 | 否 | 是 | 否 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`The confident composure he previously maintained completely vanishes; his eyes widen slightly and his jaw slackens as he processes the physically impossible events in front of him.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：`composure`

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：`Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.`
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：`Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.`

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, medium shot, holding a Static Shot.`；`[Shot 2] At 00:05.200, the camera cuts to a close-up of the walnut tea table, executing a slow Push In.`；`In Boss Qian's resting hands, the string holding the black prayer beads from Shot 1 snaps without warning.`；`[Shot 3] At 00:08.000, the shot transitions to a close-up of Boss Qian's face from Shot 1, using a Static Shot.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`as`；`suddenly`；`then`

**11. 否定句**
`In Boss Qian's resting hands, the string holding the black prayer beads from Shot 1 snaps without warning.`

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：4
- 官方 `non_diegetic_music` 原文：`Low-frequency ambient drone, slow tempo, featuring a deep, sustained synth bass that subtly underscores the supernatural tension without overpowering the physical foreground sounds.`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `In Boss Qian's resting hands, the string holding the black prayer beads from Shot 1 snaps without warning.`
  - `The confident composure he previously maintained completely vanishes; his eyes widen slightly and his jaw slackens as he processes the physically impossible events in front of him.`
  - `Low-frequency ambient drone, slow tempo, featuring a deep, sustained synth bass that subtly underscores the supernatural tension without overpowering the physical foreground sounds.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field.`
  - `The string of black prayer beads slips loose from his wrist, and the beads scatter across the walnut, roll, slow down and stop one by one against the teapot.`
  - `For the first time his polite composure holds perfectly still: his hand stays where the beads were, his jaw tightens a fraction, and a beat later he swallows.`
---

## 用例：couple_split（15 秒）

**1. 镜头数与切点**
- 官方：1 个，切点 （单镜头）
- skill：5 个，切点 2.40 4.60 7.40 10.20
- codex（如有）：4 个，切点 3.00 6.50 10.00

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实都市情感剧， | 是 | `[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.` |
| 夜里安静的梧桐树人行道， | 是 | `[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.` |
| 钠灯一盏盏投下暖黄光圈。 | 是 | `[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.` |
| 年轻女人（齐肩黑直发、燕麦色长大衣、斜挎小黑包）站在画面左边， | 是 | `A young on-screen woman (S1) with shoulder-length straight black hair, wearing an oatmeal-colored long coat and a small black crossbody bag, stands on the left side of the frame.` |
| 年轻男人（黑色飞行夹克、灰卫衣）站在右边， | 是 | `Facing her on the right is a young on-screen man (S2) in a black bomber jacket over a gray hoodie.` |
| 吵架。 | 是 | `The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.`；`He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.` |
| 她眼里有泪但没掉， | 是 | `The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.` |
| 声音低：“你每次都说下次。 | 是 | `The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.` |
| ”他看向别处、揉后颈， | 是 | `The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.` |
| 疲惫地说：“我今天真的很累。 | 是 | `He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.` |
| ”她更轻地说：“那你回去休息吧。 | 是 | `He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.` |
| ”她先转身朝画面左边走， | 是 | `He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.` |
| 不回头； | 是 | `He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.` |
| 他停一拍， | 是 | `The man (S2) stands frozen for a beat, then takes three slow steps towards the right side of the frame.` |
| 往右走三步， | 是 | `The man (S2) stands frozen for a beat, then takes three slow steps towards the right side of the frame.` |
| 停下回头看她。 | 是 | `He abruptly stops and turns his head to look back over his left shoulder at her departing figure.` |
| 最后镜头绕到他右肩后面， | 是 | `The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.` |
| 远处她越走越小， | 是 | `The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.` |
| 始终没回头。 | 是 | `The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.` |
| 他全程在画面里。 | 是 | `[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.`；`The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.` |

官方额外加了、简报里没有的事件（原句）：`He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：`你每次都说下次。` → 一致；`我今天真的很累。` → 一致；`那你回去休息吧。` → 一致
- 官方 `<d>` 原文：`你每次都说下次。`；`我今天真的很累。`；`那你回去休息吧。`

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.`；`A young on-screen woman (S1) with shoulder-length straight black hair, wearing an oatmeal-colored long coat and a small black crossbody bag, stands on the left side of the frame.`
- skill [Shot 1] 前两句原文：`[Shot 1] Live-action urban relationship drama, photoreal, 16:9, at night on a long, straight, empty tree-lined sidewalk in a quiet city.`；`Mature plane trees line the street; tall sodium-vapor streetlamps stand evenly spaced, each throwing a warm amber pool on the paving, with cool blue-cyan shadow between the pools.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`A young on-screen woman (S1) with shoulder-length straight black hair, wearing an oatmeal-colored long coat and a small black crossbody bag, stands on the left side of the frame.`
- 这句里有几个外形特征（逐个列出）：3；`shoulder-length straight black hair`；`oatmeal-colored long coat`；`small black crossbody bag`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `The man (S2) stands frozen for a beat, then takes three slow steps towards the right side of the frame.` | 否 | 否 | 是 | 否 |
| `He abruptly stops and turns his head to look back over his left shoulder at her departing figure.` | 否 | 否 | 是 | 是 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.`；`He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：无

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：`The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.`；`He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.`
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：`The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.`

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, a medium two-shot holds on a quiet sycamore-lined sidewalk at night, illuminated by overhead sodium street lamps that cast warm yellow halos onto the paved ground.`；`The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`while`；`immediately`；`then`

**11. 否定句**
`He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.`；`The camera initiates a smooth arc shot, tracking to the right and moving in to position itself just behind the man's right shoulder, keeping him continuously in the foreground frame while the woman (S1) grows smaller and smaller in the distant warm street light, continuing her steady walk away into the night without turning around.`

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：3
- 官方 `non_diegetic_music` 原文：`Solo acoustic piano playing slow, sparse chords, with a subtle, sustained low cello drone underneath, maintaining a quiet, restrained dynamic throughout without any swell.`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `A young on-screen woman (S1) with shoulder-length straight black hair, wearing an oatmeal-colored long coat and a small black crossbody bag, stands on the left side of the frame.`
  - `He exhales heavily and replies tiredly, <d>[Chinese] 我今天真的很累。</d> Staring at him for a brief second, the woman (S1) softens her posture slightly and murmurs even more quietly, <d>[Chinese] 那你回去休息吧。</d> Without waiting for a response, she immediately turns to her left and begins walking away down the shadowy, leaf-strewn sidewalk, never looking back.`
  - `Solo acoustic piano playing slow, sparse chords, with a subtle, sustained low cello drone underneath, maintaining a quiet, restrained dynamic throughout without any swell.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `A medium two-shot from the side under one streetlamp: the young woman stands on the left of the frame, shoulder-length straight black hair, an oatmeal-beige long wool coat over a cream turtleneck, a small black leather bag on her left shoulder; the young man stands on the right, one step away, short neat black hair, a black bomber jacket over a grey hoodie, both hands empty.`
  - `Her right hand grips the strap of her bag and her eyes glisten, though no tears fall.`
  - `By about 13 seconds the camera settles behind his right shoulder, the back of his head and his shoulder soft in the right third of the frame, her figure sharp in the distance.`
---

## 用例：quiet_shen_fire（10 秒）

**1. 镜头数与切点**
- 官方：1 个，切点 （单镜头）
- skill：1 个，切点 （单镜头）
- codex（如有）：1 个，切点 （单镜头）

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实电影感， | 是 | `[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.` |
| 雨夜古代纸扎铺， | 是 | `[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.`；`The room is cluttered with hanging paper lanterns and skeletal bamboo frames, illuminated primarily by the orange, flickering glow of a cast-iron brazier in the lower foreground and the cold, desaturated blue light filtering through the rain-streaked wooden shop door.` |
| 一镜到底的安静戏。 | 是 | `[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.` |
| 三十多岁的沈娘子（低发髻插木簪、浅灰绿麻布上衣、灰蓝长裙， | 是 | `Shen Niangzi (S1), a woman in her thirties with a simple low hair bun secured by a single polished wood hairpin, wearing a muted light-grey-green linen top and a dusty grey-blue skirt, is crouched on the uneven floorboards before the brazier.` |
| 朴素）蹲在铁火盆前守火， | 是 | `Shen Niangzi (S1), a woman in her thirties with a simple low hair bun secured by a single polished wood hairpin, wearing a muted light-grey-green linen top and a dusty grey-blue skirt, is crouched on the uneven floorboards before the brazier.` |
| 往火里添一张黄纸。 | 是 | `She carefully feeds a single sheet of yellow ritual paper into the flames, her expression focused and solemn.` |
| 火光映着她半张脸， | 是 | `Her face is partially bathed in warm embers-light, contrasting with the dark, moody shadows of the shop.` |
| 门外是冷蓝的雨。 | 是 | `The room is cluttered with hanging paper lanterns and skeletal bamboo frames, illuminated primarily by the orange, flickering glow of a cast-iron brazier in the lower foreground and the cold, desaturated blue light filtering through the rain-streaked wooden shop door.` |
| 画外忽然传来一声纸片窸窣， | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 她手停住， | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 眼睛先往声音方向瞟， | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 头慢半拍才转过去一点； | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 什么也没有， | 否 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 她松了口气， | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 但头没有完全转回来， | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 手里那张黄纸还捏着。 | 是 | `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 镜头从中景慢慢推到她的脸和火光。 | 是 | `[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.`；`Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` |
| 没有台词。 | 是 | 无 |

官方额外加了、简报里没有的事件（原句）：`Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.`；`The constant, rhythmic patter of heavy rain against the wooden shop exterior provides a base layer of ambient sound, punctuated by the sharp, crackling hiss of the burning yellow paper as it catches in the brazier. A crisp, brittle rustle of paper occurs from the dark corner, followed by the faint, rhythmic creaking of old floorboards under the woman's weight shift, and the soft, labored breathing of the woman (S1) as she reacts to the noise.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：无
- 官方 `<d>` 原文：无

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.`；`The room is cluttered with hanging paper lanterns and skeletal bamboo frames, illuminated primarily by the orange, flickering glow of a cast-iron brazier in the lower foreground and the cold, desaturated blue light filtering through the rain-streaked wooden shop door.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic, 16:9.`；`A vast dark hall of an ancient Chinese paper-effigy shop on a rainy night: black wooden pillars, wet stone floor, white paper lotus lanterns hanging from the beams, white paper horses standing in the shadows.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`Shen Niangzi (S1), a woman in her thirties with a simple low hair bun secured by a single polished wood hairpin, wearing a muted light-grey-green linen top and a dusty grey-blue skirt, is crouched on the uneven floorboards before the brazier.`
- 这句里有几个外形特征（逐个列出）：4；`simple low hair bun`；`single polished wood hairpin`；`muted light-grey-green linen top`；`dusty grey-blue skirt`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `She carefully feeds a single sheet of yellow ritual paper into the flames, her expression focused and solemn.` | 否 | 是 | 否 | 否 |
| `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.` | 是 | 否 | 是 | 是 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`She carefully feeds a single sheet of yellow ritual paper into the flames, her expression focused and solemn.`；`Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：`expression`；`contemplative`

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：无
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：无

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, medium shot, the camera slowly pushes in toward a dimly lit, weathered paper craft shop at night.`；`Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`before`；`Suddenly`；`as`

**11. 否定句**
无

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：2
- 官方 `non_diegetic_music` 原文：`N/A`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `The room is cluttered with hanging paper lanterns and skeletal bamboo frames, illuminated primarily by the orange, flickering glow of a cast-iron brazier in the lower foreground and the cold, desaturated blue light filtering through the rain-streaked wooden shop door.`
  - `Shen Niangzi (S1), a woman in her thirties with a simple low hair bun secured by a single polished wood hairpin, wearing a muted light-grey-green linen top and a dusty grey-blue skirt, is crouched on the uneven floorboards before the brazier.`
  - `Suddenly, a distinct sound of dry paper rustling emanates from the dark corner behind her, prompting the woman (S1) to freeze mid-motion; her eyes shift sharply toward the source of the noise before her head turns slowly and cautiously to inspect the shadows, her grip tightening on the remaining yellow paper, before she relaxes slightly but maintains her vigilance, head still angled toward the void as the camera closes in on the flickering flames and her contemplative profile.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `A vast dark hall of an ancient Chinese paper-effigy shop on a rainy night: black wooden pillars, wet stone floor, white paper lotus lanterns hanging from the beams, white paper horses standing in the shadows.`
  - `Early in the shot she feeds a sheet of yellow joss paper into the fire; its edge curls, blackens and catches, and a few sparks lift toward the beams.`
  - `Nothing moves in the shadows beyond the paper horses.`
---

## 用例：office_two_speakers（10 秒）

**1. 镜头数与切点**
- 官方：2 个，切点 5.20
- skill：3 个，切点 3.40 6.60
- codex（如有）：3 个，切点 2.00 5.50

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实职场剧， | 是 | `[Shot 1] Cinematic, medium two-shot, eye-level angle, static shot.` |
| 开放式办公区， | 是 | `The setting is a dimly lit, modern open-plan office at night, with blurred glass partitions and empty desks stretching into the background.` |
| 显示器冷光当主光。 | 是 | `The primary light source is the harsh, cool bluish-white glow from a computer monitor on the right, illuminating the scene with a stark cold tone.` |
| 疲惫的年轻男同事小张（黑眼圈、格子衬衫、黑框眼镜）坐在画面右边对着屏幕打字， | 是 | `An on-screen exhausted young male with heavy dark circles, wearing a faded blue-and-white plaid shirt and thick black-rimmed glasses (S1), sits on the right side of the frame.`；`The young man (S1) types on his keyboard, his eyes fixed squarely on the screen.` |
| 一直不看对方； | 是 | `The young man from Shot 1 (S1) is visible as an out-of-focus silhouette in the right foreground, still facing his screen.` |
| 新来的中年男人（深灰小西装、左耳古铜耳机）站在画面左边他工位旁边。 | 否 | `Standing on the left side of the frame, right next to the cubicle, is an on-screen middle-aged male wearing a tailored dark grey suit jacket and a distinctive metallic bronze earphone in his left ear (S2).` |
| 小张头也不抬， | 是 | `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.` |
| 平淡地说：“新来的？工位在那边。 | 是 | `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.` |
| ”新来的人看了一眼他指的方向， | 是 | `He shifts his gaze slightly to the right, glancing toward the direction indicated earlier.` |
| 低沉地说：“我知道了。 | 是 | `With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.` |
| ”然后转身走向那边。 | 是 | `With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.` |
| 两个人轮流说， | 是 | `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`；`With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.` |
| 一人一句。 | 是 | `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`；`With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.` |

官方额外加了、简报里没有的事件（原句）：无

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：`新来的？工位在那边。` → 一致；`我知道了。` → 一致
- 官方 `<d>` 原文：`新来的？工位在那边。`；`我知道了。`

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, medium two-shot, eye-level angle, static shot.`；`The setting is a dimly lit, modern open-plan office at night, with blurred glass partitions and empty desks stretching into the background.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic live-action, 16:9.`；`Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`An on-screen exhausted young male with heavy dark circles, wearing a faded blue-and-white plaid shirt and thick black-rimmed glasses (S1), sits on the right side of the frame.`
- 这句里有几个外形特征（逐个列出）：3；`heavy dark circles`；`faded blue-and-white plaid shirt`；`thick black-rimmed glasses`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.` | 否 | 否 | 是 | 否 |
| `With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.` | 是 | 否 | 是 | 否 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：`expression`

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：`Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`；`With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.`
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：`Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`；`The young man from Shot 1 (S1) is visible as an out-of-focus silhouette in the right foreground, still facing his screen.`

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, medium two-shot, eye-level angle, static shot.`；`[Shot 2] At 00:05.200, the camera cuts to a medium close-up of the middle-aged man (S2), executing a slow push in.`；`The young man from Shot 1 (S1) is visible as an out-of-focus silhouette in the right foreground, still facing his screen.`；`With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`as`；`Immediately`；`after`

**11. 否定句**
`Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：3
- 官方 `non_diegetic_music` 原文：`Subtle, pulsing ambient synthesizer drone, slow tempo, sustained low bass frequencies underneath, no melodic swell or percussion.`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `The setting is a dimly lit, modern open-plan office at night, with blurred glass partitions and empty desks stretching into the background.`
  - `An on-screen exhausted young male with heavy dark circles, wearing a faded blue-and-white plaid shirt and thick black-rimmed glasses (S1), sits on the right side of the frame.`
  - `The bronze earphone on the middle-aged man (S2) gleams under the ambient cool light.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `Location light: cold fluorescent overheads kept low, the blue-white monitor glow as key light on faces, soft daylight from the window row giving a hair rim glow.`
  - `The young man on the right with a flat, tired voice (S1) says, without looking up: <d>[Chinese]新来的？工位在那边。</d> As his line ends his lips close and his fingers go straight back to the keys.`
  - `Xiao Zhang does not turn his head; his typing pauses for half a beat as the man leaves, he swallows, and then the typing resumes.`
---

## 用例：wrist_grab（8 秒）

**1. 镜头数与切点**
- 官方：2 个，切点 3.20
- skill：3 个，切点 2.60 5.00
- codex（如有）：2 个，切点 2.00

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实悬疑短剧， | 是 | `[Shot 1] Cinematic, Medium Close-Up, pushing in slowly.` |
| 昏暗的档案室， | 是 | `The scene is set in a dimly lit archive room with faintly visible blurred metal shelving in the background.` |
| 桌上摊着一份牛皮纸文件。 | 是 | `A young man on the left, in his mid-20s with a slim build, wearing a crisp white button-up shirt with rolled-up sleeves, reaches his right hand toward a thick kraft paper document spread open on the table.` |
| 穿白衬衫的年轻男人伸手去拿文件， | 是 | `A young man on the left, in his mid-20s with a slim build, wearing a crisp white button-up shirt with rolled-up sleeves, reaches his right hand toward a thick kraft paper document spread open on the table.` |
| 旁边穿深色西装的中年男人一把抓住他的手腕把手按回桌上， | 是 | `Just as his fingertips graze the paper, an older man on the right—mid-50s, heavy-set, wearing a textured dark charcoal suit jacket over a grey shirt—lunges forward.`；`The older man forcefully grabs the young man's wrist with a thick hand, pressing his arm violently back down onto the tabletop.` |
| 文件没被拿走。 | 是 | `The hand of the older man from Shot 1 grips the wrist of the young man from Shot 1 tightly, pinning his arm against the edge of the kraft paper document from Shot 1.` |
| 两人僵持一秒， | 否 | `After a tense, motionless standoff, the young man slowly relaxes his fingers.` |
| 年轻男人慢慢把手抽回来。 | 是 | `He drags his hand backward, his fingertips scraping heavily across the rough surface of the document, slowly sliding out from under the older man's unyielding grip and retreating into the dark shadows at the edge of the frame.` |
| 没有台词， | 是 | 无 |
| 只有呼吸声和纸张摩擦声。 | 否 | `A thick, dead room tone establishes the quiet archive, suddenly broken by a sharp rustle of cotton fabric as an arm extends. A loud, forceful thud dominates the foreground as flesh and bone hit the solid wooden table, immediately followed by the crisp, dry crinkle of stiff paper being compressed. Distinct, strained nasal exhales and heavy, trembling breaths from both men fill the audio track during the physical standoff. This tension seamlessly transitions into a pronounced, prolonged scraping sound as fingertips drag slowly across the textured surface of the heavy paper.` |
| 动作要真实有重量。 | 是 | `The older man forcefully grabs the young man's wrist with a thick hand, pressing his arm violently back down onto the tabletop.`；`The young man's shoulders tense sharply as his forward momentum is halted.` |

官方额外加了、简报里没有的事件（原句）：`Just as his fingertips graze the paper, an older man on the right—mid-50s, heavy-set, wearing a textured dark charcoal suit jacket over a grey shirt—lunges forward.`；`Their hands tremble visibly under the intense physical strain, the older man's knuckles turning pale white under the bright beam of the desk lamp.`；`After a tense, motionless standoff, the young man slowly relaxes his fingers.`

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：无
- 官方 `<d>` 原文：无

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, Medium Close-Up, pushing in slowly.`；`The scene is set in a dimly lit archive room with faintly visible blurred metal shelving in the background.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic live-action, 16:9, a dim archive room with tall metal shelves of box files, a single desk lamp throwing a warm pool of light on a wooden table, cool grey shadow everywhere else.`；`50mm lens, shallow depth of field, fine film grain, real skin texture.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`A young man on the left, in his mid-20s with a slim build, wearing a crisp white button-up shirt with rolled-up sleeves, reaches his right hand toward a thick kraft paper document spread open on the table.`
- 这句里有几个外形特征（逐个列出）：3；`slim build`；`crisp white button-up shirt`；`rolled-up sleeves`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `The older man forcefully grabs the young man's wrist with a thick hand, pressing his arm violently back down onto the tabletop.` | 否 | 是 | 是 | 是 |
| `He drags his hand backward, his fingertips scraping heavily across the rough surface of the document, slowly sliding out from under the older man's unyielding grip and retreating into the dark shadows at the edge of the frame.` | 否 | 是 | 是 | 否 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：`The young man's shoulders tense sharply as his forward momentum is halted.`；`After a tense, motionless standoff, the young man slowly relaxes his fingers.`
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：`tense`

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：无
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：无

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, Medium Close-Up, pushing in slowly.`；`[Shot 2] At 00:03.200, the camera cuts to an Extreme Close-Up of the hands on the table, holding a static shot.`；`The hand of the older man from Shot 1 grips the wrist of the young man from Shot 1 tightly, pinning his arm against the edge of the kraft paper document from Shot 1.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`as`；`After`

**11. 否定句**
无

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：4
- 官方 `non_diegetic_music` 原文：`N/A`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `Just as his fingertips graze the paper, an older man on the right—mid-50s, heavy-set, wearing a textured dark charcoal suit jacket over a grey shirt—lunges forward.`
  - `Their hands tremble visibly under the intense physical strain, the older man's knuckles turning pale white under the bright beam of the desk lamp.`
  - `He drags his hand backward, his fingertips scraping heavily across the rough surface of the document, slowly sliding out from under the older man's unyielding grip and retreating into the dark shadows at the edge of the frame.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `A medium two-shot across the table: on the right of the frame, a young man in a white shirt with the sleeves rolled to the forearm; on the left, a middle-aged man in a dark suit, standing close beside the table.`
  - `Then the young man slowly draws his hand back toward himself; the older man's grip loosens and lets the wrist slide free.`
  - `The young man straightens up with his hand at his side, and the older man rests his own palm flat on the closed folder and keeps it there until the end.`
---

## 用例：tea_pour（8 秒）

**1. 镜头数与切点**
- 官方：1 个，切点 （单镜头）
- skill：1 个，切点 （单镜头）
- codex（如有）：1 个，切点 （单镜头）

**2. 节拍覆盖**（简报原文按逗号、句号、分号拆分）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| 写实电影感特写， | 是 | `[Shot 1] Cinematic, close-up shot with a slow camera push in, capturing a carved bamboo tea tray on a wooden table in an evening teahouse.` |
| 傍晚茶室， | 是 | `[Shot 1] Cinematic, close-up shot with a slow camera push in, capturing a carved bamboo tea tray on a wooden table in an evening teahouse.` |
| 一位老人双手提起紫砂壶往白瓷小杯里倒茶， | 是 | `With both hands, he carefully lifts a dark purple clay teapot.`；`He tilts the vessel, pouring a thin, steady, continuous line of amber tea into a small, pristine white porcelain cup resting on the tray.` |
| 茶水细细一线落进杯里， | 是 | `He tilts the vessel, pouring a thin, steady, continuous line of amber tea into a small, pristine white porcelain cup resting on the tray.` |
| 满到七分， | 是 | `Once the tea fills exactly to seventy percent of the small cup's capacity, the man stops pouring and gently lowers the teapot, resting it firmly back onto the slatted wooden tea tray.` |
| 他把壶放回茶盘， | 是 | `Once the tea fills exactly to seventy percent of the small cup's capacity, the man stops pouring and gently lowers the teapot, resting it firmly back onto the slatted wooden tea tray.` |
| 用两根手指把杯子推到对面。 | 是 | `He then extends his right hand, lightly pressing his index and middle fingers against the outside rim of the white cup, and smoothly pushes it forward across the wooden surface toward the opposite side of the frame.` |
| 暖色侧光， | 是 | `Warm amber side lighting streams in from the left, casting deep, textured shadows across the table and illuminating the space.` |
| 热气升起。 | 是 | `Thick white steam billows up from the hot liquid, glowing as it catches the warm side light.` |
| 没有台词。 | 是 | 无 |

官方额外加了、简报里没有的事件（原句）：无

**3. 台词**（从 analysis/dialogue_check.md 抄）
- 简报台词 → 状态：无
- 官方 `<d>` 原文：无

**4. 开头**
- 官方 [Shot 1] 前两句原文：`[Shot 1] Cinematic, close-up shot with a slow camera push in, capturing a carved bamboo tea tray on a wooden table in an evening teahouse.`；`Warm amber side lighting streams in from the left, casting deep, textured shadows across the table and illuminating the space.`
- skill [Shot 1] 前两句原文：`[Shot 1] Photoreal cinematic live-action, 16:9, a tea room at dusk with warm low side light from a paper window on the left, dark wood surfaces and soft shadow on the right.`；`85mm lens, shallow depth of field, fine film grain, real skin texture.`

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：`An elderly man, visible only by his dark brown linen tunic and deeply wrinkled, weathered hands, reaches into the frame.`
- 这句里有几个外形特征（逐个列出）：2；`dark brown linen tunic`；`deeply wrinkled, weathered hands`

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| `Once the tea fills exactly to seventy percent of the small cup's capacity, the man stops pouring and gently lowers the teapot, resting it firmly back onto the slatted wooden tea tray.` | 是 | 是 | 是 | 是 |
| `He then extends his right hand, lightly pressing his index and middle fingers against the outside rim of the white cup, and smoothly pushes it forward across the wooden surface toward the opposite side of the frame.` | 否 | 是 | 是 | 否 |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：无
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：无

**8. 台词前后**（无台词写“无”）
- 说话前描述声线的原句：无
- 说完后描述嘴、下颌、表情的原句：无
- 听的人的原句：无

**9. 运镜**
- 官方所有写运镜的原句：`[Shot 1] Cinematic, close-up shot with a slow camera push in, capturing a carved bamboo tea tray on a wooden table in an evening teahouse.`
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：否

**10. 时间衔接词**
`as`；`then`

**11. 否定句**
无

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：3
- 官方 `non_diegetic_music` 原文：`Solo acoustic guqin, very slow tempo, playing sparse and sustained plucked notes with a meditative, quiet dynamic.`
- 是否含情绪词（抄 features.md 的 music_mood_words）：0

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
  - `[Shot 1] Cinematic, close-up shot with a slow camera push in, capturing a carved bamboo tea tray on a wooden table in an evening teahouse.`
  - `An elderly man, visible only by his dark brown linen tunic and deeply wrinkled, weathered hands, reaches into the frame.`
  - `Solo acoustic guqin, very slow tempo, playing sparse and sustained plucked notes with a meditative, quiet dynamic.`
- skill 有、官方没有的 3 件事（每件配 skill 原句）：
  - `85mm lens, shallow depth of field, fine film grain, real skin texture.`
  - `When the tea reaches about seven tenths of the cup, he tips the pot back upright; the stream thins and breaks off, and one last drop falls from the spout onto the tray.`
  - `His hand withdraws and rests on the edge of the tray, and the steam keeps rising from the still cup until the end.`

---

## 跨用例统计（只统计官方改写；每格填“是/否”，最后一列数“是”的个数）

| 检查项 | 判断方法 | zhiyin_ep1_06 | linqi_04 | yanwang_ep02 | couple_split | quiet_shen_fire | office_two_speakers | wrist_grab | tea_pour | 是的个数 |
|---|---|---|---|---|---|---|---|---|---|---|
| A. [Shot 1] 以画风词开头 | 第一句含 cinematic / live-action / photoreal 之一 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 8 |
| B. 用 "from Shot N" 复指人物 | features.md 的 reidentify > 0 | 是 | 否 | 是 | 否 | 否 | 是 | 是 | 否 | 4 |
| C. 台词后写闭嘴或下颌停 | 第 8 项第 2 行不是"无" | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 0 |
| D. 听的人写嘴闭着 | 第 8 项第 3 行含 lips/mouth + closed/still | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 1 |
| E. 直接用情绪词 | 第 7 项第 2 行不是"无" | 否 | 否 | 是 | 否 | 是 | 是 | 是 | 否 | 4 |
| F. 用了否定句 | 第 11 项不是"无" | 否 | 是 | 是 | 是 | 否 | 是 | 否 | 否 | 4 |
| G. 运镜带幅度或速度 | features.md 的 amplitude_speed > 0 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 0 |
| H. soundscape 在 1–4 句 | features.md 的 soundscape_sentences 在 1–4 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 8 |
| I. 配乐含情绪词 | features.md 的 music_mood_words > 0 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 1 |
| J. 每镜都 ≥ 1.5 秒 | features.md 的 min_shot_s ≥ 1.5 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 8 |
| K. 镜头数 ≤ skill 表上限 | 对照 SKILL.md "时长、镜头数、字数"表 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 8 |
| L. 写明在场人数 | features.md 的 people_count > 0 | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 2 |
| M. 写了左右站位 | features.md 的 left_right > 0 | 是 | 是 | 是 | 是 | 否 | 是 | 是 | 是 | 7 |
| N. 改动了台词 | dialogue_check.md 出现"被改写或拆分"或"缺失" | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 0 |
| O. 加了简报里没有的事件 | 第 2 项"额外加了"不是"无" | 是 | 是 | 是 | 是 | 是 | 否 | 是 | 否 | 6 |
| P. 至少一处物理四步全写 | 第 6 项表格有一行四个"是" | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 2 |

## 平均值对比（从 features.md 的“平均值”段落抄）

| 指标 | 官方 | skill | codex |
|---|---|---|---|
| shots | 1.9 | 3.4 | 2.6 |
| words | 274.9 | 448.8 | 399.0 |
| words_per_shot | 163.8 | 164.4 | 185.0 |
| avg_sentence_words | 25.8 | 22.1 | 16.9 |
| camera | 2.0 | 1.5 | 0.6 |
| temporal | 3.5 | 6.9 | 5.8 |
| reidentify | 1.0 | 0.0 | 0.0 |
| lips | 0.2 | 2.0 | 2.5 |
| emotion | 0.8 | 0.4 | 0.1 |
| physics | 2.5 | 3.4 | 2.6 |
| negation | 0.9 | 2.1 | 0.2 |
