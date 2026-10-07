#!/usr/bin/env python3
"""Send the prompts of a V7.3 director JSON through the official H3-Context-IR API
and write a copy of the JSON whose prompts are the official rewrites.

Only shots WITHOUT {{ref:...}} placeholders are rewritten (text-only T2VA shots);
shots that use assets are left unchanged and listed, because the official rewrite
cannot know how the director maps {{ref:alias}} to labels.

Usage:
    export MINIMAX_API_KEY=...
    python3 rewrite_director_json.py PROJECT.json --limit 5
    python3 rewrite_director_json.py PROJECT.json --only 01 02 07
    python3 rewrite_director_json.py PROJECT.json --limit 40 --base https://api.minimax.io

Outputs, next to the input unless --out-dir is given:
    PROJECT_官方改写.json        same file, rewritten prompts, every other field untouched
    PROJECT_官方改写_log.md      per shot: status, dialogue check, lint summary, token usage
    ir_cache/<project>/<shot id>.prompt.txt   cached rewrites (re-runs do not pay twice)
--limit caps how many NEW API calls are made in this run (cached shots are free).
"""
import argparse
import importlib.util
import json
import os
import re
import sys


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dialogue(text):
    return [re.sub(r"\s+", "", d) for d in re.findall(r"<d>(.*?)</d>", text or "", flags=re.S)]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    batch = load("context_ir_batch", os.path.join(here, "context_ir_batch.py"))
    lint_path = os.path.join(here, "..", "..", "h3-shot-prompt", "scripts", "lint_prompt.py")
    linter = load("lint_prompt", lint_path) if os.path.isfile(lint_path) else None

    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--ratio", default="16:9")
    ap.add_argument("--base", default=os.environ.get("MINIMAX_API_BASE", batch.DEFAULT_BASE))
    ap.add_argument("--out-dir")
    args = ap.parse_args()

    key = os.environ.get("MINIMAX_API_KEY")
    if not key:
        sys.exit("MINIMAX_API_KEY is not set")
    data = json.load(open(args.project, encoding="utf-8"))
    stem = os.path.splitext(os.path.basename(args.project))[0]
    out_dir = args.out_dir or os.path.dirname(os.path.abspath(args.project))
    cache = os.path.join(here, "ir_cache", re.sub(r"[^\w\-]", "_", stem))
    os.makedirs(cache, exist_ok=True)

    log = [f"# {stem} 官方改写日志\n", "| 段 | 状态 | 台词 | lint | tokens |", "|---|---|---|---|---|"]
    new_calls = 0
    for shot in data.get("shots", []):
        sid = str(shot.get("id"))
        if not shot.get("enabled", True):
            log.append(f"| {sid} | 跳过：未启用 | | | |")
            continue
        if args.only and sid not in args.only:
            continue
        old = shot.get("prompt", "")
        if "{{ref:" in old:
            log.append(f"| {sid} | 跳过：挂了素材（保持原样） | | | |")
            continue
        cpath = os.path.join(cache, sid + ".prompt.txt")
        tokens = ""
        if os.path.exists(cpath):
            new = open(cpath, encoding="utf-8").read().strip()
            status = "已改写（缓存）"
        elif new_calls >= args.limit:
            log.append(f"| {sid} | 跳过：达到 --limit {args.limit} | | | |")
            continue
        else:
            new_calls += 1
            case = {"id": sid, "duration": int(shot.get("durationSeconds", 10)), "ratio": args.ratio, "text": old}
            print(f"run  {sid} ({case['duration']}s) ...", flush=True)
            try:
                result = batch.run_case(case, args.base.rstrip("/"), key, 5, 600)
            except Exception as e:
                log.append(f"| {sid} | 失败：{str(e)[:80]} | | | |")
                print(f"FAIL {sid}: {e}")
                continue
            new = result["task"]["content"]["prompt"].strip()
            with open(cpath, "w", encoding="utf-8") as f:
                f.write(new + "\n")
            with open(os.path.join(cache, sid + ".json"), "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            tokens = str(result.get("task", {}).get("usage", {}).get("total_tokens", ""))
            status = "已改写"
        shot["prompt"] = new
        d_old, d_new = dialogue(old), dialogue(new)
        dstat = "无台词" if not d_old and not d_new else ("一致" if d_old == d_new else "**有变化，需人工核对**")
        lstat = ""
        if linter:
            _, errors, warns = linter.lint(new, int(shot.get("durationSeconds", 10)))
            lstat = f"{len(errors)} ERROR / {len(warns)} WARN"
        log.append(f"| {sid} | {status} | {dstat} | {lstat} | {tokens} |")

    out_json = os.path.join(out_dir, stem + "_官方改写.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(os.path.join(out_dir, stem + "_官方改写_log.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")
    print(f"wrote {out_json} ({new_calls} new API calls)")


if __name__ == "__main__":
    main()
