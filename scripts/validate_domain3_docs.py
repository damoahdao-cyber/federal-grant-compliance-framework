#!/usr/bin/env python3
"""Check FGCF Domain 3 draft Markdown consistency.

This is a mechanical documentation check. It does not assess legal accuracy,
award-specific eligibility, privacy compliance or practical effectiveness.
"""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = ROOT / "framework" / "03-eligibility-program-management"
REQUIRED = {
    "README.md",
    "program-eligibility-rule-register.md",
    "award-intake-and-readiness.md",
    "participant-eligibility-decision.md",
    "case-file-and-service-delivery.md",
    "program-workplan-and-monitoring.md",
    "change-control-and-escalation.md",
    "regulatory-source-register.md",
    "synthetic-worked-examples.md",
    "review-checklist.md",
}
errors = []
files = set(p.name for p in DOMAIN.glob("*.md"))
if REQUIRED - files:
    errors.append("Missing required documents: " + ", ".join(sorted(REQUIRED - files)))
if files - REQUIRED:
    print("Additional Domain 3 documents:", ", ".join(sorted(files - REQUIRED)))
internal_links = 0
for source in sorted(DOMAIN.glob("*.md")):
    content = source.read_text(encoding="utf-8")
    if "CC BY 4.0" not in content:
        errors.append(f"Missing attribution in {source.relative_to(ROOT)}")
    for match in re.finditer(r"\]\(([^)]+)\)", content):
        url = match.group(1).strip().split("#", 1)[0]
        if not url or url.startswith(("https://", "http://", "mailto:")):
            continue
        internal_links += 1
        destination = (source.parent / unquote(url)).resolve()
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            errors.append(f"Missing local target: {source.relative_to(ROOT)} -> {url}")

sample = DOMAIN / "synthetic-worked-examples.md"
if sample.exists():
    content = sample.read_text(encoding="utf-8")
    for token in ("**5 eligible**", "**2 pending**", "**1 ineligible**", "**8**", "**62.5%**",
                  "**12 documented training sessions**", "**7**", "**5**", "**58.33%**"):
        if token not in content:
            errors.append(f"Synthetic example field absent: {token}")
    if 5 + 2 + 1 != 8 or 5 / 8 * 100 != 62.5:
        errors.append("Eligibility example totals do not reconcile")
    if 7 + 5 != 12 or round(7 / 12 * 100, 2) != 58.33:
        errors.append("Workplan example totals do not reconcile")
print(f"Examined {len(files)} Domain 3 Markdown documents and {internal_links} local links")
if errors:
    for issue in errors:
        print("FAIL:", issue, file=sys.stderr)
    sys.exit(1)
print("PASS: required docs, attribution, local references and fixed synthetic arithmetic")
