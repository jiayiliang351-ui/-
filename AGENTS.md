# 给 AI 编程助手的说明

本仓库存放 MiniMax H3 本地视频生成用的提示词 skill（`h3-shot-prompt`、`h3-action-prompt-design`、`h3-director-json-review`、异能配套 `h3-power-fx`）和校准工具（`tools/context_ir/`）。

## 如果你被要求执行"校准"或"调用学习"

严格按 `tools/context_ir/CODEX_RUNBOOK.md` 的第二部分逐步执行，从第 1 步开始，不跳步，遵守其中的硬规则。

## 如果你被要求跑"异能用例"或"超能力用例"

严格按 `tools/context_ir/powers/CODEX_RUNBOOK_POWERS.md` 的第二部分逐步执行，从第 1 步开始，不跳步，遵守其中的硬规则。

## 通用规则

- 不打印、不写入、不提交任何 API Key 或密钥；不运行打印全部环境变量的命令。
- 不修改 `h3-shot-prompt/SKILL.md`、`h3-shot-prompt/references/` 下的规则文件和任何 `.py` 脚本，除非用户明确要求修改那个具体文件。
- 提示词（发给视频模型的文本）用英文写；台词和画面文字保留原语言。
- 写或检查提示词后，运行 `python h3-shot-prompt/scripts/lint_prompt.py <文件> --seconds <秒数>`。
- 和用户交流用中文。
