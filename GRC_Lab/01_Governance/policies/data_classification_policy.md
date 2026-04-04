# Data Classification Policy

**SecureTech Inc.**
**Document Owner:** Chief Information Security Officer (CISO)
**Effective Date:** [Date you complete this]
**Last Review:** [Same date]
**Next Review:** [One year from effective date]
**Version:** 1.0

> 📖 **Instructions:** Fill in each section. Data classification is the foundation of data protection — you can't protect data appropriately if you don't know how sensitive it is. This policy defines the classification levels and handling rules for each.

---

## 1. Purpose

<!-- YOUR WORK: Write 2-3 sentences explaining why SecureTech needs a Data Classification Policy.

Think about:
- Not all data is equally sensitive — customer PII needs more protection than a marketing blog draft
- Without classification, employees either over-protect everything (slowing work down) or under-protect sensitive data (creating risk)
- Compliance frameworks require data classification (SOC 2, ISO 27001 both reference it directly)
-->

---

## 2. Scope

<!-- YOUR WORK: Define what's covered.

Think about:
- All data in all formats: digital files, emails, databases, paper documents, verbal discussions
- All storage locations: local drives, cloud storage, SaaS applications, email, backups
- All states: data at rest (stored), data in transit (being sent), data in use (being accessed)
- All people: employees, contractors, vendors who handle SecureTech data
-->

---

## 3. Roles & Responsibilities

<!-- YOUR WORK: Define roles for data classification.

Key roles:
- **Data Owners** — business leaders who determine the classification of data in their domain (e.g., VP of Engineering owns source code classification, VP of Sales owns customer data classification)
- **Data Custodians** — IT/engineering team members who implement the technical controls to protect data according to its classification
- **Data Users** — everyone who accesses data — responsible for handling it according to its classification
- **CISO** — owns the classification policy and framework
- **Legal/Compliance** — advise on regulatory requirements that affect classification (privacy laws, contractual obligations)

Key question: Who DECIDES a classification level vs. who ENFORCES it? These should be different roles.
-->

---

## 4. Policy Statements

<!-- YOUR WORK: Define classification levels and handling rules.

### 4.1 Classification Levels

Define 4 levels (this is the industry standard). For each level, describe:
- What kind of data falls into this category
- Examples specific to SecureTech

Suggested levels:

**Public** — Information intended for public release. No restrictions on sharing.
Examples: marketing materials, blog posts, public job listings

**Internal** — General business information not intended for public release. Low risk if disclosed.
Examples: internal meeting notes, org charts, non-sensitive project plans

**Confidential** — Sensitive business information that could cause harm if disclosed. Restricted access.
Examples: financial reports, business strategies, employee records, vendor contracts

**Restricted** — Highly sensitive data that would cause severe harm if disclosed. Strictest controls.
Examples: customer PII, encryption keys, authentication credentials, security vulnerability reports

### 4.2 Handling Requirements

Create a table showing what's required at each classification level:

| Requirement | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Encryption at rest | ... | ... | ... | ... |
| Encryption in transit | ... | ... | ... | ... |
| Access control | ... | ... | ... | ... |
| Sharing externally | ... | ... | ... | ... |
| Storage locations | ... | ... | ... | ... |
| Disposal method | ... | ... | ... | ... |
| Labeling required | ... | ... | ... | ... |

Fill in each cell with the specific requirement (e.g., "Required", "Not required", "Approved cloud storage only", "Secure deletion required", etc.)

### 4.3 Labeling
(How should classified documents be labeled? Headers, footers, file naming conventions, email subject line tags?)

### 4.4 Data in Specific Contexts
(Rules for: email, cloud storage, removable media, paper documents, verbal discussions in public places)

### 4.5 Reclassification
(Data classification can change — when and how does reclassification happen? Who approves it?)

### 4.6 Default Classification
(What classification applies to data that hasn't been explicitly classified? Most organizations default to "Internal" — not too restrictive, but not public.)
-->

---

## 5. Enforcement

<!-- YOUR WORK: Consequences for mishandling classified data.

Consider severity based on classification level:
- Mishandling Public data → probably just a reminder
- Mishandling Restricted data → serious consequences (investigation, possible termination)
- Intentional exfiltration of any classified data → termination + legal action
-->

---

## 6. Review Schedule

<!-- YOUR WORK: Review schedule table.

Additional triggers for data classification reviews:
- When new types of data are collected (new product, new customer segment)
- When regulations change (new privacy laws, updated contractual requirements)
- After a data breach or classification-related incident
-->

---

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | [Date] | [Your name] | Initial policy creation |
