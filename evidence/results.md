# Executed migration rehearsal

Run UTC: 2026-10-22T19:41:36.086805+00:00

**12 source requests = 6 accepted + 6 quarantined. Acceptance rate: 50%.**

| Source | Expected | Actual | Result |
|---|---|---|---|
| S001 | ACCEPTED | ACCEPTED | PASS |
| S002 | ACCEPTED | ACCEPTED | PASS |
| S003 | ACCEPTED | ACCEPTED | PASS |
| S004 | ACCEPTED | ACCEPTED | PASS |
| S005 | ACCEPTED | ACCEPTED | PASS |
| S006 | ACCEPTED | ACCEPTED | PASS |
| S007 | DUPLICATE_EMAIL | DUPLICATE_EMAIL | PASS |
| S008 | UNKNOWN_BRANCH | UNKNOWN_BRANCH | PASS |
| S009 | CONSENT_MISSING | CONSENT_MISSING | PASS |
| S010 | INVALID_EMAIL | INVALID_EMAIL | PASS |
| S011 | MISSING_NAME | MISSING_NAME | PASS |
| S012 | INVALID_DATE | INVALID_DATE | PASS |

All fixture data checks passed. Business UAT and Power BI Desktop validation are pending. Release recommendation: **NO-GO**, because six exceptions remain unresolved and business acceptance has not occurred.
