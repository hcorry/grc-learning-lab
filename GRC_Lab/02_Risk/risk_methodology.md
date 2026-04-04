# Risk Scoring Methodology — SecureTech Inc.

**Document Owner:** CISO
**Version:** 1.0
**Last Review:** [Date]

> 📖 **Instructions:** This document defines HOW SecureTech assesses risks. The guide (`day3_4_guide.md`) explains all the concepts — this document is where you formalize them for SecureTech. Much of the structure is provided; your job is to complete the sections marked `> **✏️ YOUR WORK**
> YOUR WORK` and customize the methodology to fit SecureTech's context.

---

## 1. Purpose

This document establishes the risk assessment methodology for SecureTech Inc. It defines how risks are identified, scored, categorized, and prioritized to ensure consistent and repeatable risk management.

---

## 2. Risk Scoring Framework

### 2.1 Likelihood Scale

| Score | Level | Description | Frequency Guidance |
|---|---|---|---|
| 1 | Rare | Could happen but very unlikely | Less than once every 5 years |
| 2 | Unlikely | Not expected but possible | Once every 2-5 years |
| 3 | Possible | Could reasonably happen | Once every 1-2 years |
| 4 | Likely | Probably will happen | Once or more per year |
| 5 | Almost Certain | Expected to happen regularly | Multiple times per year |

### 2.2 Impact Scale

> **✏️ YOUR WORK**
> YOUR WORK: Build SecureTech's impact scale. The guide provides a generic version — customize it for SecureTech's context.
>
> For each level (1-5), define the impact across these dimensions:
> - Financial (what dollar amounts make sense for a funded startup with ~100 employees?)
> - Operational (how much disruption to the business?)
> - Reputational (how does it affect SecureTech's brand and customer trust?)
> - Legal/Regulatory (what compliance or legal consequences?)
>
> Fill in the table below:
>
> | Score | Level | Financial Impact | Operational Impact | Reputational Impact | Legal/Regulatory Impact |
> |---|---|---|---|---|---|
> | 1 | Negligible | ... | ... | ... | ... |
> | 2 | Minor | ... | ... | ... | ... |
> | 3 | Moderate | ... | ... | ... | ... |
> | 4 | Major | ... | ... | ... | ... |
> | 5 | Catastrophic | ... | ... | ... | ... |
>
> Think about what each level means for a company SecureTech's size. $1M is catastrophic for a startup but a rounding error for a Fortune 500. Calibrate accordingly.

### 2.3 Risk Matrix

```
Impact →    1-Negligible  2-Minor  3-Moderate  4-Major  5-Catastrophic
Likelihood↓
5-Almost Certain    5         10        15        20         25
4-Likely            4          8        12        16         20
3-Possible          3          6         9        12         15
2-Unlikely          2          4         6         8         10
1-Rare              1          2         3         4          5
```

### 2.4 Severity Thresholds and Required Actions

| Score Range | Severity | Color | Required Action | Review Frequency |
|---|---|---|---|---|
| 20-25 | **Critical** | Red | Immediate executive attention. Treatment plan within 7 days. | Weekly until mitigated |
| 12-19 | **High** | Orange | Treatment plan required within 30 days. CISO oversight. | Monthly |
| 6-11 | **Medium** | Yellow | Treatment plan required within 90 days. | Quarterly |
| 1-5 | **Low** | Green | Monitor and review at next assessment cycle. | Annually |

---

## 3. Risk Appetite Statement

> **✏️ YOUR WORK**
> YOUR WORK: Write SecureTech's risk appetite statement.
>
> Risk appetite defines how much risk the organization is willing to accept in pursuit of its objectives. This is a BUSINESS decision, not just a security decision.
>
> Consider:
> - SecureTech is a cybersecurity company — reputational risk from a breach would be especially damaging
> - SecureTech is a startup — it needs to move fast and can't eliminate all risk
> - SecureTech has customers who trust it with sensitive data
>
> Write 2-3 paragraphs that address:
> 1. Overall risk appetite (low? moderate? where does SecureTech draw the line?)
> 2. Risk tolerance by severity (e.g., "Critical and High risks are not accepted and must be treated. Medium risks may be accepted with CISO approval and documented justification. Low risks are generally accepted.")
> 3. Areas of zero tolerance (e.g., risks involving customer data breach, regulatory non-compliance, etc.)
>
> Example opening: "SecureTech Inc. maintains a [low/moderate] risk appetite, reflecting our position as a cybersecurity company entrusted with..."

---

## 4. Risk Categories

> **✏️ YOUR WORK**
> YOUR WORK: Define the risk categories you'll use in the risk register. This makes scoring consistent and ensures you cover all areas.
>
> Suggested categories (customize as needed):
>
> | Category | Description | Examples |
> |---|---|---|
> | Cloud & Infrastructure | ... | ... |
> | People & Culture | ... | ... |
> | Access & Identity | ... | ... |
> | Data Protection | ... | ... |
> | Compliance & Legal | ... | ... |
> | Operations & Business Continuity | ... | ... |
> | Third-Party / Vendor | ... | ... |
> | Physical Security | ... | ... |
>
> For each category, write a 1-sentence description and 2-3 example risks.

---

## 5. Assessment Process

> **✏️ YOUR WORK**
> YOUR WORK: Describe the process for conducting a risk assessment at SecureTech.
>
> Cover:
> 1. **Who participates?** (CISO leads, department heads contribute risks from their areas)
> 2. **How often?** (Annual comprehensive assessment, plus ad-hoc for new projects/changes)
> 3. **What's the process?** (Identify risks → Score likelihood and impact → Calculate risk score → Assign severity → Determine treatment → Document in risk register)
> 4. **How are disagreements resolved?** (If two people score a risk differently, who decides?)
> 5. **How are results communicated?** (Risk register shared with executive team, summary to board)
>
> Write this as a numbered procedure (5-7 steps).

---

## 6. Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | [Date] | [Your name] | Initial methodology |
