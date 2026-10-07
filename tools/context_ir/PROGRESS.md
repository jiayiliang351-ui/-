# 校准进度

PY = python

- [x] 第 1 步 环境检查：Python 3.14.5；临时密钥 KEY OK；基础 lint OK；results 尚不存在。
- [x] 第 2 步 Codex 按 skill 写 8 条：8 个文件首次 lint OK，全部原句台词由脚本核对一致，官方接口尚未调用。
- [x] 第 3 步 试跑一条接口：国内站新密钥成功；tea_pour 290 words，tokens=8173；第一行 integrated_multimodal_description: 已确认。
- [x] 第 4 步 跑全部接口：8 / 8 成功，合计 68562 tokens；tea_pour 已自动跳过，未重复调用。
- [x] 第 5 步 自动分析：24 rows，官方无缺失；6 项统计文件及 8 项逐镜并排文件已确认。
- [x] 第 6 步 对比报告 REPORT.md：8 条完整填写；16 行跨用例统计核对；328 次英文原句引用由脚本验证来源完全一致，无空格或占位格。
- [x] 第 7 步 修改建议 PROPOSALS.md：仅 C=0、D=1 两项满足规则冲突门槛，各附 3 个官方用例原句；官方 lint 的 1 条 WARN 已原样复制；未改 skill。
- [x] 第 8 步 写入 official-calibration.md：append_calibration.py 写入 8 cases；8 条原文逐字核对，标记前内容除脚本设计的状态行外未变。
- [x] 第 9 步 出片对照 JSON：54 shots，580 秒；同种子、提示词逐字、独立无素材/接力、schemaVersion=5 的静态检查通过。尚未导入或渲染。
- [x] 第 10 步 真实项目改写（可选）：跳过；PROJECT_JSON 未指定，REAL_LIMIT=0，未调用额外接口。
- [ ] 第 11 步 收尾：交付文件已核验并本地提交；git push 因 GitHub 未登录失败，尚未推送。

## 阻塞

当前阻塞：第 11 步 GitHub 本机凭据缺失，无法推送。接口阻塞已解除，8 条结果全部取得；以下为历史接口故障记录。

2026-10-07：第 3 步真实接口认证失败。未重试、未调用其余 7 条、未修改脚本或 skill。需要本机环境中可用于目标 H3 接口的 MiniMax 开放平台密钥；如果使用海外站密钥，还需确认 API 基址。已完成第 1、2 步，保留独立写作结果。第 4–11 步未执行，校准未完成，分支尚未推送。

错误原文：

```text
run  tea_pour (8s) ...
FAIL tea_pour: HTTP 401 from https://api.minimaxi.com/v2/h3_context_ir: {"type":"error","error":{"type":"authorized_error","message":"invalid api key (2049)","http_code":"401"},"request_id":"0714fb1e85d2520ab40d2b6247d4fbd6"}
```

本机 Git 未配置作者身份，本轮仅对提交命令临时指定 Codex <codex@openai.com>，没有修改全局或仓库 Git 配置。密钥仅进入调用进程环境，没有写入仓库或持久化环境变量。

## 第 2 步 lint 记录

| 用例 id | 修改次数 | 最后 WARN 数 |
|---|---:|---:|
| zhiyin_ep1_06 | 0 | 0 |
| linqi_04 | 0 | 0 |
| yanwang_ep02 | 0 | 0 |
| couple_split | 0 | 0 |
| quiet_shen_fire | 0 | 0 |
| office_two_speakers | 0 | 0 |
| wrist_grab | 0 | 0 |
| tea_pour | 0 | 0 |

## 海外站确认后的第 3 步重试

用户确认密钥来源：https://platform.minimax.io/console/plan 。官方 H3 README 及接口文档确认海外基址为 https://api.minimax.io 。仅用 --base 参数更正地址，没有修改脚本。

```text
run  tea_pour (8s) ...
FAIL tea_pour: HTTP 402 from https://api.minimax.io/v2/h3_context_ir: {"type":"error","error":{"type":"insufficient_balance_error","message":"insufficient balance (1008)","http_code":"402"},"request_id":"0714fe18ba0c76b34a378dd6ac6898b0"}
```

历史阻塞（现已解除）：当时海外接口响应为余额不足。先前国内接口 401 不应作为海外密钥无效的结论。未获得 task_id，未进行批量请求，校准仍未完成。需用户确认 H3-Context-IR 所用的计费余额、资源包或套餐权益；未执行充值或购买。

官方来源：
- https://github.com/MiniMax-AI/MiniMax-H3/blob/main/README.md
- https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir
- https://platform.minimax.io/protocol/paid-agreement （标准按量 API Key 与 Token Plan 订阅 Key 分开且不可互换，具体权益以服务页面为准。）

第 9 步脚本输出末行：

```text
wrote C:\Users\Administrator\Videos\提示词参考视频\h3-calibration\tools\context_ir\render_compare.json: 54 shots, about 580 seconds of video to render
```

仅 3 条用例有 old_versions，其他 5 条只有 skill/codex/official；脚本按实际可用版本生成，未补造旧版本。实际总量为 580 秒，区别于方案预估约 400 秒。

## 第 11 步推送阻塞

已执行 git push -u origin codex/context-ir-calibration。本机凭据管理器一直等待；结束该次凭据读取后返回：

```text
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

本机未获得 GitHub 登录凭据；不是网络错误，按方案不做网络重试。需要用户完成 GitHub 登录后再运行相同推送命令。校准文件已经本地提交，远端分支未确认建立；未创建 PR、未合并、未改写历史。

## 交付清单

- [x] tools/context_ir/analysis/REPORT.md：8 个用例、16 行跨用例统计、11 项平均值。
- [x] tools/context_ir/analysis/PROPOSALS.md：2 条待审核建议，未直接修改 skill。
- [x] tools/context_ir/analysis/SKILL_CLARITY.md：5 条清晰度反馈。
- [x] tools/context_ir/analysis/features.md：24 条数据记录。
- [x] tools/context_ir/results/：16 个文件（8 个 .prompt.txt + 8 个 .json）；68,562 tokens。
- [x] tools/context_ir/render_compare.json：54 段，约 580 秒；2 个同种子，尚未导入或渲染。
- [x] h3-shot-prompt/references/official-calibration.md：按原脚本写入 8 条官方原文。
- [x] tools/context_ir/codex_versions/：8 条独立写作版本，调用接口前提交，全部 lint OK。
- [x] tools/context_ir/analysis/REPORT_EVIDENCE.json、REPORT_QUOTE_CHECK.json：抽取位置与 328 次英文原句来源核对记录。
- [x] tools/context_ir/project_rewrites/：不适用，未指定真实项目，按方案跳过。
- [ ] origin/codex/context-ir-calibration：GitHub 登录阻塞，尚未推送。

最终范围核对：46 个改动文件均在允许清单内；所有 .py、SKILL.md、其他规则文件、cases.json、templates、skill_versions、old_versions 保持原样；提交内容未检出密钥字符串。未执行视频生成，文本/API/JSON 验证不代表导播台导入或成片效果验收。
