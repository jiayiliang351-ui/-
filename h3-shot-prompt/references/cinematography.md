# 摄影：电影感底座、光、色、运镜动机

## 1. 电影感底座（写实真人剧，默认套用，已实测）

来源：「H3-青橙电影提示词大师」改成 16:9 后在《阎王打工记》实测，比只写 `cinematic, 35mm` 明显更有电影感（人有质感、光有来源、画面有空气）。

T2VA 和关键帧模式：紧跟在 `[Shot 1]` 后照抄。Ref2VA：写在 `detailed_description` 开头、`[Shot 1]` 之前。再接一句本场光源：
```text
Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores.
```
- **本场光源**写具体、写来源：`Location light: cold fluorescent overheads kept low, the blue-white monitor glow as key light on faces, soft daylight from the window row giving a hair rim glow.` 不同场景只换这一句，底座一字不改。
- 镜头里写焦段：`an 85mm close-up`、`a 50mm medium shot`、`an over-the-shoulder shot`。
- 安静戏、情绪戏的手持只写"轻微"；需要稳定压迫感的场面写 `steady, with only a faint handheld breath`。
- 同一场戏的多段用同一个底座和同一句光源，能减少色差，但不能保证成片颜色不跳，出片后要对照检查。最稳的办法是用上一段末帧做下一段首帧（I2VA）。

## 2. 光和色

- 光写三件事：从哪来、软还是硬、落在哪里看得见（`a warm amber pool from the pendant lamp over the tea table, cold blue dusk from the window behind; faces half warm, half cool`）。
- 颜色绑定具体物体：`the red seal paste is the only saturated colour in the frame`。给一组 3–5 个主色有助于跨段稳定。
- 优先写看得见的结果，不写参数：`the sky keeps its detail, dark clothing stays readable`。

## 3. 运镜动机与落点

谁的动作或视线触发移动 → 镜头沿哪里走 → 揭示什么 → 停在什么构图。例如人物听到门后响声，镜头沿视线移向门缝，停在门把和人物侧脸同框。不为凑运镜种类而绕拍或切镜；没有新的叙事需要时，保持机位或重复同类运镜。

- "少切镜"不是"不切镜"。用户要求别乱切时，切点只放在说话权交换处，用近景、过肩、反应镜头交替；整段一个固定机位，看起来像监控录像。
- 跟拍可以选一项轻微的不完美（跟随慢半拍、短暂的前景遮挡、构图回调），写明随后重新接住主体。不是每镜都加；固定机位、关键文字、道具展示保持稳定。

## 4. 画面文字和字幕

- 画面里真实可见的字，用英文半角双引号逐字写：`the terminal screen reads "余额不足"`。给一个静止的插入特写（`The camera holds a static shot on the screen.`），字才清楚。剧情靠字成立时（日期、金额），字要短。
- 不要字幕时，全项目只用这一句实测过的文字防护：`The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.` 其他地方不写"no X"——本地正向里写"没有 X"也算提到 X（实测"no subtitles"反而招来了字幕）。
- 挂了纯色底角色卡、背景变成影棚时，用 `h3-action-prompt-design` 第 1 节的 `Behind them is ONLY <Subject N>: …` 背景句。
