# Days 5–7 Guide: Compliance Framework Mapping

**Estimated time: 12–14 hours across 3 days**

## What You're Building

Over the next three days, you'll document controls from three major compliance frameworks, build a **cross-framework mapping** (also called a "cross-walk"), and perform a **gap analysis** for SecureTech Inc.

The cross-walk is the killer deliverable of this project. It demonstrates that you understand frameworks aren't isolated checklists — they overlap significantly, and a mature GRC program maps controls once and satisfies multiple frameworks simultaneously.

---

## What Is Compliance?

Compliance means meeting the requirements of external frameworks, regulations, or standards that apply to your organization. Companies pursue compliance because:

1. **Customers require it** — Enterprise buyers won't purchase from a vendor without SOC 2 or ISO 27001
2. **Regulations mandate it** — Privacy laws (GDPR, CCPA), industry regulations (HIPAA, PCI DSS)
3. **It's good business** — Frameworks codify security best practices; following them improves your security posture
4. **Competitive advantage** — Compliance certifications open doors to larger customers and markets

### Compliance vs. Security

Important distinction: **compliance ≠ security**. A company can be compliant (checked all the boxes) but not secure (the controls are poorly implemented). Conversely, a company can be very secure but not compliant (hasn't documented or audited their controls).

The goal of GRC is to make compliance and security work together — compliance as the floor, not the ceiling.

---

## The Three Frameworks

### NIST Cybersecurity Framework 2.0 (NIST CSF 2.0)

**What:** A voluntary framework created by the U.S. National Institute of Standards and Technology. It organizes cybersecurity activities into 6 high-level functions.

**Why companies use it:** Most widely referenced framework in the U.S. cybersecurity industry. Not a certification — it's a guide for building and assessing a security program. Many job postings list NIST CSF familiarity.

**Structure:**
```
6 Functions → Categories → Subcategories
```

| Function | Purpose | Key Question |
|---|---|---|
| **Govern (GV)** | Establish cybersecurity strategy, risk management, and oversight | "How do we manage our cybersecurity program?" |
| **Identify (ID)** | Understand your assets, risks, and business context | "What do we need to protect?" |
| **Protect (PR)** | Implement safeguards to ensure delivery of services | "How do we protect it?" |
| **Detect (DE)** | Discover cybersecurity events in a timely manner | "How do we know something happened?" |
| **Respond (RS)** | Take action when an incident is detected | "What do we do when something happens?" |
| **Recover (RC)** | Restore capabilities after an incident | "How do we get back to normal?" |

**New in 2.0:** The "Govern" function was added to emphasize that cybersecurity governance (risk management, strategy, supply chain) is foundational.

### SOC 2 Type II

**What:** An audit framework created by the American Institute of Certified Public Accountants (AICPA). A SOC 2 report is an independent auditor's opinion on whether a company's controls are properly designed (Type I) and operating effectively over time (Type II).

**Why companies use it:** Required by most enterprise customers for SaaS/cloud vendors. "Do you have a SOC 2?" is one of the first questions in a vendor security review.

**Structure:**
```
5 Trust Service Categories → Common Criteria (CC series)
```

| Category | Purpose | Relevant When |
|---|---|---|
| **Security** (CC series) | Protection against unauthorized access | Always — this is the baseline for every SOC 2 |
| **Availability** (A series) | Systems are available for operation and use | SLAs, uptime commitments |
| **Processing Integrity** (PI series) | System processing is complete, valid, and accurate | Financial systems, data processing |
| **Confidentiality** (C series) | Information designated as confidential is protected | Handling sensitive business data |
| **Privacy** (P series) | Personal information is collected, used, and disclosed properly | Handling PII |

**Key detail:** Security is always in scope. The other four categories are optional — companies choose which ones apply to their services.

**Type I vs Type II:**
- **Type I** — Controls are properly designed at a point in time (snapshot)
- **Type II** — Controls are operating effectively over a period of time (usually 6-12 months)
- Type II is the gold standard — it proves controls actually work over time, not just that they exist on paper

### ISO 27001:2022

**What:** An international standard for information security management systems (ISMS) published by the International Organization for Standardization. Companies can be certified by an accredited certification body.

**Why companies use it:** Recognized globally. Required by many European and international customers. The certification demonstrates a systematic approach to managing security.

**Structure:**
```
ISMS Requirements (Clauses 4-10) + Annex A Controls (93 controls in 4 themes)
```

| Annex A Theme | # Controls | Focus |
|---|---|---|
| **Organizational** | 37 | Policies, roles, asset management, access, supplier relationships |
| **People** | 8 | Screening, training, awareness, responsibilities, remote work |
| **Physical** | 14 | Physical security, equipment protection, clear desk |
| **Technological** | 34 | Technical controls: encryption, logging, network security, development |

**Key detail:** ISO 27001 requires a formal Information Security Management System (ISMS) — it's not just controls, it's a management framework for continuously improving security. This connects directly to the governance work you did in Days 1-2.

---

## Why Cross-Framework Mapping Matters

Most companies need to comply with multiple frameworks simultaneously. Without a cross-walk:
- You do the same work three times (write an access control policy for NIST, then again for SOC 2, then again for ISO 27001)
- You miss overlaps and waste resources
- You can't efficiently answer customer security questionnaires

With a cross-walk:
- Implement a control ONCE and check it off against all applicable frameworks
- Quickly identify which frameworks a specific control satisfies
- Efficiently respond to customer security questionnaires by knowing which evidence applies to which requirement

### Interview Gold

The cross-walk is your strongest interview talking point. It shows:
- You understand that frameworks overlap significantly
- You can think about compliance efficiently (implement once, satisfy many)
- You can build tools that save the organization time and money

---

## Worked Example: Cross-Walk Row

Here's how one control maps across all three frameworks:

| Control Area | NIST CSF 2.0 | SOC 2 | ISO 27001:2022 |
|---|---|---|---|
| **Access Control — Least Privilege** | PR.AA-05: Access permissions and authorizations are defined using least privilege and separation of duties | CC6.3: The entity authorizes, modifies, or removes access to data, software, functions, and other protected information assets based on roles | A.8.3: Access to information and information processing facilities shall be limited in accordance with the access control policy |

**What this tells you:** All three frameworks require access control based on least privilege. If SecureTech implements a strong access control system, it satisfies a requirement in all three frameworks simultaneously.

---

## Your Day 5-7 Checklist

### Day 5
- [ ] Read this guide completely
- [ ] Begin `framework_controls/nist_csf_2.md` — document relevant subcategories for each function
- [ ] Begin `framework_controls/soc2_criteria.md` — document key criteria for each Trust Service Category

### Day 6
- [ ] Finish framework control documents
- [ ] Complete `framework_controls/iso27001_annex_a.md` — document key controls for each theme
- [ ] Begin `compliance_matrix.md` — map controls across frameworks

### Day 7
- [ ] Finish `compliance_matrix.md`
- [ ] Complete `gap_analysis.md` 🏆 (challenge — less scaffolding!)
- [ ] Update your skills tracker
- [ ] Commit everything to GitHub

---

## Research Tips

- **NIST CSF 2.0:** The full framework is freely available at nist.gov. Focus on the subcategory descriptions — those tell you what's required.
- **SOC 2:** The Trust Service Criteria are published by AICPA. The CC (Common Criteria) series maps to COSO principles.
- **ISO 27001:2022:** The Annex A control list is widely published in summaries online. The full standard is paid, but you can find the control titles and descriptions in many free resources.

You don't need to memorize every control — focus on the controls that are most relevant to a company like SecureTech.

---

## When You're Done

You should be able to:
1. Explain the purpose and structure of each framework
2. Describe how they overlap and where they differ
3. Walk through a specific control and show how it maps across all three
4. Explain what a gap analysis is and how it guides remediation priorities
5. Articulate why a cross-walk saves an organization time and money

Practice this question: *"How would you approach compliance if your company needed both SOC 2 and ISO 27001?"* Your answer: "I'd build a cross-framework mapping to identify overlapping controls, implement them once, and track compliance across both frameworks simultaneously."
