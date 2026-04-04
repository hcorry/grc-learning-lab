# =============================================================================
# Exercise 02: Lists and Dictionaries
# =============================================================================
# Lists and dictionaries let you store COLLECTIONS of data.
# A list is an ordered sequence: ["item1", "item2", "item3"]
# A dictionary is a set of key-value pairs: {"name": "value", "score": 16}
#
# In GRC, you'll use lists for collections (list of risks, list of controls)
# and dictionaries for structured records (a single risk with multiple fields).
# =============================================================================


# -----------------------------------------------------------------------------
# CONCEPT: Lists
# -----------------------------------------------------------------------------
# A list stores multiple values in order. Created with square brackets [].
# Items are accessed by index (position), starting at 0.

# Worked example:
frameworks = ["NIST CSF 2.0", "SOC 2 Type II", "ISO 27001:2022"]

print("=== Lists ===")
print(f"Frameworks: {frameworks}")
print(f"First framework: {frameworks[0]}")  # Index 0 = first item
print(f"Last framework: {frameworks[-1]}")  # Index -1 = last item
print(f"Number of frameworks: {len(frameworks)}")
print()


# YOUR TURN: Create and access lists
# Fill in the blanks:

# Create a list of 5 policy names
policies = ______  # A list containing: "Information Security", "Acceptable Use", "Access Control", "Incident Response", "Data Classification"

print(f"All policies: {policies}")
print(f"First policy: {______}")  # Access the first item (index 0)
print(f"Third policy: {______}")  # Access the third item
print(f"Total policies: {len(policies)}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: List Operations
# -----------------------------------------------------------------------------
# .append(item)  — add an item to the end
# .remove(item)  — remove first occurrence of an item
# .sort()        — sort the list alphabetically/numerically
# item in list   — check if item exists (returns True/False)

# Worked example:
risk_scores = [16, 12, 8, 20, 4]
print("=== List Operations ===")
print(f"Original scores: {risk_scores}")

risk_scores.append(15)
print(f"After append(15): {risk_scores}")

risk_scores.sort()
print(f"After sort(): {risk_scores}")

print(f"Is 20 in the list? {20 in risk_scores}")
print(f"Highest score: {max(risk_scores)}")
print(f"Lowest score: {min(risk_scores)}")
print(f"Average score: {sum(risk_scores) / len(risk_scores)}")
print()


# YOUR TURN: Manipulate a list of severity levels
# Fill in the blanks:

severity_counts = [3, 7, 5, 2]  # [Critical, High, Medium, Low]

total_risks = ______  # Use sum() to get the total number of risks
highest_count = ______  # Use max() to find the largest count

# Add a new count (1 more Critical risk was found)
severity_counts[0] = ______  # Update the first element from 3 to 4

print(f"Total risks: {total_risks}")
print(f"Highest category count: {highest_count}")
print(f"Updated counts: {severity_counts}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Dictionaries
# -----------------------------------------------------------------------------
# A dictionary stores key-value pairs. Created with curly braces {}.
# Keys are strings (usually), values can be anything.
# Access values using dict["key"] syntax.

# Worked example:
risk = {
    "id": "RISK-001",
    "title": "Phishing Attack",
    "category": "People & Culture",
    "likelihood": 4,
    "impact": 4,
    "score": 16,
    "owner": "CISO"
}

print("=== Dictionaries ===")
print(f"Risk ID: {risk['id']}")
print(f"Title: {risk['title']}")
print(f"Score: {risk['score']}")
print(f"All keys: {list(risk.keys())}")
print()


# YOUR TURN: Create and access a dictionary
# Fill in the blanks:

control = {
    "id": ______,  # Set to "CC6.3"
    "framework": ______,  # Set to "SOC 2"
    "description": ______,  # Set to "Access authorized based on roles"
    "status": ______,  # Set to "Partially Implemented"
}

print(f"Control: {control['id']} ({control['framework']})")
print(f"Description: {______}")  # Access the 'description' key
print(f"Status: {______}")  # Access the 'status' key
print()


# -----------------------------------------------------------------------------
# CONCEPT: Dictionary Operations
# -----------------------------------------------------------------------------
# dict["new_key"] = value  — add or update a key-value pair
# del dict["key"]          — remove a key-value pair
# "key" in dict            — check if key exists
# dict.get("key", default) — get value or default if key missing

# Worked example:
policy = {"name": "Access Control", "version": 1.0, "status": "Draft"}

print("=== Dictionary Operations ===")
print(f"Before: {policy}")

policy["status"] = "Approved"  # Update existing key
policy["owner"] = "CISO"  # Add new key
print(f"After update: {policy}")

print(f"Has 'owner' key? {'owner' in policy}")
print(f"Review date: {policy.get('review_date', 'Not set')}")  # Key doesn't exist, returns default
print()


# YOUR TURN: Update a risk dictionary
# Fill in the blanks:

risk_entry = {
    "id": "RISK-005",
    "title": "Ransomware Attack",
    "likelihood": 3,
    "impact": 5,
}

# Calculate and add the risk score
risk_entry["score"] = ______  # Calculate: likelihood * impact

# Add a treatment strategy
risk_entry[______] = "Mitigate"  # Add a new key called "treatment"

# Update the likelihood (new intelligence suggests it's more likely now)
risk_entry["likelihood"] = ______  # Change from 3 to 4

# Recalculate the score with new likelihood
risk_entry["score"] = ______  # Recalculate with updated likelihood

print(f"Risk: {risk_entry['title']}")
print(f"Score: {risk_entry['score']} (was 15, now should be 20)")
print(f"Treatment: {risk_entry['treatment']}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Lists of Dictionaries
# -----------------------------------------------------------------------------
# The real power: a list where each item is a dictionary.
# This is how you represent a table of data (like a risk register).

# Worked example:
risk_register = [
    {"id": "RISK-001", "title": "Phishing Attack", "score": 16},
    {"id": "RISK-002", "title": "Cloud Misconfiguration", "score": 15},
    {"id": "RISK-003", "title": "Key Person Dependency", "score": 12},
]

print("=== Lists of Dictionaries ===")
print(f"Number of risks: {len(risk_register)}")
print(f"First risk: {risk_register[0]['title']} (Score: {risk_register[0]['score']})")
print()


# YOUR TURN: Build a mini compliance register
# Fill in the blanks:

controls = [
    {"id": "CC6.1", "framework": "SOC 2", "status": "Implemented"},
    ______,  # Add a dict: {"id": "PR.AA-05", "framework": "NIST CSF", "status": "Partially Implemented"}
    ______,  # Add a dict: {"id": "A.8.3", "framework": "ISO 27001", "status": "Not Implemented"}
]

print(f"Total controls tracked: {len(controls)}")
print(f"First control: {controls[0]['id']} — {controls[0]['status']}")
print(f"Second control: {controls[1]['id']} — {controls[1]['status']}")
print(f"Third control: {controls[2]['id']} — {controls[2]['status']}")
print()


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (Challenge)
# -----------------------------------------------------------------------------
# Build a small risk register as a list of dictionaries.
# Create 3 risks, each with: id, title, likelihood, impact, score, severity
#
# Then print:
#   1. The total number of risks
#   2. The risk with the highest score
#   3. A formatted summary of each risk
#
# Hint: To find the highest score, you can use a loop (Exercise 03),
# or you can compare manually since there are only 3 risks.
#
# Write your code below:

