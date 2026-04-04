#!/usr/bin/env python3
"""
Report Generator — Executive GRC Summary Report
================================================

🏆 CHALLENGE EXERCISE — Less scaffolding than the previous tools!

This tool pulls data from BOTH the risk register (risk_data.csv) and the
compliance mapping (compliance_data.csv), then generates a formatted
executive summary report in markdown.

GOAL:
    Read both data files, analyze the GRC posture, and produce a professional
    report that a CISO could present to the executive team or board.

INPUT FILES:
    data/risk_data.csv          — Risk register data
    data/compliance_data.csv    — Cross-framework compliance mappings

OUTPUT:
    ../05_Reports/generated/executive_grc_report.md

WHAT THE REPORT SHOULD INCLUDE:
    1. Report header (title, date, prepared by)
    2. Risk posture summary:
       - Total risks, breakdown by severity
       - Top 5 highest-scoring risks
       - Treatment strategy breakdown (how many mitigate/transfer/accept)
       - Average risk score before and after treatment
    3. Compliance posture summary:
       - Number of frameworks covered
       - Total control areas mapped
       - List of control areas organized by category
    4. Key recommendations (3-5 actionable items based on the data)
    5. Appendix: full risk table and full compliance mapping table

HINTS (but you decide the implementation):
    - You already know how to: read CSVs, calculate scores, classify severity,
      recommend treatments, format markdown tables
    - You'll need functions from concepts in risk_scorer.py and compliance_mapper.py
    - Start by writing the functions you need, then a main() that ties them together
    - Think about: what would make this report useful to a non-technical executive?

RUN:
    python GRC_Lab/04_Automation/report_generator.py
"""

import csv
import os
from datetime import date


# =============================================================================
# CONFIGURATION
# =============================================================================

RISK_DATA_FILE = "GRC_Lab/04_Automation/data/risk_data.csv"
COMPLIANCE_DATA_FILE = "GRC_Lab/04_Automation/data/compliance_data.csv"
OUTPUT_DIR = "GRC_Lab/05_Reports/generated"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "executive_grc_report.md")


# =============================================================================
# YOUR CODE GOES HERE
# =============================================================================
#
# Build this tool yourself. Here's a suggested approach, but you can
# structure it however you want:
#
# 1. Write helper functions:
#    - A function to read and process risk data (reuse logic from risk_scorer.py)
#    - A function to read compliance data
#    - A function to generate the risk summary section
#    - A function to generate the compliance summary section
#    - A function to generate recommendations
#    - A function to generate the full report
#
# 2. Write a main() function that:
#    - Reads both data files
#    - Generates each section
#    - Combines them into the full report
#    - Writes the report to the output file
#    - Prints a confirmation message
#
# 3. Don't forget:
#    - os.makedirs(OUTPUT_DIR, exist_ok=True) before writing
#    - if __name__ == "__main__": main()
#    - Convert CSV string values to integers where needed
#    - The report should be readable by a non-technical executive
#
# If you get stuck, look at how risk_scorer.py and compliance_mapper.py
# handle similar tasks. But try to write this from memory first.
#
# =============================================================================


