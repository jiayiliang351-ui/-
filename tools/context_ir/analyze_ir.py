#!/usr/bin/env python3
"""Compare official Context-IR rewrites with the h3-shot-prompt skill versions.

Usage:
    python3 analyze_ir.py --cases cases.json --results results --skill skill_versions --out analysis

Writes (all UTF-8 Markdown/CSV, no network, standard library only):
    analysis/features.csv, analysis/features.md   numeric features per case and source
    analysis/lint.md                              lint_prompt.py results for both sources
    analysis/dialogue_check.md                    quoted lines in the brief vs <d> in the official rewrite
    analysis/sentences.md                         official sentences grouped by category, for quoting
    analysis/phrases.md                           phrases that recur across official rewrites
    analysis/side_by_side/<id>.md                 brief, then official and skill versions shot by shot
"""
import argparse
import csv
import importlib.util
import json
import os
import re
from collections import Counter, defaultdict

CATEGORIES = {
    "camera": r"\b(push(es|ed|ing)? in|pull(s|ed|ing)? out|zoom(s|ed|ing)? (in|out)|pan(s|ned|ning)? (left|right)|truck(s|ed|ing)? (left|right)|tilt(s|ed|ing)? (up|down)|pedestal|arc shot|tracking shot|track(s|ed|ing)?\b|static shot|shake(s)? (slightly|strongly)|\bPOV\b|roll(s|ed|ing)? (clockwise|counterclockwise)|camera (holds|moves|follows|drifts|cranes|rises|lowers))",
    "amplitude_speed": r"with (small|large) amplitude|at (slow|fast) speed",
    "temporal": r"\b(as|while|then|until|before|after|suddenly|immediately|a beat (later|after)|moments? later|early in the clip|as the clip progresses|throughout|toward the end|towards the end|in the final|finally|at the same time|simultaneously)\b",
    "reidentify": r"from Shot \d|from \[Shot \d\]",
    "lips": r"\b(lips?|jaw|mouth)\b",
    "emotion": r"\b(sad|sadness|angry|anger|happy|joy|nervous|anxious|tense|tension|hurt|relief|relieved|fear|afraid|shock|shocked|surprise|surprised|grief|contemplat\w*|determin\w*|resolve|expression|emotion\w*|mood|warmth|tender\w*|calm|composure|frustrat\w*)\b",
    "physics": r"\b(weight|heavy|force|momentum|impact|jolt\w*|settl\w*|slid\w*|skid\w*|trembl\w*|ripple\w*|splash\w*|drip\w*|bounc\w*|scatter\w*|roll\w*|slam\w*|press\w*|crush\w*|buckl\w*|sway\w*|stagger\w*|brace\w*|recoil\w*|land\w*|drag\w*|tilt\w*)\b",
    "negation": r"\b(no|not|never|without|nobody|nothing|none)\b|n't\b",
    "left_right": r"\b(left|right)\b",
    "people_count": r"\b(only|alone|the only|two of them|three of them)\b",
    "rule_words": r"\b(IMPORTANT|FORBIDDEN|MUST|NEVER)\b",
}
MOOD_WORDS = r"\b(nostalgic|melanchol\w*|sad|happy|joyful|heartwarming|comforting|cozy|tense|mournful|hopeful|romantic|dramatic|emotional|mood|atmosphere)\b"
STOP = set("the a an of and to in on at with his her their its is are as from into by for that this it he she they them him over while then one two".split())


def load_linter(here):
    path = os.path.join(here, "..", "..", "h3-shot-prompt", "scripts", "lint_prompt.py")
    if not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location("lint_prompt", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def field(text, name):
    m = re.search(r"(^|\n)" + name + r":(.*?)(?=\n[a-z_]+:\s|\Z)", text, flags=re.S)
    return m.group(2).strip() if m else ""


def main_field(text):
    return field(text, "detailed_description") or field(text, "integrated_multimodal_description")


def split_shots(desc):
    parts = re.split(r"(?=\[Shot \d+\])", desc)
    shots = [p.strip() for p in parts if p.strip().startswith("[Shot")]
    head = parts[0].strip() if parts and not parts[0].strip().startswith("[Shot") else ""
    return head, shots


def sentences(text):
    text = re.sub(r"<d>.*?</d>", "<d/>", text, flags=re.S)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 3]


def features(text, seconds):
    desc = main_field(text)
    head, shots = split_shots(desc)
    times = [0.0]
    for s in shots[1:]:
        m = re.search(r"At (\d\d):(\d\d)\.(\d\d\d)", s[:60])
        if m:
            times.append(int(m.group(1)) * 60 + int(m.group(2)) + int(m.group(3)) / 1000)
    durs = [b - a for a, b in zip(times, times[1:] + [seconds])]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", re.sub(r"<d>.*?</d>", " ", desc, flags=re.S))
    sents = sentences(desc)
    sound = field(text, "overall_soundscape")
    music = field(text, "non_diegetic_music")
    row = {
        "shots": len(shots),
        "cut_times": " ".join(f"{t:.2f}" for t in times[1:]),
        "min_shot_s": round(min(durs), 2) if durs else "",
        "words": len(words),
        "words_per_shot": round(len(words) / max(1, len(shots))),
        "sentences": len(sents),
        "avg_sentence_words": round(len(words) / max(1, len(sents)), 1),
        "dialogue_lines": len(re.findall(r"<d>", desc)),
        "speaker_ids": " ".join(sorted(set(re.findall(r"\(S\d(?:,S\d)*\)", desc)))),
        "voiceover": len(re.findall(r"off-screen voiceover", desc)),
        "soundscape_sentences": len(sentences(sound)),
        "music_mood_words": len(re.findall(MOOD_WORDS, music, flags=re.I)),
        "style_opening": (shots[0][9:120].strip() if shots else head[:110]),
    }
    for name, pat in CATEGORIES.items():
        flags = 0 if name == "rule_words" else re.I
        row[name] = len(re.findall(pat, re.sub(r"<d>.*?</d>", " ", desc, flags=re.S), flags=flags))
    return row


def brief_quotes(text):
    return [q.strip() for q in re.findall(r"[“\"]([^”\"]+)[”\"]", text)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="cases.json")
    ap.add_argument("--results", default="results")
    ap.add_argument("--skill", default="skill_versions")
    ap.add_argument("--codex", default="codex_versions", help="optional third source (versions Codex wrote with the skill)")
    ap.add_argument("--out", default="analysis")
    args = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    linter = load_linter(here)
    cases = json.load(open(args.cases, encoding="utf-8"))
    os.makedirs(os.path.join(args.out, "side_by_side"), exist_ok=True)

    rows, lint_lines, dlg_lines = [], ["# lint_prompt.py 结果\n"], ["# 台词核对（简报里的引号台词 vs 官方改写的 <d>）\n"]
    sent_by_cat = defaultdict(list)
    ngram_cases = defaultdict(set)
    missing = []
    for c in cases:
        cid, sec = c["id"], c["duration"]
        real = linter.effective_seconds(sec) if linter else float(sec)
        official = read(os.path.join(args.results, cid + ".prompt.txt"))
        skill = read(os.path.join(args.skill, cid + ".txt"))
        codex = read(os.path.join(args.codex, cid + ".txt"))
        if official is None:
            missing.append(cid)
        for source, text in (("official", official), ("skill", skill), ("codex", codex)):
            if text is None:
                continue
            row = {"case": cid, "source": source, "seconds": sec}
            row.update(features(text, real))
            rows.append(row)
            if linter:
                summary, errors, warns = linter.lint(text, sec)
                lint_lines.append(f"## {cid} / {source}\n\n`{summary}`\n")
                lint_lines += [f"- ERROR {e}" for e in errors] + [f"- WARN {w}" for w in warns]
                if not errors and not warns:
                    lint_lines.append("- OK")
                lint_lines.append("")
        if official:
            said = [re.sub(r"^\[[A-Za-z]+\]\s*", "", d).strip() for d in re.findall(r"<d>(.*?)</d>", official, flags=re.S)]
            dlg_lines.append(f"## {cid}\n")
            for q in brief_quotes(c["text"]):
                status = "一致" if q in said else ("被改写或拆分" if any(q[:3] in s for s in said) else "缺失")
                dlg_lines.append(f"- 简报：`{q}` → {status}")
            for s in said:
                dlg_lines.append(f"- 官方 <d>：`{s}`")
            dlg_lines.append("")
            for s in sentences(main_field(official)):
                for name in ("camera", "temporal", "reidentify", "lips", "emotion", "physics", "negation", "people_count"):
                    flags = re.I
                    if re.search(CATEGORIES[name], s, flags=flags):
                        sent_by_cat[name].append((cid, s))
            body = " ".join([main_field(official), field(official, "overall_soundscape"), field(official, "non_diegetic_music")])
            body = re.sub(r"<d>.*?</d>|\[Shot \d+\]|<[A-Za-z]+ \d+>", " ", body, flags=re.S)
            toks = [w.lower() for w in re.findall(r"[A-Za-z']+", body)]
            for n in (3, 4, 5):
                for i in range(len(toks) - n + 1):
                    g = toks[i:i + n]
                    if g[0] in STOP or g[-1] in STOP:
                        continue
                    ngram_cases[" ".join(g)].add(cid)
        # side by side
        sbs = [f"# {cid}（{sec} 秒，实际 {real:.3f} 秒）\n", "## 简报\n", c["text"], ""]
        versions = [("官方", official), ("skill", skill)] + ([("codex", codex)] if codex else [])
        split = [(label, split_shots(main_field(t or ""))[1]) for label, t in versions]
        for i in range(max(len(sh) for _, sh in split)):
            sbs.append(f"## Shot {i + 1}\n")
            for label, sh in split:
                sbs.append(f"**{label}：**\n\n" + (sh[i] if i < len(sh) else "（无）") + "\n")
        for name in ("overall_soundscape", "non_diegetic_music"):
            sbs.append(f"## {name}\n")
            for label, t in versions:
                sbs.append(f"**{label}：** " + (field(t or "", name) or "（无）") + "\n")
        with open(os.path.join(args.out, "side_by_side", cid + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(sbs) + "\n")

    keys = list(rows[0].keys()) if rows else []
    with open(os.path.join(args.out, "features.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    show = [k for k in keys if k not in ("style_opening", "cut_times")]
    md = ["# 特征对比\n", "| " + " | ".join(show) + " |", "|" + "---|" * len(show)]
    md += ["| " + " | ".join(str(r[k]) for k in show) + " |" for r in rows]
    md += ["", "## 切点", ""] + [f"- {r['case']} / {r['source']}: {r['cut_times'] or '（单镜头）'}" for r in rows]
    md += ["", "## 开头第一句", ""] + [f"- {r['case']} / {r['source']}: {r['style_opening']}" for r in rows]
    for src in ("official", "skill", "codex"):
        sub = [r for r in rows if r["source"] == src]
        if sub:
            md.append(f"\n## 平均值（{src}，{len(sub)} 条）\n")
            for k in ("shots", "words", "words_per_shot", "avg_sentence_words", "camera", "amplitude_speed", "temporal",
                      "reidentify", "lips", "emotion", "physics", "negation", "left_right", "people_count", "rule_words"):
                md.append(f"- {k}: {sum(r[k] for r in sub) / len(sub):.1f}")
    if missing:
        md.append("\n还没有官方结果的用例：" + ", ".join(missing))
    with open(os.path.join(args.out, "features.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    with open(os.path.join(args.out, "lint.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lint_lines) + "\n")
    with open(os.path.join(args.out, "dialogue_check.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(dlg_lines) + "\n")
    out = ["# 官方改写里的句子（按类别，供引用）\n"]
    for name, items in sent_by_cat.items():
        out.append(f"## {name}（{len(items)} 句）\n")
        out += [f"- [{cid}] {s}" for cid, s in items]
        out.append("")
    with open(os.path.join(args.out, "sentences.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    rec = sorted(((len(v), k, sorted(v)) for k, v in ngram_cases.items() if len(v) >= 2), reverse=True)[:150]
    with open(os.path.join(args.out, "phrases.md"), "w", encoding="utf-8") as f:
        f.write("# 在两条以上官方改写里重复出现的短语\n\n| 出现在几条 | 短语 | 用例 |\n|---|---|---|\n")
        f.writelines(f"| {n} | {k} | {', '.join(v)} |\n" for n, k, v in rec)
    print(f"wrote {args.out}/ ({len(rows)} rows; missing official: {', '.join(missing) or 'none'})")


if __name__ == "__main__":
    main()
