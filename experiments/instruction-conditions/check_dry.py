#!/usr/bin/env python3
"""Fail if any rule line appears in more than one skill of a condition.

Usage: python3 check_dry.py [condition_dir]   (default: c2)
A "rule line" is a non-heading body line longer than 40 characters,
compared case-insensitively after removing list markers and bold markers.
"""
import collections, glob, re, sys

cond = sys.argv[1] if len(sys.argv) > 1 else "c2"
seen = collections.defaultdict(set)
for path in glob.glob(f"{cond}/*/SKILL.md"):
    body = open(path, encoding="utf-8").read().split("---", 2)[2]
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = re.sub(r"^[-*]\s+|\*\*", "", line).lower()
        if len(line) > 40:
            seen[line].add(path.split("/")[1])
dups = {rule: skills for rule, skills in seen.items() if len(skills) > 1}
for rule, skills in dups.items():
    print(f"DUPLICATE in {sorted(skills)}: {rule[:100]}")
print(f"{cond}: {len(glob.glob(f'{cond}/*/SKILL.md'))} skills, {len(dups)} duplicate rule lines")
sys.exit(1 if dups else 0)
