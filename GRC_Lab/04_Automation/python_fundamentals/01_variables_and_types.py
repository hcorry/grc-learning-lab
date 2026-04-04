# =============================================================================
# Exercise 01: Variables and Data Types
# =============================================================================
# In this exercise, you'll learn how Python stores information using variables.
# Everything in Python has a "type" — text (strings), numbers (integers/floats),
# and true/false values (booleans). These are the building blocks of every program.
#
# WORKED EXAMPLES are provided first, then you'll fill in the blanks.
# Replace every ______ with the correct Python code.
# =============================================================================


# -----------------------------------------------------------------------------
# CONCEPT: Variables
# -----------------------------------------------------------------------------
# A variable is a name that points to a value. You create one with = (assignment).
# Variable names should be descriptive — "risk_score" is better than "x".

# Worked example:
policy_name = "Information Security Policy"
policy_version = 1.0
is_approved = True

print("=== Variables ===")
print(f"Policy: {policy_name}")
print(f"Version: {policy_version}")
print(f"Approved: {is_approved}")
print()


# YOUR TURN: Create variables for a security risk
# Fill in the blanks:

risk_name = ______  # Set this to the string "Phishing Attack"
risk_likelihood = ______  # Set this to the integer 4
risk_impact = ______  # Set this to the integer 4

print(f"Risk: {risk_name}")
print(f"Likelihood: {risk_likelihood}")
print(f"Impact: {risk_impact}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Data Types
# -----------------------------------------------------------------------------
# Python has several basic types:
#   str  — text, always in quotes: "hello" or 'hello'
#   int  — whole numbers: 1, 42, -7
#   float — decimal numbers: 3.14, 2.0, -0.5
#   bool — True or False (capitalized!)
#
# You can check a value's type with type()

# Worked example:
print("=== Data Types ===")
print(f"'{policy_name}' is type: {type(policy_name)}")  # <class 'str'>
print(f"{policy_version} is type: {type(policy_version)}")  # <class 'float'>
print(f"{is_approved} is type: {type(is_approved)}")  # <class 'bool'>
print()


# YOUR TURN: Create one variable of each type for GRC data
# Fill in the blanks:

framework_name = ______  # A string: "NIST CSF 2.0"
total_controls = ______  # An integer: the number 108
compliance_percentage = ______  # A float: 73.5
audit_passed = ______  # A boolean: False

print(f"Framework: {framework_name} ({type(framework_name)})")
print(f"Total controls: {total_controls} ({type(total_controls)})")
print(f"Compliance: {compliance_percentage}% ({type(compliance_percentage)})")
print(f"Audit passed: {audit_passed} ({type(audit_passed)})")
print()


# -----------------------------------------------------------------------------
# CONCEPT: String Operations
# -----------------------------------------------------------------------------
# Strings are text. You can combine them, format them, and manipulate them.
#
# Concatenation (combining): "hello" + " " + "world" → "hello world"
# f-strings (formatting): f"Score is {score}" — puts the variable's value in the string
# Methods: "hello".upper() → "HELLO", "HELLO".lower() → "hello"

# Worked example:
department = "Engineering"
role = "Security Analyst"
full_title = f"{role} — {department}"
print("=== String Operations ===")
print(f"Full title: {full_title}")
print(f"Uppercase: {full_title.upper()}")
print(f"Title has {len(full_title)} characters")
print()


# YOUR TURN: Build a risk description string
# Fill in the blanks:

threat = "External Attacker"
vulnerability = "Unpatched Software"

# Combine threat and vulnerability into a risk description using an f-string
risk_description = ______  # Should produce: "Threat: External Attacker | Vulnerability: Unpatched Software"

print(f"Risk description: {risk_description}")
print(f"Description length: {len(risk_description)} characters")
print(f"Uppercase: {risk_description.upper()}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Number Operations
# -----------------------------------------------------------------------------
# Python does math with standard operators:
#   +  addition       -  subtraction
#   *  multiplication /  division
#   ** exponent       // integer division (rounds down)
#   %  modulo (remainder)

# Worked example:
likelihood = 4
impact = 5
risk_score = likelihood * impact
print("=== Number Operations ===")
print(f"Risk score: {likelihood} × {impact} = {risk_score}")
print()


# YOUR TURN: Calculate risk scores
# Fill in the blanks:

risk_a_likelihood = 3
risk_a_impact = 4
risk_a_score = ______  # Calculate: likelihood times impact (should be 12)

risk_b_likelihood = 5
risk_b_impact = 2
risk_b_score = ______  # Calculate: likelihood times impact (should be 10)

# Calculate the average of the two risk scores
average_score = ______  # Add both scores and divide by 2 (should be 11.0)

print(f"Risk A score: {risk_a_score}")
print(f"Risk B score: {risk_b_score}")
print(f"Average score: {average_score}")
print()


# -----------------------------------------------------------------------------
# CONCEPT: Type Conversion
# -----------------------------------------------------------------------------
# Sometimes you need to convert between types:
#   str(42)    → "42"    (number to string)
#   int("42")  → 42      (string to number)
#   float("3.14") → 3.14

# Worked example:
score_as_string = "16"
score_as_number = int(score_as_string)
print("=== Type Conversion ===")
print(f"String: '{score_as_string}' → Number: {score_as_number}")
print(f"Can do math now: {score_as_number + 4}")
print()


# YOUR TURN: Convert between types
# Fill in the blanks:

controls_text = "93"
controls_number = ______  # Convert controls_text to an integer

implemented = 68
implementation_rate = ______  # Divide implemented by controls_number, multiply by 100 (should be about 73.1)

summary = ______  # Create an f-string: "68 of 93 controls implemented (73.1%)"
# Hint: Use round(implementation_rate, 1) to round to 1 decimal place

print(summary)
print()


# -----------------------------------------------------------------------------
# TRY IT YOURSELF (Challenge)
# -----------------------------------------------------------------------------
# No blanks here — write the code yourself from scratch.
#
# Create variables for a complete risk entry:
#   - risk_id (string): "RISK-001"
#   - risk_title (string): any risk title you choose
#   - category (string): any risk category
#   - likelihood (int): a number 1-5
#   - impact (int): a number 1-5
#   - risk_score (calculated): likelihood * impact
#   - severity (string): based on score — "Critical" if >= 20, "High" if >= 12,
#                         "Medium" if >= 6, "Low" if < 6
#     (Hint: you haven't learned if/else yet, so just assign the correct
#      severity string manually based on your score)
#
# Then print a formatted summary using f-strings like:
#   "RISK-001: [Title] | Category: [Category] | Score: [Score] (Severity)"
#
# Write your code below:

