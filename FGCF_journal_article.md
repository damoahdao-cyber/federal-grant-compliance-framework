# Building an Openly Licensed Federal Grant Compliance Framework

## A knowledge commons design and proposed evaluation

**David Amoah Oduro**  
Project lead, Federal Grant Compliance Framework  
Contact: damoah.dao@gmail.com

**Working paper, revised September 30, 2026.** This is a framework design paper and evaluation proposal. It is not represented as a published or peer-reviewed journal article. The legacy filename is retained for link continuity. The project is in early development. Independent practitioner review, operational testing, and pilot evaluation remain pending.

## Abstract

The Federal Grant Compliance Framework (FGCF) is an openly licensed resource-development project for nonprofit and research organizations administering U.S. federal awards. It aims to translate selected grant administration requirements into practical guides, editable schedules, and review checklists. The proposed architecture contains seven domains, with initial resources currently available in financial management and reporting. The present package includes a starter workbook, workbook instructions, seven supporting guides or templates, and synthetic worked examples. This paper describes the design rationale, current artifact, source mapping, and a proposed sequence of technical review and feasibility evaluation. Knowledge commons scholarship informs the approach to sharing and maintaining resources. Design science research informs the proposed cycle of building, inspecting, using, and revising the artifact. Neither literature establishes this framework's effectiveness. Limited development checks cover synthetic calculations, document links, and worksheet presentation. No participant data, adoption evidence, validated assessment instrument, or effectiveness results are reported. Future evaluation should document the version used, organizational context, review methods, permissions, and actual findings before making outcome claims.

Keywords: federal awards, nonprofit financial management, compliance resources, knowledge commons, design science, implementation.

## 1. Purpose and problem definition

Federal award administration involves maintaining award information, reconciling financial records, comparing expenditures with budgets, preparing reports, documenting controls, and applying award-specific requirements. For example, 2 CFR 200.302 sets financial management requirements, including award identification, records, and budget comparison. A reusable schedule may help organize these tasks, but completing a template does not itself establish that an organization meets the requirements.

FGCF addresses a practical design question: how can an openly licensed set of resources help professionals organize selected requirements and document their work in a consistent, inspectable way? Its intended users include nonprofit finance and grants professionals, research administration teams, and program staff responsible for award records. The project does not assume that these organizations have identical needs, systems, staffing, or award terms.

This paper does not estimate national compliance failure rates, market prices, or savings. It reports no systematic review, audit-database analysis, or practitioner survey. Claims about the prevalence of problems or the absence of competing resources would require a separately documented method and evidence. The current rationale is a proposal to develop useful resources and test their usefulness, rather than a claim that the proposed approach has already solved a measured national problem.

## 2. Conceptual design rationale

### 2.1 Knowledge commons

Frischmann, Madison, and Strandburg (2014) describe a framework for studying how knowledge and information are shared and governed. FGCF draws on that perspective to consider attribution, participation, resource boundaries, maintenance responsibilities, and revision rules. This is a proposed application to grant administration resources. It does not demonstrate that open licensing alone improves compliance.

The current materials use CC BY 4.0, except where separately identified. Attribution and modification notices support traceability as users adapt resources. Prior CC0 permissions for earlier distributions remain valid. The project lead currently maintains the repository. Contribution guidelines and a code of conduct provide initial participation rules. A functioning advisory council, sustained contributor community, or institutional partnership has not been documented.

### 2.2 Artifact development and evaluation

Hevner, March, Park, and Ram (2004) discuss building and evaluating artifacts in design science research. FGCF adapts that broad approach as a development rationale: define the intended task, build a resource, inspect it against sources and examples, seek user feedback, revise it, and evaluate use. The current package represents early artifact development. It is not a completed design science evaluation.

Implementation context also matters. Damschroder and colleagues (2009) developed the Consolidated Framework for Implementation Research in health services. Its attention to organizational setting, individuals, and implementation processes offers a conceptual starting point for future interview topics. Any use in federal award administration requires adaptation and review. It does not validate a new questionnaire or justify transferring findings from health services to nonprofit finance.

## 3. Framework architecture and current scope

The proposed architecture preserves seven domains:

| Domain | Intended scope | September 2026 status |
| --- | --- | --- |
| 1. Financial Management and Reporting | Award records, budgets, cash procedures, allocation, financial reports, SEFA working data | Initial workbook, instructions, seven supporting guides or templates |
| 2. Compliance Policies and Procedures | Written procedures and policy development | Scope page only |
| 3. Eligibility Verification and Program Management | Award-specific eligibility and program administration | Scope page only |
| 4. Reporting and Performance Management | Program reporting and performance documentation | Scope page only |
| 5. Subrecipient Monitoring | Subaward administration and monitoring | Scope page only |
| 6. Audit Readiness and Internal Controls | Control documentation, issue follow-up, audit preparation | Scope page only |
| 7. Training and Capacity Building | Learning resources and implementation support | Scope page only |

The domains are an organizational structure, not a claim of complete regulatory coverage. The six scope-only domains do not contain finished operating tools. The resource inventory, limitations, and review status are recorded in [STATUS.md](STATUS.md) and the [framework index](framework/README.md).

## 4. Initial financial management artifact

The starter workbook contains five worksheets: Budget review, Portfolio, SEFA preparation, Cost allocation, and Read me. The four numerical schedules are independent. They do not connect to a ledger, select transactions by date, or synchronize amounts with each other. Inputs must be reconciled to authorized records for the stated scope and period.

The Budget review worksheet separates actual expenditures, open obligations, and additional uncommitted forecast costs. This distinction helps users avoid counting obligations twice and separates a current balance from forecast headroom. The Portfolio worksheet provides award-level balances and forecasts. A positive portfolio total must not conceal a deficit on an individual award or be treated as authority to shift costs between awards.

The Cost allocation worksheet illustrates a proportional allocation of a shared direct cost using a documented benefit basis, including nonfederal activities where applicable. It does not implement an indirect cost rate agreement or certify personnel effort. The SEFA preparation worksheet organizes component expenditure amounts and award identifiers. Users must separately address program and cluster presentation, required notes, special assistance treatments, and reconciliation. It is not a complete SEFA.

Supporting resources cover an award register, budget monitoring, cash management procedures, shared direct cost allocation, financial reporting review, SEFA preparation, and an award monitoring checklist. Each resource provides a starting structure to adapt to applicable requirements. The [workbook guide](framework/01-financial-management/workbook-guide.md) records input conventions and row limits.

## 5. Source mapping and applicability

The initial source basis includes selected provisions of 2 CFR Part 200. The [development record](docs/development-record.md) maps them to resources and records the source review date. Financial management and control resources refer to sections 200.302 and 200.303. Payment and budget revision guides refer to sections 200.305 and 200.308. Financial reporting review refers to section 200.328. Cost treatment and allocation refer to sections 200.403, 200.405, and 200.414. SEFA preparation refers to sections 200.502 and 200.510.

This mapping supports traceability, not agency approval or certification. Users must identify the provisions, effective requirements, agency guidance, and award terms applicable to their circumstances. Source updates may require revising instructions or examples. A maintenance record should identify the reviewed source version and the resulting change. The framework should avoid hardcoding a universal reporting deadline, payment method, or cost treatment where applicability varies.

## 6. Development checks completed

The workbook was recalculated using the authoring calculation engine. Baseline results were compared with separately specified expected values. Input-change checks covered a zero budget, missing forecast input, an additional portfolio row within the designed range, changed subrecipient amounts, and zero, missing, or negative allocation units. Temporary changes were restored before export. The restored workbook was scanned for formula errors, and each worksheet was rendered for layout review. Exported records were inspected for the expected cached values.

The synthetic budget example has $200,000 budget, $50,000 actual expenditures, $20,000 obligations, and $114,500 additional forecast costs. Its balance after obligations is $130,000, estimated total cost is $184,500, and forecast headroom is $15,500. The allocation example distributes $12,000 using 60, 30, and 10 usage units, producing $7,200, $3,600, and $1,200. The separate SEFA example totals $130,000 federal expenditures, including $13,000 provided to subrecipients.

These checks are limited development evidence. They do not establish complete formula coverage, behavior in every spreadsheet application, regulatory adequacy, user comprehension, or effectiveness in operating organizations. Native Excel or Google Sheets testing and independent practitioner review remain pending. Synthetic examples are not participant data.

## 7. Proposed evaluation

### 7.1 Review before operational testing

The next stage should obtain technical and usability feedback on a defined version. Reviewers should have relevant grant administration, finance, internal control, or audit preparation experience. Their relationship to the project, development involvement, and conflicts should be recorded accurately. Review coverage should identify specific files and tasks rather than implying examination of the entire proposed framework.

The [review brief and feedback form](docs/practitioner-review/README.md) ask reviewers to trace examples, identify misleading instructions, assess stated scope, and propose corrections. They are review aids, not validated assessment instruments. Findings should be logged with their source, practical consequence, correction, and revised version. Names, affiliations, and quotations should be disclosed only with appropriate permission.

### 7.2 Feasibility pilot

A later feasibility pilot could assess whether users can complete defined tasks, understand limitations, and integrate selected resources into their processes. No participating organizations, recruitment commitments, or sample size are reported here. Recruitment and the design should be specified after technical review and a realistic assessment of access and resources.

Before collecting data, document the protocol, participant permissions, confidentiality arrangements, and any applicable ethics review determination. Record the resource version and training provided. Predefine tasks and measures, such as task completion, reconciliation errors, time required, unresolved questions, and documentation completeness against a task-specific rubric. A proposed rubric should undergo content review and user testing before being called validated.

Collect baseline information about existing procedures, award complexity, systems, staffing, and prior experience. Maintain an issue log during use. Interviews could explore clarity, workflow fit, and the burden of adapting the materials. Record negative findings and nonuse as well as favorable comments. The pilot should primarily describe feasibility and needed revisions.

### 7.3 Analysis and outcome boundaries

A small feasibility study may support descriptive findings but cannot automatically establish causal effects on audit findings or financial performance. Differences over time may reflect staffing changes, award mix, other interventions, or reporting changes. Any later comparative outcome study requires an appropriate design, predefined outcomes, adequate follow-up, and a justified sample-size approach.

Report denominators, missing data, the exact version used, and limitations. Distinguish individual practitioner feedback from institutional adoption and distinguish adoption from demonstrated outcomes. Publish data or quotations only where permissions and confidentiality allow. If raw data cannot be released, explain the available documentation rather than promising unrestricted public access.

## 8. Governance and next development stages

The [roadmap](ROADMAP.md) proposes resource expansion, independent review, feasibility evaluation, and consideration of a stable package. These stages depend on evidence and maintenance capacity. The alpha version label identifies a development package and does not prove a formal release has been published. Release status should be verified against GitHub's release record.

Future governance could add reviewers and maintainers with documented responsibilities. Such arrangements should follow actual agreement and participation. Regulatory maintenance should identify ownership, review triggers, and handling of significant corrections. Contributors should use original or appropriately licensed material and synthetic or authorized examples.

## 9. Limitations and conclusion

FGCF currently provides a small initial financial management resource set within a broader proposed architecture. It has no documented independent review, operational evaluation, adoption record, or demonstrated effectiveness. Its sources and conceptual influences explain a design approach, not an empirical finding. This working paper replaces unsupported statements in the earlier draft with an explicit account of what exists and what remains proposed. Earlier versions remain in repository history.

The immediate contribution is a reviewable artifact: editable schedules, practical guides, synthetic examples, and a transparent development record. The next contribution must come from documented review and use. Claims about benefit should follow that evidence and remain proportionate to its quality and scope.

## References and source links

- Damschroder, L. J., Aron, D. C., Keith, R. E., Kirsh, S. R., Alexander, J. A., and Lowery, J. C. (2009). Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science. *Implementation Science*, 4, Article 50. https://doi.org/10.1186/1748-5908-4-50
- Frischmann, B. M., Madison, M. J., and Strandburg, K. J. (Eds.). (2014). *Governing Knowledge Commons*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199972036.001.0001
- Hevner, A. R., March, S. T., Park, J., and Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1). [Publisher repository record](https://aisel.aisnet.org/misq/vol28/iss1/6/).
- Electronic Code of Federal Regulations. *2 CFR Part 200: Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards*. Selected sections reviewed September 30, 2026. [Official eCFR](https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200). Section links and resource mapping appear in the [development record](docs/development-record.md).
- Creative Commons. *Attribution 4.0 International*. [License terms](https://creativecommons.org/licenses/by/4.0/legalcode).

## Author and artifact statement

David Amoah Oduro is identified as project lead and author of this framework design working paper. No institutional sponsorship or endorsement is asserted by that designation. The repository contains materials prepared and revised with AI-assisted drafting and development. Maintainer checks are documented separately from independent review. This paper reports no human-participant study and no empirical results. Framework citation metadata appear in [CITATION.cff](CITATION.cff).
