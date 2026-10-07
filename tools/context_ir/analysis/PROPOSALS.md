# 对 h3-shot-prompt 的修改建议（待 Claude 审核，执行者不要直接改 skill）

> 填写规则（给执行者）：
> 1. 只根据 `REPORT.md` 的"跨用例统计"表提建议。
> 2. 触发条件只有两种：
>    - **官方常做、skill 不做或禁止**：某检查项在官方里"是"的个数 ≥ 5，而 skill 的规则禁止它或没写它。
>    - **官方几乎不做、skill 要求做**：某检查项在官方里"是"的个数 ≤ 1，而 skill 的规则要求它。
> 3. 不满足触发条件的观察，写进最后的"其他观察"，不算建议。
> 4. 每条建议必须给出：skill 里相关的原文（文件名 + 原句）、官方证据（至少 3 个用例的原句）、建议怎么改（一句话）。
> 5. 不要修改任何 skill 文件。


## 建议 1

- 触发条件：官方几乎不做、skill 要求做
- 检查项：C
- 官方“是”的个数：0 / 8
- skill 现在的写法：`h3-shot-prompt/SKILL.md`：「- 说完写闭嘴：`As his line ends, his lips close and his jaw stops moving.`」
- 官方证据：
  - [linqi_04] `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`
  - [yanwang_ep02] `Staring directly at Boss Qian, the King of Hell (S1) says in a low, steady voice, <d>[Chinese] 他的活本王干，一分钱不要。</d> Boss Qian and Xiao Zhang watch silently, their mouths kept firmly closed.`
  - [office_two_speakers] `With a stoic expression, the middle-aged man (S2) replies in a low, resonant voice, <d>[Chinese] 我知道了。</d> Immediately after speaking, he pivots smoothly on his heel, the fabric of his dark grey suit shifting, and walks deliberately away into the shadowy background of the office, slowly exiting the frame to the left as the shot concludes.`
- 建议改法：把统一必写收口改为注明“本地防串词实测补充”，按对白风险选用，并保留已实测场景的收口写法。

## 建议 2

- 触发条件：官方几乎不做、skill 要求做
- 检查项：D
- 官方“是”的个数：1 / 8
- skill 现在的写法：`h3-shot-prompt/SKILL.md`：「- 听的人写看得见的反应，并写 `her lips stay closed`。」
- 官方证据：
  - [linqi_04] `Lao Xu, his voice rough and weary, says, <d>[Chinese] 那我帮你扔。</d> Hearing this, the camera captures a close-up of Xiao Su as her hands pause their movement for a brief second; her lips curl slightly into a microscopic smile, though she does not turn around.`
  - [couple_split] `The woman (S1), her eyes glistening with unshed tears, looks directly at him and says in a low, trembling voice, <d>[Chinese] 你每次都说下次。</d> The man (S2) breaks eye contact, looking away towards the dark street while awkwardly rubbing the back of his neck with his right hand.`
  - [office_two_speakers] `Without lifting his head, he lazily raises one hand from the keyboard, points a finger toward the background, and says flatly, <d>[Chinese] 新来的？工位在那边。</d> The middle-aged man (S2) stands perfectly still, his face half-illuminated by the monitor's spill light.`
- 建议改法：把统一必写听者闭嘴改为注明“本地防串词实测补充”，保留相似人物、近距离多人对白等高风险场景默认使用。

---

## 其他观察（不满足触发条件，只记录）

- C、D 按模板统计 8 条，其中仅 4 条含对白；上述证据只反映文本分布，未验证本地渲染或串词效果，不据此撤销原有实测结论。
- B=4、E=4、F=4，没有达到 ≥5 或 ≤1 的触发门槛。
- G=0；SKILL.md 原文：“类型 + 幅度 + 速度（只在有意义时写幅度、速度）”。原规则已经允许省略，未据此提建议。
- I=1；skill 没有强制配乐写情绪词，未据此提建议。
- L=2，未达到 ≤1 门槛。模板指定的 people_count 是关键词计数，下列原句中的 only 分别修饰纸关节和可见范围，不能证明写明人数：
  - [zhiyin_ep1_06] `The stiff paper tiger (crafted from thick white paper with visible rough fibers, thick black ink stripes, a small bronze bell on his neck, one amber ink eye, and one blank paper eye) sprints aggressively on all fours, his limbs bending only at his stiff paper joints.`
  - [tea_pour] `An elderly man, visible only by his dark brown linen tunic and deeply wrinkled, weathered hands, reaches into the frame.`
- O=6，但 skill 未禁止对未充分说明的内容按常理补充，故本项不直接形成修改建议；新增事件逐条保留在 REPORT.md。
- P=2，未达到 ≤1 或 ≥5 的触发门槛。
- A、H、J、K、M 属于官方常做且 skill 已写的项目，N 的台词原样要求也未与本次官方结果冲突，不提修改建议。

## 官方改写在 lint_prompt.py 上报的问题

| 用例 | ERROR / WARN 原文 |
|---|---|
| linqi_04 | `WARN ALL-CAPS words: MCU` |
