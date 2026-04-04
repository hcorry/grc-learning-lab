# Learning Notes: compliance_mapper.py

> 📖 **Instructions:** Document what you learned while building the compliance mapper. This tool is more complex than the risk scorer — it introduces interactive input, string pattern matching, and searching across multiple columns.

---

## Concepts Used

### 1. String Pattern Matching

> **✏️ YOUR WORK**
> YOUR WORK: In your own words, explain:
> - How did you detect which framework a control ID belongs to?
> - What string methods did you use? (.startswith(), .upper(), .lower(), "in")
> - Why is case-insensitive matching important for a search tool?

### 2. Searching Across Multiple Columns

> **✏️ YOUR WORK**
> YOUR WORK: In your own words, explain:
> - How did you search for a control ID that could be in any of three columns?
> - What's the approach for checking "does this value appear in column A OR column B OR column C"?
> - How would you handle partial matches (e.g., searching "CC6" to find all CC6.x controls)?

### 3. Interactive Input with while Loops

> **✏️ YOUR WORK**
> YOUR WORK: In your own words, explain:
> - How does the input() function work?
> - How does the while True loop with a "quit" command work?
> - What does .strip() do to user input and why is it important?

### 4. String Formatting for Aligned Output

> **✏️ YOUR WORK**
> YOUR WORK: In your own words, explain:
> - How do f-string width specifiers work? (e.g., {text:<30})
> - What's the difference between < (left-align), > (right-align), and ^ (center)?
> - How did you format the output table to be readable?

### 5. Functions as Building Blocks

> **✏️ YOUR WORK**
> YOUR WORK: In your own words, explain:
> - How do the functions in compliance_mapper.py work together?
> - Which function calls which other functions?
> - Why is breaking the code into functions better than writing everything in main()?

---

## Comparison: risk_scorer.py vs compliance_mapper.py

> **✏️ YOUR WORK**
> YOUR WORK: Compare the two tools. What's different about them?
> - How is reading data different? (One processes all rows, the other searches)
> - How is output different? (One writes a file, the other is interactive)
> - Which was harder to build? Why?

## What Was Hardest

> **✏️ YOUR WORK**
> YOUR WORK: What challenged you most? How did you work through it?

## How This Connects to GRC

> **✏️ YOUR WORK**
> YOUR WORK: When would a GRC professional use a cross-framework mapping tool?
> Think about: audit preparation, vendor questionnaires, control implementation planning, compliance gap analysis.
