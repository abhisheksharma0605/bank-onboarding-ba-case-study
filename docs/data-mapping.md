# Source-to-target mapping

Grain: one submitted request per source_id. Accepted means ready for review, not an approved account.

| Source | Target | Rule | Exception |
|---|---|---|---|
| source_id | case_id | Preserve unique key | Duplicate source key fails batch |
| applicant_name | applicant_name | Trim | MISSING_NAME |
| email | email | Lowercase/trim; basic pattern | INVALID_EMAIL / DUPLICATE_EMAIL |
| branch_code | branch_code | Trim and reference lookup | UNKNOWN_BRANCH |
| consent | Validation only | Uppercase/trim; require Y | CONSENT_MISSING |
| submitted_date | submitted_date | Exact valid ISO date | INVALID_DATE |
| None | case_status | READY_FOR_REVIEW | Does not imply approval |

**Extract:** read CSV fixtures. **Transform:** normalize and evaluate SQL rules. **Load:** accepted
cases and an exception queue. **Validate:** reconcile the source against both outputs.

The email check is basic data quality, not RFC-complete validation or ownership verification.
Consent is a simulated field, not a legal determination. The date helper rejects February 30.
Every rehearsal rebuilds a full snapshot, not an incremental production load.

Reporting retains invalid raw dates in assessed.csv and uses null in the typed fact table.
Branch 999 has an explicit Unmapped branch dimension row so it cannot silently disappear.
