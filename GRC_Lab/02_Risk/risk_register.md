# Risk Register — SecureTech Inc.

**Document Owner:** CISO
**Last Assessment:** [Date]
**Next Assessment:** [Date + 1 year]

> 📖 **Instructions:** This is your organization's master list of identified risks. Three example risks are provided to show you the format and level of detail expected. You need to add **12-17 more risks** to reach the 15-20 total.
>
> Use the risk categories from your `risk_methodology.md` to ensure you're covering all areas. Don't cluster all your risks in one category — a real risk register spans the full landscape.

---

## Risk Register

### RISK-001: Phishing Attack Compromises Employee Credentials

> ℹ️ **Worked example** — study the level of detail, then write your own risks in this format.

| Field | Value |
|---|---|
| **Risk ID** | RISK-001 |
| **Category** | People & Culture |
| **Description** | An employee falls victim to a phishing email, revealing their credentials. The attacker uses the compromised account to access internal systems and potentially customer data. |
| **Asset/Process Affected** | Email system, SSO/identity provider, customer database, internal communications |
| **Threat Source** | External attacker (cybercriminal) |
| **Vulnerability** | Human error, insufficient phishing awareness, lack of advanced email filtering |
| **Likelihood** | 4 (Likely) — SecureTech receives targeted phishing attempts weekly |
| **Impact** | 4 (Major) — Compromised credentials could lead to data breach, customer notification, regulatory scrutiny |
| **Risk Score** | **16 (High)** |
| **Current Controls** | Basic email filtering, annual security awareness training, MFA on some systems |
| **Risk Owner** | CISO |

---

### RISK-002: Cloud Infrastructure Misconfiguration

> ℹ️ **Worked example**

| Field | Value |
|---|---|
| **Risk ID** | RISK-002 |
| **Category** | Cloud & Infrastructure |
| **Description** | A misconfigured cloud resource (S3 bucket, database, API endpoint) exposes sensitive data to the internet. Common in fast-moving startups where developers prioritize speed over security configuration. |
| **Asset/Process Affected** | Cloud infrastructure (AWS/Azure/GCP), customer data, application databases |
| **Threat Source** | Internal (accidental misconfiguration), External (attackers scanning for exposed resources) |
| **Vulnerability** | Lack of infrastructure-as-code review, insufficient cloud security posture management, no automated configuration scanning |
| **Likelihood** | 3 (Possible) — Cloud misconfigs are the #1 cause of breaches in cloud-native companies |
| **Impact** | 5 (Catastrophic) — Public data exposure would be devastating for a cybersecurity company's reputation |
| **Risk Score** | **15 (High)** |
| **Current Controls** | Manual configuration reviews during deployment, basic cloud provider security settings |
| **Risk Owner** | VP of Engineering |

---

### RISK-003: Key Person Dependency

> ℹ️ **Worked example**

| Field | Value |
|---|---|
| **Risk ID** | RISK-003 |
| **Category** | People & Culture |
| **Description** | Critical knowledge about systems, processes, or customer relationships is held by one person. If that person leaves, is unavailable, or is incapacitated, the organization cannot maintain or recover critical functions. |
| **Asset/Process Affected** | Infrastructure management, customer relationships, security operations |
| **Threat Source** | Employee departure (voluntary or involuntary), illness, burnout |
| **Vulnerability** | Insufficient documentation, no cross-training, single points of failure in small team |
| **Likelihood** | 4 (Likely) — Startup employees change roles frequently; at 100 employees, many functions have single owners |
| **Impact** | 3 (Moderate) — Temporary operational disruption, delayed projects, potential customer impact during transition |
| **Risk Score** | **12 (High)** |
| **Current Controls** | Limited documentation, informal knowledge sharing |
| **Risk Owner** | Department Heads |

---

### YOUR RISKS START HERE

<!-- YOUR WORK: Add 12-17 more risks using the same format. Aim for 15-20 total (including the 3 examples above).

Spread your risks across categories. Here are prompts to help you think of realistic risks for SecureTech:

**Cloud & Infrastructure:**
- What if a critical cloud service goes down?
- What if there's no disaster recovery plan?
- What if logs aren't being collected or monitored?

**People & Culture:**
- What about insider threats (intentional or accidental)?
- What if employees use unauthorized tools (shadow IT)?
- What if security training is inadequate?

**Access & Identity:**
- What about orphaned accounts (ex-employees still having access)?
- What if privileged access isn't properly managed?
- What about weak authentication on critical systems?

**Data Protection:**
- What about ransomware encrypting company data?
- What if data isn't backed up properly?
- What about third-party vendors mishandling SecureTech data?

**Compliance & Legal:**
- What if SecureTech fails a SOC 2 audit?
- What about changing regulations (privacy laws)?
- What if contractual security obligations aren't met?

**Operations & Business Continuity:**
- What if there's no business continuity plan?
- What about supply chain attacks on tools SecureTech uses?

**Third-Party / Vendor:**
- What if a critical vendor has a security breach?
- What if vendor security isn't being assessed?

**Physical Security:**
- What about laptop theft?
- What about unauthorized physical access to the office?

For each risk, you must fill in ALL fields: Risk ID, Category, Description, Asset/Process Affected, Threat Source, Vulnerability, Likelihood, Impact, Risk Score, Current Controls, Risk Owner.

Use this format for each risk:

### RISK-004: [Short Risk Title]

| Field | Value |
|---|---|
| **Risk ID** | RISK-004 |
| **Category** | [Category from your methodology] |
| **Description** | [2-3 sentences describing the risk scenario] |
| **Asset/Process Affected** | [What systems, data, or processes are at risk?] |
| **Threat Source** | [Who or what causes this risk?] |
| **Vulnerability** | [What weakness does the threat exploit?] |
| **Likelihood** | [1-5] ([Level]) — [Brief justification] |
| **Impact** | [1-5] ([Level]) — [Brief justification] |
| **Risk Score** | **[Score] ([Severity])** |
| **Current Controls** | [What's already in place?] |
| **Risk Owner** | [Who's accountable?] |

Remember:
- Justify your Likelihood and Impact scores — don't just pick numbers
- "Current Controls" shows what SecureTech already has (often basic for a startup)
- "Risk Owner" should be a role that makes sense (CISO, VP Engineering, HR Director, etc.)
-->

---

## Risk Register Summary

<!-- YOUR WORK: After completing all risks, fill in this summary table for a quick overview.

| Risk ID | Short Title | Category | Score | Severity |
|---|---|---|---|---|
| RISK-001 | Phishing attack | People & Culture | 16 | High |
| RISK-002 | Cloud misconfiguration | Cloud & Infrastructure | 15 | High |
| RISK-003 | Key person dependency | People & Culture | 12 | High |
| RISK-004 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

Sort by Risk Score (highest first) when you're done.
-->
