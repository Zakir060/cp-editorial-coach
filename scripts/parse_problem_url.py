#!/usr/bin/env python3
"""Normalize and classify common competitive-programming problem URLs.

Supports Codeforces, AtCoder, and LeetCode.
Prints JSON so the skill can use the result in downstream reasoning.
"""

from __future__ import annotations

import json
import re
import sys
from urllib.parse import urlparse


CF_PATTERNS = [
    re.compile(r"^/contest/(?P<contest_id>\d+)/problem/(?P<problem>[A-Za-z0-9]+)$"),
    re.compile(r"^/problemset/problem/(?P<contest_id>\d+)/(?P<problem>[A-Za-z0-9]+)$"),
    re.compile(r"^/gym/(?P<contest_id>\d+)/problem/(?P<problem>[A-Za-z0-9]+)$"),
]

ATCODER_PATTERN = re.compile(
    r"^/contests/(?P<contest>[a-zA-Z0-9_]+)/tasks/(?P<task>[a-zA-Z0-9_]+)$"
)

LEETCODE_PATTERN = re.compile(r"^/problems/(?P<slug>[a-z0-9-]+)/?$")


def normalize_url(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("empty url")
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", raw):
        raw = "https://" + raw
    return raw


def parse_codeforces(parsed):
    for pattern in CF_PATTERNS:
        match = pattern.match(parsed.path)
        if match:
            contest_id = match.group("contest_id")
            problem = match.group("problem")
            kind = "gym" if "/gym/" in parsed.path else "contest"
            base = "https://codeforces.com"
            if kind == "gym":
                normalized = f"{base}/gym/{contest_id}/problem/{problem}"
            else:
                normalized = f"{base}/contest/{contest_id}/problem/{problem}"
            return {
                "platform": "codeforces",
                "kind": kind,
                "contest_id": contest_id,
                "problem": problem,
                "normalized_url": normalized,
            }
    return None


def parse_atcoder(parsed):
    match = ATCODER_PATTERN.match(parsed.path)
    if not match:
        return None
    contest = match.group("contest")
    task = match.group("task")
    normalized = f"https://atcoder.jp/contests/{contest}/tasks/{task}"
    return {
        "platform": "atcoder",
        "contest": contest,
        "task": task,
        "normalized_url": normalized,
    }


def parse_leetcode(parsed):
    match = LEETCODE_PATTERN.match(parsed.path)
    if not match:
        return None
    slug = match.group("slug")
    normalized = f"https://leetcode.com/problems/{slug}/"
    return {
        "platform": "leetcode",
        "slug": slug,
        "normalized_url": normalized,
    }


def parse_problem_url(raw: str):
    normalized_input = normalize_url(raw)
    parsed = urlparse(normalized_input)
    host = parsed.netloc.lower()

    result = None
    if host in {"codeforces.com", "www.codeforces.com", "m1.codeforces.com", "m2.codeforces.com"}:
        result = parse_codeforces(parsed)
    elif host in {"atcoder.jp", "www.atcoder.jp"}:
        result = parse_atcoder(parsed)
    elif host in {"leetcode.com", "www.leetcode.com"}:
        result = parse_leetcode(parsed)

    if result is None:
        return {
            "platform": "unknown",
            "normalized_url": normalized_input,
            "supported": False,
        }

    result["supported"] = True
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: parse_problem_url.py <url>", file=sys.stderr)
        return 1

    try:
        result = parse_problem_url(sys.argv[1])
    except Exception as exc:  # pragma: no cover - defensive cli path
        print(json.dumps({"error": str(exc)}))
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
