# 单支飞箭冻结：用户出片通过的参照

用于复用“单人抬手，使一支飞箭停止并悬停到片尾”的写法。单镜头、8 秒、T2VA；角色在左、箭从右向左来，左掌触发、右手留在身侧，箭与掌之间有空隙。

## 出片证据与边界

2026-10-08，用户对方向修正版的两段视频反馈原话：**“这两段视频都没问题”**。对应 `freeze_direction_s1` / `freeze_direction_s2`，种子 **2026100701 / 2026100702**，每段 **8 秒**；两条 prompt 完全相同。这是用户观看后的整体通过反馈，Codex 未直接观看，未取得实际云端模型、LoRA、采样参数、有效提示词或单项声音测量。不把 2/2 样本写成稳定成功率。

上一版同种子被报告先飞后停、能悬停且没有增生，但两段箭头均从出现时反向。修正版只换箭首次出现的一处描述，把金属箭头、羽毛箭尾的左右位置及其与角色的远近关系写明，再写箭头领飞；JSON 的时长、种子、其他生成字段和冻结动作链保持一致。实际云端配置未经独立核对，不能证明文字替换是改善的唯一原因。

复用相似镜头时可参考下面两端形状与人物相对位置的写法，按实际构图调整；不把本例的一箭、8 秒或一镜到底设为所有异能戏的硬规则。它尚未验证全场时间静止、多箭、拨箭或其他接触、抱人、解除恢复、I2VA/Ref2VA，也没有改变主 skill 的分镜表。

摄影底座的手持和半身构图是全段默认；按[主 skill 的镜头覆盖规则](../../h3-shot-prompt/references/cinematography.md)，本例的具体镜头覆盖为静止机位和膝上构图。保留下方已获反馈的原文，不另改底座。

## 成功参照原文

下列三段式从已获用户反馈的 JSON 中直接提取，未经摘要或重写。更改角色、动作、输入模式或时长后仍需重新出片判断。

```text
integrated_multimodal_description: [Shot 1] Photoreal cinematic live-action, 16:9. Shot on ARRI Alexa Mini LF with Cooke Panchro/i Classic primes and a 1/4 Black Pro-Mist filter; 35mm for relationships, 50mm for mid shots, 85mm for faces, T2.0–T2.8 shallow depth of field. Kodak Portra 400 film emulation, about 50% teal-orange grade: teal-leaning shadows, warm amber skin. Fine film grain, soft-focus diffusion, a gentle haze in the air, soft halation on highlights, edges of the frame evenly lit. Lightly handheld throughout: a real handheld micro-shake and breathing motion. Framing stays on the people: chest- or waist-up, with headroom, hands and the key props visible in the lower frame. Real skin texture, visible pores. Soft daylight between the tiled roofs lights her face and hands against a pale plaster wall. A 35mm medium-wide side view holds a static shot across a stone-paved lane between tiled houses in one continuous take. A young woman in fitted teal robes and a high black ponytail stands at screen-left, facing right, framed from the knees upward with both hands open at her sides. She is the only person in the lane. A single wooden arrow enters from screen-right at her shoulder height, fully visible side-on against the pale wall. Its sharp metal arrowhead is at the left end nearest the woman, and its black-feathered tail is at the right end farther from her; the arrow travels point-first. It flies leftward toward her. Watching the approaching arrow, she raises her left hand, turning her open palm toward it. As her palm reaches shoulder height, the arrow abruptly stops in midair, its tip a forearm's length from her palm. The horizontal shaft and the open hand share the same focus plane, with a clear gap of air between them. Her right hand stays open beside her hip. She holds her left palm up and blinks once while studying the suspended arrow. The arrow keeps exactly the same position, height and angle through the final frame. The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.

overall_soundscape: A low breeze moves through the lane, with a faint rustle from her robe. A distinct, thin whistle follows the arrow's leftward flight and cuts off at the instant it stops in the air. Soft fabric brushes as her left sleeve rises; a quiet exhale is clearly heard while she watches the suspended shaft.

non_diegetic_music: N/A
```

## 源记录

- 源仓库 `tools/context_ir/powers/render/freeze_direction_v2/H3时间静止_只修箭头方向_2段16秒.json`。
- 用户反馈与证据边界：源仓库 `tools/context_ir/powers/analysis/RENDER_FEEDBACK_2.json`、`RENDER_FEEDBACK_3.json`。
- 源 JSON SHA-256：`4ae09306579f2867471b764f1318b01a88c0baaa79af36d206f9c1270f404e43`。
- prompt（含末尾换行）SHA-256：`8cf9ce209f5721ac2747f428c7e6a9095ab086261c84a38899156c57580fe064`。

这些源路径仅用于追溯，不是安装包内依赖；上方原文和证据说明可独立读取。
