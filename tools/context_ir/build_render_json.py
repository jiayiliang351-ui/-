#!/usr/bin/env python3
"""Build a V7.3 director JSON (schemaVersion 5) that renders every available version
of each calibration case with the same seeds, for a side-by-side comparison.

Usage:
    python3 build_render_json.py --out render_compare.json
    python3 build_render_json.py --cases-only zhiyin_ep1_06 linqi_04 --seeds 2026100701 2026100702

Versions picked up for each case id in cases.json (whichever exist):
    old       old_versions/<id>.txt        the old-style prompt that was run before
    skill     skill_versions/<id>.txt      written by Claude with the new skill
    codex     codex_versions/<id>.txt      written by Codex with the new skill
    official  results/<id>.prompt.txt      official H3-Context-IR rewrite
Shot ids look like <id>__<version>__s<seed index>, titles are Chinese labels.
No assets are attached; latent relay is off so every shot is independent.
"""
import argparse
import json
import os

VERSIONS = [("old", "old_versions/{id}.txt", "旧写法"),
            ("skill", "skill_versions/{id}.txt", "skill新写法"),
            ("codex", "codex_versions/{id}.txt", "Codex按skill写"),
            ("official", "results/{id}.prompt.txt", "官方改写")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="cases.json")
    ap.add_argument("--cases-only", nargs="*")
    ap.add_argument("--versions", nargs="*", default=[v[0] for v in VERSIONS])
    ap.add_argument("--seeds", nargs="*", type=int, default=[2026100701, 2026100702])
    ap.add_argument("--out", default="render_compare.json")
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    cases = json.load(open(os.path.join(here, args.cases), encoding="utf-8"))
    shots, table = [], []
    for c in cases:
        if args.cases_only and c["id"] not in args.cases_only:
            continue
        for key, pattern, label in VERSIONS:
            if key not in args.versions:
                continue
            path = os.path.join(here, pattern.format(id=c["id"]))
            if not os.path.isfile(path):
                continue
            prompt = open(path, encoding="utf-8").read().strip()
            for i, seed in enumerate(args.seeds, 1):
                shots.append({
                    "id": f"{c['id']}__{key}__s{i}",
                    "title": f"{c['id']} {label} 种子{i}",
                    "prompt": prompt,
                    "negativePrompt": "",
                    "durationSeconds": c["duration"],
                    "enabled": True,
                    "latentRelay": False,
                    "secondSamplingMode": "super_resolution_only",
                    "seed": seed,
                    "disabledAssetIds": [],
                })
            table.append(f"{c['id']:<22} {key:<9} {c['duration']}s x {len(args.seeds)} seeds")
    data = {
        "schemaVersion": 5,
        "project": {"id": "h3_calibration", "name": "H3写法校准对比", "runId": "h3_calibration_t1"},
        "defaults": {"fps": 24, "baseSeed": args.seeds[0] if args.seeds else 2026100701},
        "promptPrefix": "", "promptSuffix": "",
        "continuity": {"mode": "h3_av_latent", "videoContextFrames": 22, "audioContextFrames": 24,
                       "durationMode": "final_output"},
        "assets": [],
        "shots": shots,
    }
    out = os.path.join(here, args.out) if not os.path.isabs(args.out) else args.out
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\n".join(table))
    total = sum(s["durationSeconds"] for s in shots)
    print(f"wrote {out}: {len(shots)} shots, about {total} seconds of video to render")


if __name__ == "__main__":
    main()
