#!/usr/bin/env python3
"""
Compliance Mapper — Cross-Framework Control Lookup Tool
=======================================================
This tool reads compliance mapping data from a CSV file and lets you
look up a control ID from any framework to find its equivalents in
the other two frameworks.

Input:  data/compliance_data.csv
Output: Prints results to terminal (and optionally writes to a file)

Run:    python GRC_Lab/04_Automation/compliance_mapper.py

Examples:
    Look up NIST control:  Enter "PR.AA-05" → shows SOC 2 and ISO 27001 equivalents
    Look up SOC 2 control: Enter "CC6.3" → shows NIST and ISO 27001 equivalents
    Look up ISO control:   Enter "A.8.3" → shows NIST and SOC 2 equivalents
"""

import csv
import os


# =============================================================================
# CONFIGURATION
# =============================================================================

INPUT_FILE = "GRC_Lab/04_Automation/data/compliance_data.csv"
OUTPUT_DIR = "GRC_Lab/05_Reports/generated"


# =============================================================================
# FUNCTION: load_compliance_data
# =============================================================================
def load_compliance_data(filepath):
    """
    Read compliance mapping data from a CSV file.

    Args:
        filepath (str): Path to the compliance data CSV

    Returns:
        list: List of dictionaries, one per control mapping row

    Each dictionary has these keys (from the CSV columns):
        control_area, nist_csf_id, nist_csf_description,
        soc2_id, soc2_description, iso27001_id, iso27001_description
    """
    # TODO: Open the CSV file with csv.DictReader and return all rows as a list.
    #
    # Steps:
    #   1. Open the file
    #   2. Create a DictReader
    #   3. Convert to a list (hint: list(reader))
    #   4. Return the list
    #
    # Don't forget to handle the case where the file doesn't exist.
    # Use os.path.exists(filepath) to check.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: find_control
# =============================================================================
def find_control(data, control_id):
    """
    Search the compliance data for a control ID and return all matching rows.

    The control_id could be from ANY framework (NIST, SOC 2, or ISO 27001).
    Search all three ID columns for a match.

    Args:
        data (list): The compliance data (list of dictionaries)
        control_id (str): The control ID to search for (e.g., "PR.AA-05", "CC6.3", "A.8.3")

    Returns:
        list: List of matching row dictionaries (could be 0, 1, or multiple matches)

    Hint: A control ID might appear in nist_csf_id, soc2_id, OR iso27001_id.
          Check all three columns for each row.
          Use .upper() on both the search term and the data to make it case-insensitive.
    """
    # TODO: Implement the search.
    #
    # Steps:
    #   1. Create an empty results list
    #   2. Convert control_id to uppercase for case-insensitive matching
    #   3. Loop through each row in data
    #   4. Check if control_id matches any of the three ID columns
    #      (also convert each column value to uppercase)
    #   5. If it matches, append the row to results
    #   6. Return results
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: detect_framework
# =============================================================================
def detect_framework(control_id):
    """
    Determine which framework a control ID belongs to based on its format.

    Args:
        control_id (str): The control ID to identify

    Returns:
        str: "NIST CSF 2.0", "SOC 2", "ISO 27001", or "Unknown"

    Patterns:
        NIST CSF 2.0: Starts with 2-letter function code + dot (e.g., PR.AA-05, ID.RA-01, GV.PO-01)
        SOC 2: Starts with "CC", "A1", "C1", "PI", or "P1" (e.g., CC6.3, A1.2, C1.1)
        ISO 27001: Starts with "A." followed by a number (e.g., A.5.1, A.8.3)

    Hint: Use the string method .startswith() or check the first few characters.
    """
    # TODO: Implement framework detection.
    #
    # This is a good exercise in string pattern matching.
    # Think about what makes each framework's IDs unique.
    #
    # NIST: Two uppercase letters, then a dot, then more letters (PR.xx, ID.xx, GV.xx, DE.xx, RS.xx, RC.xx)
    # SOC 2: Starts with CC, or a letter+number combo (A1, C1, PI, P1)
    # ISO: Starts with "A." then a number
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: format_mapping_result
# =============================================================================
def format_mapping_result(matches, search_id):
    """
    Format search results as a readable string for terminal display.

    Args:
        matches (list): List of matching row dictionaries
        search_id (str): The control ID that was searched for

    Returns:
        str: Formatted output string

    Expected output format:
        ═══════════════════════════════════════════
        Cross-Framework Mapping for: PR.AA-05
        Source Framework: NIST CSF 2.0
        ═══════════════════════════════════════════

        Match 1: Access Control - Least Privilege
        ───────────────────────────────────────────
        NIST CSF 2.0:  PR.AA-05 — Access permissions use least privilege and separation of duties
        SOC 2:         CC6.3 — Access authorized modified or removed based on roles
        ISO 27001:     A.8.3 — Information access restriction
    """
    # TODO: Build and return the formatted string.
    #
    # Steps:
    #   1. Start with a header showing the search ID
    #   2. Use detect_framework() to show the source framework
    #   3. If no matches found, return a "No matches found" message
    #   4. For each match, show the control area and all three framework mappings
    #   5. Align the output for readability (use f-string width specifiers)
    #
    # Hint for alignment: f"{'NIST CSF 2.0:':<16} {row['nist_csf_id']} — {row['nist_csf_description']}"
    # The :<16 means left-align in a 16-character wide field.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: search_by_area
# =============================================================================
def search_by_area(data, keyword):
    """
    Search for control mappings by control area keyword.

    Args:
        data (list): The compliance data
        keyword (str): Keyword to search for in control_area (e.g., "access", "risk")

    Returns:
        list: List of matching rows where the keyword appears in the control_area

    Hint: Use "keyword.lower() in row['control_area'].lower()" for case-insensitive matching.
    """
    # TODO: Implement keyword search.
    #
    # This is simpler than find_control — just search the control_area column.
    pass  # Remove this line when you write the code


# =============================================================================
# FUNCTION: list_all_controls
# =============================================================================
def list_all_controls(data):
    """
    Print a summary table of all control mappings.

    Args:
        data (list): The compliance data

    Returns:
        str: Formatted table string showing all mappings

    Output should look like:
        | # | Control Area               | NIST       | SOC 2  | ISO 27001 |
        |---|----------------------------|------------|--------|-----------|
        | 1 | Access Control - Least ... | PR.AA-05   | CC6.3  | A.8.3     |
    """
    # TODO: Build and return a formatted table of all control mappings.
    #
    # Hint: Use f-strings with width specifiers for column alignment.
    # Example: f"| {i:>2} | {row['control_area']:<30} | ..."
    pass  # Remove this line when you write the code


# =============================================================================
# MAIN — Interactive Mode
# =============================================================================
def main():
    """Main function — provides an interactive control lookup interface."""
    print("=" * 50)
    print("  Compliance Mapper — Cross-Framework Lookup")
    print("=" * 50)
    print()

    # Load data
    data = load_compliance_data(INPUT_FILE)

    if data is None:
        print("ERROR: load_compliance_data() returned None. Did you implement it?")
        return

    print(f"Loaded {len(data)} control mappings from {INPUT_FILE}")
    print()

    # Interactive loop
    print("Commands:")
    print("  Enter a control ID (e.g., PR.AA-05, CC6.3, A.8.3) to look up mappings")
    print("  Enter a keyword (e.g., 'access', 'risk') to search by control area")
    print("  Type 'list' to see all control mappings")
    print("  Type 'quit' to exit")
    print()

    while True:
        user_input = input("Search: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "list":
            result = list_all_controls(data)
            if result:
                print(result)
            continue

        # Try control ID lookup first
        matches = find_control(data, user_input)

        if matches:
            result = format_mapping_result(matches, user_input)
            if result:
                print(result)
        else:
            # Try keyword search
            keyword_matches = search_by_area(data, user_input)
            if keyword_matches:
                print(f"\nNo exact control ID match. Found {len(keyword_matches)} results for keyword '{user_input}':\n")
                for match in keyword_matches:
                    print(f"  • {match['control_area']}")
                    print(f"    NIST: {match['nist_csf_id']} | SOC 2: {match['soc2_id']} | ISO: {match['iso27001_id']}")
                    print()
            else:
                print(f"\nNo matches found for '{user_input}'. Try a control ID or keyword.\n")


if __name__ == "__main__":
    main()
