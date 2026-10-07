#!/usr/bin/env python3
"""Mechanical checks for a MiniMax H3 prompt written with the h3-shot-prompt skill.

Usage:
    python3 lint_prompt.py PROMPT_FILE --seconds 10
    python3 lint_prompt.py - --seconds 15 < prompt.txt

--seconds is the integer duration typed into the director/workflow (5-15).
Exit code 1 if any ERROR is found. WARN lines are advisory.
"""
import argparse
import math
import re
import sys

LEGAL_FRAMES = [n for n in range(124, 363) if n % 17 == 5]
MIN_SHOT = 1.5        # dialogue, drama, quiet scenes, and the last shot
MIN_SHOT_FAST = 1.0   # fast action quick cuts

BASE_FIELDS = ["integrated_multimodal_description", "overall_soundscape", "non_diegetic_music"]
REF_FIELDS = ["subject_definitions", "summary", "retention_analysis",
              "detailed_description", "overall_soundscape", "non_diegetic_music"]
REF_TASKS = {"keyframe completion", "reference generation", "video editing",
             "video continuation", "audio reuse", "audio reference"}
VISIBLE_MARKERS = {"fully_preserved", "partially_preserved", "attribute_transfer", "weak_reference"}
AUDIO_MARKERS = {"fully_copy", "partially_copy", "reference", "weak_reference"}

RULE_WORDS = re.compile(r"\b(IMPORTANT|FORBIDDEN|MUST|NEVER|DO NOT|DON'T|NOTE)\b")
STATE_TAG = re.compile(r"\(\s*[A-Za-z][\w ]{0,20}:\s*[A-Z][A-Z _]+\s*\)")
CAPS_WORD = re.compile(r"\b[A-Z][A-Z\-]{2,}\b")
CAPS_ALLOW = {"ARRI", "LF", "LED", "CCTV", "ATM", "UI", "TV", "POV", "ID", "OK", "USB", "SUV", "BBQ",
              "VIP", "CEO", "NHZX", "IMAX", "HDR", "LCD", "CRT", "DSLR", "GPS"}
LAND_TIME = re.compile(r"[Ll]ine lands about|Total runtime is exactly")
# In-clip times (a clip is at most 15.08 s, so larger numbers are decades, sizes, etc.).
CLIP_SECONDS = re.compile(
    r"\b(?:by|at|until|around|after)\s+(?:about\s+)?(?:1[0-5]|\d)(?:\.\d+)?\s*(?:s|sec|seconds)\b"
    r"|\b(?:1[0-5]|\d)(?:\.\d+)?-second mark\b"
    r"|\((?:1[0-5]|\d)\.\d+s\)", re.I)
# "no X" naming an absent thing; skip "no longer", "No. 7", "no-nonsense", "no wider than".
ABSENT_THING = re.compile(
    r"\b(?:no|nobody|nothing)\b"
    r"(?!\s+longer\b|\.\s*\d|-(?!one\b)|\s+(?:more|less|[a-z]+er)\s+than\b)", re.I)
# Fixed sentences the skill tells writers to copy verbatim; exempt from style checks.
FIXED_SENTENCES = [
    "Nobody stands idle or poses for the camera.",
    "The frame remains free of subtitles, captions, title cards, and text overlays. Dialogue is audible speech only.",
    "Do not repeat, paraphrase or continue beyond the listed spoken content.",
    "No extra body, duplicate face or mirror double enters.",
    "There is no grey wall, no studio backdrop and no plain seamless background anywhere in the frame.",
]
FIXED_RES = [re.compile(r"\s+".join(map(re.escape, f.split())), re.I) for f in FIXED_SENTENCES]
BG_ONLY = re.compile(r"Behind (?:them|the people) is ONLY\b[^\n]*?\.(?=\s|$)")


def strip_fixed(text):
    """Remove the skill's verbatim fixed sentences so style checks do not flag them."""
    for rx in FIXED_RES:
        text = rx.sub(" ", text)
    return BG_ONLY.sub(" ", text)
CJK = re.compile(r"[　-〿㐀-鿿＀-￯‘’“”]")


def effective_seconds(nominal):
    frames = nominal * 24
    snapped = next((n for n in LEGAL_FRAMES if n >= frames), LEGAL_FRAMES[-1])
    return snapped / 24.0


def strip_allowed(text):
    """Remove spans where non-English text is allowed: <d>...</d> and "quoted on-screen text"."""
    text = re.sub(r"<d>.*?</d>", " ", text, flags=re.S)
    text = re.sub(r'(?<![\w"])"[^"\n]*"', " ", text)
    return text


def split_fields(text, names):
    pos = []
    for name in names:
        m = re.search(r"(^|\n)" + re.escape(name) + r":", text)
        pos.append((name, m.start() if m else -1, m.end() if m else -1))
    found = [p for p in pos if p[1] >= 0]
    body = {}
    for i, (name, start, end) in enumerate(found):
        nxt = found[i + 1][1] if i + 1 < len(found) else len(text)
        body[name] = text[end:nxt].strip()
    order_ok = [p[1] for p in found] == sorted(p[1] for p in found)
    missing = [p[0] for p in pos if p[1] < 0]
    return body, missing, order_ok


class _Args:
    def __init__(self, seconds):
        self.seconds = seconds


def lint(text, seconds):
    """Return (summary, errors, warns) for one prompt; seconds is the integer duration typed in."""
    args = _Args(int(seconds))
    text = text.strip().replace("\r\n", "\n")
    text = re.sub(r"\{\{ref:[^}]*\}\}", "<Picture 0>", text)  # director placeholders

    errors, warns = [], []
    eff = effective_seconds(args.seconds)
    first_line = text.split("\n", 1)[0]

    # Mode and alignment sentence
    is_ref = text.startswith("subject_definitions:")
    if first_line.startswith("For the target video, at 0.00 seconds"):
        mode = "I2VA"
    elif first_line.startswith("How the reference pictures align"):
        mode = "FL2VA" if first_line.count("-second mark") >= 2 else "L2VA"
    elif is_ref:
        mode = "Ref2VA"
    elif first_line.startswith("integrated_multimodal_description:"):
        mode = "T2VA"
    else:
        mode = "?"
        errors.append("first line is neither an alignment sentence nor a field name")
    if mode in ("I2VA", "FL2VA", "L2VA"):
        if not re.match(r"^[^\n]+\n\n", text):
            errors.append("alignment sentence must be followed by exactly one blank line")
        marks = re.findall(r"(\d+\.\d\d)-second mark", first_line)
        if mode in ("FL2VA", "L2VA") and marks:
            s = float(marks[-1])
            real = math.floor(eff * 100 + 0.5) / 100
            if abs(s - real) > 0.001 and abs(s - args.seconds) > 0.001:
                errors.append(f"alignment S.SS {s:.2f} matches neither {real:.2f} (real) nor {args.seconds:.2f} (nominal)")

    names = REF_FIELDS if is_ref else BASE_FIELDS
    body, missing, order_ok = split_fields(text, names)
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if not order_ok:
        errors.append("fields are out of order")
    main_field = "detailed_description" if is_ref else "integrated_multimodal_description"
    desc = body.get(main_field, "")

    # Shots and cut times
    shots = re.findall(r"\[Shot (\d+)\]([^\n\[]{0,40})", desc)
    if re.search(r"\[Shot \d+ ·", desc):
        errors.append("range-style shot header '[Shot N · a–b s]' is not the official format")
    elif not shots:
        errors.append("no [Shot N] headers found")
    nums = [int(n) for n, _ in shots]
    if nums and nums != list(range(1, len(nums) + 1)):
        errors.append(f"shot numbers not contiguous from 1: {nums}")
    times = []
    for n, tail in shots:
        m = re.match(r"\s*At (\d\d):(\d\d)\.(\d\d\d)", tail)
        if n == "1":
            if m:
                errors.append("[Shot 1] must not carry a timestamp")
            continue
        if not m:
            errors.append(f"[Shot {n}] lacks 'At MM:SS.mmm'")
            continue
        times.append((int(n), int(m.group(1)) * 60 + int(m.group(2)) + int(m.group(3)) / 1000))
    prev = 0.0
    for n, t in times:
        if t <= prev:
            errors.append(f"[Shot {n}] cut {t:.3f}s is not after the previous cut")
        elif t - prev < MIN_SHOT_FAST:
            warns.append(f"shot before [Shot {n}] lasts {t - prev:.2f}s (< {MIN_SHOT_FAST}s, too short even for fast action)")
        elif t - prev < MIN_SHOT:
            warns.append(f"shot before [Shot {n}] lasts {t - prev:.2f}s (< {MIN_SHOT}s; fine only for fast-action quick cuts)")
        if t >= eff:
            errors.append(f"[Shot {n}] cut {t:.3f}s is at/after the real end {eff:.3f}s")
        prev = t
    if times and eff - prev < MIN_SHOT:
        warns.append(f"last shot lasts {eff - prev:.2f}s (< {MIN_SHOT}s)")
    n_shots = len(shots) + len(re.findall(r"\[Shot \d+ ·", desc))
    if n_shots > 9:
        warns.append(f"{n_shots} shots in one clip; even fast action tops out around 9 per 15 s")
    if len(shots) >= 2 and not re.search(r"\bfrom \[?Shot \d", desc, re.I):
        warns.append("multi-shot clip never re-identifies people or props with 'from Shot N'")

    # Style: rule words, tags, caps, timing notes
    plain = strip_fixed(strip_allowed(text.split("\n", 1)[1] if mode in ("I2VA", "FL2VA", "L2VA") else text))
    for w in sorted(set(RULE_WORDS.findall(plain))):
        errors.append(f"rule/instruction word '{w}' — rewrite as an observable statement")
    for tag in sorted(set(STATE_TAG.findall(plain))):
        errors.append(f"state tag {tag} — write the state as a sentence")
    if LAND_TIME.search(plain):
        warns.append("timing note ('Line lands about' / 'Total runtime') — not in the official format")
    desc_plain = strip_fixed(strip_allowed(desc))
    clip_times = sorted(set(x.group(0) for x in CLIP_SECONDS.finditer(plain)))
    if clip_times:
        warns.append("in-clip time " + ", ".join(f"'{m}'" for m in clip_times[:6])
                     + (" ..." if len(clip_times) > 6 else "") + " — anchor timing to events instead")
    absent = sorted(set(w.lower() for w in ABSENT_THING.findall(desc_plain)))
    if absent:
        warns.append("names an absent thing (" + "/".join(absent) + ") — prefer a positive state; fixed sentences are exempt")
    caps = sorted({w for w in CAPS_WORD.findall(plain) if w not in CAPS_ALLOW})
    if caps:
        warns.append("ALL-CAPS words: " + ", ".join(caps[:12]) + (" ..." if len(caps) > 12 else ""))
    bad = sorted(set(CJK.findall(plain)))
    if bad:
        errors.append("CJK or full-width characters outside <d> and quoted on-screen text: " + "".join(bad[:20]))

    # Dialogue
    lines = re.findall(r"<d>(.*?)</d>", text, flags=re.S)
    for i, line in enumerate(lines, 1):
        if not re.match(r"\[[A-Za-z]+\]", line):
            errors.append(f"dialogue #{i} lacks a language tag like [Chinese]")
        elif not re.match(r"\[[A-Za-z]+\] ", line):
            warns.append(f"dialogue #{i}: no space after the language tag (official form is '<d>[Chinese] ...</d>')")
    zh = sum(len(re.findall(r"[一-鿿]", l)) for l in lines)
    if zh:
        limit = min(48, math.floor(eff * 3.5))
        if zh > limit:
            errors.append(f"{zh} spoken Chinese characters; hard limit for {eff:.2f}s is about {limit}")
        elif zh > args.seconds * 3:
            warns.append(f"{zh} spoken Chinese characters is near the upper budget")
    for m in re.finditer(r"off-screen voice-?over[:,]?\s*<d>.*?</d>(.{0,160})", desc, flags=re.S):
        if "closed" not in m.group(1):
            errors.append("off-screen voiceover not followed by a 'lips remain completely closed' clause")
    if lines and not re.search(r"\(S\d", desc):
        errors.append("dialogue present but no speaker ID (S1) in the description")

    # Ref2VA specifics
    if is_ref:
        summ = body.get("summary", "")
        m = re.match(r"\[([^\]]+)\]", summ)
        if not m:
            errors.append("summary lacks a [task type] prefix")
        else:
            tasks = [t.strip() for t in m.group(1).split("+")]
            unknown = [t for t in tasks if t not in REF_TASKS]
            if unknown:
                errors.append("unknown task types: " + ", ".join(unknown))
            if len(tasks) != len(set(tasks)):
                errors.append("repeated task type in summary prefix")
        ret = body.get("retention_analysis", "")
        if re.search(r"\(S\d", ret):
            errors.append("retention_analysis must not contain (Sx)")
        for line in [l for l in ret.split("\n") if l.strip()]:
            mm = re.search(r":\s*([a-z_]+)\s*-", line)
            if not mm:
                warns.append("retention line without a marker: " + line[:60])
                continue
            marker = mm.group(1)
            allowed = AUDIO_MARKERS if line.startswith("<Audio") else VISIBLE_MARKERS
            if marker not in allowed:
                errors.append(f"invalid retention marker '{marker}' in: {line[:60]}")
        defined = set(re.findall(r"^(<(?:Subject|Picture|Video|Audio) \d+>)", body.get("subject_definitions", ""), flags=re.M))
        used = set(re.findall(r"<(?:Subject|Picture|Video|Audio) \d+>", desc))
        for lab in sorted(used - defined):
            if not lab.startswith("<Picture") and not lab.startswith("<Video"):
                errors.append(f"{lab} used in the description but never defined")
    for lab in sorted(set(re.findall(r"<(Image|Ref|Img|Frame|Clip) ?\d+>", text))):
        errors.append(f"label <{lab} N> is not one of Subject/Picture/Video/Audio")

    # Length
    words = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", strip_allowed(desc)))
    if words < 150:
        warns.append(f"{main_field} has {words} words; under-writing is a common failure")
    elif words > 650:
        warns.append(f"{main_field} has {words} words; check for rules or repetition")

    summary = f"mode={mode}  shots={n_shots}  real_duration={eff:.3f}s  words={words}  spoken_zh={zh}"
    return summary, errors, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--seconds", type=int, required=True)
    args = ap.parse_args()
    text = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    summary, errors, warns = lint(text, args.seconds)
    print(summary)
    for e in errors:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    if not errors and not warns:
        print("OK")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
