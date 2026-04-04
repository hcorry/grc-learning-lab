# Python Fundamentals — GRC-Themed Exercises

Welcome to Python! These exercises teach you programming basics using GRC data and scenarios — no generic "hello world" here.

## How These Exercises Work

Each exercise file has:
1. **Explanations** of the Python concept (in comments at the top)
2. **Worked examples** showing the concept in action
3. **Fill-in-the-blank exercises** where you write the missing code
4. **A "Try It Yourself" challenge** at the end

The blanks look like this:
```python
risk_score = ______  # Calculate: likelihood times impact
```

Replace `______` with the correct Python code.

## Running the Exercises

Open a terminal and run each exercise with:
```bash
python GRC_Lab/04_Automation/python_fundamentals/01_variables_and_types.py
```

If your code is correct, the output will match what the comments describe. If something's wrong, Python will show you an error message — read it carefully, it usually tells you what to fix.

## Exercise Order

| Exercise | Concepts | Prerequisite |
|---|---|---|
| **01** — Variables and Types | Variables, strings, numbers, booleans, f-strings | None |
| **02** — Lists and Dicts | Lists, dictionaries, accessing elements, adding/removing | Exercise 01 |
| **03** — Conditionals and Loops | if/elif/else, for loops, while loops | Exercise 02 |
| **04** — Functions | Defining functions, parameters, return values | Exercise 03 |
| **05** — File I/O | Reading files, writing files, CSV format | Exercise 04 |

## Schedule

- **Days 8-9:** Complete exercises 01-03, then build `risk_scorer.py`
- **Days 10-11:** Complete exercises 04-05, then build `compliance_mapper.py`

## Tips

- **Type the code yourself** — don't copy-paste. Typing builds muscle memory.
- **Read the error messages** — Python errors are usually descriptive. Start from the bottom of the error.
- **Use `print()` to debug** — When something isn't working, print the variable to see what's in it.
- **Ask Claude Code for help** — But try to solve it yourself first. Say what you've tried and what happened.
