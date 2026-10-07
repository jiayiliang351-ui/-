#!/usr/bin/env python3
"""Copy the official rewrites in results/ into h3-shot-prompt/references/official-calibration.md.

Idempotent: everything below the CODEX-INSERT-BELOW marker is regenerated on each run,
and the status line is updated. Never edits anything above the marker.

Usage:
    python3 append_calibration.py
"""
import datetime
import json
import os
import re

MARKER = "<!-- CODEX-INSERT-BELOW"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    target = os.path.normpath(os.path.join(here, "..", "..", "h3-shot-prompt", "references", "official-calibration.md"))
    cases = json.load(open(os.path.join(here, "cases.json"), encoding="utf-8"))
    doc = open(target, encoding="utf-8").read()
    idx = doc.find(MARKER)
    if idx < 0:
        raise SystemExit("marker not found in " + target)
    head_end = doc.find("\n", idx) + 1
    head = doc[:head_end]
    blocks, n = [], 0
    for c in cases:
        path = os.path.join(here, "results", c["id"] + ".prompt.txt")
        if not os.path.isfile(path):
            continue
        prompt = open(path, encoding="utf-8").read().strip()
        n += 1
        blocks.append(f"\n## {c['id']}（{c['duration']} 秒）\n\n**简报：** {c['text']}\n\n```text\n{prompt}\n```\n")
    today = datetime.date.today().isoformat()
    head = re.sub(r"状态：.*\n", f"状态：**已收集 {n} 条**（{today}，官方 H3-Context-IR 接口改写，纯文字 T2VA）。\n", head, count=1)
    with open(target, "w", encoding="utf-8") as f:
        f.write(head + "".join(blocks))
    print(f"wrote {n} cases into {target}")


if __name__ == "__main__":
    main()
