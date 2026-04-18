# Evidence Collection Guide — ISO 27001:2022 Audit

> This guide tells you exactly what to request from the auditee for each control domain. Use this to prepare your evidence request list before fieldwork.

---

## Pre-Audit Document Request List

Send this to the auditee 10 business days before fieldwork:

### Policies & Procedures
- [ ] Information Security Policy (all versions, current + previous)
- [ ] All subsidiary policies (access control, IR, change mgmt, BCP, vendor risk, data classification)
- [ ] Statement of Applicability (SoA) — current version
- [ ] Risk Assessment and Risk Treatment Plan
- [ ] ISMS Scope document

### Governance
- [ ] ISMS Management Review minutes (last 12 months)
- [ ] Risk Committee meeting minutes (last 4 quarters)
- [ ] Internal audit programme and last 2 audit reports
- [ ] Previous external audit/certification body report and NC closure evidence
- [ ] CISO/DPO appointment letters

### Access Control
- [ ] User access review reports (last 4 quarters)
- [ ] Privileged account inventory
- [ ] Joiner/Mover/Leaver process documentation
- [ ] MFA implementation evidence (configuration screenshots)
- [ ] PAM vault reports (if applicable)
- [ ] Role-based access matrix

### Incident Management
- [ ] Incident register / ITSM incident list (last 12 months)
- [ ] Last 3 major incident Post-Incident Reviews
- [ ] Tabletop exercise report (last 12 months)
- [ ] Regulatory incident notifications made (if any)

### Supplier Management
- [ ] Third-party vendor register
- [ ] Last 3 vendor security assessment reports
- [ ] Sample of 3 supplier contracts (security clauses)
- [ ] Data Processing Agreements for top-5 data processors

### Change Management
- [ ] Change advisory board (CAB) minutes (last 3 months)
- [ ] Change request log (last 90 days)
- [ ] Emergency change log (last 12 months)
- [ ] Evidence of segregation of duties in change process

### Vulnerability & Patch Management
- [ ] Last 3 vulnerability scan reports
- [ ] Patch management KPI dashboard
- [ ] Last penetration test report + remediation tracker

### Business Continuity
- [ ] Business Continuity Plan (current)
- [ ] Business Impact Analysis (BIA)
- [ ] Last DR test report with RTO/RPO results

### Training & Awareness
- [ ] Security awareness training completion report (last 12 months)
- [ ] Phishing simulation results
- [ ] New joiner onboarding security training records

### Technical Configurations
- [ ] Backup policy + last successful restoration test evidence
- [ ] SIEM logging configuration + retention settings
- [ ] Network topology diagram (high-level)
- [ ] Encryption standards documentation

---

## Evidence Evaluation Criteria

| Evidence Type | Strength | Notes |
|--------------|---------|-------|
| System-generated logs/reports | **High** | Objective, difficult to fabricate |
| Policy documents | **Medium** | Document existence ≠ implementation |
| Interview responses | **Medium** | Corroborate with other evidence |
| Observation (system demo) | **High** | You see it working in real-time |
| Management representations | **Low** | Require corroborating evidence |
| Historical records | **High** | Shows sustained compliance |

---

## Audit Sampling Guidelines

| Population | Minimum Sample | Sample Method |
|-----------|---------------|---------------|
| User access rights review | 25 users or 10%, whichever is larger | Random |
| Privileged account review | All (or 100% if ≤20; 50% if >20) | Judgement |
| Change requests | 25 or 10% of total, min 5 | Random |
| Vendor assessments | All Tier 1; 20% Tier 2 | Risk-based |
| Security incidents | All Major; 20% Minor | Judgement |
| Training records | 25 or 10%, whichever is larger | Random |

---
*Methodology: ISO 19011:2018 | Auditor: [Name] | Document: EVD-GUIDE-001*
