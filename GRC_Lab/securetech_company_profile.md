# SecureTech Inc. — Company Profile

**Reference document.** Use this whenever you need company context while writing policies, assessing risks, or mapping compliance controls. Every artifact you build should be grounded in these details.

---

## Company at a Glance

| | |
|---|---|
| **Founded** | 2021 |
| **Headquarters** | Austin, TX (remote-first; employees across 12 U.S. states) |
| **Employees** | ~100 (targeting 140 by end of year) |
| **Stage** | Series B — $48M total raised |
| **Revenue** | ~$14M ARR, growing 65% year-over-year |
| **Business model** | B2B SaaS — annual contracts, enterprise sales |
| **Fiscal year** | January 1 – December 31 |

---

## What SecureTech Does

SecureTech sells a **cloud identity security platform** that helps enterprise companies detect and respond to identity-based threats — compromised accounts, privilege escalation, suspicious access patterns, and insider threats.

The core product has three modules:
- **IdentityGuard** — Continuous monitoring of user identities across cloud apps (Okta, Azure AD, Google Workspace)
- **AccessIQ** — Automated access reviews and least-privilege enforcement
- **ThreatLens** — Behavioral analytics that surfaces anomalous user activity

**Why this matters for GRC:** SecureTech's product handles highly sensitive data — customer employee credentials, access logs, and behavioral data. A breach at SecureTech could directly compromise dozens of customer environments. The security bar is higher than a typical SaaS company.

---

## Customers

| | |
|---|---|
| **Total customers** | 87 enterprise accounts |
| **Average contract value** | ~$160K/year |
| **Industries served** | Financial services (32%), Healthcare (24%), Technology (28%), Other (16%) |
| **Customer size** | 500–15,000 employees per customer |
| **Geographic markets** | United States (78%), Europe (18%), Canada (4%) |

**Key customer demands:** Most customers require SecureTech to maintain SOC 2 Type II. Several financial services customers also require ISO 27001. European customers trigger GDPR obligations.

---

## Organizational Structure

### Headcount by Department

| Department | Headcount | Notes |
|---|---|---|
| Engineering | 42 | Product, platform, security engineering |
| Sales & Marketing | 22 | Enterprise AEs, SDRs, marketing, partnerships |
| Customer Success | 14 | Implementation, support, renewals |
| G&A (Finance, HR, Legal, Ops) | 11 | Shared services |
| Security & GRC | 5 | CISO + 4 staff (you are one of them) |
| Executive | 4 | CEO, CTO, CRO, CFO |
| **Total** | **98** | |

### Key Roles for GRC Purposes

| Role | Person | GRC Relevance |
|---|---|---|
| **CEO** | Marcus Webb | Ultimate accountability; signs off on risk appetite |
| **CTO** | Priya Nair | Technical controls, engineering security practices |
| **CISO** | David Okonkwo | Your manager; owns the security program |
| **CFO** | Sarah Chen | Budget approvals, financial risk, cyber insurance |
| **General Counsel** | James Park | Legal obligations, contract review, breach notification |
| **VP Engineering** | Alex Rivera | Enforces security requirements within engineering |
| **VP Sales** | Taylor Morrison | Customer-facing compliance questions, contract terms |
| **HR Director** | Mia Hartley | Employee onboarding/offboarding, training, background checks |

---

## Technology Infrastructure

### Cloud & Hosting

| System | Detail |
|---|---|
| **Primary cloud** | AWS (us-east-1 primary, us-west-2 disaster recovery) |
| **Secondary cloud** | Google Cloud (BigQuery for analytics workloads) |
| **CDN** | Cloudflare |
| **DNS** | Cloudflare |
| **Environment separation** | Production, Staging, Development — all separate AWS accounts |

### Core Systems

| Category | Tool |
|---|---|
| **Identity provider** | Okta (SSO + MFA enforced company-wide) |
| **Code repositories** | GitHub Enterprise |
| **CI/CD** | GitHub Actions |
| **Cloud infrastructure** | Terraform (infrastructure as code) |
| **Databases** | AWS RDS (PostgreSQL) — customer data; AWS DynamoDB — session/event data |
| **Secrets management** | AWS Secrets Manager |
| **Logging & SIEM** | Datadog (logs, APM, alerts) |
| **Endpoint management** | Jamf (Mac fleet) + CrowdStrike (EDR) |
| **Email** | Google Workspace |
| **Communication** | Slack |
| **Video** | Zoom |
| **HR/Payroll** | Rippling |
| **CRM** | Salesforce |
| **Ticketing** | Jira + Confluence |
| **Vulnerability scanning** | Wiz (cloud), Snyk (code) |

### Data Handled

| Data Type | Sensitivity | Examples |
|---|---|---|
| Customer identity data | **Restricted** | OAuth tokens, directory syncs, user attributes from customer IdPs |
| Customer behavioral logs | **Restricted** | Access events, login history, anomaly detections |
| Customer PII | **Confidential** | Names, email addresses, employee IDs of customer users |
| SecureTech employee data | **Confidential** | Payroll, performance reviews, personal details |
| Product telemetry | **Internal** | Usage metrics, feature adoption, error rates |
| Marketing/public content | **Public** | Blog posts, product docs, case studies |

---

## Security Posture (Current State)

### What SecureTech Has Today

- Okta SSO with MFA enforced for all employees
- CrowdStrike EDR on all endpoints
- Wiz cloud security scanning (but findings aren't being systematically remediated)
- Annual penetration test (last conducted 8 months ago)
- Basic security awareness training at onboarding (no recurring training program)
- Informal incident response process (no documented procedure)
- No formal risk register
- No access review process (access is granted but rarely reviewed or revoked)
- Cyber insurance: $5M policy through Crum & Forster

### What's Missing (Your Job to Build)

- Formal written policies (you're building these now)
- Documented procedures for day-to-day security operations
- A risk register with scored, tracked risks
- Cross-framework compliance mapping (NIST CSF / SOC 2 / ISO 27001)
- Gap analysis against current compliance posture
- Quarterly access reviews
- Recurring security awareness training

---

## Compliance Obligations

| Framework | Status | Driver |
|---|---|---|
| **SOC 2 Type II** | In progress — audit scheduled in 5 months | Required by 80% of customers |
| **ISO 27001:2022** | Target: 18 months | Required by 3 European enterprise prospects worth $2M combined |
| **GDPR** | Partial compliance — gaps identified | European customer data |
| **CCPA** | Partial compliance | California residents in customer user bases |
| **HIPAA** | Not in scope (yet) | No direct PHI handling currently |

---

## Risk Profile

SecureTech operates at **elevated inherent risk** compared to most SaaS companies because:

1. **High-value target:** A company selling identity security that itself gets breached would be catastrophic for reputation
2. **Privileged access to customer environments:** The product requires read access to customer identity systems
3. **Rapid growth:** Headcount doubled in 18 months — security practices haven't kept pace
4. **SOC 2 deadline pressure:** Audit in 5 months creates urgency across all control areas
5. **Remote-first:** No physical perimeter; all access is network/identity-based

**Risk appetite (from CEO):** "We accept operational inefficiency before we accept customer data risk. If in doubt, lock it down."

---

## Budget & Resources

| | |
|---|---|
| **Annual security budget** | $1.4M (including headcount) |
| **Security headcount cost** | ~$900K (5 FTEs fully-loaded) |
| **Tools & infrastructure** | ~$280K/year |
| **Training & certifications** | $40K/year |
| **Pen test & audits** | $120K/year |
| **Discretionary / projects** | ~$60K available |

The CISO has authority to approve security spending up to $25K without CFO sign-off. Anything above requires a business case presented to the CFO and, if above $100K, the CEO.

---

## Useful Context for Writing Artifacts

**When writing policies:** SecureTech is remote-first and engineer-heavy. Policies need to be practical for a distributed, technical workforce. Overly bureaucratic policies won't get compliance. Keep them clear and enforceable.

**When assessing risk:** The SOC 2 audit in 5 months is the most time-sensitive driver. Risks that could surface as audit findings should be scored higher for urgency.

**When mapping frameworks:** SecureTech needs SOC 2 first, ISO 27001 second. Build the compliance matrix so SOC 2 controls map to ISO 27001 — implement once, satisfy both.

**When writing for the CISO (David):** He's pragmatic and results-oriented. He wants "what's the risk, what's the fix, how much does it cost, how long will it take" — not theory.
