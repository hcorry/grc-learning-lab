# GRC Engineering Learning Lab

A hands-on portfolio project building an integrated Governance, Risk, and Compliance (GRC) program for **SecureTech Inc.** — a fictional cybersecurity startup with ~100 employees.

## What This Project Demonstrates

- **Governance:** 5 security policies with companion procedures, tied together by a governance framework
- **Risk Management:** Risk register with 15-20 scored risks, treatment plans, and a 5x5 scoring methodology
- **Compliance:** Control mapping across NIST CSF 2.0, SOC 2 Type II, and ISO 27001:2022 with gap analysis
- **Automation:** Python tools that automate risk scoring, cross-framework mapping, and report generation
- **Communication:** Executive summary, blog post, and interview-ready career materials

## Project Structure

```
GRC_Lab/
├── 01_Governance/     # Policies, procedures, governance framework
├── 02_Risk/           # Risk register, methodology, treatment plans
├── 03_Compliance/     # Framework controls, cross-walk matrix, gap analysis
├── 04_Automation/     # Python fundamentals + 3 automation tools
└── 05_Reports/        # Executive summary + generated reports

GRC_Profile/           # Career materials (resume, STAR stories, skills tracker)
```

## Running the Automation Tools

Requires Python 3 (standard library only — no external packages).

```bash
# Score and prioritize risks from the risk register
python GRC_Lab/04_Automation/risk_scorer.py

# Look up equivalent controls across NIST CSF, SOC 2, and ISO 27001
python GRC_Lab/04_Automation/compliance_mapper.py

# Generate an executive summary report from GRC data
python GRC_Lab/04_Automation/report_generator.py
```

## Frameworks Covered

| Framework | Focus | Why It's Here |
|---|---|---|
| **NIST CSF 2.0** | 6 functions (Govern, Identify, Protect, Detect, Respond, Recover) | Most widely referenced in U.S. cybersecurity roles |
| **SOC 2 Type II** | 5 Trust Service Categories | Required for SaaS/cloud companies selling to enterprises |
| **ISO 27001:2022** | Annex A controls across 4 themes | International standard, demonstrates global awareness |

## About This Project

Built as a 2-week intensive learning lab — Week 1 building GRC artifacts manually to understand fundamentals, Week 2 learning Python to automate GRC workflows. The manual-first approach proves understanding before tooling.
