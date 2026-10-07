# 摄影：电影感底座、光、色、运镜动机

## 1. 电影感底座（写实真人剧，默认套用，已实测）

来源：「H3-青橙电影提示词大师」改成 16:9 后在《阎王打工记》实测，比只写 `cinematic, 35mm` 明显更有电影感（人有质感、光有来源、画面有空气）。

T2VA 和关键帧模式：紧跟在 `[Shot 1]` 后照抄。Ref2VA：写在 `detailed_description` 开头、`[Shot 1]` 之前。再接一句本场光源。它属于 SKILL.md 的"固定句例外"，不计入字数预算。项目卡有自己的画风开头时（《纸引》），用项目卡那段代替底座，两段不叠加。
```text
Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores.
```
- **本场光源**写具体、写来源：`Location light: cold fluorescent overheads kept low, the blue-white monitor glow as key light on faces, soft daylight from the window row giving a hair rim glow.` 不同场景只换这一句，底座一字不改。
- **景别和运镜状态**：底座和本场光源之后的第一句构图句，写清景别和运镜状态（`A 50mm medium two-shot, holding a static shot with a faint handheld breath, shows …`）；后续每个切镜句也同时写景别和运镜状态（`the camera cuts to an 85mm close-up of …, pushing in slowly`）。官方改写 8/8 条第一句含景别，15 个镜头里 14 个写了运镜状态。把景别标签插到底座前面（`[Shot 1] Photoreal cinematic live-action, 16:9, medium two-shot, static shot. Shot on ARRI …`）更像官方，但会挪动实测底座的位置，只作为 A/B 表第 16 项，不设为默认。
- 镜头里写焦段：`an 85mm close-up`、`a 50mm medium shot`、`an over-the-shoulder shot`。景别写全称，可以用 Title Case（`Medium Close-Up`），不写缩写（`MCU`）。
- **底座是全段默认，镜头可以覆盖**：底座里的 `Lightly handheld throughout` 和 `Framing stays on the people: chest- or waist-up` 是全段默认，底座本身不改。某个镜头要稳定或静止（插入特写、关键文字、道具展示、稳定压迫感），就在那个镜头里写 `The camera holds a static shot` 或 `the camera holds steady, with only a faint handheld breath`；某个镜头要全景，或者手部、道具特写，就在镜头里写明景别（`a 35mm wide shot`、`an extreme close-up of the teapot spout`）。镜头里的写法只管那一个镜头。整段都要稳定时，能不能把底座的手持句换掉还没测过；要换，按 `pipeline-and-settings.md` 第 5 节做 A/B。
- 同一场戏的多段用同一个底座和同一句光源，能减少色差，但不能保证成片颜色不跳，出片后要对照检查。用上一段末帧做下一段首帧，颜色最稳；但只靠末帧会累积身份漂移。有人物的段按 `pipeline-and-settings.md` 第 1 节，首帧和身份参考图一起挂（Ref2VA 的 `[keyframe completion + reference generation]`）。

## 2. 光和色

- 光写三件事：从哪来、软还是硬、落在哪里看得见（`a warm amber pool from the pendant lamp over the tea table, cold blue dusk from the window behind; faces half warm, half cool`）。
- 颜色绑定具体物体：`the red seal paste is the only saturated colour in the frame`。给一组 3–5 个主色有助于跨段稳定。
- 优先写看得见的结果，不写参数：`the sky keeps its detail, dark clothing stays readable`。

## 3. 运镜动机与落点

谁的动作或视线触发移动 → 镜头沿哪里走 → 揭示什么 → 停在什么构图。例如人物听到门后响声，镜头沿视线移向门缝，停在门把和人物侧脸同框。不为凑运镜种类而绕拍或切镜；没有新的叙事需要时，保持机位或重复同类运镜。只想换距离或视角时，用有动机的运镜代替切镜（官方改写：跟着视线横摇 `The camera pans slowly rightward to follow his gaze`、弧形绕到肩后 `The camera initiates a smooth arc shot … just behind the man's right shoulder`）。

运镜两种写法都可以：官方指南的"类型 + 幅度 + 速度"（`pushes in with small amplitude at slow speed`），和 Context-IR 改写常用的副词式（`pushing in slowly`、`a slow push in`）。

- "少切镜"不是"不切镜"。用户要求别乱切时，切点只放在说话权交换处，用近景、过肩、反应镜头交替；整段一个固定机位，看起来像监控录像。
- 跟拍可以选一项轻微的不完美（跟随慢半拍、短暂的前景遮挡、构图回调），写明随后重新接住主体。不是每镜都加；固定机位、关键文字、道具展示保持稳定。

## 4. 画面文字和字幕

- 画面里真实可见的字，用英文半角双引号逐字写：`the terminal screen reads "余额不足"`。给一个静止的插入特写（`The camera holds a static shot on the screen.`），字才清楚。剧情靠字成立时（日期、金额），字要短。
- 不要字幕时，全项目只用这一句实测过的文字防护：`The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.` 其他地方不写"no X"——本地正向里写"没有 X"也算提到 X（实测"no subtitles"反而招来了字幕）。
- 挂了纯色底角色卡、背景变成影棚时，用 `h3-action-prompt-design` 第 1 节的 `Behind them is ONLY <Subject N>: …` 背景句。
