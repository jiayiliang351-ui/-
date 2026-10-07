# Codex 执行方案：异能 / 超能力用例的官方改写

目的：用官方 H3-Context-IR 接口改写 12 条异能用例（都市 6 条、古风仙侠 6 条），把结果存进仓库。分析、写对照版、出片对比由 Claude 做，Codex 只负责调接口、存结果、提交。

12 条用例在 `tools/context_ir/powers/cases.json`：

| id | 时长 | 内容 |
|---|---|---|
| blast_urban / blast_xianxia | 8 秒 | 能量波（掌心蓝光 / 指尖金色剑气）击中敌人 |
| telekinesis_urban / telekinesis_xianxia | 10 秒 | 隔空取物、念力（杯子浮起 / 竹叶悬浮），不用发光特效 |
| element_urban / element_xianxia | 8 秒 | 手上结冰 / 指间电弧，特写 |
| awaken_urban / awaken_xianxia | 10 秒 | 觉醒、突破：瞳孔微光、雨滴悬停 / 灵气旋转 |
| timestop_urban / timestop_xianxia | 15 秒 | 时间静止，一镜到底 |
| onevsmany_urban / onevsmany_xianxia | 15 秒 | 一打多爽片（念力 / 御剑），快剪 |

---

## 第一部分：用户先做（启动 Codex 之前）

1. **充值**：上次第一次调用报过 `insufficient balance (1008)`。这次要调 12 次，先在 MiniMax 开放平台（https://platform.minimax.io）确认余额够。
2. **设置环境变量**（和上次一样，密钥不要贴进任何聊天）：
   - Windows：系统设置 → 环境变量 → 用户变量，新建 `MINIMAX_API_KEY`（值是你的密钥）和 `MINIMAX_API_BASE`（值是 `https://api.minimax.io`）。设完关掉所有终端和 Codex 再重开。
   - macOS / Linux：在 `~/.zshrc` 或 `~/.bashrc` 里加 `export MINIMAX_API_KEY=...` 和 `export MINIMAX_API_BASE=https://api.minimax.io`，重开终端。
3. **Codex 要能联网**、能推送 GitHub（上次已经配好，不用再改）。
4. 在仓库根目录启动 Codex，把下面这句话发给它：

   > 严格按 `tools/context_ir/powers/CODEX_RUNBOOK_POWERS.md` 的第二部分逐步执行，从第 1 步开始，不跳步，遵守硬规则。

---

## 第二部分：给 Codex 的指令

### 硬规则（每一步都适用）

1. **分支**：只在 `codex/context-ir-powers` 分支上工作（第 1 步创建）。不推送到其他分支，不改写历史（不 rebase、不 force push），不建 PR。
2. **密钥**：绝不打印、记录、写入或提交 `MINIMAX_API_KEY` 的值。不运行会打印全部环境变量的命令（`env`、`set`、`printenv`、`Get-ChildItem Env:`）。检查密钥只用第 1 步给的命令。
3. **只能新建或修改这些文件**：`tools/context_ir/powers/results/` 下的文件、`tools/context_ir/powers/PROGRESS.md`。其余一律不碰：不改任何 `.py` 脚本、`cases.json`、`SKILL.md`、`references/`、`dist/`，也不改上一轮的 `tools/context_ir/results/`。
4. **不要自由发挥**：不写分析报告、不写修改建议、不自己写提示词、不改 skill。这些由 Claude 做。
5. **脚本报错时**：不改脚本。先查本文末尾的"故障处理"表；表里没有，或按表处理后还失败，就停下，把完整的错误原文写进 `PROGRESS.md` 的"阻塞"一栏，提交，告诉用户。
6. **每步完成后**：在 `PROGRESS.md` 把这一步打勾、写一行结果，然后提交：
   ```bash
   git add tools/context_ir/powers
   git commit -m "powers: step N <一句话结果>"
   ```

### 命令约定

- `PY` 指第 1 步确定的 Python 命令（`python`、`python3` 或 `py -3` 之一）。
- 所有命令都在**仓库根目录**运行，除非写了 `cd`。
- Windows PowerShell 每次新开终端先运行 `$env:PYTHONIOENCODING="utf-8"`；macOS / Linux 运行 `export PYTHONIOENCODING=utf-8`。

### 第 1 步：环境检查

1. 拉最新代码并建分支：
   ```bash
   git fetch origin claude/cloud-mode-status-19m8rv
   git checkout -b codex/context-ir-powers origin/claude/cloud-mode-status-19m8rv
   ```
   如果分支已存在：`git checkout codex/context-ir-powers`。
   **成功标准**：`tools/context_ir/powers/cases.json` 存在。
2. 确定 Python：依次试 `python --version`、`python3 --version`、`py -3 --version`，用第一个输出 `Python 3.8` 或更高版本的命令作为 `PY`。
3. 检查密钥和地址（只输出有没有，不输出密钥的值）：
   ```bash
   PY -c "import os; print('KEY OK' if os.environ.get('MINIMAX_API_KEY') else 'KEY MISSING'); print('BASE', os.environ.get('MINIMAX_API_BASE', '(not set)'))"
   ```
   - 输出 `KEY MISSING`：停下，告诉用户按第一部分第 2 条设置并重开终端。
   - `BASE` 不是 `https://api.minimax.io`：停下，告诉用户按第一部分第 2 条设置 `MINIMAX_API_BASE`。
4. 创建 `tools/context_ir/powers/PROGRESS.md`，内容照抄下面，然后提交（`powers: step 1 environment ok`）：
   ```markdown
   # 异能用例进度

   PY = （填第 1 步确定的命令）

   - [x] 第 1 步 环境检查：
   - [ ] 第 2 步 试跑一条：
   - [ ] 第 3 步 跑全部：
   - [ ] 第 4 步 检查结果：
   - [ ] 第 5 步 推送：

   ## 阻塞

   无
   ```

### 第 2 步：试跑一条

```bash
cd tools/context_ir
PY context_ir_batch.py powers/cases.json --out powers/results --only element_urban
cd ../..
```
- **成功标准**：输出一行 `ok   element_urban: N words, tokens=M`，并且 `tools/context_ir/powers/results/element_urban.prompt.txt` 存在，第一行以 `integrated_multimodal_description:` 开头。
- 在 `PROGRESS.md` 记下 tokens 数。
- 失败：查"故障处理"表。**这一步不成功就不要做第 3 步。**
- 提交：`powers: step 2 first call ok`

### 第 3 步：跑全部

```bash
cd tools/context_ir
PY context_ir_batch.py powers/cases.json --out powers/results
cd ../..
```
- 已经跑过的会自动跳过。某条失败时脚本会继续跑下一条。全部跑完后，如果有失败的，对它们再运行一次同样的命令（只重试一次）。
- **成功标准**：`tools/context_ir/powers/results/` 里有 12 个 `.prompt.txt` 和 12 个 `.json`。仍有失败的，把用例 id 和错误原文记进 `PROGRESS.md`，继续往下做。
- 提交：`powers: step 3 N of 12 rewrites collected`

### 第 4 步：检查结果

1. 数文件：
   ```bash
   PY -c "import glob; fs=sorted(glob.glob('tools/context_ir/powers/results/*.prompt.txt')); print(len(fs)); [print(f) for f in fs]"
   ```
2. 确认密钥没有被写进任何文件（只输出结论，不输出密钥）：
   ```bash
   PY -c "import os,glob; k=os.environ['MINIMAX_API_KEY']; bad=[f for f in glob.glob('tools/context_ir/powers/**/*', recursive=True) if os.path.isfile(f) and k in open(f, encoding='utf-8', errors='ignore').read()]; print('LEAK: ' + ', '.join(bad) if bad else 'NO KEY IN FILES')"
   ```
   **成功标准**：输出 `NO KEY IN FILES`。如果输出 `LEAK`：**不要提交**，删掉列出的文件，在 `PROGRESS.md` 阻塞栏写"密钥出现在结果文件里，已删除"，停下告诉用户。
3. 提交：`powers: step 4 results checked`

### 第 5 步：推送

```bash
git push -u origin codex/context-ir-powers
```
- 推送失败（网络错误）：等 10 秒重试，最多 3 次。权限错误：停下，告诉用户检查 GitHub 登录。
- 在 `PROGRESS.md` 第 5 步写上分支地址 `https://github.com/jiayiliang351-ui/-/tree/codex/context-ir-powers`，提交并再推送一次。
- 最后告诉用户：拿到了几条（N/12）、失败了哪几条、分支名 `codex/context-ir-powers`，请用户把这些转告 Claude。

---

## 故障处理

| 现象 | 处理 |
|---|---|
| `MINIMAX_API_KEY is not set` | 停下，让用户设置密钥并重开终端 |
| `HTTP 401` 或 `HTTP 403` | 密钥错误、过期或没有 H3 权限；也可能是地址不对。确认 `BASE` 是 `https://api.minimax.io`。仍失败就停下，告诉用户检查密钥 |
| `HTTP 402` / `insufficient balance (1008)` | 余额不足。停下，告诉用户充值，充值后从失败的那一步重跑（已完成的会自动跳过） |
| `HTTP 429` | 频率限制。等 60 秒，用同样命令重跑一次 |
| `URLError`、`timed out`、`CONNECT tunnel failed`、`Name or service not known` | 网络不通。确认 Codex 能联网；等 30 秒重跑一次，仍失败就停下 |
| `SSL: CERTIFICATE_VERIFY_FAILED` | 公司网络或代理拦截证书。告诉用户设置 `SSL_CERT_FILE` 指向本机证书文件；不要关闭证书校验 |
| `task failed` / `still running after 600s` | 记录这条，继续下一条；第 3 步结束后只重试一次 |
| `no task_id in response` | 把错误原文记进阻塞栏，停下（接口可能改了） |
| `UnicodeEncodeError` / 中文乱码 | 先运行命令约定里的 `PYTHONIOENCODING` 设置，再重跑 |
| `git checkout -b` 报分支已存在 | 用 `git checkout codex/context-ir-powers` |
| `git push` 被拒绝（权限） | 停下，告诉用户检查 GitHub 登录和仓库权限 |
