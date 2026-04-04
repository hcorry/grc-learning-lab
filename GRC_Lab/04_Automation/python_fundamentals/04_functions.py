# =============================================================================
# Exercise 04: Functions
# =============================================================================
# Functions let you package code into reusable blocks. Instead of writing the
# same risk-scoring logic every time, you write it once as a function and call
# it whenever you need it.
#
# This is critical for the automation tools you'll build — risk_scorer.py,
# compliance_mapper.py, and report_generator.py are all built from functions.
# =============================================================================


# -----------------------------------------------------------------------------
# CONCEPT: Defining and Calling Functions
# -----------------------------------------------------------------------------
# def function_name(parameters):
#     """Docstring — explains what the function does"""
#     ... code ...
#     return result

# Worked example:
def calculate_risk_score(likelihood, impact):
    """Calculate a risk score from likelihood and impact ratings."""
    score = likelihood * impact
    return score

print("=== Functions ===")
result = calculate_risk_score(4, 5)
print(f"Risk score: {result}")  # 20

result2 = calculate_risk_score(2, 3)
print(f"Risk score: {result2}")  # 6
print()


# YOUR TURN: Write a function that determines severity from a score
# Fill in the blanks:

def get_severity(score):
    """Return the severity level for a given risk score."""
    if score >= 20:
        return ______  # "Critical"
    elif score >= 12:
        return ______  # "High"
    elif ______:  # score >= 6
        return "Medium"
    ______:  # else
        return "Low"

# Test your function:
print(f"Score 25 → {get_severity(25)}")  # Critical
print(f"Score 16 → {get_severity(16)}")  # High
print(f"Score 9 → {get_severity(9)}")    # Medium
print(f"Score 3 → {get_severity(3)}")    # Low
print()


# -----------------------------------------------------------------------------
# CONCEPT: Functions with Multiple Parameters
# -----------------------------------------------------------------------------

# Worked example:
def format_risk_entry(risk_id, title, score):
    """Format a risk entry as a readable string."""
    severity = get_severity(score)
    return f"{risk_id}: {title} | Score: {score} ({severity})"

print("=== Multiple Parameters ===")
print(format_risk_entry("RISK-001", "Phishing Attack", 16))
print(format_risk_entry("RISK-002", "Ransomware", 20))
print()


# YOUR TURN: Write a function that creates a complete risk dictionary
# Fill in the blanks:

def create_risk(risk_id, title, category, likelihood, impact):
    """Create a risk dictionary with calculated score and severity."""
    score = ______  # Calculate score from likelihood and impact
    severity = ______  # Use your get_severity function

    risk = {
        "id": risk_id,
        "title": title,
        "category": category,
        "likelihood": likelihood,
        "impact": impact,
        "score": ______,  # Use the calculated score
        "severity": ______,  # Use the calculated severity
    }
    return ______  # Return the risk dictionary

# Test your function:
test_risk = create_risk("RISK-010", "Data Breach", "Data Protection", 3, 5)
print(f"Created: {test_risk['id']} — {test_risk['title']}")
print(f"Score: {test_risk['score']} ({test_risk['severity']})")
# Expected: Score: 15 (High)
print()


# -----------------------------------------------------------------------------
# CONCEPT: Functions That Process Lists
# -----------------------------------------------------------------------------

# Worked example:
def count_by_severity(risks):
    """Count risks in each severity category."""
    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    for risk in risks:
        severity = get_severity(risk["score"])
        counts[severity] = counts[severity] + 1
    return counts

sample_risks = [
    {"title": "Phishing", "score": 16},
    {"title": "Ransomware", "score": 20},
    {"title": "Laptop Theft", "score": 4},
    {"title": "Cloud Misconfig", "score": 15},
    {"title": "Shadow IT", "score": 9},
]

print("=== Functions Processing Lists ===")
severity_counts = count_by_severity(sample_risks)
print(f"Severity breakdown: {severity_counts}")
print()


# YOUR TURN: Write a function that filters risks by minimum score
# Fill in the blanks:

def get_risks_above_threshold(risks, threshold):
    """Return only risks with scores at or above the threshold."""
    result = ______  # Start with an empty list
    for risk in ______:  # Loop through the risks
        if risk["score"] >= ______:  # Compare score to threshold
            result.append(______)  # Add the risk to results
    return result

# Test your function:
high_priority = get_risks_above_threshold(sample_risks, 12)
print(f"Risks with score >= 12: {len(high_priority)}")
for risk in high_priority:
    print(f"  {risk['title']}: {risk['score']}")
# Expected: Phishing (16), Ransomware (20), Cloud Misconfig (15)
print()


# YOUR TURN: Write a function that calculates the average risk score
# Fill in the blanks:

def average_risk_score(risks):
    """Calculate the average risk score from a list of risks."""
    if len(risks) == 0:
        return 0  # Avoid division by zero

    total = ______  # Start at 0
    for risk in risks:
        total = ______  # Add each risk's score to total

    average = ______  # Divide total by number of risks
    return round(average, 1)  # Round to 1 decimal place

print(f"Average score (all): {average_risk_score(sample_risks)}")
print(f"Average score (high priority): {average_risk_score(high_priority)}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Functions Calling Other Functions
# -----------------------------------------------------------------------------
# Functions can call other functions. This is how you build complex tools
# from simple building blocks.

# Worked example:
def generate_risk_summary(risks):
    """Generate a text summary of a risk register."""
    total = len(risks)
    avg = average_risk_score(risks)
    counts = count_by_severity(risks)
    priority = get_risks_above_threshold(risks, 12)

    summary = f"Risk Register Summary\n"
    summary += f"{'='*30}\n"
    summary += f"Total risks: {total}\n"
    summary += f"Average score: {avg}\n"
    summary += f"Critical: {counts['Critical']}, High: {counts['High']}, "
    summary += f"Medium: {counts['Medium']}, Low: {counts['Low']}\n"
    summary += f"\nPriority risks (score >= 12):\n"
    for risk in priority:
        summary += f"  ⚠ {risk['title']}: {risk['score']} ({get_severity(risk['score'])})\n"

    return summary

print("=== Functions Calling Functions ===")
print(generate_risk_summary(sample_risks))


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (Challenge)
# -----------------------------------------------------------------------------
# Write a function called `recommend_treatment` that takes a risk dictionary
# and returns a recommended treatment strategy based on these rules:
#
#   - Score >= 20 → "Mitigate" (too high to accept)
#   - Score >= 12 → "Mitigate" (high priority)
#   - Score >= 6 and impact >= 4 → "Transfer" (low likelihood but high impact = insurance)
#   - Score >= 6 → "Mitigate" (medium risks worth reducing)
#   - Score < 6 → "Accept" (within appetite)
#
# The function should return a dictionary with:
#   "strategy": the treatment strategy
#   "reason": a brief explanation
#
# Then loop through the sample_risks list, call your function for each,
# and print the risk title, score, recommended strategy, and reason.
#
# Write your code below:

