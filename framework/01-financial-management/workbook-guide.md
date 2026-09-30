# Financial management workbook instructions

[Download the workbook](tools/financial-management-starter.xlsx).

All awards, identifiers, organizations, and amounts are synthetic. The worksheets are independent. Budget review and Portfolio illustrate the same SYN-001 financial position, but edits are not automatically transferred between them. SEFA uses its own stated fiscal period.

Inputs use blue text and pale yellow fill. Calculations use formulas. Enter an explicit zero where appropriate. Preserve formulas when clearing sample data. Dates are descriptive controls: changing a date does not filter transactions because no transaction ledger is imported.

## Budget review

Use one award's federal-share approved budget period. Copy the worksheet for another award. Six category rows are provided, 13 through 18. Extend all formulas and totals when adding categories.

| Input | Definition |
| --- | --- |
| Approved budget | Current authorized budget for the selected period and funding share |
| Actuals to date | Recorded expenditures from that period's start through the cutoff, using the stated basis |
| Open obligations | Unliquidated commitments not already included in actuals |
| Uncommitted forecast | Estimated remaining expenditure excluding open obligations |

Balance after obligations = approved budget minus actuals minus open obligations.

Forecast total = actuals plus open obligations plus uncommitted forecast.

Forecast headroom = approved budget minus forecast total. A negative value indicates a projected funding shortfall. Actual budget used = actuals divided by budget. A zero denominator displays `n.a.`. It does not demonstrate allowability or the right to rebudget.

Missing numeric inputs produce review messages. Record credits and corrections only where supported by ledger documentation. Do not interpret remaining balance as cash available.

## Portfolio

Rows 8 through 22 support 15 awards. Use one unique internal award ID per row. Maintain the full award metadata in [award-register.md](award-register.md). Include authorized funding only. Do not include proposed funding or count overlapping funding increments twice.

Forecast total already includes actuals and obligations. The Portfolio worksheet subtracts it once from authorized funding. This worksheet does not determine reporting deadlines or periods of performance.

## SEFA preparation

Rows 8 through 20 support 13 award workpaper rows. Enter expenditures for the stated fiscal period, using a documented consistent basis. The template adds own direct costs, indirect costs, and amounts provided to subrecipients. Own direct costs must exclude the other two columns.

The sample Assistance Listing identifiers are fictional placeholders. Replace them with verified identifiers. Add program and cluster subtotals, required notes, and special-assistance workpapers before preparing a final schedule. Read [sefa-preparation.md](sefa-preparation.md).

## Cost allocation

Rows 9 through 15 support seven benefiting activities. Enter one allowable shared direct cost pool and a documented benefit measure. Include relevant nonfederal activities. Shares equal each activity's units divided by all measured units. Each allocation is rounded to cents.

The rounding-difference field compares the pool with the sum of allocations. Resolve a nonzero difference through a documented adjustment. Missing, negative, or collectively zero units require review. This schedule is not an indirect rate agreement or a personnel effort certification.

## Synthetic control totals

| Worksheet | Expected result |
| --- | --- |
| Budget review | Budget $200,000. Actuals $50,000. Open obligations $20,000. Uncommitted forecast $114,500. Forecast total $184,500. Balance after obligations $130,000. Forecast headroom $15,500. |
| Portfolio | Funding $430,000. Actuals $226,000. Open obligations $36,000. Balance after obligations $168,000. Forecast total $414,500. Forecast headroom $15,500. |
| SEFA preparation | Own direct costs $106,000. Indirect costs $11,000. Provided to subrecipients $13,000. Federal expenditures $130,000. |
| Cost allocation | Pool $12,000. Shares 60%, 30%, and 10%. Allocations $7,200, $3,600, and $1,200. Rounding difference $0.00. |

Recalculate after edits. Review missing-input messages and reconcile against independent source totals. When extending a schedule, extend its totals, formulas, conditional formatting, and review checks together. Record preparer, reviewer, date, and retained file location.

Project lead: David Amoah Oduro. Development material, September 30, 2026. [CC BY 4.0](../../LICENSE).
