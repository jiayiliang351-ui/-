# H3 拆分前独立基线检索测试

测试日期：2026-10-07。

测试根目录：`C:\Users\Administrator\Videos\提示词参考视频\H3异能配套skill_20261007`。以下相对路径均相对此目录。检索范围仅为 `baseline-skills` 下三个现有 skill 的 `SKILL.md`、各自 references，以及文件清单；未读取脚本源码、仓库、其它版本或旧优化输出，未联网、调用 API、写提示词、运行 lint 或渲染。除本报告外未修改文件。

## 基线结论

- **没有独立可发现的 `h3-power-fx`。** 文件清单中仅有 `h3-shot-prompt/SKILL.md`、`h3-action-prompt-design/SKILL.md`、`h3-director-json-review/SKILL.md` 三个入口；入口和 references 中搜索 `h3-power-fx` 无匹配。
- **异能规则和六类能力索引已经存在，位于主 skill 的 references。** 当前依赖链是 `h3-shot-prompt` → `references/powers-and-effects.md` → `references/official-powers-calibration.md`，并非独立配套 skill。
- **普通对白不必继续读取两份异能参考文件。** 主入口按“异能、元素变化、时间静止、御剑或一打多”条件引导阅读，未要求每段都读异能全文；不过主入口、普通表演参考和动作手册内仍散布异能例外。
- **不存在可用于评价的 `h3-power-fx` description。** 现有 `powers-and-effects.md:3` 的用途句直接包含“仙侠”，未明确排除“仙侠题材但没有能力效果的普通文戏”。若直接把该句当成新入口描述，有误触发风险。现有主入口的条件路由较窄，不能据此声称未来独立入口的描述已通过误触发测试。

## 场景 1：普通便利店两人对白，没有异能

**任务约束**：普通文戏、两人对白；没有能力效果。未指定参考素材、项目、接力或导播台 JSON。

**入口与检索链**：

1. 读 `baseline-skills/h3-shot-prompt/SKILL.md`。它的 description 明确覆盖“对话戏、安静戏”，第 44–52 行规定每段流程，第 113–119 行处理台词和听者。
2. 必要参考：
   - `baseline-skills/h3-shot-prompt/references/official-format.md`：主入口第 184 行明确“每次都读”；查模式、镜头标记、台词和声音字段。
   - `baseline-skills/h3-shot-prompt/references/performance-and-dialogue.md`：查第 1 节普通人物表演、第 2 节声线、收口、听者反应、防串词。普通对白仍采用其默认表演规则。
   - `baseline-skills/h3-shot-prompt/references/cinematography.md`：写实真人戏底座、本场光源和运镜。
   - `baseline-skills/h3-shot-prompt/references/physics-and-action.md` 第 1 节：主流程第 47 行要求可行性检查；只有涉及接触、杯子等道具操作时继续读对应章节。
3. 初次使用或拿不准文体时读 `baseline-skills/h3-shot-prompt/references/examples.md` 第 1 节；其 1.3 是两人对话 Ref2VA 范例。可参照 `baseline-skills/h3-shot-prompt/references/official-calibration.md` 的 `office_two_speakers`（第 61 行起）；`linqi_04` 有便利店场景，但并非完整两人轮流对白，不能只凭同地点套用。

**必要边界与条件依赖**：

- 不需要读取 `powers-and-effects.md` 和 `official-powers-calibration.md`。便利店场景本身不触发异能；该校准文件中虽有“便利店结霜”样本，也不适用于此任务。
- `baseline-skills/h3-action-prompt-design/SKILL.md` 按主题选读：有参考素材才读第 1 节，需细查双人空间与站位读第 3 节，粤语才读第 6 节对应细则。它第 8 行写明“用不到的章节不读”。
- `baseline-skills/h3-director-json-review/SKILL.md` 是整份 JSON 审查入口，此单段任务无须加载。
- 不自动读取《纸引》或《阎王打工记》项目卡；未指定这些项目。

**共用格式与 lint**：沿主入口读取 `official-format.md`；单段 lint 位置见下文共用设施。

**结果**：普通文戏的按需检索链可成立；能避免读取异能参考全文，但现有通用文件中仍能看到静止和能力例外，尚未形成完全独立的异能入口。

## 场景 2：10 秒隐形念力让杯子浮起，仅冰箱、杯底摩擦、呼吸声

**任务约束**：不发光念力；杯子浮起；声音严格限定为三类，不能额外补落杯、溅水、衣料、魔法拟音或配乐。未指定松劲、落杯等结尾动作，不从样本擅自继承。

**入口与检索链**：

1. 仍先读 `baseline-skills/h3-shot-prompt/SKILL.md`。第 47 行通过“异能”条件直接指向 `references/powers-and-effects.md`；第 79 行说明单个物件悬浮不因特效强套快剪。名义 10 秒对应其本地实际时长表中的 10.13 秒。
2. 规则入口是 `baseline-skills/h3-shot-prompt/references/powers-and-effects.md`：
   - 第 1 节（第 7–13 行）：保留能力、对象、范围、结束状态、一镜到底和封闭声源约束。
   - 第 2 节能力表（第 19–26 行）：选择“不发光的念力”；第 28 行区分隐形力量与发光效果；第 17、30 行限制擅自增加落地或消散。
3. 样本索引是 `baseline-skills/h3-shot-prompt/references/official-powers-calibration.md` 的“用例目录”（第 15–28 行）。选择 `telekinesis_urban`（第 62–76 行），先读文件第 5–13 行偏差说明。

**六种能力索引的真实位置**：

| 六类 | 规则表位置 | 校准样本 ID |
|---|---|---|
| 能量波、剑气 | `powers-and-effects.md:21` | `blast_urban`、`blast_xianxia` |
| 不发光念力 | `powers-and-effects.md:22` | `telekinesis_urban`、`telekinesis_xianxia` |
| 结霜、电弧 | `powers-and-effects.md:23` | `element_urban`、`element_xianxia` |
| 觉醒、局部领域 | `powers-and-effects.md:24` | `awaken_urban`、`awaken_xianxia` |
| 时间静止 | `powers-and-effects.md:25` | `timestop_urban`、`timestop_xianxia` |
| 一打多、御剑 | `powers-and-effects.md:26` | `onevsmany_urban`、`onevsmany_xianxia` |

上表两个文件均在 `baseline-skills/h3-shot-prompt/references/` 下。没有独立的六能力索引文件或 `h3-power-fx` 目录。

**必要边界与条件依赖**：

- `official-powers-calibration.md:10` 已明确警告念力都市样本增加了简报以外的声音。样本第 74 行实际包含落杯 `clack` 和 `splash`，因此“文件可找到”不等于“可逐字照抄”。
- 声音总限制需同时约束正文、`overall_soundscape`、`non_diegetic_music`；主入口第 146 行要求“只有某某声”时配乐为 `N/A`。
- `official-format.md`、写实摄影参考、物理可行性仍沿主 skill 共用。若有人物表演，按需读表演参考；若挂素材，再读动作手册第 1 节。

**共用格式与 lint**：没有异能专用格式或 lint；使用主 skill 的模式格式与单段 lint。

**结果**：规则、六类能力索引和近似样本均可检索；独立配套入口缺失。封闭声源已在规则中覆盖，必须人工核对，不能直接继承官方样本声音。

## 场景 3：仙侠 15 秒一镜到底，左手冻住箭雨，右手拨箭、抱走孩子后解除

**任务约束**：实际时间静止能力；15 秒；全片一镜；左手触发、右手拨箭；救走孩子后解除。未指定静止期间只有脚步声，不套用都市时间静止的声源限制。

**入口与检索链**：

1. `baseline-skills/h3-shot-prompt/SKILL.md` → `references/powers-and-effects.md`，依靠“时间静止”条件触发，而非仅依靠“仙侠”题材。主入口第 79 行保留明确的一镜到底，第 101、153 行给出全局表演段例外。名义 15 秒对应其本地实际时长表中的 15.08 秒。
2. 重点读 `baseline-skills/h3-shot-prompt/references/powers-and-effects.md` 第 3 节（第 34–41 行）：
   - 静止动作：第 36–38 行区分范围、逐个写受限姿态、冻结物被移动后的新状态；省去要求全员小动作的全局表演段。
   - 手占用：第 39 行要求从触发到解除追踪维持手势、拨箭、腾手抱孩子、放下孩子与解除；不为修占用而改掉抬手定住、放手恢复的设定。
   - 声音：第 40 行按正常、静止期间允许声源、恢复三阶段描述；仙侠简报没有相同限制时不套都市版静音约定。
   - 连续镜头：第 41 行承认一镜救人高风险，靠跟拍接近手部、操作空间减负，不靠偷偷切镜或声称已解决穿模。
3. `baseline-skills/h3-action-prompt-design/SKILL.md` 第 5 节（第 167–173 行）补通用手和道具账：身体左右与画面左右、哪只手已占用、先放下或松开再操作、持续状态。
4. `baseline-skills/h3-shot-prompt/references/performance-and-dialogue.md:36` 补普通表演层的静止例外：完全冻结对象不眨眼、不换重心；普通定身与完全时间静止不混同。
5. `baseline-skills/h3-shot-prompt/references/official-powers-calibration.md` 查 `timestop_xianxia`（第 174–188 行），但先看第 11 行偏差说明。

**必要边界与条件依赖**：

- 校准样本把女侠写成左手维持后又用左臂抱孩子，且向上拨偏的箭最终又与箭雨共同钉进原地；开头已经标出这两处待核对。它不能替代本任务的左、右手状态账和箭轨迹检查。
- 现有规则明确要求检查手占用，但未提供一份已渲染验证的本场景操作方案。不能仅凭读到规则就断言抱孩子和解除已经可稳定完成。
- `physics-and-action.md` 第 1 节仍用于评估抱起、移动、遮挡等风险；不能用其默认拆镜建议覆盖本任务的一镜要求。
- 无台词不需加载对白细则；挂素材时才补动作手册第 1 节；只有整份导播台 JSON 审查才需要 `h3-director-json-review`。

**共用格式与 lint**：单段仍使用 `official-format.md`；lint 只负责文档声明的机械检查，手占用、箭轨迹、静止小动作与声音限制仍须人工核对。

**结果**：静止动作、声音和手占用都能从已有引用链找齐。它们分布在主 skill 两份 references 与动作手册，尚无独立 `h3-power-fx` 入口；存在明确文本证据边界，不能算渲染通过。

## 共用设施、依赖与缺失

| 项目 | 真实位置或状态 | 结论 |
|---|---|---|
| 共用文体、时长、镜头和自查 | `baseline-skills/h3-shot-prompt/SKILL.md` | 三场景均依赖 |
| 共用三段式、对齐句、Ref2VA 六段式 | `baseline-skills/h3-shot-prompt/references/official-format.md`；主入口第 127–148 行 | 异能不另建格式 |
| 素材职责、手、方向等补充 | `baseline-skills/h3-action-prompt-design/SKILL.md` | 只按相关主题读取 |
| 单段 lint | `baseline-skills/h3-shot-prompt/scripts/lint_prompt.py` | 文件清单确认存在；入口第 51、196 行说明用法。本测试未读源码或执行 |
| JSON lint | `baseline-skills/h3-director-json-review/scripts/lint_json.py` | 文件清单确认存在；其入口第 47 行声明会调用主 skill 的 lint。本测试未验证实际调用实现 |
| 独立异能入口 | `baseline-skills/h3-power-fx/SKILL.md` 不存在 | 独立发现目标未满足 |
| 异能规则与样本 | 主 skill 的 `references/powers-and-effects.md`、`references/official-powers-calibration.md` | 实际存在，可由主入口找到 |
| 从零项目规划 skill | JSON 审查入口第 15 行提及本机 `h3-seg-prompt-design` | 不在本基线清单；三个单段检索任务无需使用，未去其它位置读取 |
| `tools/context_ir/...` 仓库证据 | 主入口第 42 行明确为源仓库路径，不是安装包路径 | 不将其当成本地必备文件；本测试未读取或联网核查 |

本次仅确认文件现实、入口发现与条件引用链。普通对白无需异能参考全文、异能两场景可找到规则，属于静态检索结论；不构成提示词、API 改写、lint、导入或成片验收。
