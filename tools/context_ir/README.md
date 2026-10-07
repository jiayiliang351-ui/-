# 官方 Context-IR 校准

用官方 H3-Context-IR 接口把一句话需求改写成官方版提示词，作为"标准答案"来校准 `h3-shot-prompt`。

## 准备

1. MiniMax 开放平台的 API Key，放进环境变量 `MINIMAX_API_KEY`（不要写进文件、不要贴到聊天里）。
2. 能访问 `api.minimaxi.com`（国内）或 `api.minimax.io`（海外，用 `--base https://api.minimax.io`）。
3. Python 3，不需要装别的包。

## 跑

```bash
cd tools/context_ir
python3 context_ir_batch.py cases.json --out results/
# 只跑几条
python3 context_ir_batch.py cases.json --out results/ --only zhiyin_ep1_06 linqi_04
```

每条生成两个文件：`results/<id>.prompt.txt`（改写后的提示词，可以直接喂本地 H3-Base）和 `results/<id>.json`（完整返回，含 token 用量）。已经跑过的会跳过，加 `--force` 重跑。

## 测试用例（cases.json）

全部是纯文字（T2VA），一句话需求的写法和在海螺上随手输入差不多：

| id | 时长 | 测什么 |
|---|---|---|
| `zhiyin_ep1_06` | 8 | 纸扎动作戏、接触、状态（尾火） |
| `linqi_04` | 15 | 活人感、画外台词、6 个节拍 |
| `yanwang_ep02` | 10 | 单声源台词、法力只拍物理后果 |
| `couple_split` | 15 | 三句对白、走位、弧形绕拍 |
| `quiet_shen_fire` | 10 | 一镜到底安静戏、触发 → 反应 → 余波 |
| `office_two_speakers` | 10 | 两人轮流说话（看官方怎么防串词） |
| `wrist_grab` | 8 | 两人肢体接触的物理 |
| `tea_pour` | 8 | 手部和道具、液体 |

前四条和 `h3-shot-prompt` 的 `examples.md` 里已有的段对应，可以三方对比：旧写法 / skill 新写法 / 官方改写。

## 跑完之后

1. 把 `results/` 提交到仓库（或发给 Claude），让它逐句对比官方改写和 skill 写法，把规律写回 skill。
2. 挑两三条官方改写，在本地 H3-Base 上和 skill 版本同种子各跑一次，看出片差距。
3. 官方改写可能补了你没要的细节、或者改了台词；台词以原文为准。
