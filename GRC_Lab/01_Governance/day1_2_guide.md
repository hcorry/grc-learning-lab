# Days 1-2 Guide: Governance — Policies & Procedures

## What You're Building

Over the next two days, you'll write **5 security policies** and a **companion procedure for each one**. These are the foundation of any GRC program — they define what your organization expects and how people should follow through.

By the end of Day 2, you'll have a complete governance framework for SecureTech Inc.

---

## What Is Governance?

Governance is the system of rules, practices, and processes that direct and control an organization's approach to security. Think of it as the "constitution" of your security program.

In practice, governance means:
- **Policies** — high-level statements of intent ("We will protect customer data")
- **Procedures** — step-by-step instructions for following policies ("Here's how to classify data")
- **Standards** — specific technical requirements ("Passwords must be 12+ characters")
- **Guidelines** — recommended practices ("Consider using a password manager")

For this project, you'll focus on **policies and procedures**. Standards and guidelines are important but less commonly asked about in interviews.

### Why Governance Matters in Interviews

GRC interview questions almost always include some version of:
- *"How would you build a security program from scratch?"*
- *"What policies would you implement first?"*
- *"How do you ensure employees follow security policies?"*

Your answer to all of these starts with governance. Having built 5 policies from scratch gives you concrete stories to tell.

---

## Anatomy of a Security Policy

Every enterprise security policy follows a similar structure. Here's what each section does and why it's there:

| Section | Purpose | Example |
|---|---|---|
| **Purpose** | Why this policy exists — the business need it addresses | "To establish rules for how employees use company systems" |
| **Scope** | Who and what this policy applies to | "All employees, contractors, and third-party vendors using SecureTech systems" |
| **Roles & Responsibilities** | Who is accountable for what | "The CISO approves policy changes; department heads enforce compliance" |
| **Policy Statements** | The actual rules — what is required, allowed, and prohibited | "All access must use multi-factor authentication" |
| **Enforcement** | What happens if someone violates the policy | "Violations may result in disciplinary action up to termination" |
| **Review Schedule** | How often the policy is reviewed and updated | "This policy is reviewed annually or after a significant incident" |

### Tips for Writing Good Policies

1. **Be specific enough to enforce, but general enough to last.** "Use strong passwords" is too vague. "Passwords must be at least 12 characters" is a standard, not a policy. "Users must follow the password standard defined in [link]" is just right for a policy.

2. **Write for the reader, not yourself.** Policies are read by employees, auditors, and executives. Use clear, direct language. Avoid jargon where possible.

3. **Every statement should be enforceable.** If you can't verify compliance or take action on a violation, the statement shouldn't be in the policy.

4. **Use "must" for requirements, "should" for recommendations, "may" for permissions.** This language is standard in compliance frameworks and auditors will look for it.

---

## Worked Example: Information Security Policy

Below is a **fully completed** Information Security Policy for SecureTech Inc. This is your reference for quality and structure. Study it before writing the other four.

The completed example is in `policies/information_security_policy.md`.

**After reading the example, you'll write these four policies yourself:**
1. `acceptable_use_policy.md` — Rules for how employees use company systems
2. `access_control_policy.md` — Who gets access to what, and how
3. `incident_response_policy.md` — What happens when a security incident occurs
4. `data_classification_policy.md` — How to label and handle data based on sensitivity

Each template has section headers, instructions telling you what to include, and prompts to guide your thinking. Use the Information Security Policy as your model.

---

## Policies vs. Procedures

This is a common interview question: **"What's the difference between a policy and a procedure?"**

| | Policy | Procedure |
|---|---|---|
| **Level** | Strategic — the "what" and "why" | Operational — the "how" |
| **Audience** | Everyone in scope | People performing specific tasks |
| **Changes** | Rarely (annual review) | More often (as processes evolve) |
| **Length** | 1-3 pages | Can be longer — step-by-step detail |
| **Example** | "All incidents must be reported within 1 hour" | "Step 1: Open the incident tracking system. Step 2: Click 'New Incident'..." |

For each policy you write, you'll also create a **companion procedure** that explains how to carry out the policy in practice.

---

## Your Day 1-2 Checklist

### Day 1
- [ ] Read this guide completely
- [ ] Study the worked example (Information Security Policy)
- [ ] Write the Acceptable Use Policy
- [ ] Write the Access Control Policy
- [ ] Write companion procedures for the Acceptable Use and Access Control policies
  (The Information Security Procedure is already completed as a worked example)

### Day 2
- [ ] Write the Incident Response Policy
- [ ] Write the Data Classification Policy
- [ ] Write companion procedures for both
- [ ] Complete the Governance Overview
- [ ] Update your skills tracker
- [ ] Commit everything to GitHub

---

## Research Resources

As you write each policy, you'll need to research what's standard. Here are some approaches:

- **Search for "[policy name] template" or "[policy name] example"** — Many organizations publish their policies publicly
- **Look at SANS policy templates** — SANS Institute has widely-used policy templates
- **Read the framework controls** — NIST CSF, SOC 2, and ISO 27001 all reference governance requirements (you'll learn these in Days 5-7, but a quick preview is fine)
- **Think about SecureTech's context** — A 100-person cybersecurity startup has different needs than a 10,000-person bank. Keep policies practical and proportionate

---

## When You're Done

You should be able to:
1. Explain what each policy covers and why it's needed
2. Describe how policies connect to each other (the governance framework)
3. Articulate the difference between a policy and a procedure
4. Talk through your process for creating policies at a new organization

These are all common interview topics. Practice explaining them out loud.
