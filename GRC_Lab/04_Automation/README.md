# GRC Automation Tools

Three Python tools that automate GRC workflows for SecureTech Inc. Built using Python 3 standard library only — no external packages needed.

## Tools

### 1. Risk Scorer (`risk_scorer.py`)

Reads risk data from CSV, calculates risk scores, assigns severity levels, recommends treatment strategies, and generates a prioritized risk report.

```bash
python GRC_Lab/04_Automation/risk_scorer.py
```

- **Input:** `data/risk_data.csv`
- **Output:** `../05_Reports/generated/risk_score_report.md`

### 2. Compliance Mapper (`compliance_mapper.py`)

Interactive tool for looking up equivalent controls across NIST CSF 2.0, SOC 2, and ISO 27001. Enter a control ID from any framework to find its cross-framework mappings.

```bash
python GRC_Lab/04_Automation/compliance_mapper.py
```

- **Input:** `data/compliance_data.csv`
- **Output:** Interactive terminal display

### 3. Report Generator (`report_generator.py`)

Combines risk and compliance data to generate an executive summary report suitable for CISO-to-board communication.

```bash
python GRC_Lab/04_Automation/report_generator.py
```

- **Input:** `data/risk_data.csv` + `data/compliance_data.csv`
- **Output:** `../05_Reports/generated/executive_grc_report.md`

## Data Files

| File | Description |
|---|---|
| `data/risk_data.csv` | Risk register with 12 risks — IDs, scores, categories, controls |
| `data/compliance_data.csv` | Cross-framework control mapping — 18 control areas across 3 frameworks |

## Requirements

- Python 3.6+ (uses f-strings)
- No external packages — standard library only (`csv`, `os`, `datetime`)

## Learning Notes

Each tool has a companion `_learning_notes.md` file documenting the Python concepts learned while building it.
