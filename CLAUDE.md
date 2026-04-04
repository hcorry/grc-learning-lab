# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GRC Engineering Learning Lab — a 2-week intensive portfolio project building an integrated GRC (Governance, Risk, and Compliance) program for a fictional cybersecurity startup ("SecureTech Inc.", ~100 employees). The learner is non-technical, transitioning from business operations into a GRC Analyst/Engineer role.

The design spec at `docs/superpowers/specs/2026-04-03-grc-learning-lab-design.md` is the source of truth for project structure, deliverables, and sequencing.

## Architecture

The project has two phases:

- **Week 1 (Manual):** Build GRC artifacts by hand — policies, risk register, compliance framework mappings. All markdown files written from scratch to demonstrate understanding.
- **Week 2 (Automation):** Learn Python fundamentals using GRC-themed exercises, then build three automation tools (`risk_scorer.py`, `compliance_mapper.py`, `report_generator.py`).

Key directories:
- `GRC_Lab/01_Governance/` through `05_Reports/` — numbered for GitHub display order
- `GRC_Lab/04_Automation/python_fundamentals/` — progressive Python exercises (01-05)
- `GRC_Profile/` — career materials (resume bullets, STAR stories, skills tracker)

## Python Constraints

- **Standard library only** — no external packages, no pip installs
- **Data formats:** Markdown and CSV only — no databases, no servers
- All three tools read from GRC artifacts and output to `GRC_Lab/05_Reports/generated/`

## Running the Tools

```bash
python GRC_Lab/04_Automation/risk_scorer.py
python GRC_Lab/04_Automation/compliance_mapper.py
python GRC_Lab/04_Automation/report_generator.py
```

## Working With This Learner

This is a teaching context. The learner should write code themselves with Claude as assistant, not generator. When helping:
- Explain Python concepts using GRC scenarios, not generic examples
- Each automation script has a companion `_learning_notes.md` the learner fills out
- Prioritize understanding over efficiency — verbose, well-commented code is preferred
- The three frameworks in scope are NIST CSF 2.0, SOC 2 Type II, and ISO 27001:2022
