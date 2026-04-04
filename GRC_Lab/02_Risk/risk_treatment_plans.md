# Risk Treatment Plans — SecureTech Inc.

**Document Owner:** CISO
**Version:** 1.0

> 📖 **Instructions:** Every risk in your risk register needs a treatment plan. This document says what you're going to DO about each risk. Three worked examples are provided to match the three example risks in the register. You'll write treatment plans for all remaining risks.

---

## How to Write a Treatment Plan

For each risk, decide one of the four strategies:

| Strategy | When to Use |
|---|---|
| **Mitigate** | You can reduce the risk with reasonable effort/cost |
| **Accept** | The risk is within appetite, or mitigation costs more than the potential loss |
| **Transfer** | Someone else can bear the risk better (insurance, outsourcing) |
| **Avoid** | The risk is unacceptable and you can eliminate the activity causing it |

Then document: what you'll do, why, the timeline, and what the risk score becomes after treatment (residual risk).

---

## Treatment Plans

### RISK-001: Phishing Attack Compromises Employee Credentials

> ℹ️ **Worked example**

| Field | Value |
|---|---|
| **Risk ID** | RISK-001 |
| **Current Risk Score** | 16 (High) |
| **Treatment Strategy** | **Mitigate** |
| **Justification** | Score exceeds risk appetite. Phishing is the most common and likely attack vector. Cost of mitigation is reasonable compared to potential breach costs. |
| **Planned Actions** | 1. Deploy advanced email filtering with AI-based phishing detection (reduces Likelihood) |
| | 2. Implement monthly phishing simulation exercises with mandatory remedial training for employees who fail (reduces Likelihood) |
| | 3. Enforce MFA on ALL systems, not just some (reduces Impact — compromised password alone is insufficient) |
| | 4. Implement data loss prevention (DLP) monitoring on email and cloud storage (reduces Impact) |
| **Action Owner** | CISO (overall), IT Director (email filtering, MFA), HR (training coordination) |
| **Timeline** | Email filtering: 30 days. MFA enforcement: 45 days. Phishing simulations: 60 days. DLP: 90 days. |
| **Residual Likelihood** | 2 (Unlikely) |
| **Residual Impact** | 2 (Minor) |
| **Residual Risk Score** | **4 (Low)** — Within risk appetite |

---

### RISK-002: Cloud Infrastructure Misconfiguration

> ℹ️ **Worked example**

| Field | Value |
|---|---|
| **Risk ID** | RISK-002 |
| **Current Risk Score** | 15 (High) |
| **Treatment Strategy** | **Mitigate** |
| **Justification** | A public data exposure would be catastrophic for a cybersecurity company's reputation. The cost of automated scanning tools is minimal compared to potential damage. |
| **Planned Actions** | 1. Deploy Cloud Security Posture Management (CSPM) tool for automated configuration scanning (reduces Likelihood) |
| | 2. Implement infrastructure-as-code (IaC) with mandatory security review in CI/CD pipeline (reduces Likelihood) |
| | 3. Establish "secure defaults" templates for common cloud resources (reduces Likelihood) |
| | 4. Conduct monthly cloud configuration audits (detective control) |
| **Action Owner** | VP of Engineering (IaC, secure defaults), CISO (CSPM tool, audits) |
| **Timeline** | CSPM deployment: 30 days. IaC security review: 60 days. Secure defaults: 60 days. Monthly audits: begin immediately. |
| **Residual Likelihood** | 1 (Rare) |
| **Residual Impact** | 5 (Catastrophic) — Impact doesn't change; we reduced the chance, not the consequence |
| **Residual Risk Score** | **5 (Low)** — Within risk appetite |

> 💡 **Notice:** The residual Impact stayed at 5. That's realistic — if a misconfiguration DID happen, it would still be catastrophic. The controls reduced the Likelihood from 3 to 1. This is common — some risks can only be mitigated on one dimension.

---

### RISK-003: Key Person Dependency

> ℹ️ **Worked example**

| Field | Value |
|---|---|
| **Risk ID** | RISK-003 |
| **Current Risk Score** | 12 (High) |
| **Treatment Strategy** | **Mitigate** |
| **Justification** | At 100 employees, key person dependencies are inevitable but manageable. The cost of documentation and cross-training is low compared to the disruption of losing a critical team member. |
| **Planned Actions** | 1. Identify all single points of failure — who holds unique knowledge? (assessment) |
| | 2. Require documentation of critical processes in a shared knowledge base (reduces Impact) |
| | 3. Implement cross-training program — each critical function must have at least 2 people capable (reduces Impact) |
| | 4. Include knowledge transfer in offboarding procedures (reduces Impact of voluntary departures) |
| **Action Owner** | Department Heads (identify SPOFs, cross-training), CISO (process documentation standard) |
| **Timeline** | SPOF identification: 14 days. Documentation initiative: ongoing, 50% complete in 90 days. Cross-training: ongoing, key roles covered in 120 days. |
| **Residual Likelihood** | 4 (Likely) — People will still leave; we can't change that |
| **Residual Impact** | 2 (Minor) — With documentation and cross-training, departure is a manageable disruption |
| **Residual Risk Score** | **8 (Medium)** — Acceptable with CISO review |

> 💡 **Notice:** The Likelihood stayed at 4. You can't stop people from leaving a startup. But you CAN reduce the Impact by ensuring knowledge isn't locked in one person's head. This is a good example of treating only one dimension.

---

## YOUR TREATMENT PLANS START HERE

<!-- YOUR WORK: Write a treatment plan for EVERY remaining risk in your risk register.

Use this format for each:

### RISK-XXX: [Short Title from Risk Register]

| Field | Value |
|---|---|
| **Risk ID** | RISK-XXX |
| **Current Risk Score** | [Score] ([Severity]) |
| **Treatment Strategy** | **[Mitigate / Accept / Transfer / Avoid]** |
| **Justification** | [Why this strategy? 1-2 sentences.] |
| **Planned Actions** | [Numbered list of specific actions] |
| **Action Owner** | [Who's responsible for each action?] |
| **Timeline** | [When will each action be completed?] |
| **Residual Likelihood** | [New score] ([Level]) |
| **Residual Impact** | [New score] ([Level]) |
| **Residual Risk Score** | **[New score] ([Severity])** |

Guidelines:
- Most risks should be MITIGATED — that's the most common strategy
- Include at least 1-2 ACCEPTED risks (low-scoring ones)
- Consider TRANSFERRING at least one risk (cyber insurance is a common example)
- If any risk should be AVOIDED, explain why eliminating the activity makes business sense
- Residual risk should be lower than current risk (unless you're accepting it)
- Timelines should be realistic for a startup — don't say "immediately" for everything
- Action owners should match the Risk Owner or delegate to someone appropriate
-->

---

## Treatment Summary

<!-- YOUR WORK: After completing all treatment plans, fill in this summary.

| Risk ID | Title | Current Score | Strategy | Residual Score | Status |
|---|---|---|---|---|---|
| RISK-001 | Phishing attack | 16 (High) | Mitigate | 4 (Low) | In Progress |
| RISK-002 | Cloud misconfiguration | 15 (High) | Mitigate | 5 (Low) | Planned |
| RISK-003 | Key person dependency | 12 (High) | Mitigate | 8 (Medium) | Planned |
| ... | ... | ... | ... | ... | ... |

Status options: Planned, In Progress, Completed
-->

---

## Risk Appetite Compliance Check

<!-- YOUR WORK: After completing all treatment plans, answer these questions:

1. Are all residual risk scores within SecureTech's risk appetite? (Check against your risk_methodology.md)
2. How many risks are you accepting vs. mitigating vs. transferring vs. avoiding?
3. Are there any residual risks still rated Critical or High? If so, why are they acceptable?
4. What's the total cost/effort of all planned mitigations? Is it realistic for a startup?

Write 2-3 paragraphs summarizing.
-->
