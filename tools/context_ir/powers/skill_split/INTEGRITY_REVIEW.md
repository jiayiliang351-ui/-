# H3 异能配套 skill 拆分独立完整性审核

审核日期：2026-10-08。结论：**四 skill 的静态分工、依赖链接与迁移完整性可接受，适合将四个目录作为一组安装；未发现由本次拆分引入的 P0/P1 阻断问题。** 不能把该结论扩写为“所有原文件字节未变”“已经验证检索不会误触发”“embedding 已安装/云端支持”或“异能出片有效”。

## 审核范围与方法

仅读取 `H3异能配套skill_20261007/baseline-skills`、`H3异能配套skill_20261007/candidate-skills` 和同目录的 `embedding_evidence.json`。没有读取写手结果、检索结果或旧优化输出；没有访问网络、API、云端、本地 H3 运行目录，也没有渲染、下载、安装或改动候选 skill。唯一交付写入是本报告。

以冻结 baseline 为唯一前后比较基准。比较原始 SHA-256 与规范化换行后的全文，核查 Markdown 相对路径/锚点、frontmatter、职责交叉引用、共享规则段和迁移文件；在内存中编译原脚本，运行原有 lint 对 12 个已随包提供的官方样本做前后行为比较。未生成候选目录的编译缓存。

下文文件与行号均相对 `candidate-skills`，另有说明的除外。P0/P1 表示阻断安装的问题；P2 表示需要补齐的重要证据或行为问题；P3 表示非阻断的维护/兼容性问题。证据限制不自动判定文案为错误。

## 发现与限制

### [P3] “正文原样”成立，但“原文件字节原样”不成立

涉及 `h3-shot-prompt/scripts/lint_prompt.py:1–282`、`h3-director-json-review/scripts/lint_json.py:1–92`、`h3-shot-prompt/references/cinematography.md:1–36`、`references/official-format.md:1–153`、`references/examples.md:1–275`、`references/official-calibration.md:1–89`、`references/troubleshooting.md:1–36`、`references/projects/yanwang.md:1–28`、`references/projects/zhiyin.md:1–40`（以上未完整写出的目录均为 `h3-shot-prompt/` 下）。

这 9 个文件正文与 baseline 完全一致，但 LF 被改成 CRLF，SHA-256 因此变化。比如原 `lint_prompt.py` 为 13,517 字节，候选为 13,799 字节，恰好多出 282 个 CR；`lint_json.py` 为 3,759 → 3,851 字节，多出 92 个 CR。没有发现语句、脚本逻辑、摄影底座、官方格式、既有范例或项目卡正文改变。新旧 lint 在已有 12 个样本上的结果也一致。

影响是无必要的文件差异及哈希变化，不是当前已观测到的功能变化。如果交付要求是原文件逐字节不动，应从 baseline 恢复这 9 个无需修改的文件；若允许换行归一化，安装说明应准确写成“正文/逻辑未变”。本审核没有执行恢复。

### [证据限制，非已证实内容错误] embedding 来源与当前解析实现没有可离线复核的原文

位置：`h3-power-fx/references/effects-embeddings.md:7–9,13–16`；`embedding_evidence.json:3–17`。

候选文案把效果资源归为社区贡献者 silveroxides，经 Comfy-Org 托管，并给出 ComfyUI 文档、托管目录及实现 PR 三个来源。`embedding_evidence.json` 恰好列出相同三个 URL，以及三个运行源文件哈希。但该 JSON 不含来源网页摘录、托管文件清单、PR 代码差异或 tokenizer/编码路径检查结果。

因此，本次允许读取的证据可以确认“引用的 URL 与证据清单一致”“记录声称做过运行源码检查”，不能独立证明作者归属、恰好 10 个文件、目录中的精确文件名或某一运行版本的实际解析行为。本报告不把这些事实判为错误，也不把来源 URL 本身当作内容已经核验的证明。若要宣称这部分事实已由本轮独立复核，应另附相关来源的只读摘录和实际解析路径结论；不需要因此默认下载或安装效果文件。

### [P3，兼容性边界] 旧文件路径保留，旧深链接锚点未保留

位置：`h3-shot-prompt/references/powers-and-effects.md:1–5`、`h3-shot-prompt/references/official-powers-calibration.md:1–5`。

两个旧路径均存在，并有真实可达的迁移链接；但它们现在只有 5 行，不保留原章节或案例锚点。原路径不带片段的访问可以人工点入新文件；旧的 `official-powers-calibration.md#blast_urban` 这类深链接不能直接定位旧文件的原案例。候选内部已存在的 12 个案例锚点位于新文件且全部有效，未发现候选内部断链。

此项不阻止安装。若“旧路径兼容”还包括外部收藏的原片段链接，需补充兼容锚点或给出明确迁移说明；普通文件入口迁移已经完成。

## 四 skill 的职责与实际依赖

| skill | 静态职责与证据 | 审核结果 |
|---|---|---|
| `h3-shot-prompt` | `SKILL.md:3,44–52,54–92,127–154,180–197`：单段文体、格式、时长、镜头表、预算、摄影、表演/对白与 lint。第 47、188 行按异能条件指向新 skill。 | 保持主规则所有权，没有新建第二套格式或脚本。 |
| `h3-power-fx` | `SKILL.md:3,8–23`：六类能力条件；明确共享主 skill 的格式、预算、摄影、对白和检查脚本；第 12 行真实链接主 skill，第 15 行说明缺依赖时停止发明格式。 | 独立 metadata 入口存在，但它是配套 skill，不是自带全部格式的独立替代品。四目录同级安装可满足依赖。 |
| `h3-action-prompt-design` | `SKILL.md:3,8–10,25,29–32,151,234–237`：素材、空间、门、手/道具、粤语、接力、故障定位及 LoRA 等补充；异能/embedding 指向新 skill。 | 没有复制异能规则全文或继续维护错误的“MiniMax 自带”embedding 清单。 |
| `h3-director-json-review` | `SKILL.md:12–17,48–64,78–86,125–131`：整份 JSON 的盘点、逐段改写、批量校验与交付；异能条件指向新 skill。 | JSON 审查仍复用原 lint，未复制 prompt linter 或新增另一套 JSON 字段规范。 |

主 skill、补充手册、导播审查中原有的部分对白预算/镜头阈值重复摘要仍存在，例如主 skill 第 92 行、表演参考第 40 行、导播审查第 57 行、补充手册第 19 行。数值一致，均明确以主 skill 为准；这属于 baseline 原有摘要，不是本次新增第二套规则。新 skill 本身没有复制数字表、三/六段式模板、防串词段或 lint 实现。

发现 39 个 Markdown 链接，其中 34 个为本地路径或片段，均真实存在，涉及的显式锚点均匹配；5 个外部 URL 未联网验证。新 skill 指向主 skill、补充手册、导播审查、能力细则、官方原文、embedding 页的链接全部可达。`h3-director-json-review/scripts/lint_json.py:21–32` 的默认定位实际解析到同组 `h3-shot-prompt/scripts/lint_prompt.py`，没有落入安装包外。

## 独立发现与误触发边界

`h3-power-fx/SKILL.md:1–4` 有独立的 `name` 与 `description`，描述同时覆盖都市/仙侠的具体超自然效果，并明确排除普通文戏、普通徒手打斗、只有古风服装或场景。正文第 13 行要求混合项目只对有特效的段启用，第 27 行禁止只因“仙侠”新增灵气、发光、古筝或夸张表演。

`h3-shot-prompt/SKILL.md:47` 与 `h3-director-json-review/SKILL.md:80` 的入口也把原来宽泛的“一打多”收窄成“异能一打多”，避免普通打斗仅因人数多而读异能细则。按静态描述，应当：

| 请求类型 | 应用边界 |
|---|---|
| 都市念力、能量波、结霜、电弧、时间静止 | 主 skill + 新 skill |
| 仙侠御剑、剑气、领域、法术交锋 | 主 skill + 新 skill |
| 仙侠两人饮茶对话、只有古装/山门背景 | 主 skill；按素材/对白需要查补充手册，不启用新 skill |
| 普通徒手一对一或一打多 | 主 skill 的动作规则；不因“一打多”单独启用新 skill |

这是 description 与入口路由的静态预期，不是平台实际检索/skill 自动触发测试。本轮被要求不读检索结果，因此不能声称已验证动态发现率或零误触发。

新能力参考 `references/powers-and-effects.md:3` 的旧正文仍使用较宽的“仙侠、一打多”概括，因要求逐字迁移而保留；其加载受新入口第 3、13 行限制，不构成新的 metadata 误触发入口。

## 静止例外、对白与时长规则

主 skill 第 79 行保留“一镜到底不按快剪表强拆”；第 101、153、173 行保留时间静止/集体定身省去全局表演段；第 178 行继续检查静止对象、数量和声源。表演参考第 36 行除更新真实链接外，原有静止例外全文未变。导播审查第 58、80、123 行也保留静止例外，第 121 行要求尾声遵守声音限制。新 skill 第 21 行和能力参考第 37–40 行与这些规则一致，没有要求被冻结的人眨眼、换重心、慢半拍回应或默认增加声源。

主 skill 第 109 行“一条主动作链，最多一个反应”，与能力参考第 45 行“群体受力是同一次攻击的结果”形成有说明的条件细化，不把多个主动攻击者的并行动作伪装为一条链。能力参考第 12、17、30 行也避免强制快剪、强制消散或强加投射轨迹。未发现本次拆分新增互相矛盾的格式、时长、对白或镜头规则。

逐段提取比较已确认以下主规则正文与 baseline 完全一致：合法时长及镜头数表（第 56–76 行）、正文字数和对白预算（第 86–92 行）、台词与防串词规则（第 113–119 行）、写实默认层及其静止例外（第 150–154 行）。摄影底座全文与两个项目卡正文也完全一致。

## 迁移完整性与原有内容保留

baseline 有 17 个文件，candidate 有 21 个文件；旧路径无删除，新增的是新 skill 的 `SKILL.md` 与 3 个参考文件。8 个既有路径发生正文修改；其中 2 个变为迁移入口，其余 6 个修改限定为职责/加载描述、真实引用链接或 embedding 纠错入口。

| 冻结文件 → 新维护位置 | 比较结果 | SHA-256 |
|---|---|---|
| `h3-shot-prompt/references/powers-and-effects.md` → `h3-power-fx/references/powers-and-effects.md:1–54` | 原始字节完全相同；全部能力条件、证据边界、声音与连续性说明保留 | `7de94d8bdb69071ec33935ea21814e093ea17754c50ec6f9d66740aba188302a` |
| `h3-shot-prompt/references/official-powers-calibration.md` → `h3-power-fx/references/official-powers-calibration.md:1–220` | 原始字节完全相同；12 例、中文需求、英文原文、已有瑕疵与偏差说明全部保留 | `13c489ba84b5f924a16f7b2d3db61eb874c08b76b9b0c52d5fee29211feceff1` |

12 例均存在且不重不漏：`blast_urban`、`blast_xianxia`、`telekinesis_urban`、`telekinesis_xianxia`、`element_urban`、`element_xianxia`、`awaken_urban`、`awaken_xianxia`、`timestop_urban`、`timestop_xianxia`、`onevsmany_urban`、`onevsmany_xianxia`。标题分别位于新官方原文文件第 30、46、62、78、94、110、126、142、158、174、190、206 行。开头第 3、7–13 行仍明确一次采样、无参考图、未渲染、官方原文也可能加戏。

两个原有 Python 脚本通过在内存中的语法编译。用 baseline 与 candidate 的原 lint 对同一 12 例运行，全部返回完全相同的 summary、ERROR、WARN；均为 0 ERROR，共 3 WARN，分别是 `blast_xianxia` 的 1 个及 `awaken_urban` 的 2 个。未为消除警告修改官方原文。**这只证明脚本行为未因迁移改变，不证明样本满足所有人工规则或能够正确出片。**

## embedding 的启用与证据边界

可在现有证据范围内确认：

- `effects-embeddings.md:3,13–16` 不默认加触发词；只有用户要求效果文件才读取；要求检查实际解析路径、搜索目录与文件，避免靠模型名称推断支持。
- 第 9 行不把 bullet time 等同于全场时间静止；第 15 行触发词以实际文件名为前提；第 16 行不承诺强度可调，也不把无日志错误当成视觉成功。
- 第 17、19 行明确要做同配置、同种子的出片对照；当前没有该项目出片结论。新 skill 第 15、34–36 行无 API/渲染授权扩张，不把文字检查称为本地出片有效。
- `embedding_evidence.json:8–13` 只列出 `put_embeddings_or_textual_inversion_concepts_here` 占位项，`cloud_runtime_checked=false`，`downloads=0`，`render_jobs=0`。它不支持“效果文件已安装”“云端可装/可用”或“视觉有效”的任何结论；候选文案未作这些承诺。

社区来源/文件数量和实现语法的事实独立核验仍受上面的证据限制约束。本文不访问实际 runtime，也不把 2026-10-07 的哈希记录当作 2026-10-08 当前运行状态验证。

## 安装判断与静态验证限制

**可作为四目录同级的一组 skill 安装，静态层面无阻断。** 不宜只安装 `h3-power-fx` 后声称它不需要主 skill；其依赖已在正文明确。该判断不等于已经安装或已被平台重新发现，本轮没有执行安装。

交付时应保留三条界限：

1. 异能规则与 12 例是逐字逐字节迁移；9 个本应不改的其他文件只是正文保持一致，换行格式有变化。
2. skill 的独立 metadata、排除条件及相对链接已检查；动态检索、实际自动触发和外部 URL 访问状态未测试。
3. 所有验证均为文件、文字、链接、语法与原 lint 的静态/机械验证；没有导入导播台、访问编码运行路径、调用 API、安装 embedding、渲染、播放、听音、检查口型、物理或视觉质量。候选中“通过盲写检查”的历史陈述并非本轮重新验证，本报告没有读取其结果。
