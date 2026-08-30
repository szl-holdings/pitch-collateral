# Security diligence index

| Control area | Required evidence | State |
|---|---|---|
| Ownership and scope | Promoted services, data flows, owners, environments | PARTIAL |
| Threat model | Assets, actors, trust boundaries, abuse cases, mitigations | NOT YET PREPARED |
| Identity/access | Account inventory, MFA, least privilege, access review | NOT YET PREPARED |
| Secrets | Storage, rotation, scanning, incident handling | NOT YET PREPARED |
| Supply chain | Dependencies, pins, SBOM, signatures, attestations by artifact | PARTIAL |
| CI/CD | Protected change flow, exact-head checks, deployment authority | PARTIAL |
| Runtime | Isolation, persistence, backups, restore, availability, logging | PARTIAL |
| Data | Classification, encryption, retention, deletion, residency | NOT YET PREPARED |
| Detection/response | Logs, alerts, incident plan, exercises, incident history | NOT YET PREPARED |
| Vulnerability management | Disclosure, triage, patch SLAs, external assessment | PARTIAL |
| Business continuity | Recovery objectives, tested restore, dependencies | NOT YET PREPARED |
| Compliance | Applicability and scoped external evidence | NONE EVIDENCED |

## Truth boundary

A workflow run, SBOM, signature, HTTP 200, runtime status, or roadmap is not a security certification or production-readiness finding. Each promoted artifact needs its own source, build, signature, deployment, runtime, and limitation evidence.

