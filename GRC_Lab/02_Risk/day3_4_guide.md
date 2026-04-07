# Days 3–4 Guide: Risk Management

**Estimated time: 10–12 hours across 2 days**

## What You're Building

Over the next two days, you'll build a complete **risk management program** for SecureTech Inc. This includes the methodology for how you score risks, a register of 15-20 realistic risks, and treatment plans for addressing each one.

Risk management is the engine of GRC — governance tells you the rules, compliance tells you the standards, but risk management tells you **where to focus your limited resources**.

---

## What Is Risk Management?

Risk management is the process of identifying, analyzing, and responding to risks that could affect your organization. In GRC, this means information security risks — things that could compromise the confidentiality, integrity, or availability of your data and systems.

### The Risk Management Lifecycle

```
Identify → Assess → Treat → Monitor → (repeat)
```

1. **Identify** — What could go wrong? (threats, vulnerabilities, scenarios)
2. **Assess** — How likely is it? How bad would it be? (scoring)
3. **Treat** — What do we do about it? (mitigate, accept, transfer, avoid)
4. **Monitor** — Is the risk changing? Are our controls working? (ongoing)

This lifecycle never ends — it's continuous. New risks emerge, existing risks change, and your controls need regular evaluation.

### Key Risk Terms

| Term | Definition | Example |
|---|---|---|
| **Threat** | Something that could cause harm | A hacker, a natural disaster, a disgruntled employee |
| **Vulnerability** | A weakness that a threat could exploit | Unpatched software, weak passwords, no backups |
| **Risk** | The combination of a threat exploiting a vulnerability | A hacker (threat) exploits unpatched software (vulnerability) to steal customer data |
| **Likelihood** | How probable is this risk? | 1 (Rare) to 5 (Almost Certain) |
| **Impact** | How severe would the consequences be? | 1 (Negligible) to 5 (Catastrophic) |
| **Risk Score** | Likelihood × Impact | Score of 1-25, mapped to severity levels |
| **Control** | Something that reduces likelihood or impact | A firewall, a policy, employee training |
| **Residual Risk** | Risk remaining after controls are applied | Even with controls, some risk remains |
| **Risk Appetite** | How much risk the organization is willing to accept | "We accept risks scoring 8 or below" |

---

## The 5×5 Risk Matrix

This is the standard approach for scoring risks. You'll build your own in `risk_methodology.md`.

### How It Works

Each risk gets two scores:
- **Likelihood** (1-5): How likely is this to happen?
- **Impact** (1-5): If it happens, how bad is it?

**Risk Score = Likelihood × Impact** (range: 1-25)

### Likelihood Scale

| Score | Level | Description |
|---|---|---|
| 1 | Rare | Could happen but very unlikely (less than once every 5 years) |
| 2 | Unlikely | Not expected but possible (once every 2-5 years) |
| 3 | Possible | Could happen (once every 1-2 years) |
| 4 | Likely | Probably will happen (once or more per year) |
| 5 | Almost Certain | Expected to happen (multiple times per year) |

### Impact Scale

| Score | Level | Description |
|---|---|---|
| 1 | Negligible | Minimal impact, easily absorbed. No customer impact. |
| 2 | Minor | Small financial loss (<$10K), minor operational disruption, limited to one team |
| 3 | Moderate | Meaningful financial loss ($10K-$100K), multiple teams affected, minor reputational damage |
| 4 | Major | Significant financial loss ($100K-$1M), operations severely impacted, customer trust affected |
| 5 | Catastrophic | Existential threat (>$1M loss), data breach requiring notification, regulatory action, major press coverage |

### Risk Matrix (Likelihood × Impact)

```
Impact →    1-Negligible  2-Minor  3-Moderate  4-Major  5-Catastrophic
Likelihood↓
5-Almost Certain    5         10        15        20         25
4-Likely            4          8        12        16         20
3-Possible          3          6         9        12         15
2-Unlikely          2          4         6         8         10
1-Rare              1          2         3         4          5
```

### Severity Thresholds

| Score Range | Severity | Required Action |
|---|---|---|
| 20-25 | **Critical** | Immediate action required. Executive attention. |
| 12-19 | **High** | Treatment plan required within 30 days. |
| 6-11 | **Medium** | Treatment plan required within 90 days. |
| 1-5 | **Low** | Monitor and review at next assessment cycle. |

---

## The Four Risk Treatment Strategies

When you've scored a risk, you need to decide what to do about it. There are exactly four options:

### 1. Mitigate (Reduce)
**What:** Implement controls to reduce the likelihood or impact.
**When:** The risk is too high to accept, and you can do something about it.
**Example:** Risk: Employee falls for phishing email. Mitigation: Deploy email filtering + conduct phishing awareness training.

### 2. Accept
**What:** Acknowledge the risk and do nothing (or continue with current controls).
**When:** The risk is within your risk appetite, or the cost of mitigation exceeds the potential loss.
**Example:** Risk: Minor typo on internal wiki page. Accept: The impact is negligible and not worth a formal process.

### 3. Transfer
**What:** Shift the risk to a third party (insurance, outsourcing, SLAs).
**When:** You can't mitigate effectively, but someone else can absorb the risk.
**Example:** Risk: Data center flood. Transfer: Use cloud hosting (AWS/Azure assumes infrastructure risk) + purchase cyber insurance.

### 4. Avoid
**What:** Eliminate the risk by eliminating the activity that creates it.
**When:** The risk is too high and can't be adequately mitigated or transferred.
**Example:** Risk: Storing customer SSNs creates regulatory liability. Avoid: Stop collecting SSNs — use a different identifier.

### Interview Tip
When asked about risk treatment, always mention all four strategies and give an example of when each is appropriate. Then explain that in practice, **most risks are mitigated** (you add controls), some are **accepted** (within appetite), a few are **transferred** (insurance, outsourcing), and **avoidance is rare** but important for truly unacceptable risks.

---

## Worked Example: A Single Risk Entry

Here's what one complete risk looks like across all three documents. Use this as your model.

### In the Risk Register:

| Field | Value |
|---|---|
| **Risk ID** | RISK-001 |
| **Risk Description** | Employee falls victim to a phishing attack, compromising their credentials and potentially exposing customer data |
| **Category** | People & Culture |
| **Asset/Process Affected** | Email system, customer database, employee credentials |
| **Threat Source** | External attacker |
| **Vulnerability** | Human error, insufficient security awareness |
| **Likelihood** | 4 (Likely) — Phishing attacks target SecureTech weekly |
| **Impact** | 4 (Major) — Compromised credentials could lead to data breach, regulatory notification, customer trust damage |
| **Risk Score** | 16 (High) |
| **Current Controls** | Basic email filtering, annual security awareness training |
| **Risk Owner** | CISO |

### In the Risk Treatment Plan:

| Field | Value |
|---|---|
| **Risk ID** | RISK-001 |
| **Treatment Strategy** | Mitigate |
| **Justification** | The risk score (16/High) exceeds our risk appetite. Phishing is the #1 attack vector and the most likely to succeed. |
| **Planned Actions** | 1. Deploy advanced email filtering with AI-based phishing detection (reduces likelihood). 2. Implement quarterly phishing simulation exercises (reduces likelihood). 3. Require MFA on all accounts (reduces impact — compromised password alone isn't enough). 4. Implement data loss prevention monitoring on email (reduces impact). |
| **Timeline** | Email filtering: 30 days. Phishing simulations: 60 days. MFA: already in progress. DLP: 90 days. |
| **Residual Likelihood** | 2 (Unlikely) — Advanced filtering + trained employees significantly reduce success rate |
| **Residual Impact** | 2 (Minor) — MFA prevents most credential-based attacks; DLP catches data exfiltration |
| **Residual Risk Score** | 4 (Low) — Within risk appetite |

---

## Realistic Risks for SecureTech

You need 15-20 risks. Here are some categories to think about for a 100-person cybersecurity startup. **Don't just copy these** — research and write your own descriptions, but use these as starting points:

**Cloud & Infrastructure:** Cloud misconfiguration, data loss from provider outage, insufficient logging
**People:** Phishing, insider threat, key person dependency, inadequate training
**Access:** Unauthorized access, privilege escalation, orphaned accounts (ex-employees still having access)
**Data:** Data breach, data loss from ransomware, improper data handling, third-party data exposure
**Compliance:** Regulatory non-compliance, failed audit, contractual security obligations not met
**Operations:** Business continuity failure, supply chain compromise, shadow IT (unapproved tools)
**Physical:** Laptop theft, office break-in (less common for startups but worth including)

---

## Your Day 3-4 Checklist

### Day 3
- [ ] Read this guide completely
- [ ] Study the worked example risk entry above
- [ ] Complete `risk_methodology.md` (build your own 5×5 matrix and severity thresholds)
- [ ] Start `risk_register.md` (complete at least 8-10 risks)

### Day 4
- [ ] Finish `risk_register.md` (15-20 risks total)
- [ ] Complete `risk_treatment_plans.md` (treatment plan for every risk)
- [ ] Review: do your treatment plans actually reduce the risk scores?
- [ ] Update your skills tracker
- [ ] Commit everything to GitHub

---

## When You're Done

You should be able to:
1. Explain the 5×5 risk matrix and why you chose specific scores
2. Walk through a risk from identification to treatment
3. Describe all four treatment strategies with examples
4. Articulate SecureTech's risk appetite and how it guides decisions
5. Explain the difference between inherent risk and residual risk

Practice answering: *"Tell me about a risk you identified and how you recommended treating it."* Use your risk register to tell a specific story.
