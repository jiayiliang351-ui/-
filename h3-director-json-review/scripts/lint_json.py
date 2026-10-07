#!/usr/bin/env python3
"""Lint every enabled shot prompt in a V7.3 director JSON (schemaVersion 5).

Usage:
    python3 lint_json.py PROJECT.json [--lint PATH/TO/lint_prompt.py] [--all] [--quiet]

By default it looks for h3-shot-prompt/scripts/lint_prompt.py next to this skill
(installed skills usually sit side by side). Pass --lint to point at it directly.
--all also checks disabled shots; --quiet prints only shots with ERROR.
Also reports {{ref:alias}} placeholders that point at missing or disabled assets.
Exit code 1 if any shot has an ERROR.
"""
import argparse
import importlib.util
import json
import os
import re
import sys


def find_linter(explicit):
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [explicit] if explicit else [
        os.path.join(here, "..", "..", "h3-shot-prompt", "scripts", "lint_prompt.py"),
        os.path.join(here, "lint_prompt.py"),
    ]
    for path in candidates:
        if path and os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("lint_prompt", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, os.path.normpath(path)
    sys.exit("lint_prompt.py not found; pass --lint PATH (it ships with the h3-shot-prompt skill)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--lint")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    linter, path = find_linter(args.lint)
    data = json.load(open(args.project, encoding="utf-8"))
    assets = {a.get("alias"): a for a in data.get("assets", [])}
    prefix = data.get("promptPrefix", "") or ""
    suffix = data.get("promptSuffix", "") or ""
    if prefix.strip() or suffix.strip():
        print("NOTE promptPrefix/promptSuffix are not empty; they are prepended/appended to every shot")

    total_err = 0
    rows = []
    for shot in data.get("shots", []):
        if not shot.get("enabled", True) and not args.all:
            continue
        sid = shot.get("id")
        prompt = (prefix + shot.get("prompt", "") + suffix)
        seconds = shot.get("durationSeconds")
        summary, errors, warns = linter.lint(prompt, seconds)
        disabled = set(shot.get("disabledAssetIds", []))
        for alias in re.findall(r"\{\{ref:([^}]*)\}\}", prompt):
            a = assets.get(alias)
            if a is None:
                errors.append(f"{{{{ref:{alias}}}}} has no matching asset")
            elif not a.get("enabled", False) or a.get("id") in disabled:
                errors.append(f"{{{{ref:{alias}}}}} points at a disabled asset")
            elif a.get("shotIds") and sid not in a.get("shotIds"):
                warns.append(f"{{{{ref:{alias}}}}} asset's shotIds do not include this shot")
        if shot.get("negativePrompt"):
            warns.append("negativePrompt is not empty (V7.3 does not wire it)")
        total_err += bool(errors)
        rows.append((sid, shot.get("title", ""), seconds, summary, len(errors), len(warns)))
        if args.quiet and not errors:
            continue
        print(f"\n=== {sid}  {shot.get('title', '')}  ({seconds}s)")
        print("    " + summary)
        for e in errors:
            print("    ERROR", e)
        for w in warns:
            print("    WARN ", w)

    print(f"\nlinter: {path}")
    print(f"{'id':<12}{'sec':>4}  {'err':>3} {'warn':>4}  summary")
    for sid, title, sec, summary, ne, nw in rows:
        print(f"{str(sid):<12}{str(sec):>4}  {ne:>3} {nw:>4}  {summary}")
    print(f"\n{len(rows)} shots checked, {total_err} with errors")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
