# GRC Engineering Learning Lab — Start Here

Welcome to your 2-week intensive GRC (Governance, Risk, and Compliance) learning lab. By the end, you'll have a complete, portfolio-ready GRC program for a fictional company called **SecureTech Inc.** — a cybersecurity startup with ~100 employees where you're the solo GRC person.

---

## How This Course Works

- **Each day has a guide** (`_guide.md`) that explains concepts, shows worked examples, and walks you through what to build
- **Templates have `<!-- YOUR WORK -->` markers** — that's where you write your content
- **Worked examples show what "good" looks like** — use them as a reference, but write in your own words
- **Don't skip the learning notes** — explaining concepts in your own words is how you internalize them
- **Commit to GitHub daily** — your commit history tells a story to employers

### Time Commitment

Each day assumes ~6-8 hours of focused work:

| Time Block | Activity |
|---|---|
| Morning (3-4 hrs) | Build artifacts — write policies, fill registers, write code |
| Afternoon (2-3 hrs) | Research — read framework docs, study examples, look up concepts |
| End of day (1 hr) | Update skills tracker, write notes, commit to GitHub |

---

## Week 1: Manual GRC Foundation

Build your GRC program by hand. No shortcuts. This is where you prove you understand the fundamentals.

### Days 1-2: Governance — Policies & Procedures

📂 `GRC_Lab/01_Governance/`
📖 Start with: `GRC_Lab/01_Governance/day1_2_guide.md`

**What you'll build:**
- 5 security policies (Information Security, Acceptable Use, Access Control, Incident Response, Data Classification)
- A companion procedure for each policy
- A governance overview tying everything together

**Learning objectives:**
- Understand what a security policy is and why organizations need them
- Learn the standard structure of an enterprise policy
- Know the difference between a policy (the "what") and a procedure (the "how")
- Understand how policies relate to each other in a governance framework

---

### Days 3-4: Risk Management

📂 `GRC_Lab/02_Risk/`
📖 Start with: `GRC_Lab/02_Risk/day3_4_guide.md`

**What you'll build:**
- A risk scoring methodology (5x5 matrix)
- A risk register with 15-20 identified risks
- Risk treatment plans for each risk

**Learning objectives:**
- Understand the risk management lifecycle
- Learn how to score risks using likelihood and impact
- Know the four risk treatment strategies (Accept, Mitigate, Transfer, Avoid)
- Be able to articulate risk appetite and tolerance

---

### Days 5-7: Compliance Framework Mapping

📂 `GRC_Lab/03_Compliance/`
📖 Start with: `GRC_Lab/03_Compliance/day5_7_guide.md`

**What you'll build:**
- Control documentation for three frameworks (NIST CSF 2.0, SOC 2, ISO 27001)
- A cross-framework compliance matrix (the "cross-walk")
- A gap analysis for SecureTech Inc.

**Learning objectives:**
- Understand what compliance frameworks are and why companies adopt them
- Know the structure and purpose of NIST CSF 2.0, SOC 2 Type II, and ISO 27001:2022
- Learn how controls map across frameworks
- Be able to assess compliance gaps and recommend remediation

**🏆 Challenge:** The gap analysis has less scaffolding — you'll apply what you learned in Days 1-4 to assess SecureTech's compliance posture with minimal hand-holding.

---

## Week 2: Python + Automation

Learn Python using GRC scenarios, then build tools that automate your Week 1 work.

### Days 8-9: Python Fundamentals + Risk Scorer

📂 `GRC_Lab/04_Automation/`
📖 Start with: `GRC_Lab/04_Automation/python_fundamentals/exercises_README.md`

**What you'll learn:**
- Variables, data types, strings, numbers
- Lists and dictionaries
- Conditionals (if/else) and loops

**What you'll build:**
- Complete exercises 01-03 (fill-in-the-blank style with GRC data)
- `risk_scorer.py` — reads risk data, calculates scores, outputs a prioritized report

**Learning objectives:**
- Understand Python's basic building blocks using GRC scenarios
- Read data from a CSV file
- Perform calculations and format output

---

### Days 10-11: More Python + Compliance Mapper

📖 Continue with exercises, then build the mapper
📖 Start with: `GRC_Lab/04_Automation/python_fundamentals/exercises_README.md` (exercises 04-05)

**What you'll learn:**
- Functions (reusable blocks of code)
- File I/O (reading and writing files)

**What you'll build:**
- Complete exercises 04-05
- `compliance_mapper.py` — look up a control ID from any framework and find its equivalents

**Learning objectives:**
- Write reusable functions
- Read CSV data and search through it
- Format and display results clearly

---

### Days 12-13: Report Generator + Documentation

📖 Start with: `GRC_Lab/04_Automation/report_generator.py`

**What you'll build:**
- `report_generator.py` — pulls data from risk register and compliance matrix, generates an executive summary
- Tool documentation (README for the automation folder)

**🏆 Challenge:** The report generator has less scaffolding than the previous tools. You'll get the goal and expected output, but you decide how to structure the code. This is your chance to apply everything you've learned.

**Learning objectives:**
- Combine multiple data sources into one output
- Generate formatted markdown reports
- Work more independently with less guidance

---

### Day 14: Career Materials

📂 `GRC_Profile/`
📖 Start with: `GRC_Profile/learner_profile.md`

**What you'll build:**
- Resume bullets tied to your project work
- STAR-formatted interview stories
- LinkedIn content strategy
- Skills tracker mapped to job postings
- Blog post about your learning journey

**Learning objectives:**
- Translate technical project work into interview-ready language
- Build a professional narrative around your GRC transition

---

## When You're Done

You'll have:
- ✅ A complete GRC program (governance + risk + compliance)
- ✅ Three working Python automation tools
- ✅ A GitHub portfolio that demonstrates GRC knowledge and technical skills
- ✅ Interview-ready career materials
- ✅ A blog post documenting your journey

**The portfolio tells this story:** "I built an entire GRC program from scratch, understood the frameworks deeply enough to map them together, then learned Python to automate the workflows. Here's the evidence."

Good luck. Start with Day 1. 🚀
