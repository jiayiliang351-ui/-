# H3 异能配套 skill 最终完整性复核

审核日期：2026-10-08。

**结论：本次指定的三项收尾问题已解决。`final-skills` 静态层面适合将四个 skill 同级成组安装，未发现新增 P0/P1/P2 阻断或需修复问题。** 原文件字节保留与旧深链接兼容问题关闭；embedding 证据可复核性已补齐到所提供资料包的摘录/观测摘要/源码片段层面。本结论不代表独立联网核验、已安装、实际编码成功、云端支持或渲染有效。

## 范围与方法

本轮仅读取：

- `H3异能配套skill_20261007/final-skills`
- `H3异能配套skill_20261007/baseline-skills`
- `H3异能配套skill_20261007/embedding_evidence.json`

没有读取写手结果、检索结果、旧优化输出或 candidate 快照，没有访问实际 runtime 源码文件或云端，没有联网、调用 API、渲染、下载、安装或修改 skill。仅在任务目录写入本报告。脚本语法检查与原 lint 比较在内存中执行，不生成 skill 目录的编译缓存。

以下 skill 文件行号均相对 `final-skills`。证据 JSON 行号相对任务目录。

## 三项问题的关闭结果

| 前轮项目 | 最终证据 | 结论 |
|---|---|---|
| 9 个无需修改的文件换行改变，导致字节/哈希变化 | 逐文件读取 baseline 与 final 原始字节，9/9 完全相同，文件长度和 SHA-256 均一致 | 已关闭；现在可以准确称这 9 个文件“原始字节保持不变” |
| 旧路径存在，但原章节/案例深链接锚点丢失 | 两个旧文件保留 baseline 的全部标题，标题文本、顺序及对应锚点完全相同，且每节有指向新对应章节的真实链接 | 已关闭；旧深链接可定位旧入口中的对应章节，再点击进入迁移原文 |
| embedding 资料包只有 URL/哈希，无法核对来源与实现说明 | 更新 JSON 提供 primary 短摘录、HF 数量/文件名摘要、PR 状态/范围及本地源码片段；文案与这些材料一致，检查边界明确 | 资料包内复核问题已关闭；没有将摘录提升为本审核独立联网或当前运行核验 |

### 1. 9 个文件已恢复 baseline 原始字节

| 文件 | 行号 | 比较结果 |
|---|---|---|
| `h3-shot-prompt/scripts/lint_prompt.py` | 1–282 | 字节及 SHA-256 相同，13,517 字节 |
| `h3-director-json-review/scripts/lint_json.py` | 1–92 | 字节及 SHA-256 相同，3,759 字节 |
| `h3-shot-prompt/references/cinematography.md` | 1–36 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/examples.md` | 1–275 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/official-calibration.md` | 1–89 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/official-format.md` | 1–153 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/troubleshooting.md` | 1–36 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/projects/yanwang.md` | 1–28 | 字节及 SHA-256 相同 |
| `h3-shot-prompt/references/projects/zhiyin.md` | 1–40 | 字节及 SHA-256 相同 |

因此，原有两个检查脚本、摄影底座、格式参考、范例、已有校准资料、故障表及项目卡没有正文或换行变化。

### 2. 旧路径与全部原标题锚点已保留

`h3-shot-prompt/references/powers-and-effects.md:1–25` 保留原 H1 和 5 个 H2，共 6 个标题；第 9、13、17、21、25 行分别链接新能力细则的对应章节。`h3-shot-prompt/references/official-powers-calibration.md:1–61` 保留原 H1、“阅读前先核对”“用例目录”和 12 个案例标题，共 15 个标题；第 9、13、17–61 行的各节链接指向新原文对应锚点。

两组标题的文本和顺序与 baseline 完全一致，因此旧章节/案例片段保留；这仍是兼容入口加人工点击跳转，不是 HTTP 自动重定向。两个入口第 3 行明确只保留路径与章节，不复制第二套规则或官方原文。

本轮扫描得到 **53 个本地 Markdown 路径/片段链接，全部有效，0 个断链或无效锚点**。另有 5 个外部 URL，本轮没有联网测试其访问状态。

### 3. embedding 摘录与文案一致，边界准确

`h3-power-fx/references/effects-embeddings.md:7–9` 的资源归属、文件数量与两个示例文件名，和更新证据包一致：

- `embedding_evidence.json:19–24` 提供 ComfyUI 文档短摘录，说明资源为社区成员 silveroxides 贡献的非官方资源，支持文案对原“MiniMax 自带”说法的纠正。
- JSON 第 25–32 行记录 HF 托管目录观察到 10 个效果文件，并列出 `minimaxh3_art_is_explosion.safetensors` 与 `minimaxh3_bullet_time.safetensors`；和文案第 7、9 行一致。
- JSON 第 33–38 行记录 PR 为 Merged、2026-08-18，以及 H3 tokenizer embedding 语法支持的范围；文案将 PR 用作支持范围核对材料，没有扩大成所有 H3 服务自动支持。
- JSON 第 40–85 行提供 H3 tokenizer 调用、通用 embedding 加载/切分逻辑和两个 H3 编码节点入口片段。各片段记录的 SHA-256 与该 JSON 顶部同路径哈希一致。片段支持“应核对实际解析入口、文件名、空白与日志”的检查方向；它们不是实际 tokenizer 执行或效果文件加载结果。
- JSON 第 87–88 行明确为可用已安装源码检查，未执行 tokenizer、未检查活动工作流、未加载效果文件，并记录源码重新检查日期。第 11–13 行仍为 `cloud_runtime_checked=false`、`downloads=0`、`render_jobs=0`；第 8–10 行仍只列出 embedding 占位文件。

`effects-embeddings.md:3,13–19` 继续要求用户提出效果文件需求后才读取，先检查实际解析路径、搜索目录及文件，按真实文件名使用，不把无报错当视觉有效，不承诺强度调节，不承诺云端可安装或可用。这些边界和证据包一致。

**本审核仅检查提供的摘录、观测摘要、源码片段与最终文案之间的一致性。** 没有独立打开原网站，没有从实际源码文件重新计算哈希，不能据此证明原站此刻内容、当前进程加载路径或真正编码结果。资料包中的 HF 数量与 PR 状态也是来源记录，不是本审核重新抓取的结果。

## 无新规则改写与迁移完整性

baseline 有 17 个文件，final 有 21 个文件；没有删除原有路径。相对 baseline：9 个原文件原始字节不变；8 个原路径有预期正文差异，其中 2 个为带完整标题的迁移入口，其余 6 个差异仍限定为 skill 职责/条件加载描述、真实引用链接或 embedding 纠错入口。未发现额外修改对白、摄影底座、合法时长、镜头数量表、原有 lint 或项目设定的内容。

直接提取并比较主 skill 的合法时长和镜头表（`h3-shot-prompt/SKILL.md:56–76`）、正文字数和对白预算（86–92）、台词和防串词规则（113–119）、写实默认层与静止例外（150–154），均与 baseline 全文一致。时间静止/集体定身例外仍见主 skill 第 101、153、173 行、表演参考第 36 行、导播审查第 58、80、123 行及新 skill 第 21 行，未引入要求被定住的人持续小动作的相反规则。

两个迁移后的正文仍与 baseline 原文件 **逐字节相同**：

| 迁移正文 | SHA-256 |
|---|---|
| `h3-power-fx/references/powers-and-effects.md:1–54` | `7de94d8bdb69071ec33935ea21814e093ea17754c50ec6f9d66740aba188302a` |
| `h3-power-fx/references/official-powers-calibration.md:1–220` | `13c489ba84b5f924a16f7b2d3db61eb874c08b76b9b0c52d5fee29211feceff1` |

12 例不重不漏，中文需求、英文原文、偏差说明和原有瑕疵全部保留。旧入口新增的仅为标题和链接，没有形成第二份可漂移的规则正文。

新 skill 仍有独立 name/description（`h3-power-fx/SKILL.md:1–4`），明确排除普通文戏、普通徒手打斗和只有古风服装/场景；第 8、12–15、23 行仍复用主 skill 与两个原脚本，第 27 行禁止只凭“仙侠”新增灵气、发光或古筝。主 skill 第 47 行和导播审查第 80 行仍只在“异能一打多”等有特效条件下加载配套细则。静态职责与误触发防护未改变，动态检索/触发仍不在本轮验证范围。

## 机械检查与安装判断

两个 Python 脚本通过内存语法编译。用 baseline 和 final 的原 lint 分别检查随包同一 12 个官方样本，全部 summary、ERROR、WARN 结果一致：12 例均为 0 ERROR，总计 3 WARN（`blast_xianxia` 1 个，`awaken_urban` 2 个）。`lint_json.py` 的默认依赖实际解析到 final 同组的 `h3-shot-prompt/scripts/lint_prompt.py`，未越出 skill 组。

**适合安装 `final-skills` 中的四个同级目录。** 此为静态完整性结论，本轮没有执行安装或平台重新发现。没有导入导播台、运行编码、检查云端、渲染、播放、听音或验收口型、物理和画质；原文保留和 lint 一致均不能代替这些验证。没有读取或重新验证写手/检索测试，未将它们写成独立审核证据。
