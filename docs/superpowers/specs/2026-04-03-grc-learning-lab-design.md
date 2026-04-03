# GRC Engineering Learning Lab — Design Spec

## Overview

A 2-week intensive learning lab that builds an integrated GRC (Governance, Risk, and Compliance) program as a portfolio project. The learner builds everything manually in Week 1 to understand fundamentals, then learns Python to automate GRC workflows in Week 2. The end product is a GitHub-ready portfolio with career materials targeting GRC Analyst/Engineer roles.

## Learner Profile

- **Current role:** Business Operations
- **Technical level:** Non-technical, coded only with Claude Code
- **Industry:** Cybersecurity startup (<100 employees)
- **GRC experience:** None — learning from scratch
- **Goal:** Land a GRC Analyst or GRC Engineer role (actively interviewing)
- **Timeline:** 2-week intensive full-time sprint

## Project Scenario

The learner acts as the solo GRC person at **"SecureTech Inc."** — a fictional cybersecurity startup with ~100 employees. This mirrors their real context and gives a concrete narrative for interviews.

## Folder Structure

```
GRC_Lab_Claude/
├── GRC_Profile/                        # Career materials & learner tracking
│   ├── learner_profile.md              # Background, skills, goals
│   ├── resume_bullets.md               # Impact-driven resume lines
│   ├── star_stories.md                 # STAR method interview answers
│   ├── linkedin_strategy.md            # Content plan & post drafts
│   └── skills_tracker.md              # Skills learned, mapped to job postings
│
├── GRC_Lab/                            # Portfolio project
│   ├── 01_Governance/                  # Policies & procedures
│   │   ├── policies/
│   │   │   ├── information_security_policy.md
│   │   │   ├── acceptable_use_policy.md
│   │   │   ├── access_control_policy.md
│   │   │   ├── incident_response_policy.md
│   │   │   └── data_classification_policy.md
│   │   ├── procedures/
│   │   │   └── (how-to docs for each policy)
│   │   └── governance_overview.md
│   │
│   ├── 02_Risk/                        # Risk management program
│   │   ├── risk_register.md            # 15-20 identified risks with scoring
│   │   ├── risk_methodology.md         # 5x5 Likelihood x Impact matrix
│   │   └── risk_treatment_plans.md     # Accept/Mitigate/Transfer/Avoid per risk
│   │
│   ├── 03_Compliance/                  # Framework mapping & tracking
│   │   ├── framework_controls/
│   │   │   ├── nist_csf_2.md           # 6 functions, relevant subcategories
│   │   │   ├── soc2_criteria.md        # 5 Trust Service Categories
│   │   │   └── iso27001_annex_a.md     # Key controls from 4 themes
│   │   ├── compliance_matrix.md        # Cross-framework control mapping
│   │   └── gap_analysis.md             # Implemented vs. gaps for SecureTech
│   │
│   ├── 04_Automation/                  # Python tools + learning
│   │   ├── python_fundamentals/        # GRC-themed Python exercises
│   │   │   ├── 01_variables_and_types.py
│   │   │   ├── 02_lists_and_dicts.py
│   │   │   ├── 03_conditionals_and_loops.py
│   │   │   ├── 04_functions.py
│   │   │   ├── 05_file_io.py
│   │   │   └── exercises_README.md
│   │   ├── risk_scorer.py              # Automated risk scoring calculator
│   │   ├── risk_scorer_learning_notes.md
│   │   ├── compliance_mapper.py        # Cross-framework mapping tool
│   │   ├── compliance_mapper_learning_notes.md
│   │   ├── report_generator.py         # Auto-generate GRC reports
│   │   ├── report_generator_learning_notes.md
│   │   └── README.md                   # How to use the tools
│   │
│   └── 05_Reports/                     # Generated outputs
│       ├── executive_summary.md        # Board-level GRC summary
│       └── generated/                  # Auto-generated reports
│
├── blog_post.md                        # Project walkthrough write-up
├── README.md                           # GitHub landing page
└── docs/
    └── superpowers/
        └── specs/
            └── (this file)
```

## Week 1: Manual GRC Foundation (Days 1-7)

### Days 1-2: Governance — Policies & Procedures

**Objective:** Write 5 security policies and their companion procedures from scratch.

**Policies to create:**
1. Information Security Policy (top-level "constitution")
2. Acceptable Use Policy (employee system usage rules)
3. Access Control Policy (who gets access to what)
4. Incident Response Policy (what happens when things go wrong)
5. Data Classification Policy (how to label/handle sensitive data)

**Policy template structure:** Purpose, Scope, Roles & Responsibilities, Policy Statements, Enforcement, Review Schedule.

**Each policy gets a companion procedure** with step-by-step operational instructions.

**Governance overview** ties everything together — how policies relate to each other, who owns what, review cadence.

**Why these five:** Most frequently asked about in interviews, map to controls across all three target frameworks.

### Days 3-4: Risk Management

**Objective:** Build a complete risk management program for SecureTech Inc.

**Artifacts:**
- **Risk Methodology** — 5x5 Likelihood x Impact scoring matrix, severity thresholds (Critical/High/Medium/Low), risk appetite statement
- **Risk Register** — 15-20 realistic risks for a cybersecurity startup. Each entry: Risk ID, Description, Asset/Process Affected, Threat Source, Likelihood (1-5), Impact (1-5), Risk Score, Current Controls, Risk Owner
- **Risk Treatment Plans** — For each risk: treatment strategy (Accept, Mitigate, Transfer, Avoid), justification, planned actions, residual risk score, timeline

**Scenario context:** Risks should be realistic for a <100 person cybersecurity startup — cloud infrastructure risks, insider threats, third-party vendor risks, regulatory risks, etc.

### Days 5-7: Compliance Framework Mapping

**Objective:** Map controls across three frameworks and perform a gap analysis.

**Frameworks:**
- **NIST CSF 2.0** — all 6 functions (Govern, Identify, Protect, Detect, Respond, Recover) with relevant subcategories
- **SOC 2 Type II** — 5 Trust Service Categories (Security, Availability, Processing Integrity, Confidentiality, Privacy)
- **ISO 27001:2022** — key Annex A controls from all 4 themes (Organizational, People, Physical, Technological)

**Compliance matrix (cross-walk):** Maps equivalent controls across frameworks. Example: NIST CSF PR.AC-1 ↔ SOC 2 CC6.1 ↔ ISO 27001 A.9.1.1. This is the killer deliverable — shows understanding that frameworks overlap.

**Gap analysis:** For SecureTech Inc., assess each control: Implemented / Partially Implemented / Not Implemented / Not Applicable. Include remediation recommendations for gaps.

### Week 1 Daily Schedule
| Time Block | Activity |
|---|---|
| Morning (3-4 hrs) | Build artifacts — write policies, fill registers, map controls |
| Afternoon (2-3 hrs) | Research — read actual framework docs, study real examples |
| End of day (1 hr) | Update skills tracker, write notes on what you learned |

## Week 2: Python Learning + Automation Layer (Days 8-14)

### Python Learning Approach

The learner writes code themselves with Claude Code as an assistant (not a generator). Each script is preceded by learning the Python concepts it requires. All exercises use GRC scenarios, not generic examples.

**Progressive concept introduction:**

| Script | Python Concepts Learned |
|---|---|
| `risk_scorer.py` | Variables, data types, lists, dictionaries, if/else, basic math |
| `compliance_mapper.py` | Reading CSV files, loops, string matching, functions |
| `report_generator.py` | File I/O, string formatting, combining data from multiple sources |

Each script has a companion `learning_notes.md` where the learner documents what each Python concept does in their own words.

### Days 8-9: Python Fundamentals + Risk Scorer

**Learning block:**
- Complete `python_fundamentals/` exercises (01-03): variables, lists, dicts, conditionals, loops
- All exercises use GRC data (risk scores, control names, severity levels)

**Build: `risk_scorer.py`**
- Input: risk data (asset, threat, likelihood, impact)
- Processing: calculate risk score, assign severity level, recommend treatment
- Output: prioritized risk report as markdown
- Reads from risk register data, outputs to `05_Reports/generated/`

**Technical constraints:** No external libraries. Standard Python only. Well-commented code.

### Days 10-11: Compliance Mapper

**Learning block:**
- Complete `python_fundamentals/` exercises (04-05): functions, file I/O

**Build: `compliance_mapper.py`**
- Input: a control ID from any of the three frameworks
- Processing: look up equivalent controls across the other two frameworks
- Output: formatted cross-framework mapping
- Reads from compliance matrix data (CSV format)

### Days 12-13: Report Generator + Documentation

**Build: `report_generator.py`**
- Pulls data from risk register and compliance matrix
- Generates a formatted executive summary report
- Outputs to `05_Reports/generated/`

**Documentation:**
- `README.md` — project overview, what it demonstrates, how to run the tools
- `blog_post.md` — personal narrative of the learning journey
- `GRC_Lab/04_Automation/README.md` — tool usage instructions

### Day 14: Career Materials

**Build all career deliverables:**
- `resume_bullets.md` — impact-driven lines tied to project work
- `star_stories.md` — 5-6 STAR-formatted interview answers from project experiences
- `linkedin_strategy.md` — 4-week content calendar with draft posts
- `skills_tracker.md` — every skill learned, mapped to job posting requirements

### Week 2 Daily Schedule
| Time Block | Activity |
|---|---|
| Morning (3-4 hrs) | Python exercises + build automation tools |
| Afternoon (2-3 hrs) | Write career materials, polish documentation |
| End of day (1 hr) | Test tools, commit to GitHub, update tracker |

## Final Deliverables

| Deliverable | Purpose | Location |
|---|---|---|
| 5 security policies + procedures | Governance knowledge | `GRC_Lab/01_Governance/` |
| Risk register + methodology + treatments | Risk management skills | `GRC_Lab/02_Risk/` |
| 3-framework compliance matrix + gap analysis | Framework expertise | `GRC_Lab/03_Compliance/` |
| Python fundamentals exercises | Python learning evidence | `GRC_Lab/04_Automation/python_fundamentals/` |
| 3 automation tools + learning notes | Technical differentiation | `GRC_Lab/04_Automation/` |
| Executive summary report | Communication skills | `GRC_Lab/05_Reports/` |
| Blog post | Online presence | `blog_post.md` |
| Resume bullets + STAR stories | Interview readiness | `GRC_Profile/` |
| LinkedIn content plan | Job search strategy | `GRC_Profile/` |
| GitHub README | First impression for employers | `README.md` |

## Design Decisions

1. **Numbered folders (01_, 02_, etc.)** — Display in logical order on GitHub
2. **Three frameworks (NIST CSF 2.0, SOC 2, ISO 27001)** — Most requested in job postings, enough to show cross-mapping without scope creep
3. **Fictional company mirrors learner's context** — Cybersecurity startup, ~100 employees, solo GRC
4. **Manual-first, automate-second** — Proves understanding before tooling; strongest interview narrative
5. **Python learning embedded in GRC context** — No generic exercises; every code example uses GRC data
6. **No external Python libraries** — Keeps technical barrier low, avoids dependency confusion
7. **Markdown + CSV for data** — No databases, no servers, readable by humans and tools
8. **Learning notes as deliverables** — Documents the learning process itself, shows self-awareness
