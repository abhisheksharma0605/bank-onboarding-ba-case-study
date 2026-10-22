# Release recommendation: NO-GO

All 12 source rows reconcile, but six exceptions remain and business UAT has not occurred.
A successful script run does not authorize deployment under this scenario's release gate.

| Risk | Impact | Proposed owner | Mitigation |
|---|---|---|---|
| Email duplicate key | Distinct people conflated | Product owner | Agree a stronger key |
| Missing consent | Invalid intake accepted | Operations | Verify evidence; never invent permission |
| Unknown branch | Incorrect routing | Branch lead | Confirm mapping |
| Null date hidden in charts | Misleading totals | BI analyst | Retain invalid-date count |
| Automation mistaken for sign-off | Premature release | Release owner | Separate technical and business gates |

## CR-01 — permit unknown branches (proposed, not approved)

Benefit: fewer exceptions. Risk: inaccurate routing and metrics. Recommend rejecting a blanket
bypass; confirm mapping or formally design an unassigned queue with accountable ownership.
Affected artifacts: BA-03, mapping, UAT-04, branch dimension and release gate.

## Cutover / rollback — conceptual

Freeze a versioned source; rehearse in isolation; inspect exceptions; correct with evidence;
rerun; complete human UAT; obtain release-owner approval. Retain the source and prior target
version. To roll back, stop routing, restore the prior verified target and reconcile again.
The demo rebuilds an in-memory database and has no production deployment.

The corrected-fixture test produces 12 accepted rows. It proves rule behaviour, not actual
permission from applicants or stakeholder approval of any correction.
