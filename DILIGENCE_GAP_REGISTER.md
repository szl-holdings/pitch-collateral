# Diligence gap register

**Updated:** 2026-08-30

| ID | Area | Gap | State | Risk | Closure evidence |
|---|---|---|---|---|---|
| DD-001 | Financing | Monthly operating model and runway scenarios absent | NOT YET PREPARED | Financing ask cannot be reconciled | Board/founder-approved model with assumptions and version |
| DD-002 | Corporate | Entity, good standing, capitalization, and obligations index absent | NOT YET PREPARED | Ownership and financing diligence incomplete | Counsel-reviewed corporate index and source documents |
| DD-003 | IP | Founder/contributor assignment record absent | NOT YET PREPARED | Chain of title unproved | Executed assignments and contributor schedule |
| DD-004 | Licensing | Estate-wide dependency and license-obligation schedule absent | NOT YET PREPARED | Distribution obligations unknown | Revisioned SBOM/license report per promoted artifact |
| DD-005 | Commercial | No independently verified customer, pilot, LOI, revenue, or pipeline evidence | NONE EVIDENCED | Product-market and financing claims unsupported | Dated interview records, agreements, invoices, and reconciled CRM/finance records |
| DD-006 | Market | Bottom-up buyer, pricing, cycle, and conversion model absent | NOT YET PREPARED | Market and growth assumptions ungrounded | Cited assumption model tied to customer discovery |
| DD-007 | Product | Roadmap not reconciled to financing milestones and acceptance criteria | PARTIAL | Use-of-funds narrative not executable | Milestone roadmap with owner, budget, dependency, date, and evidence gate |
| DD-008 | Runtime | Promoted deployment evidence varies by surface | PARTIAL | Reachability may be mistaken for production | Source/artifact/deployment/served-revision receipt and runtime witness |
| DD-009 | Hugging Face | Governed-receipt verifier had served fail-open code older than current signed source | VERIFIED | Regressions could reintroduce permissive receipt acceptance | Remediation and runtime witness: `HF_VERIFIER_RUNTIME_EVIDENCE_2026-08-30.md`; live Space `59cfd859608c22925a1161967217a4338779d006`; byte-equal signed source `7d5976f089bec8af95aec915a7485d8091253190` |
| DD-010 | Security | DDQ, control matrix, risk register, incident history, and external assessment incomplete | NOT YET PREPARED | Enterprise security diligence incomplete | Scoped security package and dated evidence |
| DD-011 | Privacy/legal | Terms, privacy, DPA, subprocessors, export posture, and counsel review incomplete | NOT YET PREPARED | Customer contracting path incomplete | Counsel-reviewed current documents and applicability matrix |
| DD-012 | Metrics | No customer/user/revenue/retention KPI history established | NONE EVIDENCED | Repository activity may be misread as traction | Instrumented, defined, reconciled KPI report |

Close a gap only when the named evidence exists and is reviewed. Do not downgrade risk because a roadmap or draft exists.

The August 26 static-Space 404 conclusion is superseded: those probes used noncanonical `*.hf.space` hosts. Current static Spaces serve from Hugging Face's API-reported `*.static.hf.space` hosts.
