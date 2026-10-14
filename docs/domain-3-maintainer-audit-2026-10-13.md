# Domain 3 maintainer drafting and consistency audit

Audit date: October 13, 2026. Scope: draft Domain 3 resource set and associated development-status files. This is an internal source and documentation check. It is **not** an external legal opinion, an independent practitioner review, a real beneficiary eligibility assessment, a system privacy/security audit, operational adoption, or a pilot evaluation.

## Scope reviewed

- Six original draft procedures for source-based eligibility rules, award intake, participant decisions, service-delivery records, program milestones, and change approvals.
- One regulatory source register, four wholly fictional scenarios, one structured review checklist, and the Domain 3 index.
- Framework and root indexes, STATUS, CHANGELOG and ROADMAP for consistent status descriptions.
- One Python documentation-validation script and one GitHub Actions workflow, both subject to actual CI execution verification.

## Dated reference checks

Checked section identity and key operative distinctions for the following references on October 13, 2026. eCFR pages inspected presented Title 2 current through October 8–9, 2026, with the last reported amendment on August 17, 2026. These dates describe *displayed source editions*, not blanket applicability to any historic award.

| Topic | Reference checked | Draft treatment |
| --- | --- | --- |
| Funding opportunity and applicant eligibility | [2 CFR 200.204](https://www.ecfr.gov/current/title-2/section-200.204), [Appendix I](https://www.law.cornell.edu/cfr/text/2/appendix-I_to_part_200) | The NOFO supplies eligible applicant types and restrictions |
| Applicant registration | [2 CFR 25.200](https://www.ecfr.gov/current/title-2/section-25.200) | Applicant / recipient UEI and SAM obligations have specified exceptions; they are not participant checks |
| Agency applicant review | [2 CFR 200.205](https://www.ecfr.gov/current/title-2/section-200.205), [200.206](https://www.ecfr.gov/current/title-2/section-200.206) | Agency merit and risk assessment are not universal individual beneficiary screening |
| Award conditions and performance goals | [2 CFR 200.211](https://www.ecfr.gov/current/title-2/section-200.211), [200.208](https://www.ecfr.gov/current/title-2/section-200.208), [200.301](https://www.ecfr.gov/current/title-2/section-200.301) | Extract authorized award objectives, specific conditions and indicators rather than inventing measures |
| Privacy and internal control | [2 CFR 200.303](https://www.ecfr.gov/current/title-2/section-200.303) | Safeguard participant records in restricted systems and document applicable controls |
| Program activity oversight | [2 CFR 200.329](https://www.ecfr.gov/current/title-2/section-200.329) | Track actual award program activities and source evidence, separately from official performance reports |
| Budget and program revisions | [2 CFR 200.308](https://www.ecfr.gov/current/title-2/section-200.308) | Check scope changes and specified approvals even if no budget change occurs |
| Covered lower-tier transactions | [2 CFR 180.300](https://www.ecfr.gov/current/title-2/section-180.300), [200.332](https://www.ecfr.gov/current/title-2/section-200.332) | Do not equate subrecipient exclusion verification with individual program participant eligibility; 180.300 includes three methods |

## Mechanical review

- Retrieved ten Domain 3 Markdown documents from the development branch.
- Resolved relative cross-references against the expected repository files; no missing internal targets were found in this audited set.
- Confirmed each of the ten Domain 3 Markdown documents contains CC BY 4.0 attribution.
- Recalculated illustrative totals: 5 eligible + 2 pending + 1 ineligible = 8 total cases, 5/8 = 62.5%; 7 completed + 5 remaining = 12 planned sessions, 7/12 = 58.33% when rounded to two decimal places.
- Checked the Domain 3 README index against the nine linked supporting Markdown resources.
- Added [Python validation](../scripts/validate_domain3_docs.py) and [CI workflow](../.github/workflows/domain3-doc-checks.yml) to automate file inventory, local link, attribution and static example checks on relevant future changes. A successful live GitHub Actions run has not yet been verified.
- Source section identity was reviewed selectively; the entire set of external URLs has not undergone complete automated HTTP/status validation.

## Defects and corrections during drafting

1. Replaced an unverified eCFR Appendix I URL with the known Appendix I citation hosted by Cornell Law School.
2. Corrected the number of fictional scenarios in STATUS so they are not described as real eligibility cases.
3. Corrected the ROADMAP description of Domain 2, already merged into the main branch.

## Outstanding review before operational use

- Program-specific eligibility requirements must be supplied from a **real** applicable award, law, agency policy and approved source version. No one should screen a real beneficiary using only these samples.
- Obtain documented feedback from professionals with relevant grants program, privacy, compliance and award management expertise; record conflicts and permissions.
- Test confidential records, access, exceptions, reconsideration processes and service evidence within an appropriately authorized organizational system before claiming adoption or effectiveness.
- Independently validate CI run status and review external hyperlinks.
- Do not conflate a maintainer review of regulatory source headings with legal certification or an agency compliance determination.

Prepared for internal development review. Project lead: David Amoah Oduro. [CC BY 4.0](../LICENSE).
