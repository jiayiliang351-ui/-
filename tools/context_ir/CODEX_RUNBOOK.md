# Codex 执行方案：H3 官方改写校准

这份方案分两部分：**第一部分是用户在启动 Codex 之前要做的事**；**第二部分是给 Codex 的逐步指令**。Codex 从第二部分的第 1 步开始，按顺序执行，不跳步、不自由发挥。

---

## 第一部分：用户先做（启动 Codex 之前）

1. **拉代码**（在你自己电脑上）：
   ```bash
   git clone https://github.com/jiayiliang351-ui/-.git h3-calibration
   cd h3-calibration
   git checkout claude/cloud-mode-status-19m8rv
   ```
2. **设置 API Key**（不要写进任何文件，不要贴进 Codex 的对话框）：
   - Windows PowerShell：`setx MINIMAX_API_KEY "你的key"`，然后**关掉终端重新打开**。
   - macOS / Linux：`export MINIMAX_API_KEY="你的key"`（写进 `~/.zshrc` 或 `~/.bashrc` 可以长期生效）。
   - 用海外站的 Key 时，再设一个 `MINIMAX_API_BASE=https://api.minimax.io`；国内站不用设。
3. **让 Codex 能联网**：Codex CLI 默认的沙箱不让命令联网。二选一：
   - 在 `~/.codex/config.toml` 里加：
     ```toml
     [sandbox_workspace_write]
     network_access = true
     ```
   - 或者 Codex 跑 `context_ir_batch.py` 被拦时，选择允许这条命令在沙箱外运行。
   - 用 Codex 网页版（云端）也行，但它的环境默认不联网、也没有你的 Key，要在它的环境设置里打开网络并添加密钥。推荐用本地 CLI。
4. **决定要不要改写真实项目**（第 10 步，可选，额外花钱）。要的话，把下面两行改好再启动 Codex：
   - `PROJECT_JSON =`（你的导播台 JSON 的完整路径，例如 `D:/剧集/阎王打工记/EP02_导播台.json`；不做就留空）
   - `REAL_LIMIT = 0`（最多改写多少段；0 表示跳过第 10 步。先填 5 试试，看 token 用量再加）
5. **启动 Codex**：在仓库根目录运行 `codex`，然后发这一句：
   > 按 tools/context_ir/CODEX_RUNBOOK.md 第二部分执行，从第 1 步开始，严格按步骤做，每步完成后更新 tools/context_ir/PROGRESS.md 并提交。

预计花费：第 4 步共 8 次接口调用，每次是纯文字改写（官方示例约 5000 token 一次）。第 10 步按段数另算。

---

## 第二部分：给 Codex 的指令

### 硬规则（每一步都适用）

1. **分支**：只在 `codex/context-ir-calibration` 分支上工作（第 1 步创建）。不要推送到其他分支，不要改写历史（不 rebase、不 force push）。
2. **密钥**：绝不打印、记录、写入或提交 `MINIMAX_API_KEY` 的值。不要运行会打印全部环境变量的命令（`env`、`set`、`Get-ChildItem Env:`）。检查密钥只用第 1 步给的命令。
3. **允许改动的文件**（只能改这些，其余一律不碰）：
   - 新建或修改：`tools/context_ir/results/`、`tools/context_ir/analysis/`、`tools/context_ir/codex_versions/`、`tools/context_ir/ir_cache/`、`tools/context_ir/project_rewrites/`、`tools/context_ir/render_compare.json`、`tools/context_ir/PROGRESS.md`
   - 只通过脚本修改：`h3-shot-prompt/references/official-calibration.md`（第 8 步的 `append_calibration.py`）
   - **不要改**任何 `.py` 脚本、`SKILL.md`、`references/` 下的其他文件、`cases.json`、`skill_versions/`、`old_versions/`、`templates/`。
4. **脚本报错时**：不要改脚本。先查本文末尾的"故障处理"表；表里没有，或按表处理后还失败，就停下来，把完整的错误原文写进 `PROGRESS.md` 的"阻塞"一栏，提交，然后告诉用户。
5. **不要自由发挥**：报告只填模板要求的内容；对 skill 的修改意见只写进 `PROPOSALS.md`，不直接改 skill。
6. **每步完成后**：在 `PROGRESS.md` 把这一步打勾、写一行结果，然后提交：
   ```bash
   git add -A tools/context_ir h3-shot-prompt/references/official-calibration.md
   git commit -m "calibration: step N <一句话结果>"
   ```

### 命令约定

- 下文的 `PY` 指第 1 步确定的 Python 命令（`python`、`python3` 或 `py -3` 之一）。
- 所有命令都在**仓库根目录**运行，除非写了 `cd`。
- Windows PowerShell 下，每次新开终端先运行 `$env:PYTHONIOENCODING="utf-8"`；macOS/Linux 运行 `export PYTHONIOENCODING=utf-8`。

---

### 第 1 步：环境检查

1. 创建分支：
   ```bash
   git checkout claude/cloud-mode-status-19m8rv
   git checkout -b codex/context-ir-calibration
   ```
   如果分支已存在：`git checkout codex/context-ir-calibration`。
2. 确定 Python：依次试 `python --version`、`python3 --version`、`py -3 --version`，用第一个输出 `Python 3.8` 或更高版本的命令作为 `PY`。都不行就停下，告诉用户安装 Python 3。
3. 检查密钥（只输出有没有，不输出值）：
   ```bash
   PY -c "import os; print('KEY OK' if os.environ.get('MINIMAX_API_KEY') else 'KEY MISSING')"
   ```
   输出 `KEY MISSING` 就停下，告诉用户按第一部分第 2 条设置并重开终端。
4. 检查脚本能跑：
   ```bash
   PY h3-shot-prompt/scripts/lint_prompt.py tools/context_ir/skill_versions/tea_pour.txt --seconds 8
   ```
   **成功标准**：输出里有 `OK`。
5. 创建 `tools/context_ir/PROGRESS.md`，内容照抄下面，然后提交（`calibration: step 1 environment ok`）：
   ```markdown
   # 校准进度

   PY = （填第 1 步确定的命令）

   - [x] 第 1 步 环境检查：
   - [ ] 第 2 步 Codex 按 skill 写 8 条：
   - [ ] 第 3 步 试跑一条接口：
   - [ ] 第 4 步 跑全部接口：
   - [ ] 第 5 步 自动分析：
   - [ ] 第 6 步 对比报告 REPORT.md：
   - [ ] 第 7 步 修改建议 PROPOSALS.md：
   - [ ] 第 8 步 写入 official-calibration.md：
   - [ ] 第 9 步 出片对照 JSON：
   - [ ] 第 10 步 真实项目改写（可选）：
   - [ ] 第 11 步 收尾：

   ## 阻塞

   （没有就写"无"）
   ```

### 第 2 步：Codex 按 skill 写 8 条（必须在调接口之前做）

完整执行 `tools/context_ir/templates/CODEX_WRITING_TASK.md` 里的任务。
- **必须在第 3 步之前完成**，这时 `results/` 还不存在，保证写的时候看不到官方答案。
- **成功标准**：`tools/context_ir/codex_versions/` 里有 8 个 `.txt` 文件，文件名和 `cases.json` 的 `id` 一一对应；`analysis/SKILL_CLARITY.md` 已写。
- 提交：`calibration: step 2 codex versions written`

### 第 3 步：试跑一条接口

```bash
cd tools/context_ir
PY context_ir_batch.py cases.json --out results --only tea_pour
cd ../..
```
- **成功标准**：输出 `ok   tea_pour: N words, tokens=M`，且 `tools/context_ir/results/tea_pour.prompt.txt` 存在。打开它，确认第一行以 `integrated_multimodal_description:` 开头。
- 在 `PROGRESS.md` 记下 tokens 数。
- 失败：查"故障处理"表。
- 提交：`calibration: step 3 first call ok`

### 第 4 步：跑全部接口

```bash
cd tools/context_ir
PY context_ir_batch.py cases.json --out results
cd ../..
```
- 已经跑过的会自动跳过。某条失败时脚本会继续跑下一条；全部跑完后，对失败的那几条再运行一次同样的命令（只重试一次）。
- **成功标准**：`results/` 里有 8 个 `.prompt.txt`。仍有失败的，把用例 id 和错误原文记进 `PROGRESS.md`，继续往下做（后面的步骤会跳过缺失的用例）。
- 提交：`calibration: step 4 N of 8 rewrites collected`

### 第 5 步：自动分析

```bash
cd tools/context_ir
PY analyze_ir.py --cases cases.json --results results --skill skill_versions --codex codex_versions --out analysis
cd ../..
```
- **成功标准**：`analysis/` 里有 `features.md`、`features.csv`、`lint.md`、`dialogue_check.md`、`sentences.md`、`phrases.md` 和 `side_by_side/` 目录（8 个文件）。
- 提交：`calibration: step 5 analysis generated`

### 第 6 步：对比报告

1. 复制模板：把 `tools/context_ir/templates/REPORT_TEMPLATE.md` 复制为 `tools/context_ir/analysis/REPORT.md`。
2. 按模板顶部的"填写规则"逐条填写。8 条用例每条一节（把"用例：<id>"那一节复制 8 份）。
3. 数据来源：数字从 `analysis/features.md` 抄；原句从 `analysis/side_by_side/<id>.md` 和 `analysis/sentences.md` 原样复制；台词状态从 `analysis/dialogue_check.md` 抄。
4. 最后填"跨用例统计"表和"平均值对比"表。
- **成功标准**：没有留空的格子（没有就写"无"）；跨用例统计表 16 行都填了，最后一列是数字。
- 提交：`calibration: step 6 report written`

### 第 7 步：修改建议

1. 复制 `tools/context_ir/templates/PROPOSALS_TEMPLATE.md` 为 `tools/context_ir/analysis/PROPOSALS.md`。
2. 严格按模板的触发条件提建议：只看 `REPORT.md` 跨用例统计表最后一列。
3. 填"官方改写在 lint_prompt.py 上报的问题"表（从 `analysis/lint.md` 里只抄 official 的条目）。
- **不要修改任何 skill 文件。**
- 提交：`calibration: step 7 proposals written`

### 第 8 步：写入 official-calibration.md

```bash
cd tools/context_ir
PY append_calibration.py
cd ../..
```
- **成功标准**：输出 `wrote N cases into ...official-calibration.md`，N 等于第 4 步拿到的条数。
- 提交：`calibration: step 8 official rewrites added to skill reference`

### 第 9 步：出片对照 JSON

```bash
cd tools/context_ir
PY build_render_json.py --out render_compare.json
cd ../..
```
- **成功标准**：输出最后一行 `wrote ...render_compare.json: N shots, about S seconds of video to render`。把这一行抄进 `PROGRESS.md`。
- 这份 JSON 由用户导入 V7.3 导播台渲染，Codex 不渲染。全部版本 × 2 个种子大约要渲染 400 秒视频；用户只想先看几条时，用 `--cases-only zhiyin_ep1_06 linqi_04 couple_split` 或 `--versions skill official` 缩小范围。
- 提交：`calibration: step 9 render comparison json built`

### 第 10 步：真实项目改写（可选）

只有第一部分第 4 条里 `PROJECT_JSON` 不为空、且 `REAL_LIMIT` 大于 0 时才做；否则在 `PROGRESS.md` 写"跳过"，直接进第 11 步。

```bash
cd tools/context_ir
PY rewrite_director_json.py "<PROJECT_JSON>" --limit <REAL_LIMIT> --out-dir project_rewrites
cd ../..
```
（`project_rewrites` 目录不存在时先创建。）
- **成功标准**：`project_rewrites/` 里出现 `<项目名>_官方改写.json` 和 `<项目名>_官方改写_log.md`。
- 打开 log，把"台词"列里写着"有变化，需人工核对"的段号抄进 `PROGRESS.md`。
- 挂了素材的段会被跳过、保持原样，这是正常的。
- 提交：`calibration: step 10 project rewrite N shots`

### 第 11 步：收尾

1. 推送：
   ```bash
   git push -u origin codex/context-ir-calibration
   ```
   网络错误时等 5 秒重试，最多 4 次。
2. 在 `PROGRESS.md` 末尾写"交付清单"，列出这些文件是否存在：
   - `tools/context_ir/analysis/REPORT.md`
   - `tools/context_ir/analysis/PROPOSALS.md`
   - `tools/context_ir/analysis/SKILL_CLARITY.md`
   - `tools/context_ir/analysis/features.md`
   - `tools/context_ir/results/`（几个文件）
   - `tools/context_ir/render_compare.json`
   - `tools/context_ir/project_rewrites/`（如做了第 10 步）
3. 提交并再推送一次：`calibration: step 11 done`
4. 告诉用户："校准完成，分支 codex/context-ir-calibration 已推送。请把这个分支交给 Claude 审核 PROPOSALS.md 并更新 skill；render_compare.json 可以导入导播台渲染对比。"

---

## 故障处理

| 现象 | 处理 |
|---|---|
| `MINIMAX_API_KEY is not set` | 停下，让用户设置密钥并重开终端 |
| `HTTP 401` 或 `HTTP 403`（带 JSON 错误信息） | 密钥错误、过期或没有开通 H3 权限。停下，告诉用户检查 MiniMax 开放平台的密钥和权限 |
| `HTTP 429` | 频率限制。等 60 秒，用同样命令重跑一次（已完成的会跳过） |
| `URLError`、`timed out`、`CONNECT tunnel failed`、`Name or service not known` | 网络不通。确认第一部分第 3 条（Codex 联网）已做；国内 Key 用默认地址，海外 Key 设 `MINIMAX_API_BASE=https://api.minimax.io` |
| `SSL: CERTIFICATE_VERIFY_FAILED` | 公司网络或代理拦截证书。告诉用户设置 `SSL_CERT_FILE` 指向本机的证书文件，不要关闭证书校验 |
| `task failed` / `still running after 600s` | 记录这条，继续下一条；第 4 步结束后只重试一次 |
| `no task_id in response` | 把错误原文记进 PROGRESS.md 阻塞栏，停下（接口可能改了） |
| `UnicodeEncodeError` / 中文乱码 | 先运行命令约定里的 `PYTHONIOENCODING` 设置，再重跑 |
| `python` 找不到 | 用 `python3` 或 `py -3` |
| `lint_prompt.py not found` | 确认在仓库根目录、分支正确，`h3-shot-prompt/scripts/lint_prompt.py` 存在 |
| `git push` 被拒绝（权限） | 停下，告诉用户检查 GitHub 登录和仓库权限 |
