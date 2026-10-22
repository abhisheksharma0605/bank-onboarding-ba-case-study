![From requirements to release](assets/banner.svg)

# Banking onboarding implementation

**The migration passes its checks. Should the bank go live?**

A fictional bank is replacing spreadsheet intake with a structured review queue. This BA case
study follows the problem through requirements, mapping, migration rehearsal, UAT and a release decision.

**12 synthetic requests → 6 accepted + 6 quarantined.** The data controls pass. The simulated
release remains **NO-GO** until exceptions and business acceptance are resolved.

| Explore the work | Question it answers |
|---|---|
| [Business case](docs/business-case.md) | What problem are we solving? |
| [Process and requirements](docs/requirements.md) | What must the solution do? |
| [Data mapping](docs/data-mapping.md) | How should each field change? |
| [UAT and traceability](docs/uat.md) | How do we prove the rules work? |
| [Release decision](docs/release-decision.md) | What prevents go-live? |
| [Executed evidence](evidence/results.md) | What happened in the rehearsal? |
| [SQL reports](sql/reporting.sql) | Do the counts reconcile? |
| [Power BI exercise](powerbi/README.md) | How can the data support a dashboard? |

## Run the rehearsal

Python 3.10+, no extra packages. Open a terminal in this project folder:

~~~shell
python run_case_study.py
python -m unittest discover -s tests -v
~~~

The script loads CSV fixtures into fresh in-memory SQLite, applies rules and exports evidence.
It does not connect to a bank. [Follow the walkthrough](WALKTHROUGH.md).

**Skills:** business analysis, requirements, process mapping, ETL validation, SQL, UAT and release readiness.

Independent, AI-assisted practice; not a client engagement or employment deliverable.
Power BI import files and measures are provided; Desktop execution and a finished PBIX are pending.
No KYC verification, account approval or production impact is claimed. [Provenance](PROVENANCE.md).
