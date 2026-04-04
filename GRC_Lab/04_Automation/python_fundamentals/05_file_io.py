# =============================================================================
# Exercise 05: File I/O (Reading and Writing Files)
# =============================================================================
# Your automation tools need to read data from files (CSV risk data, compliance
# mappings) and write output to files (reports, summaries). This exercise
# teaches you how Python reads and writes files.
#
# IMPORTANT: This exercise reads/writes files in the current directory.
# Run it from the project root: python GRC_Lab/04_Automation/python_fundamentals/05_file_io.py
# =============================================================================

import csv  # Python's built-in CSV module — no installation needed
import os


# Create a temp directory for exercise output
os.makedirs("GRC_Lab/05_Reports/generated", exist_ok=True)


# -----------------------------------------------------------------------------
# CONCEPT: Reading Text Files
# -----------------------------------------------------------------------------
# open("filename", "r") opens a file for reading.
# .read() gets the entire content as a string.
# .readlines() gets each line as a list item.
# Always use "with" to automatically close the file.

# Worked example — first, let's create a file to read:
sample_text = """# SecureTech Risk Summary
Total risks identified: 15
Critical: 2
High: 5
Medium: 6
Low: 2
"""

with open("GRC_Lab/05_Reports/generated/sample_summary.txt", "w") as f:
    f.write(sample_text)
print("Created sample_summary.txt")

# Now read it back:
print("=== Reading Text Files ===")
with open("GRC_Lab/05_Reports/generated/sample_summary.txt", "r") as f:
    content = f.read()
print(content)


# Reading line by line:
print("Line by line:")
with open("GRC_Lab/05_Reports/generated/sample_summary.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"  Line {i}: {line.strip()}")  # .strip() removes the trailing newline
print()


# YOUR TURN: Write and read a file
# Fill in the blanks:

# Write a policy status report to a file
report_text = """# Policy Status Report
Information Security Policy: Approved
Acceptable Use Policy: Draft
Access Control Policy: Approved
Incident Response Policy: In Review
Data Classification Policy: Draft
"""

with open("GRC_Lab/05_Reports/generated/policy_status.txt", ______) as f:  # Open for writing ("w")
    f.______(report_text)  # Write the text to the file

# Read it back and count how many policies are "Approved"
approved_count = 0
with open("GRC_Lab/05_Reports/generated/policy_status.txt", ______) as f:  # Open for reading ("r")
    lines = f.______()  # Get all lines as a list
    for line in lines:
        if "Approved" in line:
            approved_count = ______  # Add 1

print(f"Approved policies: {approved_count}")
# Expected: 2
print()


# -----------------------------------------------------------------------------
# CONCEPT: Reading CSV Files
# -----------------------------------------------------------------------------
# CSV (Comma-Separated Values) is a simple format for tabular data.
# Each line is a row, values are separated by commas.
# Python's csv module makes it easy to read and write CSV files.

# Worked example — create a CSV file:
risk_csv_data = [
    ["risk_id", "title", "likelihood", "impact", "score"],
    ["RISK-001", "Phishing Attack", "4", "4", "16"],
    ["RISK-002", "Cloud Misconfiguration", "3", "5", "15"],
    ["RISK-003", "Key Person Dependency", "4", "3", "12"],
    ["RISK-004", "Laptop Theft", "2", "2", "4"],
    ["RISK-005", "Ransomware", "3", "5", "15"],
]

with open("GRC_Lab/04_Automation/data/sample_risks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in risk_csv_data:
        writer.writerow(row)
print("Created sample_risks.csv")

# Read it back using csv.DictReader (treats first row as headers):
print("\n=== Reading CSV Files ===")
with open("GRC_Lab/04_Automation/data/sample_risks.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['risk_id']}: {row['title']} — Score: {row['score']}")
print()

# IMPORTANT: CSV values are always strings!
# You need to convert numbers: int(row['score'])


# YOUR TURN: Read a CSV and process the data
# Fill in the blanks:

print("Processing risk CSV data:")
high_risks = []

with open("GRC_Lab/04_Automation/data/sample_risks.csv", "r") as f:
    reader = csv.______(f)  # Use DictReader to read with headers
    for row in reader:
        score = ______(row["score"])  # Convert score string to integer
        if score >= 12:
            high_risks.______(row)  # Add to high_risks list

print(f"High-priority risks (score >= 12): {len(high_risks)}")
for risk in high_risks:
    print(f"  {risk['risk_id']}: {risk['title']} (Score: {risk['score']})")
# Expected: 3 risks (RISK-001, RISK-002, RISK-003)
print()


# -----------------------------------------------------------------------------
# CONCEPT: Writing CSV Files
# -----------------------------------------------------------------------------

# Worked example:
treatment_data = [
    {"risk_id": "RISK-001", "strategy": "Mitigate", "residual_score": 4},
    {"risk_id": "RISK-002", "strategy": "Mitigate", "residual_score": 5},
    {"risk_id": "RISK-003", "strategy": "Mitigate", "residual_score": 8},
]

print("=== Writing CSV Files ===")
with open("GRC_Lab/05_Reports/generated/treatments.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["risk_id", "strategy", "residual_score"])
    writer.writeheader()  # Writes the header row
    for row in treatment_data:
        writer.writerow(row)
print("Created treatments.csv")
print()


# YOUR TURN: Write processed results to a CSV
# Fill in the blanks:

# Process risk data and write a severity report
severity_report = []

with open("GRC_Lab/04_Automation/data/sample_risks.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        score = int(row["score"])
        if score >= 20:
            severity = "Critical"
        elif score >= 12:
            severity = "High"
        elif score >= 6:
            severity = "Medium"
        else:
            severity = "Low"

        severity_report.append({
            "risk_id": row["risk_id"],
            "title": row["title"],
            "score": row["score"],
            "severity": ______,  # Use the severity variable
        })

# Write the severity report to CSV
output_path = "GRC_Lab/05_Reports/generated/severity_report.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.______(f, fieldnames=["risk_id", "title", "score", "severity"])  # Use DictWriter
    writer.______()  # Write the header row
    for row in severity_report:
        writer.______(row)  # Write each data row

print(f"Wrote severity report to {output_path}")

# Verify by reading it back
with open(output_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['risk_id']}: {row['title']} — {row['severity']}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Writing Markdown Files
# -----------------------------------------------------------------------------
# Your report generator will output markdown. Markdown is just text with
# formatting conventions (# for headers, | for tables, etc.)

# Worked example:
def generate_markdown_report(risks):
    """Generate a markdown risk report."""
    report = "# Risk Assessment Report\n\n"
    report += f"**Total Risks:** {len(risks)}\n\n"
    report += "| Risk ID | Title | Score | Severity |\n"
    report += "|---------|-------|-------|----------|\n"

    for risk in risks:
        score = int(risk["score"])
        if score >= 20:
            severity = "Critical"
        elif score >= 12:
            severity = "High"
        elif score >= 6:
            severity = "Medium"
        else:
            severity = "Low"
        report += f"| {risk['risk_id']} | {risk['title']} | {risk['score']} | {severity} |\n"

    return report

# Generate and write the report
with open("GRC_Lab/04_Automation/data/sample_risks.csv", "r") as f:
    reader = csv.DictReader(f)
    risks = list(reader)  # Convert reader to a list

report = generate_markdown_report(risks)

with open("GRC_Lab/05_Reports/generated/risk_report.md", "w") as f:
    f.write(report)

print("=== Markdown Report Generated ===")
print(report)


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (Challenge)
# -----------------------------------------------------------------------------
# Write a program that:
# 1. Reads the sample_risks.csv file
# 2. For each risk, determines the severity AND recommends a treatment strategy:
#    - Critical/High → "Mitigate"
#    - Medium with impact >= 4 → "Transfer"
#    - Medium → "Mitigate"
#    - Low → "Accept"
# 3. Writes the results to a NEW CSV file with columns:
#    risk_id, title, score, severity, treatment
# 4. Writes a markdown SUMMARY file that includes:
#    - Total risks
#    - Count per severity level
#    - Count per treatment strategy
#    - A table of all risks with their treatment
#
# Save the CSV to: GRC_Lab/05_Reports/generated/treatment_recommendations.csv
# Save the markdown to: GRC_Lab/05_Reports/generated/treatment_summary.md
#
# Write your code below:

