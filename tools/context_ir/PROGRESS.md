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
- [ ] 第 9 步 出片对照 JSON：
- [ ] 第 10 步 真实项目改写（可选）：
- [ ] 第 11 步 收尾：

## 阻塞

当前无；国内站新密钥已于 2026-10-07 成功完成 tea_pour，以下为历史故障记录。

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

当前阻塞以本次海外接口响应为准：余额不足。先前国内接口 401 不应作为海外密钥无效的结论。未获得 task_id，未进行批量请求，校准仍未完成。需用户确认 H3-Context-IR 所用的计费余额、资源包或套餐权益；未执行充值或购买。

官方来源：
- https://github.com/MiniMax-AI/MiniMax-H3/blob/main/README.md
- https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir
- https://platform.minimax.io/protocol/paid-agreement （标准按量 API Key 与 Token Plan 订阅 Key 分开且不可互换，具体权益以服务页面为准。）
