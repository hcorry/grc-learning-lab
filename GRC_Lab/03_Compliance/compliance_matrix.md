# Compliance Matrix (Cross-Framework Mapping) — SecureTech Inc.

**Document Owner:** CISO
**Version:** 1.0

> 📖 **Instructions:** This is the cross-walk — the document that maps equivalent controls across all three frameworks. This is your most impressive deliverable because it shows you understand that frameworks overlap and you can think about compliance efficiently.
>
> **Three worked example rows** are provided. You need to add **10-15 more rows** covering the major control areas.

---

## How to Read This Matrix

Each row represents a **control area** (e.g., "Access Control"). The columns show how each framework addresses that same area using its own terminology and numbering. When a control doesn't have an exact equivalent, use "Partial" or "N/A" and explain in the notes.

---

## Cross-Framework Control Mapping

### Worked Examples

| # | Control Area | NIST CSF 2.0 | SOC 2 | ISO 27001:2022 | Notes |
|---|---|---|---|---|---|
| 1 | **Access Control — Least Privilege** | PR.AA-05: Access permissions use least privilege and separation of duties | CC6.3: Access authorized, modified, or removed based on roles | A.8.3: Information access restriction | All three frameworks require role-based access with least privilege. Core control — satisfies requirements across the board. |
| 2 | **Security Awareness Training** | PR.AT-01: Personnel are provided awareness and training | CC1.4: Entity demonstrates commitment to attract, develop, and retain competent individuals + CC2.2: Entity communicates information to improve security | A.6.3: Information security awareness, education, and training | NIST and ISO have dedicated subcategories. SOC 2 addresses this across control environment (CC1) and communication (CC2). |
| 3 | **Incident Response** | RS.MA-01: Incident management plan is executed | CC7.3: Security incidents are evaluated + CC7.4: Incident response is executed | A.5.24: Incident management planning and preparation + A.5.26: Response to information security incidents | All three require incident response capability. ISO splits planning and response into separate controls. Your IR policy satisfies all three. |

---

### YOUR MAPPINGS START HERE

<!-- YOUR WORK: Add 10-15 more rows covering the major control areas below.

Control areas to map (suggested — you may combine or split as needed):

**Identity & Authentication**
- User identification, authentication (MFA), password management
- NIST: PR.AA series | SOC 2: CC6.1, CC6.2 | ISO: A.5.15, A.8.5

**Asset Management**
- Inventory of assets, ownership, classification
- NIST: ID.AM series | SOC 2: CC6.1 (partial) | ISO: A.5.9, A.5.10, A.5.12

**Data Protection / Encryption**
- Encryption at rest and in transit, data loss prevention
- NIST: PR.DS series | SOC 2: CC6.1, CC6.7, C1.1 | ISO: A.8.24, A.8.12

**Risk Assessment**
- Risk identification, analysis, response
- NIST: ID.RA series | SOC 2: CC3.1, CC3.2, CC9.1 | ISO: A.5.7 (not Annex A — this is in clauses 6.1, 8.2)

**Change Management**
- Controlled changes to systems and software
- NIST: PR.IP series | SOC 2: CC8.1 | ISO: A.8.9, A.8.25, A.8.32

**Logging & Monitoring**
- Audit logs, continuous monitoring, anomaly detection
- NIST: DE.CM, DE.AE series | SOC 2: CC7.1, CC7.2 | ISO: A.8.15, A.8.16

**Vulnerability Management**
- Vulnerability scanning, patching, remediation
- NIST: ID.RA-01, PR.IP series | SOC 2: CC7.1 | ISO: A.8.8

**Business Continuity / Recovery**
- Backup, disaster recovery, incident recovery planning
- NIST: RC.RP series | SOC 2: A1.2, A1.3 | ISO: A.5.29, A.5.30, A.8.13, A.8.14

**Third-Party / Vendor Management**
- Vendor security assessment, supply chain risk
- NIST: GV.SC series | SOC 2: CC9.2 | ISO: A.5.19, A.5.20, A.5.21

**Security Policy & Governance**
- Security policies, roles, organizational commitment
- NIST: GV.PO, GV.RR | SOC 2: CC1.1, CC1.2 | ISO: A.5.1, A.5.2

**Physical Security**
- Physical access controls, environmental protections
- NIST: PR.AA (partial), PR.IR | SOC 2: CC6.4, CC6.5 | ISO: A.7.1, A.7.2, A.7.3

**HR Security / Personnel**
- Screening, onboarding, offboarding, disciplinary
- NIST: PR.AA (access provisioning/deprovisioning) | SOC 2: CC1.4 | ISO: A.6.1-A.6.5

**Privacy / Data Handling**
- Personal data protection, consent, retention, disposal
- NIST: GV.PO (partial) | SOC 2: P series | ISO: A.5.33, A.5.34

Use this table format for your mappings:

| # | Control Area | NIST CSF 2.0 | SOC 2 | ISO 27001:2022 | Notes |
|---|---|---|---|---|---|
| 4 | **[Control Area]** | [Subcategory ID: Brief description] | [Criterion ID: Brief description] | [Control ID: Brief description] | [Notes on how well they align] |

Tips:
- Mappings don't have to be 1:1 — one NIST subcategory might map to multiple SOC 2 criteria
- If a framework doesn't have a direct equivalent, write "No direct equivalent — addressed indirectly by [X]" or "N/A"
- The Notes column is valuable — explain nuances, partial overlaps, or why a mapping isn't perfect
- Research actual control IDs — don't guess. Use the framework control documents you created.
-->

---

## Mapping Summary

<!-- YOUR WORK: After completing the matrix, answer these questions in 2-3 paragraphs:

1. Which control areas have the strongest overlap across all three frameworks? (These are your "implement once, satisfy all" opportunities)
2. Which control areas are unique to one framework or poorly represented in others?
3. What percentage of controls overlap across at least two frameworks? (Rough estimate is fine)
4. How would you use this matrix in practice? (Hint: vendor questionnaires, audit prep, prioritizing control implementation)
-->
