# Domain 2 maintainer audit

Date: October 13, 2026. Scope: the Domain 2 draft development branch and associated status documents. This records authoring and desk checks, not independent legal advice, practitioner review, operational assurance, or a completed pilot.

## Work reviewed
- Six procedural starters: allowable costs, procurement, personnel cost documentation, travel, conflicts of interest, and record retention.
- Regulatory source register, four synthetic scenarios, domain index, and review checklist.
- Repository-wide status language relevant to release and stage descriptions.

## Source verification method and results
The maintainer compared critical rules to federal sources and noted limitations. The eCFR pages checked displayed Title 2 **up to date as of October 9, 2026** and last amended August 17, 2026. This is a source-edition observation, not a determination that the same version controls every earlier award.

| Area | Evidence reviewed on October 13 | Finding or limitation |
| --- | --- | --- |
| Procurement recipient classes | [2 CFR 200.317](https://www.ecfr.gov/current/title-2/section-200.317) | Clarified the exceptions for States and Indian Tribes versus other recipients and subrecipients |
| Procurement standards and thresholds | [2 CFR 200.318](https://www.ecfr.gov/current/title-2/section-200.318), [200.320](https://www.ecfr.gov/current/title-2/section-200.320) | Verified applicable method categories, price-reasonableness support, documented recipient thresholds, higher micro-purchase rules and noncompetitive circumstances |
| General FAR thresholds | [Acquisition.gov threshold changes](https://www.acquisition.gov/threshold-changes) and [effective-date table](https://www.acquisition.gov/tableofeffectivedatesforMPTandSAT) | General micro-purchase threshold $15,000; simplified acquisition threshold $350,000, effective October 1, 2025; neither substitutes for a recipient's verified procedures and award requirements |
| Cost principles | [200.403](https://www.ecfr.gov/current/title-2/section-200.403), [200.404](https://www.ecfr.gov/current/title-2/section-200.404), [200.405](https://www.ecfr.gov/current/title-2/section-200.405), [200.406](https://www.ecfr.gov/current/title-2/section-200.406), [200.407](https://www.ecfr.gov/current/title-2/section-200.407) | Checked principal allowability, reasonableness, allocability, credits and approval references |
| Personnel records | [2 CFR 200.430](https://www.ecfr.gov/current/title-2/section-200.430) | Clarified nonexempt daily hours and the limits of budget estimates for interim charges |
| Conflict of interest | [2 CFR 200.112](https://www.ecfr.gov/current/title-2/section-200.112), [200.318(c)](https://www.ecfr.gov/current/title-2/section-200.318) | Distinguished agency-policy disclosure from procurement recusal obligations |
| Retention | [2 CFR 200.334](https://www.ecfr.gov/current/title-2/section-200.334), supplemented by [Cornell LII text](https://www.law.cornell.edu/cfr/text/2/200.334) | The direct eCFR page sometimes restricted automated viewing. Checked retention triggers and exceptions against an accessible secondary rendering; formal version-specific review remains necessary |
| Travel | [2 CFR 200.475](https://www.ecfr.gov/current/title-2/section-200.475), supplemented by [2026 regulatory rendering](https://ecfr.io/Title-2/Section-200.475) | The direct eCFR page sometimes restricted automated viewing. Confirmed whole-trip reimbursement-method language in alternate displayed text; version-specific follow-up remains open |

## Automated / mechanical checks
- The Domain 2 index and nine linked supporting Markdown files were fetched successfully.
- Relative links within the Domain 2 resource set were resolved against expected repository paths, with no missing local targets in that scope. A second branch audit retrieved 20 changed/relevant files and checked 27 Domain 2 relative links, with zero unresolved targets in that set.
- Added `scripts/validate_domain2_docs.py` and `.github/workflows/domain2-doc-checks.yml` to provide ongoing local-link, inventory, attribution and fixed-example integrity checks. The workflow was committed, but successful execution by GitHub Actions is not claimed without inspecting an actual job result.
- Synthetic allocations recalculated: $900 + $600 = $1,500; $4,800 + $2,000 + $1,200 = $8,000.
- All nine linked supporting Markdown documents include development status and CC BY 4.0 attribution.
- Relevant source references were spot-checked for section identity; the entire set of offsite links has **not** been independently crawled with a reliable HTTP status report.

## Changes prompted by review
1. Distinguished state and tribal procurement rules from general subrecipient standards.
2. Clarified that an increased micro-purchase threshold requires the relevant self-certification or agency approval.
3. Clarified personnel supporting records and after-the-fact interim-charge adjustments.
4. Clarified limits on agency or pass-through retention extensions.
5. Reclassified September 2026 release notes as historical preparation records. A published GitHub release **was not independently confirmed or disproved** during this review.

## Open review items
- Obtain paragraph-level independent review and practical usability feedback from qualified grants or financial compliance practitioners.
- Verify each external reference on the specific award-applicable date, including occasional eCFR access restrictions.
- Apply organizational policy, award-specific conditions, procurement deviations, records requirements, and relevant agency implementation before using these procedures.
- Confirm current GitHub release/tag metadata and any external archival deposit separately. Do not claim the earlier prerelease's present status on the basis of a prepared release note.
- Test the example workflows in an approved organizational setting before reporting adoption or effectiveness.

## Evidence and claims policy
This review is a **maintainer desk audit**, not an independent compliance opinion. The repository may describe these resources as drafted and internally checked, not as certified, field-tested, independently endorsed, or proven effective. Store any future signed review reports privately unless the reviewer explicitly authorizes public disclosure.
