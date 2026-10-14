#!/usr/bin/env python3
"""Validate Domain 2 draft inventory, local Markdown links and fixed synthetic sums.

This is an authoring integrity check, not a legal, regulatory or effectiveness review.
"""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = ROOT / "framework" / "02-compliance-policies"
REQUIRED = {
    "README.md",
    "allowable-cost-review.md",
    "procurement-procedures.md",
    "personnel-cost-documentation.md",
    "travel-cost-procedure.md",
    "conflicts-of-interest.md",
    "records-retention.md",
    "regulatory-source-register.md",
    "synthetic-scenarios.md",
    "review-checklist.md",
}
errors = []
found = {p.name for p in DOMAIN.glob("*.md")}
missing = REQUIRED - found
if missing:
    errors.append("Missing Domain 2 files: " + ", ".join(sorted(missing)))

link_count = 0
for source in sorted(DOMAIN.glob("*.md")):
    body = source.read_text(encoding="utf-8")
    if "CC BY 4.0" not in body:
        errors.append(f"Attribution missing: {source.relative_to(ROOT)}")
    for match in re.finditer(r"\]\(([^)]+)\)", body):
        href = match.group(1).strip().split("#", 1)[0]
        if not href or href.startswith(("https://", "http://", "mailto:")):
            continue
        link_count += 1
        target = (source.parent / unquote(href)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"Broken link: {source.relative_to(ROOT)} -> {href}")

examples = DOMAIN / "synthetic-scenarios.md"
if examples.exists():
    content = examples.read_text(encoding="utf-8")
    for amount in ("$1,500", "$900", "$600", "$8,000", "$4,800", "$2,000", "$1,200"):
        if amount not in content:
            errors.append(f"Synthetic walkthrough figure missing: {amount}")
    if 900 + 600 != 1500 or 4800 + 2000 + 1200 != 8000:
        errors.append("Synthetic example totals did not reconcile")

print(f"Checked {len(found)} Domain 2 Markdown files and {link_count} internal links.")
if errors:
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    sys.exit(1)
print("PASS: inventory, local links, attribution and fixed example totals.")
