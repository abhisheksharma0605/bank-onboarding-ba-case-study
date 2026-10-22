# UAT and traceability

[Matrix](traceability.csv) links eight requirements to ten scenarios.
[Executed evidence](../evidence/results.md) records data-check outcomes, not business sign-off.

Procedure: confirm fixture and mapping version; run the rehearsal; compare each source ID to
expected output; inspect both queues; record expected/actual result, tester, date and evidence
for manual cases. Preserve the baseline and make corrections in a separately versioned copy.

Entry: agreed example requirements and runnable fixture. Exit: Must requirements pass, no
high-impact defects, exceptions resolved or accepted, and business-owner sign-off. Human
workflow acceptance and Power BI verification are still pending.

## LAB-BA-01 — deliberately seeded duplicate

S007 repeats S001's email with capitals and spaces. A naive exact comparison could miss it.
Expected and actual: normalize, retain S001, quarantine S007. Evidence: UAT-06 and its unit test.
Severity in the scenario: high because duplicate intake creates conflicting work queues.
This is a laboratory condition, not a discovered FIS incident.

## Data issue versus software defect

If branch 999 is quarantined as required, the system passes its test but source data still needs
correction. If it loads into the target, the transformation has a defect. Neither a passing script
nor an unresolved source issue alone constitutes business acceptance.
