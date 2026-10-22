# Process and requirements

## As-is

~~~mermaid
flowchart LR
  A[Branch spreadsheet] --> B[Manual re-entry]
  B --> C[Missing or duplicate request]
  C --> D[Email follow-up]
  D --> B
~~~

## To-be

~~~mermaid
flowchart LR
  A[Source batch] --> B[Normalize and validate]
  B --> C{Rules pass?}
  C -->|Yes| D[Ready-for-review cases]
  C -->|No| E[Exception queue]
  E --> F[Operations corrects source]
  F --> A
  D --> G[Reconcile]
  E --> G
  G --> H[Human release decision]
~~~

| ID | User story | Acceptance criterion |
|---|---|---|
| BA-01 | As operations, I need all input accounted for | Source = accepted + exceptions; duplicate source_id fails batch |
| BA-02 | As reviewer, I need usable contact fields | Trim name; lowercase/trim email; quarantine blank name or malformed email |
| BA-03 | As branch operations, I need accurate routing | Branch must exist in reference data |
| BA-04 | As product owner, I need permission captured | Consent must normalize to Y |
| BA-05 | As operations, I need duplicates flagged | Same normalized email keeps lowest source_id and quarantines later IDs |
| BA-06 | As reviewer, I need usable dates | Exact ISO date and valid calendar day required |
| BA-07 | As analyst, I need complete reporting | Every source ID remains visible, including invalid dates and unknown branches |
| BA-08 | As release owner, I need explicit acceptance | No go-live without reconciled data, resolved/accepted exceptions and business sign-off |

All are Must requirements for this exercise. Email is a weak duplicate surrogate: households may
share addresses. A production design requires an approved request/identity key. Lowest source_id
is deterministic, not necessarily the earliest submission. Only the first failing rule is reported.

Proposed non-functional needs: access control, retained audit evidence, recoverable imports, masked
test data and performance targets measured against an agreed batch size. These are not implemented
or certified production capabilities in this lab.
