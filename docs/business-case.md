# Business case and discovery brief

In this fictional scenario, branch staff submit onboarding requests by spreadsheet. Operations
re-enters them into a review queue. Missing fields and duplicate rows make readiness unclear.
This is a designed practice scenario; no stakeholder interviews have been conducted.

**Objective:** account for every source row as an accepted review case or an actionable exception.
In scope: validation, mapping, exception handling, reconciliation, reporting and UAT.
Out of scope: real account opening, identity verification, credit decisions, bank integrations and communications.

Success criteria: 100% source reconciliation, zero duplicate target keys, explicit exception
reasons and business acceptance. No cost savings or improvement percentages are invented.

## Discovery questions

1. Which fields are mandatory and who approves their definitions?
2. Can legitimate applicants share an email address?
3. Who verifies missing consent rather than merely filling the field?
4. May a partial batch proceed, and who accepts the unresolved cases?
5. How are corrections and approvals traced?

| Simulated role | Responsibility |
|---|---|
| Product owner | Scope and business acceptance |
| Branch representative | Validate intake workflow |
| Operations lead | Correct exceptions and review readiness |
| BA | Clarify requirements, mapping and traceability |
| Engineer / QA | Implement and test transformations |
| Privacy/compliance reviewer | Review real data handling before production use |

These are assumed roles, not actual participants or recorded approvals.
