# =============================================================================
# Exercise 03: Conditionals and Loops
# =============================================================================
# Conditionals (if/elif/else) let your code make decisions.
# Loops (for, while) let your code repeat actions.
# Together, they let you process collections of GRC data automatically.
# =============================================================================


# -----------------------------------------------------------------------------
# CONCEPT: If / Elif / Else
# -----------------------------------------------------------------------------
# Conditionals execute different code based on conditions.
# == means "equals", != means "not equals"
# >, <, >=, <= for comparisons

# Worked example:
risk_score = 16

print("=== Conditionals ===")
if risk_score >= 20:
    severity = "Critical"
elif risk_score >= 12:
    severity = "High"
elif risk_score >= 6:
    severity = "Medium"
else:
    severity = "Low"

print(f"Score {risk_score} → Severity: {severity}")
print()


# YOUR TURN: Classify a compliance status
# Fill in the blanks:

compliance_percentage = 73.5

if ______:  # If compliance is 90 or above
    status = "Compliant"
elif ______:  # If compliance is 70 or above (but less than 90)
    status = "Partially Compliant"
elif ______:  # If compliance is 50 or above (but less than 70)
    status = "Needs Improvement"
else:
    status = "Non-Compliant"

print(f"Compliance: {compliance_percentage}% → Status: {status}")
# Expected output: "Compliance: 73.5% → Status: Partially Compliant"
print()


# YOUR TURN: Determine risk treatment recommendation
# Fill in the blanks:

score = 20
risk_appetite = 10  # Organization accepts scores at or below 10

if score > risk_appetite:
    ______ = "Treatment required"  # Assign to a variable called "recommendation"
else:
    ______ = "Risk accepted"  # Same variable name

print(f"Score: {score}, Appetite: {risk_appetite} → {recommendation}")
# Expected: "Score: 20, Appetite: 10 → Treatment required"
print()


# -----------------------------------------------------------------------------
# CONCEPT: For Loops
# -----------------------------------------------------------------------------
# A for loop repeats code once for each item in a list.
# The variable name after "for" takes on each item's value.

# Worked example:
frameworks = ["NIST CSF 2.0", "SOC 2 Type II", "ISO 27001:2022"]

print("=== For Loops ===")
for framework in frameworks:
    print(f"  → Assessing: {framework}")
print()


# YOUR TURN: Loop through a list of risk scores and classify each
# Fill in the blanks:

scores = [4, 8, 12, 16, 20, 25, 6, 15, 3, 9]

print("Risk Score Classification:")
for score in ______:  # Loop through the scores list
    if score >= 20:
        severity = ______  # "Critical"
    elif score >= 12:
        severity = ______  # "High"
    elif score >= 6:
        severity = ______  # "Medium"
    else:
        severity = ______  # "Low"
    print(f"  Score {score:2d} → {severity}")
    # Note: {score:2d} formats the number to 2 digits wide for alignment
print()


# -----------------------------------------------------------------------------
# CONCEPT: Loops with Dictionaries
# -----------------------------------------------------------------------------
# You can loop through a list of dictionaries to process structured data.

# Worked example:
risks = [
    {"id": "RISK-001", "title": "Phishing", "score": 16},
    {"id": "RISK-002", "title": "Cloud Misconfig", "score": 15},
    {"id": "RISK-003", "title": "Ransomware", "score": 20},
]

print("=== Loops with Dictionaries ===")
for risk in risks:
    print(f"  {risk['id']}: {risk['title']} (Score: {risk['score']})")
print()


# YOUR TURN: Process a list of controls and count statuses
# Fill in the blanks:

controls = [
    {"id": "CC6.1", "status": "Implemented"},
    {"id": "CC6.3", "status": "Partially Implemented"},
    {"id": "CC7.1", "status": "Not Implemented"},
    {"id": "CC7.2", "status": "Implemented"},
    {"id": "CC8.1", "status": "Partially Implemented"},
    {"id": "CC9.1", "status": "Not Implemented"},
    {"id": "CC1.1", "status": "Implemented"},
]

implemented_count = 0
partial_count = 0
not_implemented_count = 0

for control in controls:
    if control["status"] == ______:  # Check if status is "Implemented"
        implemented_count = ______  # Add 1 to implemented_count
    elif control["status"] == ______:  # Check if "Partially Implemented"
        partial_count = ______  # Add 1 to partial_count
    else:
        not_implemented_count = ______  # Add 1 to not_implemented_count

print(f"Implemented: {implemented_count}")
print(f"Partially Implemented: {partial_count}")
print(f"Not Implemented: {not_implemented_count}")
# Expected: Implemented: 3, Partially: 2, Not Implemented: 2
print()


# -----------------------------------------------------------------------------
# CONCEPT: Building Results in a Loop
# -----------------------------------------------------------------------------
# A common pattern: start with an empty list, add items in a loop.

# Worked example:
all_risks = [
    {"title": "Phishing", "score": 16},
    {"title": "Cloud Misconfig", "score": 15},
    {"title": "Ransomware", "score": 20},
    {"title": "Insider Threat", "score": 8},
    {"title": "Key Person", "score": 12},
]

high_risks = []  # Start empty
for risk in all_risks:
    if risk["score"] >= 12:
        high_risks.append(risk)  # Add to the list

print("=== Filtering with Loops ===")
print(f"Total risks: {len(all_risks)}")
print(f"High/Critical risks: {len(high_risks)}")
for risk in high_risks:
    print(f"  ⚠ {risk['title']}: {risk['score']}")
print()


# YOUR TURN: Filter controls that need remediation
# Fill in the blanks:

all_controls = [
    {"id": "CC6.1", "area": "Access Control", "status": "Implemented"},
    {"id": "CC6.3", "area": "Access Control", "status": "Partially Implemented"},
    {"id": "CC7.1", "area": "Monitoring", "status": "Not Implemented"},
    {"id": "CC7.2", "area": "Monitoring", "status": "Implemented"},
    {"id": "A.5.1", "area": "Policy", "status": "Implemented"},
    {"id": "A.8.8", "area": "Vulnerability Mgmt", "status": "Not Implemented"},
]

needs_work = ______  # Start with an empty list

for control in all_controls:
    if control["status"] ______ "Implemented":  # Use != to check if status is NOT "Implemented"
        ______(control)  # Append the control to needs_work

print(f"Controls needing remediation: {len(needs_work)}")
for control in needs_work:
    print(f"  [{control['status']}] {control['id']} — {control['area']}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Counting and Summing in Loops
# -----------------------------------------------------------------------------

# Worked example:
risk_register = [
    {"title": "Phishing", "score": 16, "treatment": "Mitigate"},
    {"title": "Ransomware", "score": 20, "treatment": "Mitigate"},
    {"title": "Laptop Theft", "score": 4, "treatment": "Accept"},
    {"title": "Cloud Outage", "score": 10, "treatment": "Transfer"},
    {"title": "Key Person", "score": 12, "treatment": "Mitigate"},
]

total_score = 0
mitigate_count = 0

for risk in risk_register:
    total_score = total_score + risk["score"]
    if risk["treatment"] == "Mitigate":
        mitigate_count = mitigate_count + 1

average_score = total_score / len(risk_register)

print("=== Counting and Summing ===")
print(f"Total risk exposure: {total_score}")
print(f"Average risk score: {average_score}")
print(f"Risks being mitigated: {mitigate_count} of {len(risk_register)}")
print()


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (Challenge)
# -----------------------------------------------------------------------------
# Given this risk register, write code that:
# 1. Loops through all risks
# 2. Assigns a severity to each based on score (Critical >= 20, High >= 12, Medium >= 6, Low < 6)
# 3. Collects all Critical and High risks into a list called "priority_risks"
# 4. Prints a summary: total risks, count per severity, and the priority risks list

risk_data = [
    {"id": "RISK-001", "title": "Phishing Attack", "score": 16},
    {"id": "RISK-002", "title": "Cloud Misconfiguration", "score": 15},
    {"id": "RISK-003", "title": "Key Person Dependency", "score": 12},
    {"id": "RISK-004", "title": "Laptop Theft", "score": 4},
    {"id": "RISK-005", "title": "Ransomware", "score": 20},
    {"id": "RISK-006", "title": "Shadow IT", "score": 9},
    {"id": "RISK-007", "title": "Failed Audit", "score": 8},
    {"id": "RISK-008", "title": "Insider Threat", "score": 12},
]

# Write your code below:

