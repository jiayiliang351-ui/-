# 生产流程、设置与 A/B 方法

## 1. 推荐流程（真人剧）

1. **角色和场景定稿图**：每个角色一张正脸定妆照 + 一张全身；主场景至少两个机位（主机位 + 反打）；桌面、茶台这类近景道具区单独一张近景空镜。
2. **关键镜头先出首帧图**：用图像模型按分镜出这一段的第一帧（人物、站位、光都对），再用 I2VA 让 H3 从这张图往下拍。纯文生（T2VA）的人物每段都会重新长一遍，一致性最差。
3. **段与段接力**：用导播台的 latent 接力，或者上一段末帧导出当下一段首帧。每段开头写清继承的状态。实测要点（细则见 `h3-action-prompt-design` 第 7 节）：
   - 只用末帧当首帧会累积漂移（第三方实例：到第五段母亲已经不像了，烧进画面的字幕也被带下去）。接力链上每一段都要挂身份参考图——需要首帧时用 Ref2VA 的 `[keyframe completion + reference generation]`，首帧和角色图一起挂。
   - 漂移明显时断链，用只靠参考图生成的一段重建锚点。
   - 不要从空画面开始一段（人走出去了、门关上了），下一个进来的人会被编一张脸。
   - 只约束首帧时，坐着的人会自己站起来；首尾都约束才坐得住。
4. **需要停在指定画面**（为了接下一段）：用 L2VA 或 FL2VA，正文用单镜头连续写法。
5. **挂素材的段**（角色图、场景图、声音参考）：Ref2VA 六段式。素材越多越贵：一张参考图的计算量大约等于整段文字的十倍，按需挂。

## 2. 用官方改写做校准（强烈建议做一次）

官方 Context-IR 有付费 API（`/v2/h3_context_ir`），输入一句话需求 + 时长 + 比例，返回改写好的完整提示词，可以直接喂给本地 H3-Base（官方 README 的 "Full 2K Workflow" 就是这么用的）。建议：
- 挑 3–5 段典型戏（对话、动作、安静戏），用 API 各改写一次，存进 `examples.md` 当"标准答案"。仓库 `tools/context_ir/` 里有批量调用脚本和 8 条现成的测试需求。
- 同一段用 API 改写版和本 skill 写的版本，同种子各跑一次，对比哪里不同。

本地替代（不花钱，效果是近似的）：
- `lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA`（Qwen3.6-27B 上训练的 LoRA，另有 8B 版），有 ComfyUI 节点 `MiniMax-H3-Prompt-Rewriter-ComfyUI`。只做 T2VA。
- `ruashots/open-h3-ir`（开源的 Context-IR 复刻，带格式校验，有 ComfyUI 节点 `ComfyUI-OpenH3-IR`）。它的作者用同种子同参考图对比：原样输入的视频"走不到目的地"，改写后按要求完成了动作和切镜。

## 3. 采样设置（出片不对时先查这里）

- **时长**：导播台和工作流里填的时长要和提示词按的时长一致；15 秒的戏填 7 秒会挤。合法时长见 SKILL.md。
- **分辨率**：16:9 原生画布 1344×768（约 0.98 MP）。本地 H3-Base 只出 768p，2K 靠官方闭源的 Regenerate-2K。
- **CFG**：开源权重是 CFG 蒸馏过的，Turbo LoRA 也是免引导蒸馏，CFG 保持 1.0，调高只会打架。
- **步数**：原版约 20 步；挂加速 LoRA 时 6–8 步最好（不是名字里的 4 步）。本地实测配置：larryvrh v4，强度 1.0，6–8 步，simple 调度器；4 步糊快动作，超过 8 步过锐。社区另一套常见配置：Euler + Beta、视频 sigma shift 12、音频 sigma shift 4–6。加速 LoRA 在 1344×768 上训练，直接出 1920×1088 会偏软，1080p 用后期放大。文戏高配流程里的"8 步加速 LoRA 0.75"值得和 1.0 对比一次。
- **negativePrompt**：权重是 CFG 蒸馏的，没有原生负向输入，只有工作流接了 NAG 这类节点才起作用；V7.3 没接就留空。
- **LoRA 触发词和效果 embedding** 放在描述正文里，不放在最后一个字段后面（否则会被当成配乐说明）。写法见 `h3-action-prompt-design` 第 9 节。
- **种子**：同一版提示词至少跑 2–3 个种子再判断好坏。
- **打戏 LoRA**：别人流畅的打戏工作流挂了 `H3_Combat_V2`（0.75）和 `wushu_spatial_physics_v2`（0.3）；本地没有这两个，同样的提示词会差一截。
- **文戏高配**：先用 0.5 MP（960×544）出片，再用 learned latent upscaler 放大 1.2 倍、精修 3 步（FeiHou Remix v0.6 模型 + 8 步加速 LoRA 0.75）。

## 4. 导播台 JSON（V7.3）

用户要导入时，按这个结构输出（一段一个 shot，不挂素材时 `assets` 为空）：
```json
{
  "schemaVersion": 5,
  "project": {"id": "英文id", "name": "中文名", "runId": "英文id_t1"},
  "defaults": {"fps": 24, "baseSeed": 2026092801},
  "promptPrefix": "", "promptSuffix": "",
  "continuity": {"mode": "h3_av_latent", "videoContextFrames": 22, "audioContextFrames": 24, "durationMode": "final_output"},
  "assets": [],
  "shots": [{"id": "段号", "title": "段名", "prompt": "（完整提示词）", "negativePrompt": "",
             "durationSeconds": 8, "enabled": true, "latentRelay": false,
             "secondSamplingMode": "super_resolution_only", "seed": 2026092801, "disabledAssetIds": []}]
}
```
- `negativePrompt` 留空（V7.3 没接这个口）。
- `durationSeconds` 填整数（8、10、15），提示词里的切点和对齐句按实际帧长（8.00、10.13、15.08）。
- prompt 是 JSON 字符串：换行写成 `\n`，双引号转义成 `\"`。画面文字的英文双引号也要转义。

## 5. A/B 方法

- 同一段、同 2–3 个种子，一次只改一处，其余一字不动。
- **提示词长度变化本身会改变结果**：H3 把文字和视频排在同一条序列里，文字变长，视频部分的位置编码整体后移。所以"加了一句话变好了"可能是长度在起作用，不一定是那句话的内容。比较两种写法时，尽量让两版字数接近；结论要多个种子都成立才算数。
- 结果回填到下表。

| # | 对比 | A（旧写法） | B（新写法 / 官方） | 结果 |
|---|---|---|---|---|
| 1 | 声音字段 | 按秒列表 | 1–4 句连续段落，同步声写进镜头 | 待测（《临期》A 版跑得好，B 版在 examples.md 里待跑） |
| 2 | 镜头头 | `[Shot N · 1.5–2.8s]` | `[Shot N] At 00:01.500, the camera cuts to …` | 待测；新 skill 默认 B |
| 3 | 运镜 | 大写词 | 官方自然句（类型 + 幅度 + 速度） | 待测；新 skill 默认 B |
| 4 | 画外音 | `continues off-screen` | `says in an off-screen voiceover … lips remain completely closed` | **B 通过**（《五点五十九》段 03，2026-10-06） |
| 5 | 中文文戏模板 | 中文正文 | 英文正文 + 中文只在 `<d>` 里 | 待测；新 skill 默认 B |
| 6 | 表演写法 | 只写微表情 | 活人感：全局表演指导 + 隐藏目的 + 大动作掩盖 + 先后过程 + 每镜 ≤2 个小动作 | **B 胜**（《五点五十九》v2 对 v1，2026-10-06） |
| 7 | 规则写法 | `IMPORTANT —` / `FORBIDDEN` / 括号状态标签 | 全部改成可观察的陈述句 | 待测（examples.md 第 3 节两组对照） |
| 8 | 镜头密度 | 8 秒 6 镜 | 8 秒 4 镜 | 待测（《纸引》EP1-06 对照） |
| 9 | 全局表演段 | 保留 | 删掉，内容写进各镜头 | 待测 |
| 10 | 对齐句时长 | 实际帧长 `10.13` | 名义时长 `10.00` | 待测 |
| 11 | Turbo LoRA 强度 | 0.75 | 1.0 | 待测 |
