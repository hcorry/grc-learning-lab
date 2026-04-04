#!/usr/bin/env python3
"""
Risk Scorer — Automated Risk Scoring Calculator
================================================
This tool reads risk data from a CSV file, calculates risk scores,
assigns severity levels, recommends treatments, and outputs a
prioritized risk report as markdown.

Input:  data/risk_data.csv
Output: ../05_Reports/generated/risk_score_report.md

Run:    python GRC_Lab/04_Automation/risk_scorer.py
"""

import csv
import os


# =============================================================================
# CONFIGURATION
# =============================================================================
# These paths are relative to the project root (where you run the script from)

INPUT_FILE = "GRC_Lab/04_Automation/data/risk_data.csv"
OUTPUT_DIR = "GRC_Lab/05_Reports/generated"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "risk_score_report.md")

# Risk appetite threshold — scores at or below this are accepted
RISK_APPETITE = 10

# Severity thresholds
CRITICAL_THRESHOLD = 20
HIGH_THRESHOLD = 12
MEDIUM_THRESHOLD = 6


# =============================================================================
# FUNCTION: get_severity
# =============================================================================
def get_severity(score):
    """
    Determine the severity level based on a risk score.

    Args:
        score (int): The calculated risk score (likelihood × impact, range 1-25)

    Returns:
        str: One of "Critical", "High", "Medium", or "Low"

    Severity thresholds:
        Critical: 20-25
        High:     12-19
        Medium:    6-11
        Low:       1-5
    """
    # TODO: Write the if/elif/else logic to return the correct severity.
    # Use the threshold constants defined above (CRITICAL_THRESHOLD, etc.)
    # Hint: Check from highest to lowest — if score >= CRITICAL_THRESHOLD first.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: calculate_risk_score
# =============================================================================
def calculate_risk_score(likelihood, impact):
    """
    Calculate the risk score from likelihood and impact ratings.

    Args:
        likelihood (int): Likelihood rating (1-5)
        impact (int): Impact rating (1-5)

    Returns:
        int: Risk score (likelihood × impact, range 1-25)
    """
    # TODO: Calculate and return the risk score.
    # This is simple multiplication, but validate that both values are in range 1-5.
    # If a value is out of range, print a warning and still calculate.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: recommend_treatment
# =============================================================================
def recommend_treatment(score, impact):
    """
    Recommend a risk treatment strategy based on score and impact.

    Args:
        score (int): The calculated risk score
        impact (int): The impact rating (used for transfer recommendation)

    Returns:
        str: One of "Mitigate", "Transfer", or "Accept"

    Rules:
        - Score >= HIGH_THRESHOLD → "Mitigate" (too high to accept)
        - Score >= MEDIUM_THRESHOLD and impact >= 4 → "Transfer" (insure against high-impact events)
        - Score >= MEDIUM_THRESHOLD → "Mitigate"
        - Score < MEDIUM_THRESHOLD → "Accept" (within risk appetite)
    """
    # TODO: Implement the treatment recommendation logic.
    # Use the rules described in the docstring.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: read_risk_data
# =============================================================================
def read_risk_data(filepath):
    """
    Read risk data from a CSV file and return a list of risk dictionaries.

    Each risk dictionary should include all original CSV fields PLUS:
        - "score": calculated risk score (int)
        - "severity": severity level (str)
        - "treatment": recommended treatment (str)

    Args:
        filepath (str): Path to the CSV file

    Returns:
        list: List of risk dictionaries with calculated fields added

    CSV columns: risk_id, title, category, threat_source, vulnerability,
                 likelihood, impact, current_controls, owner
    """
    # TODO: Implement this function.
    # Steps:
    #   1. Open the CSV file using csv.DictReader
    #   2. For each row:
    #      a. Convert likelihood and impact from strings to integers
    #      b. Calculate the risk score using calculate_risk_score()
    #      c. Get the severity using get_severity()
    #      d. Get the treatment using recommend_treatment()
    #      e. Add score, severity, and treatment to the row dictionary
    #      f. Append the row to a list
    #   3. Return the list
    #
    # Hint: row["likelihood"] is a string from the CSV — use int() to convert it.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: sort_risks_by_score
# =============================================================================
def sort_risks_by_score(risks):
    """
    Sort a list of risk dictionaries by score in descending order (highest first).

    Args:
        risks (list): List of risk dictionaries with a "score" key

    Returns:
        list: Sorted list (highest score first)

    Hint: Use the sorted() function with a key parameter.
          sorted(my_list, key=lambda x: x["score"], reverse=True)
          The lambda is a mini-function that tells sorted() which value to sort by.
    """
    # TODO: Return the sorted list.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: generate_report
# =============================================================================
def generate_report(risks):
    """
    Generate a markdown risk report from the processed risk data.

    The report should include:
    1. A title and date
    2. An executive summary (total risks, count per severity, average score)
    3. A risk matrix summary table (all risks: ID, title, score, severity, treatment)
    4. Detailed entries for Critical and High risks only
    5. Treatment strategy summary (count per strategy)

    Args:
        risks (list): Sorted list of risk dictionaries

    Returns:
        str: Complete markdown report as a string

    Hint: Build the string piece by piece using += or f-strings.
    """
    # TODO: Build and return the markdown report.
    #
    # Here's a skeleton to get you started:
    #
    # report = "# Risk Score Report\n\n"
    # report += f"**Generated by:** risk_scorer.py\n"
    # report += f"**Total Risks:** {len(risks)}\n\n"
    #
    # --- Add severity summary ---
    # Count how many risks are in each severity category.
    # Display as: "Critical: X | High: X | Medium: X | Low: X"
    #
    # --- Add risk table ---
    # Create a markdown table with columns:
    # | Risk ID | Title | Score | Severity | Treatment |
    # |---------|-------|-------|----------|-----------|
    # | RISK-001 | Phishing Attack | 16 | High | Mitigate |
    #
    # --- Add detailed section for Critical/High risks ---
    # For each Critical and High risk, show:
    #   ### RISK-001: Phishing Attack
    #   - **Score:** 16 (High)
    #   - **Category:** People & Culture
    #   - **Threat:** External attacker
    #   - **Vulnerability:** Human error
    #   - **Current Controls:** Basic email filtering
    #   - **Recommendation:** Mitigate
    #
    # --- Add treatment summary ---
    # Count how many risks get each treatment: Mitigate, Transfer, Accept
    #
    # return report
    pass  # Remove this line when you write the code


# =============================================================================
# MAIN
# =============================================================================
def main():
    """Main function — orchestrates reading, processing, and reporting."""
    print("Risk Scorer — Starting...")
    print(f"Reading data from: {INPUT_FILE}")

    # Step 1: Read and process risk data
    risks = read_risk_data(INPUT_FILE)

    if risks is None:
        print("ERROR: read_risk_data() returned None. Did you implement it?")
        return

    print(f"Loaded {len(risks)} risks")

    # Step 2: Sort by score (highest first)
    risks = sort_risks_by_score(risks)

    # Step 3: Generate the report
    report = generate_report(risks)

    if report is None:
        print("ERROR: generate_report() returned None. Did you implement it?")
        return

    # Step 4: Write to file
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(report)

    print(f"Report written to: {OUTPUT_FILE}")
    print()

    # Step 5: Print a quick summary to the terminal
    print("Quick Summary:")
    print("-" * 40)
    for risk in risks:
        print(f"  {risk['risk_id']}: {risk['title']} — {risk['score']} ({risk['severity']})")
    print()
    print("Done! Open the report file to see the full output.")


if __name__ == "__main__":
    main()
