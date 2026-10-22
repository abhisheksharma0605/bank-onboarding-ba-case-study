# Power BI readiness dashboard — build exercise

SQL totals and CSV outputs are tested. Power Query/DAX files are supplied for learning; they
have not been run in Power BI Desktop. No completed PBIX or report screenshot is claimed.

1. Run the rehearsal. Create a Text parameter DataFolder for the evidence folder's absolute path.
2. Create a blank query FactRequests; paste FactRequests.pq into Advanced Editor.
3. Import evidence/dim_branch.csv as DimBranch. Make branch_code Text in both tables.
4. Relate DimBranch[branch_code] (one) to FactRequests[branch_code] (many), single filter direction.
5. Create each measure in measures.dax separately; format Acceptance Rate as percentage.
6. Add four KPI cards, an outcome bar chart, a branch breakdown and a branch slicer.
7. Keep Invalid Date Requests visible. Date filtering excludes null dates; reconcile the full
   batch with date filters cleared.

| No-filter measure | Expected |
|---|---:|
| Requests | 12 |
| Accepted | 6 |
| Exceptions | 6 |
| Acceptance rate | 50% |
| Invalid date requests | 1 |

Central: 6 requests, 3 accepted. Riverside: 5 requests, 3 accepted. Unmapped: 1 request, 0 accepted.
Filtering outcome to ACCEPTED yields 100% acceptance in that selection, not overall readiness.
KEEPFILTERS retains the intersection of the selection and the measure condition.

Layout: navy title “Onboarding migration readiness — synthetic rehearsal”; four KPI cards;
exception reasons left and branch breakdown right. Footer: “Technical checks passed; business acceptance pending.”
Use labels as well as teal/amber colors. Save your own PBIX and image after verifying totals.

[Microsoft relationship guidance](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand).
