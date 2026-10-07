# 异能补充实际补丁一致性审查

日期：2026-10-07。仓库：`C:/Users/Administrator/Videos/提示词参考视频/h3-calibration`。比较基线：Git HEAD `0ccc1d7f5b0aec48fc2c0e21d90ed5ff2c5d9c48`。本文件审查工作树补丁，不修改仓库或已安装 skill。

审查范围：`git diff`，新增 `h3-shot-prompt/references/powers-and-effects.md`、`official-powers-calibration.md`，以及 `tools/context_ir/powers/analysis/REVIEW_SKILL.md`。没有读取基线/候选写手或导播测试输出，没有网络、API 或视频生成。下文行号对应审查时工作树；父任务若继续修订，需要按原句重新定位。

最新工作树复核结论：下列前三项措辞问题已经修正，未发现新的规则冲突或渲染效果夸大。当前仅有两个说明文档指针待父任务收尾落盘；它们不是规则验证失败。

## 已修正的发现与收尾项

### 1. 念力分支应明确各阶段按简报选用

位置：`h3-shot-prompt/references/powers-and-effects.md:22`。

修正前原句：
> | 不发光的念力 | 施力者的注视或手势 → 目标先颤动/滑移/离地 → 悬浮或定向移动 → 放松后落定；物体保留原材质与现场照明 | `telekinesis_urban`、`telekinesis_xianxia` |

同文件第 9 行已经要求“简报已有的照简报；缺的只补连接动作所需的细节，不新增能力或后果”。但表的列名是“要交代的变化”，末尾“放松后落定”容易被当成所有无光念力都需要的结束动作。`telekinesis_xianxia` 只写叶群涌出院门，没有放松施力或叶群全部落定；其官方原文结尾为：
> The old Daoist stands perfectly still in his original posture as the remaining leaves flutter wildly through the suddenly opened doorway.

已采纳。最新第 17 行明确：“各阶段只按简报选用，不补没有指定的松劲、落地或消散”。表中阶段因此是候选变化，不再要求对每个念力需求补齐整条链。这是防止模板补戏，没有更改镜头表。

### 2. 箭轨迹应保留为待核对疑点，不能判定为已证实的不一致

位置：`h3-shot-prompt/references/powers-and-effects.md:52`。

修正前原句片段：
> 拨偏箭的轨迹与最终落点不一致

对应 `official-powers-calibration.md:11` 的事实性描述较为克制：拨偏写向上，而结尾写入原地面。原始 `timestop_xianxia.prompt.txt:1` 的逐字证据是：
> She reaches out with her bare right hand and lightly pushes the side of a black arrow that is pointed squarely at the frozen boy's head, visibly deflecting its trajectory upward.

> The deflected arrow and the entire black volley instantly resume their lethal velocity, slamming violently into the now-empty bluestone paving where the boy had just been lying, burying their iron tips deep into the stone as the crowd's frantic scattering continues around them.

原文没有角度、速度或完整弹道。“向上拨偏”可以只是改变原下行角度，并不能单凭这两句证明箭最终不能落地。已采纳：最新第 52 行改为“拨偏箭的轨迹与最终落点需要核对”，左手也改为“左手触发与抱孩子的占用需要澄清”。这保留了检查点，没有把文本疑点升级为已证实错误。

### 3. 集体定身的“不眨眼”例外范围应由简报决定

位置：`h3-shot-prompt/references/performance-and-dialogue.md:36`（新增段）。

修正前原句片段：
> 被定住的人在此期间不眨眼、不换重心、不慢半拍回应。

本批直接证据是完全时间静止的 `timestop_urban`、`timestop_xianxia`，可以支持这些被冻结对象保持整个人体姿态。它没有比较“只能定住肢体，但眼神仍可活动”的其他定身设定。新段同时覆盖“时间静止、集体定身”，若以后简报明确要求肢体定住但眼睛转动，这条无条件“不眨眼”会再次覆盖用户意图。

已采纳。最新段落把“不眨眼、不换重心、不慢半拍回应”限定为完全时间静止的对象，并明确“普通定身是否仍能眨眼、呼吸或说话则按简报”。主 skill 自查与 `powers-and-effects.md:37` 同步限定；固定表演段原文没有改动。

### 4. 审查说明中两个文档指针需在交付前落盘或改指向

位置：`tools/context_ir/powers/analysis/REVIEW_SKILL.md:30` 与 `:51`。

引用 `EVIDENCE_AUDIT.md` 和 `VALIDATION.md`。审查时对以下路径的 `Test-Path` 均为 `False`：

- `tools/context_ir/powers/analysis/EVIDENCE_AUDIT.md`
- `tools/context_ir/powers/analysis/VALIDATION.md`

独立审前报告实际已保存于工作区 `H3_skill优化_异能_20261007/evidence_audit.md`。可以复制到说明所引用的仓库位置，或修改说明链接。`VALIDATION.md` 若仍在汇总，属于交付前待完成项，不能凭本次缺失认定验证失败。本次只检查文件是否存在，没有读取写手/导播测试输出。

## 已通过的核对

- **原脚本未动。** 对基线提交中的 7 个已跟踪 `.py` 文件逐个解码、统一换行比较，变化列表为空。包括原分析和 lint 脚本；本次没有给它们增加新硬性校验。
- **镜头表原样保留。** `h3-shot-prompt/SKILL.md` 的戏种表与时长/镜头数表全部表格行逐字相等。新增的是用户明确一镜到底时不强拆的适用边界。
- **电影感底座原样保留。** `references/cinematography.md` 整份文字与基线相等。
- **固定表演原文原样保留。** `references/performance-and-dialogue.md` 的所有原有 `text` 代码块逐字相等。新增的是完全静止场景的适用边界。
- **对白规则未动。** 主 skill 的“台词”章节、导播审查“对白本地化”章节，以及 `performance-and-dialogue.md` 第 2 节起的原文逐字相等。动作手册第 6 节仅调整了环境底噪须服从静音/封闭声源的条款；剔除这一条环境声音政策后，该节文字与基线逐字相等。画外音、防串词和说话人收口没有被此次补充改写。
- **新增官方存档真实。** `official-powers-calibration.md` 中 12 个英文代码块分别与对应 `.prompt.txt` 和成功 JSON 内 `task.content.prompt` 相等，只忽略文件末端换行。对应 12 份中文简报原文也存在于存档中。
- **统计数字正确，分母可核对。** 原英文词正则复算正文共 3531 词，均值 294.25；显式镜头标签合计 30。`awaken_xianxia` 的未标号转场被明确指出，没有把显式标签数冒充真实镜头数。
- **配乐分母正确。** 适用全集是下列 12 个 case；非 `N/A` 集合为 `blast_urban`、`blast_xianxia`、`telekinesis_xianxia`、`element_urban`、`element_xianxia`、`awaken_urban`、`awaken_xianxia`、`timestop_xianxia`、`onevsmany_urban`、`onevsmany_xianxia`；`N/A` 集合为 `telekinesis_urban`、`timestop_urban`，因此 10/12 正确。该固定样本比例不能单独证明官方所有任务的普遍行为；“官方倾向自加配乐”最好理解为“本批输出倾向”，新段继续遵守项目声音约定即可。
- **声音封闭列表分母正确。** `telekinesis_urban` 与 `timestop_urban` 是声明“只有某类声音”的两条，说明没有用其他不适用样本稀释分母。
- **没有发现新渲染收益宣称。** 新增文档反复明确尚未渲染，盲写/静态检查不代替实际画质、物理、声音或导入验收；旧的“已实测”结论仍属于旧规则，没有被冒用为新异能规则的效果证据。
- **没有把基线四条全判失败。** `REVIEW_SKILL.md:49-50` 明确写“四条均保留关键事件”以及冻结稿照抄全员活动段这一项实际冲突。它没有把其他三条归为失败。本次不读取测试输出，因而不独立复判四份写作质量。
- **源仓库证据指针已说明。** 主 skill 新增说明 `tools/context_ir/...` 是源仓库路径，给出两轮报告的固定提交链接。已用本地 `git cat-file -e` 确认提交 `133bd1807a55ddfae633c719846152b4afec5fcf` 内两个报告路径确实存在；没有访问网络或读取这些旧渲染报告内容。
- **清单冲突同步处理。** 最新导播审查的表演项改为按受限姿态检查，尾段声音项服从用户静音/封闭声源；补充手册环境底噪和门病症表也按相同边界处理，没有让末尾清单重新要求定住的人活动或给念力开的门补手。

## 规则衔接结论

新增的“用户指定能力和结果优先”已明确限定旧受力风险表、碎灰爽片骨架、开门手部规则和镜头数表的使用范围。普通人力开门仍保留接触和方向要求；念力开门改为核对手势、力量作用和门的反馈。投射、无光念力、元素变化、局部觉醒、时间静止和御剑分支没有被合并成必备光球/外部命中/最终消散的一条链。

同一次下压造成群体倒地，被区分为同一主动作的受力结果；没有据此放宽所有多人同时各做不同动作的限制。局部停雨没有被误写成冻结三个打手。声音许可和一镜到底要求也在入口、分支与导播审查之间保持一致。

前三项措辞修订已在最新工作树复核通过。除两份说明文档仍待落盘之外，未发现需要扩大改动范围的事项。这里的通过仅指文本一致性与保护项，仍不代表真实渲染效果。


## 交付收尾核对（主任务）

`EVIDENCE_AUDIT.md`、`VALIDATION.md` 已落盘并通过存在性检查，最后两项文档指针已闭合。安装包与旧版备份、逐文件 hash 核对记录见 `delivery_manifest.json`。未新增渲染或 API 调用。
