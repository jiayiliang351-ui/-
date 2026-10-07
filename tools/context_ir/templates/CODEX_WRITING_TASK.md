# 写作任务：按 h3-shot-prompt skill 写 8 条提示词

目的：测试 skill 写得够不够清楚——换一个执行者照着写，能不能写出合格的提示词。

## 规则

1. 先完整读这些文件，读完再写：
   - `h3-shot-prompt/SKILL.md`
   - `h3-shot-prompt/references/official-format.md`
   - `h3-shot-prompt/references/physics-and-action.md`
   - `h3-shot-prompt/references/performance-and-dialogue.md`
   - `h3-shot-prompt/references/cinematography.md`
   - `h3-shot-prompt/references/examples.md` 的第 1 节（官方示例）
   - 写《纸引》的用例时读 `h3-shot-prompt/references/projects/zhiyin.md`；写《阎王打工记》的用例时读 `h3-shot-prompt/references/projects/yanwang.md`
2. **不要看** `tools/context_ir/skill_versions/`、`tools/context_ir/results/`、`tools/context_ir/analysis/` 里的任何文件，也不要看 `h3-shot-prompt/references/official-calibration.md`。看了这个测试就没有意义了。
3. 对 `tools/context_ir/cases.json` 里的每一条：
   - 读 `text`（中文简报）和 `duration`。
   - 按 skill 写一条 T2VA 提示词（三段式：`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`）。
   - 台词逐字照抄简报里引号中的内容。
   - 保存到 `tools/context_ir/codex_versions/<id>.txt`，UTF-8 编码，只放提示词本身，不加任何说明。
4. 每写完一条，运行：
   ```
   python h3-shot-prompt/scripts/lint_prompt.py tools/context_ir/codex_versions/<id>.txt --seconds <duration>
   ```
   有 ERROR 就改到没有 ERROR 为止（最多改 3 次）。3 次后还有 ERROR，保留文件，在 `PROGRESS.md` 记下剩余的 ERROR 原文。
5. 8 条写完后，在 `PROGRESS.md` 记一张表：用例 id、改了几次才过 lint、最后剩几个 WARN。
6. 另外写一段（5 条以内）：照 skill 写的时候，哪些规则看不懂、哪些规则互相矛盾、哪里不知道该怎么办。每条指出是 skill 的哪个文件哪一句。写进 `tools/context_ir/analysis/SKILL_CLARITY.md`。
