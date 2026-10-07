#!/usr/bin/env python3
"""Call the official MiniMax H3-Context-IR API for a batch of raw scene ideas
and save the rewritten prompts, so they can be studied and run on local H3-Base.

Usage:
    export MINIMAX_API_KEY=...            # never commit or paste the key
    python3 context_ir_batch.py cases.json --out results/
    python3 context_ir_batch.py cases.json --out results/ --only zhiyin_ep1_06 linqi_04
    python3 context_ir_batch.py cases.json --out results/ --base https://api.minimax.io   # global

cases.json: a list of objects
    {"id": "zhiyin_ep1_06", "duration": 8, "ratio": "16:9", "text": "...",
     "media": [{"type": "audio_url", "url": "https://...", "role": "reference_audio"}]}
"media" is optional. video_url/audio_url with roles reference_video/reference_audio
follow the official README scripts; other media types are passed through as given.

For each case it writes results/<id>.prompt.txt (the rewritten prompt) and
results/<id>.json (the full API response). Cases with an existing .prompt.txt are
skipped unless --force is given. Only the standard library is used.
"""
import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

DEFAULT_BASE = "https://api.minimaxi.com"


def ssl_context():
    ctx = ssl.create_default_context()
    for var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE"):
        path = os.environ.get(var)
        if path and os.path.isfile(path):
            ctx.load_verify_locations(path)
    return ctx


def call(method, url, key, body=None, timeout=60):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + key)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ssl_context()) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(f"HTTP {e.code} from {url}: {detail}") from None


def build_content(case):
    content = [{"type": "text", "text": case["text"]}]
    for m in case.get("media", []):
        kind = m["type"]
        item = {"type": kind, kind: {"url": m["url"]}}
        if m.get("role"):
            item["role"] = m["role"]
        content.append(item)
    return content


def run_case(case, base, key, poll, max_wait):
    body = {"model": "MiniMax-H3", "content": build_content(case),
            "duration": case["duration"], "ratio": case.get("ratio", "16:9")}
    created = call("POST", base + "/v2/h3_context_ir", key, body)
    task_id = created.get("task_id")
    if not task_id:
        raise RuntimeError("no task_id in response: " + json.dumps(created, ensure_ascii=False)[:500])
    waited = 0
    while True:
        result = call("GET", f"{base}/v2/query/video_generation/{task_id}", key)
        task = result.get("task", {})
        status = task.get("status")
        if status == "succeeded":
            return result
        if status in ("failed", "canceled", "cancelled"):
            raise RuntimeError("task " + status + ": " + json.dumps(result, ensure_ascii=False)[:500])
        if waited >= max_wait:
            raise RuntimeError(f"task {task_id} still {status} after {max_wait}s")
        time.sleep(poll)
        waited += poll


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cases")
    ap.add_argument("--out", default="results")
    ap.add_argument("--base", default=os.environ.get("MINIMAX_API_BASE", DEFAULT_BASE))
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--poll", type=int, default=5)
    ap.add_argument("--max-wait", type=int, default=600)
    args = ap.parse_args()

    key = os.environ.get("MINIMAX_API_KEY")
    if not key:
        sys.exit("MINIMAX_API_KEY is not set")
    cases = json.load(open(args.cases, encoding="utf-8"))
    os.makedirs(args.out, exist_ok=True)
    failures = 0
    for case in cases:
        cid = case["id"]
        if args.only and cid not in args.only:
            continue
        prompt_path = os.path.join(args.out, cid + ".prompt.txt")
        if os.path.exists(prompt_path) and not args.force:
            print(f"skip {cid} (already done)")
            continue
        print(f"run  {cid} ({case['duration']}s) ...", flush=True)
        try:
            result = run_case(case, args.base.rstrip("/"), key, args.poll, args.max_wait)
        except Exception as e:  # keep going with the other cases
            failures += 1
            print(f"FAIL {cid}: {e}")
            continue
        prompt = result["task"]["content"]["prompt"]
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt.strip() + "\n")
        with open(os.path.join(args.out, cid + ".json"), "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        usage = result.get("task", {}).get("usage", {})
        print(f"ok   {cid}: {len(prompt.split())} words, tokens={usage.get('total_tokens')}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
