# ISO 27001:2022 Annex A — Master Audit Checklist

**Audit Reference:** AUD-[YEAR]-[NNN]  
**Auditee:** [Organization Name]  
**Auditor:** [Lead Auditor Name]  
**Audit Date:** [DATE]  
**Scope:** [ISMS Scope Statement]

---

## How to Use This Checklist

**Conformance Ratings:**
- ✅ **C** — Conforming: Control implemented and effective
- ⚠️ **PC** — Partial Conformance: Control exists but has gaps
- ❌ **NC-Mi** — Minor Non-Conformance: Isolated gap, systemic risk low
- 🔴 **NC-Ma** — Major Non-Conformance: Systemic failure or absent control
- ➖ **N/A** — Not Applicable: Justified exclusion in SoA

---

## 5. Organisational Controls

### A.5.1 — Policies for Information Security

**Objective:** Management direction and support for information security.

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| IS policy exists and is current (reviewed within 12 months) | Document review | Policy document with review date | | |
| Policy approved by appropriate management | Document review | Approval signature / ISMS minutes | | |
| Policy communicated to all staff and relevant external parties | Interview + records | Training records, intranet screenshots | | |
| Topic-specific policies exist (access control, IR, BCP, etc.) | Document review | List of subsidiary policies | | |
| Policies available to all applicable personnel | Observation | Intranet / SharePoint access test | | |

**Auditor Notes:**

---

### A.5.2 — Information Security Roles and Responsibilities

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| CISO/security role formally appointed | Document review | Job description, org chart | | |
| Responsibilities documented and communicated | Interview | Role descriptions, RACI matrix | | |
| Conflicts of interest addressed | Interview + review | SOD matrix | | |
| Contact with authorities defined | Document review | IRP §5 — regulatory contacts | | |

---

### A.5.3 — Segregation of Duties

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| SOD conflicts identified and managed | Document review | SOD matrix, access role matrix | | |
| No single individual controls entire sensitive process | Observation + testing | IT role assignments; change mgmt records | | |
| **SOX ITGC**: Developer cannot deploy to production | Testing | Access logs; deployment pipeline roles | | |

**⚠️ Banking/SOX Note:** This is one of the most frequently cited ITGC deficiencies. Test specifically: Can the same person raise, approve, and deploy a change?

---

### A.5.15 — Access Control

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Access control policy documented and current | Document review | POL-ACP-003 | | |
| Access provisioned on least-privilege basis | Testing | Sample of 10 user access profiles vs job roles | | |
| Privileged access formally approved | Document review | Approval records for 5 privileged accounts | | |
| Access reviews conducted at least quarterly | Document review | Access review sign-offs for last 4 quarters | | |
| Terminated employee access revoked within SLA | Testing | 5 leaver cases — access revocation timestamps | | |
| MFA enforced for remote and privileged access | Technical testing | MFA enforcement policy + screenshots | | |

**Sampling Note:** For access control, test a sample of:
- 10 active users (mix of roles)
- 5 privileged/admin accounts
- 5 terminated employee accounts (last 3 months)
- 3 vendor/third-party accounts

---

### A.5.19 — Information Security in Supplier Relationships

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Third-party register maintained | Document review | Vendor register with tier classification | | |
| Security requirements in supplier contracts | Document review | 3 sample contracts — security clauses | | |
| DPA executed for data-processing vendors | Document review | DPAs for all data processors | | |
| Right-to-audit clause in Tier 1 contracts | Document review | 2 Tier 1 contracts | | |
| Supplier security assessments conducted | Document review | Last assessment for top 3 vendors | | |
| Ongoing monitoring of supplier security posture | Interview + demo | Security rating reports (BitSight/SSC) | | |

---

### A.5.24–A.5.27 — Incident Management

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Incident response policy and procedures documented | Document review | POL-IRP-004 | | |
| IR team roles and contacts defined | Document review | IR team roster, contact list | | |
| Incident classification criteria defined | Document review | Severity matrix in IRP | | |
| Incidents logged and tracked | System demo | ITSM/GRC system — incident register | | |
| PIR conducted for major incidents | Document review | PIR reports for last 2 major incidents | | |
| IR tested (tabletop or live) in last 12 months | Document review | Tabletop exercise report | | |
| Regulatory notification timelines documented | Document review | IRP §6 — notification requirements | | |

---

### A.5.29–A.5.30 — Business Continuity

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| BCP documented and current | Document review | BCP with review date | | |
| RTO/RPO defined for critical systems | Document review | BIA document | | |
| BCP/DR tested in last 12 months | Document review | Test report with results | | |
| Backups encrypted and offsite | Technical review | Backup configuration + encryption confirmation | | |
| Backup restoration tested | Document review | Last successful restoration test report | | |

---

## 6. People Controls

### A.6.3 — Information Security Awareness

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Awareness programme exists | Document review | Training programme documentation | | |
| All staff complete annual training | Records review | Training completion report (≥90% target) | | |
| Role-based training for technical staff | Records review | Specialist training records | | |
| Phishing simulation conducted | Document review | Phishing campaign results | | |
| New joiners trained within first week | Records review | 5 new joiner training records | | |

---

## 8. Technological Controls

### A.8.8 — Management of Technical Vulnerabilities

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Vulnerability scanning programme in place | Document review | Scan policy + schedule | | |
| Scans conducted at least monthly (critical assets) | System demo | Scan reports for last 3 months | | |
| Critical vulnerabilities patched within defined SLA | Records review | Patch management KPI dashboard | | |
| Vulnerability risk-rated (CVSS scoring) | System demo | Vulnerability management platform | | |
| Penetration testing conducted annually | Document review | Last pentest report + remediation status | | |

**Benchmark SLAs:**
- Critical (CVSS 9.0+): Patch within **72 hours**
- High (CVSS 7.0–8.9): Patch within **30 days**
- Medium (CVSS 4.0–6.9): Patch within **90 days**
- Low (CVSS <4.0): Next maintenance cycle

### A.8.15–A.8.16 — Logging and Monitoring

| Test | Method | Evidence Required | Result | Finding |
|------|--------|------------------|--------|---------|
| Logging policy defined (what events, retention periods) | Document review | Logging standard | | |
| SIEM/log management platform operational | System demo | SIEM dashboard | | |
| Log retention meets regulatory requirements | Configuration review | SIEM retention settings | | |
| Privileged access logged and reviewed | System demo | Sample of privileged access logs | | |
| Security alerts actioned within defined SLA | Records review | Alert-to-closure metrics | | |
| Log integrity protected (logs cannot be altered) | Configuration review | Log forwarding to immutable storage | | |

---

## Findings Summary

| Control | Finding Type | Description | Severity |
|---------|-------------|-------------|----------|
| | | | |
| | | | |
| | | | |

**Total Findings:**
- Major Non-Conformances: ___
- Minor Non-Conformances: ___
- Observations: ___
- Conforming: ___
- Not Applicable: ___

**Compliance Score:** ___/93 controls assessed as conforming = ____%

---

*Auditor Signature: _________________ Date: _________*
