# 官方改写对比报告

> 填写规则（给执行者）：
> 1. 只填事实。引用一律从 `analysis/side_by_side/<id>.md` 或 `analysis/sentences.md` **原样复制英文原句**，放在反引号里，不翻译、不改写、不总结。
> 2. 数字一律从 `analysis/features.md` 抄，不自己数。
> 3. 某项没有就写"无"。不要写"可能""大概"。
> 4. 每条用例一节，8 条都要填。最后填"跨用例统计"表。
> 5. 不要在这份报告里提改法，改法写进 `PROPOSALS.md`。

## 0. 运行信息

- 跑接口的日期：
- 成功的用例数 / 总数：
- 失败的用例和错误原文：
- token 用量合计（从 `results/*.json` 的 `task.usage.total_tokens` 相加）：

---

## 用例：<id>（<时长> 秒）

**1. 镜头数与切点**
- 官方：<shots> 个，切点 <cut_times>
- skill：<shots> 个，切点 <cut_times>
- codex（如有）：<shots> 个，切点 <cut_times>

**2. 节拍覆盖**（把简报按逗号、句号拆成节拍，逐条写官方有没有写到）
| 简报里的节拍 | 官方写了吗（是/否） | 官方对应原句 |
|---|---|---|
| | | |

官方额外加了、简报里没有的事件（原句）：

**3. 台词**（从 `analysis/dialogue_check.md` 抄）
- 简报台词 → 状态：
- 官方 `<d>` 原文：

**4. 开头**
- 官方 [Shot 1] 前两句原文：
- skill [Shot 1] 前两句原文：

**5. 人物介绍**
- 官方第一次介绍主要人物的原句：
- 这句里有几个外形特征（逐个列出）：

**6. 动作与物理**（引用官方写动作或接触的 2 句原文）
| 原句 | 写了起因？ | 写了用力/接触？ | 写了反应？ | 写了落定？ |
|---|---|---|---|---|
| | | | | |

**7. 表演与情绪**
- 官方写情绪或表情的 1–2 句原文：
- 有没有直接用情绪词（sad、angry、nervous、contemplation 等）？列出：

**8. 台词前后**（无台词写"无"）
- 说话前描述声线的原句：
- 说完后描述嘴、下颌、表情的原句：
- 听的人的原句：

**9. 运镜**
- 官方所有写运镜的原句：
- 有没有用 `with small/large amplitude` 或 `at slow/fast speed`：

**10. 时间衔接词**（列出官方用到的：as / while / then / until / suddenly / early in the clip / as the clip progresses / throughout / toward the end 等）

**11. 否定句**（官方含 no / not / never / without 的原句，没有写"无"）

**12. 声音**
- 官方 `overall_soundscape` 句数（抄 features.md）：
- 官方 `non_diegetic_music` 原文：
- 是否含情绪词（抄 features.md 的 music_mood_words）：

**13. 差异事实**
- 官方有、skill 没有的 3 件事（每件配官方原句）：
- skill 有、官方没有的 3 件事（每件配 skill 原句）：

---

## 跨用例统计（只统计官方改写；每格填"是/否"，最后一列数"是"的个数）

| 检查项 | 判断方法 | zhiyin_ep1_06 | linqi_04 | yanwang_ep02 | couple_split | quiet_shen_fire | office_two_speakers | wrist_grab | tea_pour | 是的个数 |
|---|---|---|---|---|---|---|---|---|---|---|
| A. [Shot 1] 以画风词开头 | 第一句含 cinematic / live-action / photoreal 之一 | | | | | | | | | |
| B. 用 "from Shot N" 复指人物 | features.md 的 reidentify > 0 | | | | | | | | | |
| C. 台词后写闭嘴或下颌停 | 第 8 项第 2 行不是"无" | | | | | | | | | |
| D. 听的人写嘴闭着 | 第 8 项第 3 行含 lips/mouth + closed/still | | | | | | | | | |
| E. 直接用情绪词 | 第 7 项第 2 行不是"无" | | | | | | | | | |
| F. 用了否定句 | 第 11 项不是"无" | | | | | | | | | |
| G. 运镜带幅度或速度 | features.md 的 amplitude_speed > 0 | | | | | | | | | |
| H. soundscape 在 1–4 句 | features.md 的 soundscape_sentences 在 1–4 | | | | | | | | | |
| I. 配乐含情绪词 | features.md 的 music_mood_words > 0 | | | | | | | | | |
| J. 每镜都 ≥ 1.5 秒 | features.md 的 min_shot_s ≥ 1.5 | | | | | | | | | |
| K. 镜头数 ≤ skill 表上限 | 对照 SKILL.md "时长、镜头数、字数"表 | | | | | | | | | |
| L. 写明在场人数 | features.md 的 people_count > 0 | | | | | | | | | |
| M. 写了左右站位 | features.md 的 left_right > 0 | | | | | | | | | |
| N. 改动了台词 | dialogue_check.md 出现"被改写或拆分"或"缺失" | | | | | | | | | |
| O. 加了简报里没有的事件 | 第 2 项"额外加了"不是"无" | | | | | | | | | |
| P. 至少一处物理四步全写 | 第 6 项表格有一行四个"是" | | | | | | | | | |

## 平均值对比（从 features.md 的"平均值"段落抄）

| 指标 | 官方 | skill | codex |
|---|---|---|---|
| shots | | | |
| words | | | |
| words_per_shot | | | |
| avg_sentence_words | | | |
| camera | | | |
| temporal | | | |
| reidentify | | | |
| lips | | | |
| emotion | | | |
| physics | | | |
| negation | | | |
