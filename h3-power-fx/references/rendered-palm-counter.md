# C1 提前反击：已认可时机的历史原稿

用户定位的视频：`c1_r4_earlycounter_s1_video_00001_`。

- 片段 ID：`c1_r4_earlycounter_s1`；seed：2026100801；时长：8 秒；纯文本，无挂载素材。
- 原 JSON 中排第二，不等于种子2。来源为用户提供的第三四轮 AB 对照五段40秒文件；仓库归档：`tools/context_ir/powers/analysis/skill_optimization_20261009/evidence/c1_r4_source.json`。
- 源 JSON SHA256：`097da97c4129851556ae518d6552510a8d2732c2c6973508bc07bead23445487`。
- 下方 prompt UTF-8 SHA256（不含围栏及围栏前换行）：`809948278ef34694b7c1bd505418b3ea8759beafc360fdf10a507c12799bd1da`。
- 证据：用户反馈攻击与反击时机基本正确；本次未直接观看视频。实际渲染完整配置未独立确认，不沿用另一批 BF16/20步参数。

## 适用边界

可保留的设计是近距离威胁已经成立、挥棍落下前立即反击，不增加蓄力等待。原文要求后退两步撞柱，并非离地击飞。只有时机获认可，强能量、击飞速度、破坏、手部准确性与声音仍需逐项验证。

原稿含全大写、片内时间标签和否定句，也缺少现行 lint 所需 Shot 标记。现行检查器报告三项 ERROR：缺 Shot 标记，以及 DO NOT、NEVER 指令词；另有否定句和大写 WARN。它是历史证据，不是合规新稿范本；不能推断毫秒标签或大写就是成功原因。原样复跑保留原文并说明已知格式问题；改写另存候选，遵守主 skill，不改文戏规则。

## 精确原文

```text
integrated_multimodal_description:
REALISTIC LIVE-ACTION ACTION SCENE, 16:9. ONE CONTINUOUS LOCKED-OFF MEDIUM-WIDE SIDE VIEW, no cuts, no pan, no push-in. Natural fluorescent garage light; real skin, real human momentum. Keep BOTH characters, their hands, the iron bar, their feet and one pillar clearly visible throughout.

FIXED STAGE: Empty underground garage. Woman with short dark hair and black motorcycle jacket on SCREEN LEFT facing RIGHT, her RIGHT palm initially DOWN. Bald man in dark shirt on SCREEN RIGHT facing LEFT; holds ONE iron bar in HIS RIGHT HAND, raised already near his right shoulder. He stands just outside striking distance, ready to attack. A single square CONCRETE PILLAR is two steps BEHIND him to SCREEN RIGHT. No other people. Left/right positions do not reverse.

00:00.00 [START ONE BEAT BEFORE THE HIT]: Bald attacker is ALREADY CLOSE, shoulders coiled and iron bar cocked back over his RIGHT SHOULDER, about to bring it down. He leans aggressively toward the woman. DO NOT spend time showing him running across the garage.
00:00.15–00:00.55 [INTERRUPT]: BEFORE the bar begins any downward strike, the woman rapidly whips her RIGHT OPEN PALM from waist level toward HIS CHEST. This is a defensive counter, not a slow pose. The attacker has not hit her.
00:00.55–00:00.70 [IMMEDIATE FORCE]: The instant her open palm faces him, ONE tight blue-white pressure flash snaps across the short gap and strikes his CHEST. His shoulders and head JOLT BACK on the SAME beat, aborting his attempted swing. NO charging, NO continuous laser beam, NO delay between the gesture and his recoil.
00:00.70–00:02.50 [BACKWARD MOTION]: He recoils and is forced two strong, awkward steps toward SCREEN RIGHT, away from the woman. His wet shoes skid realistically. Keep his body continuous without disappearing or being flung as a stiff horizontal doll. The bar is still in his right hand until the pillar impact.
00:02.50–00:03.40 [SINGLE COLLISION]: His upper BACK hits the same concrete pillar behind him at SCREEN RIGHT. ONE brief puff of concrete dust. He lets go of the iron bar ONCE, which drops beside his feet. His knees buckle and he slides down.
00:03.40–00:08.00 [RESULT]: He remains slumped at the pillar, iron bar on the ground. The woman stays SCREEN LEFT and lowers her open right hand, startled by its power; she does not attack again. Dust settles naturally. No reset, no second hit.

PRIORITY: (1) raised bar about to swing, (2) woman counterattacks BEFORE any downward strike, (3) palm flash and chest recoil synchronized at ~0.6s, (4) victim travels RIGHT to the pillar. Sacrifice dust detail if necessary; NEVER delay the counterattack or reverse left/right direction. No text, captions, titles, or logos.

overall_soundscape: Rustle of raised iron bar, abrupt short WHOOMP exactly synchronized to palm flash, one pained exhale and wet skidding shoes, single back-against-pillar thud and metal clatter. Buzzing fluorescent lights beneath. No speech.
non_diegetic_music: N/A
```
