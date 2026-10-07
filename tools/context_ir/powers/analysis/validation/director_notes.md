# 导播台 JSON 实际审查记录

## 范围与证据边界

- 输入：`director_input.json`；原需求对照：`cases.json` 中的 `timestop_xianxia` 与 `telekinesis_xianxia`。
- 使用候选 `h3-director-json-review`，并按需读取同包单段、补充手册、格式、电影感底座、示例、物理及异能规则。
- 未读取 baseline/candidate 生成输出，未读取 `official-powers-calibration.md` 或 `official-calibration.md` 原文；未调用 API、未渲染、未修改 skill/脚本/仓库。
- 只生成 `director_reviewed.json` 和本说明。原输入 SHA256：`49a6287ff52f1ed019f2f57bb27f9bfbb0193bc34d338810e11776ce5df1daeb`。

## 规划与简报核对

| 段落 | 因果链及戏剧作用 | 空间、人数、手与道具 | 类型与接力 |
|---|---|---|---|
| timestop_xianxia | 箭雨将落向男孩 → 女侠抬左手定住时间、右手拨箭并抱走男孩 → 放左手恢复，箭钉入空地；兑现定时救人的能力 | 屋顶画右上、男孩街心、女侠从画左进入、安置于画左街边台阶；女侠和一个男孩，加原需求未定数量的路人；左手维持定时，右手先拨箭后抱人，背后长剑保持在鞘 | 连续移动与操作，一镜到底；`latentRelay=false`，不与下一段串接 |
| telekinesis_xianxia | 抬两指 → 枯竹叶升至膝高悬转 → 指向画右院门，叶流与风把门吹开；能力由物体运动表现 | 老道画中偏左、门画右；仅一名老道，左手背后、右手两指施力；门向外朝画右开至半开，竹叶向右通过门口 | 单一念力变化链，一镜；`latentRelay=false` |

两段均无台词、素材或声线参考，无需声线编号和六段式；使用 T2VA 三段式。未给路人、羽箭添加硬数量。两段时长、种子、id、模式、未知字段均保留。

## 问题与改动

| 问题 | 段落 | 实际改动 |
|---|---|---|
| 全员持续小动作的固定表演段与时间静止直接冲突 | timestop_xianxia | 精确删除该段固定文字及一句重复人数介绍；保留路人奔跑中冻结，明确男孩保持摔倒姿态、女侠独自行走操作；保留原来的左手维持及右手操作链 |
| 拨偏箭的恢复落点未与新角度逐一对应 | timestop_xianxia | 改写恢复句：被拨偏的一支落在画右空街，其余落在已腾空的街心，保留“所有箭钉进空地” |
| 单镜头描述过短，手的占用和风向需要更清楚 | telekinesis_xianxia | 按 skill 补齐既有电影感底座与竹林日光；明确左手背后、右手两指操作；细化已有的颤动、升高、悬转、向右叶流、木门受力和半开落定，没有新增能力 |
| 原声音结尾的“剩余竹叶落地”与全部叶流穿门的画面衔接不清 | telekinesis_xianxia | 声音改为竹叶通过门槛的窸窣，门轴声随叶流接触和半开减速绑定；不另加光环、光束或发光材质 |

时间静止段保留一个 `[Shot 1]`、无切镜句，镜头通过跟拍和接近手部串起救人。仙侠简报没有“静止期间只有脚步声”的都市版声音限制，因此保留输入的衣料声，不把都市限制套进来。两段 `non_diegetic_music: N/A`，`negativePrompt` 继续为空。未添加对白。

## 校验

输入 lint：两段 0 ERROR；念力段出现正文 134 词、描述偏短的 1 条 WARN。

最终执行：

```text
python candidate-skills/h3-director-json-review/scripts/lint_json.py director_reviewed.json

timestop_xianxia   mode=T2VA  shots=1  real_duration=15.083s  words=422  spoken_zh=0  err=0 warn=0
telekinesis_xianxia mode=T2VA shots=1  real_duration=10.125s  words=345  spoken_zh=0  err=0 warn=0
2 shots checked, 0 with errors
```

正文词数包含固定摄影底座和场景光源；按 skill 排除两者后，两段分别300/220 词，落在单镜头 150–300 词预算内。逐段检查三段顺序、最后只留既有动作余波、手占用和因果均已完成。JSON 深度比较时剥离 `shots[].prompt/negativePrompt` 后完全相同；两段的 ref 序列和 `<d>` 内容保持相同（均为空），包括 `customMetadata`、`customField` 均保留。实际只改了两段的 `prompt`，未改 `negativePrompt`。

## 尚需出片确认

- 一镜到底中拨小箭、单臂抱起处于定时状态的男孩、再放到台阶属于手部和双人接触高风险；文字细化不能证明没有穿模或多手。
- 15 秒内依次完成定时、拨箭、抱走、安置和恢复的节拍承载，须看实际运动和尾帧。
- 全场静止稳定性、门的铰接运动、竹叶数量和材质、箭轨迹及落点须看实际出片；静态校验不等于导入或渲染验收。
- 没有需要静态阶段改动剧情、素材或时长的决定；原要求的一镜到底保留。

## 候选规则交叉复核

已在生成审查产物后只读通读候选三份 `SKILL.md` 及 `h3-shot-prompt/references/powers-and-effects.md`，并检查下述指针在包内是否存在。未编辑 skill。

核心异能规则未发现彼此无法化解的硬矛盾：单段主 skill 有优先级；明确一镜到底、定时段不套全局表演、无光念力的物体与风表现、声音硬限制、真人受力结果与数量保护均相互一致；“未渲染”的证据边界也一致。没有借这次审查扩大采样、Ref2VA 或渲染质量结论。

发现两类范围/可定位性问题，均为局部文字或随包证据问题：

| 类别 | 精确位置 | 发现与影响 | 建议（本次未修改） |
|---|---|---|---|
| 后置清单未就地重复异能适用范围 | `h3-director-json-review/SKILL.md:122`；`h3-action-prompt-design/SKILL.md:189,260` | 导播检查仍问“每个人手上有小事吗”；补充手册仍要求“每段沉默下面垫什么环境声”；门自行动作病症行仍只给“人、手、接触点”。分别与定身人物不动、用户限定静止时只许脚步、念力开门不用人手的明确例外存在局部表述张力。完整阅读时能由主 skill/第 4 节/powers 的明确边界化解；若机械逐项复核或只查病症表，仍可能重新引入已修掉的问题。不是本次 JSON 的残留错误。 | 清单条目就地注明“非定身角色”“服从用户声音限制”“先判断是否为指定异能，再分别写手动或能力触发”。不要另造新的固定模板。 |
| 证据指针未随候选包提供 | `h3-shot-prompt/SKILL.md:60` | `tools/context_ir/analysis/RENDER_RESULTS_1.md` 在当前 skill 根目录、candidate-skills 根目录和工作区根目录均不存在，不能从候选包复核该条本地镜头表证据。只证明当前包不可定位，不说明原作者源仓库不存在。 | 随包附实际证据或标为外部源仓库路径，并给明确仓库根目录/可访问位置；不应伪装成包内相对链接。 |

此外，`h3-shot-prompt/references/powers-and-effects.md`、`references/pipeline-and-settings.md`、`references/official-format.md`、`references/examples.md` 与 `scripts/lint_prompt.py` 均在所属单段 skill 下存在；导播审查 lint 实际成功调用了同包单段 lint。其余简写文件名在上下文可归属对应 skill，没有据此臆造缺文件问题。电影感底座的默认手持/腰上构图由 `cinematography.md` 明确允许具体镜头的静止/宽景覆盖，因此未把该默认与这两段的宽景、静止机位判断为硬冲突。
