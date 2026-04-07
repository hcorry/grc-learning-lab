# Days 8–10 Guide: GRC Automation Theory

**Estimated time: 3–4 hours**

You are NOT writing code in this module. The goal is to understand *why* GRC automation exists, *what* the tools you'd build would do, and *how to talk about automation* in a GRC interview.

---

## Why Manual GRC Breaks at Scale

Everything you built in Week 1 — policies, risk registers, compliance matrices — was done manually. That's the right way to learn GRC. But in a real organization, manual GRC has a ceiling:

| Problem | Manual Reality | What Breaks |
|---|---|---|
| **Risk updates** | Someone has to manually update the register when new risks emerge or scores change | Register becomes stale within weeks |
| **Compliance drift** | Controls you documented as "implemented" get changed by engineers without updating the matrix | Compliance status is always slightly wrong |
| **Reporting** | Every board meeting requires someone to manually compile data from 6 spreadsheets | Reports take days and contain errors |
| **Scale** | A 100-person company has manageable complexity. A 1,000-person company has 10x the risks, systems, and controls | Manual processes collapse |

**The solution:** Automate the data collection, scoring, and reporting so your team spends time on decisions — not data entry.

---

## The Three GRC Automation Tools

This project includes three automation tools that address the problems above. You don't need to build them, but you need to understand what they do and why.

### Tool 1: Risk Scorer

**What it does:** Reads a spreadsheet (CSV file) of risks, calculates risk scores using the 5×5 matrix you built in Days 3–4, and outputs a sorted, prioritized report.

**Why it matters:** In a real GRC program, risks get added constantly — new vendor, new product feature, new regulation. A risk scorer can recalculate your entire risk register in seconds when scores change. Manual recalculation takes hours and introduces errors.

**Real-world equivalent:** GRC platforms like ServiceNow GRC, Archer, and OneTrust all have built-in risk scoring engines that do exactly this — just with a more sophisticated UI.

**Interview talking point:** "I understand that at scale, risk scoring needs to be automated so the register stays current. I built a risk scorer that reads from a data file, applies the 5×5 matrix, and outputs a prioritized report — the same logic a GRC platform uses under the hood."

---

### Tool 2: Compliance Mapper

**What it does:** Takes a control from one framework (e.g., NIST CSF PR.AA-05) and instantly shows the equivalent controls in SOC 2 and ISO 27001.

**Why it matters:** GRC teams spend enormous time answering customer security questionnaires and mapping evidence to multiple frameworks. A compliance mapper turns a 2-hour manual process into a 2-second lookup.

**Real-world equivalent:** Drata, Vanta, and Secureframe — the most popular modern compliance platforms — are essentially sophisticated compliance mappers. They integrate with your tools (AWS, GitHub, Okta), automatically collect evidence, and map it across frameworks.

**Interview talking point:** "I built a cross-framework compliance mapper that links equivalent controls across NIST CSF, SOC 2, and ISO 27001. This is the same concept as Vanta or Drata — implement a control once and have it satisfy requirements across multiple frameworks simultaneously."

---

### Tool 3: Report Generator

**What it does:** Combines risk data and compliance data to generate an executive summary report — the kind a CISO would present to the board.

**Why it matters:** Executives don't read spreadsheets. They need narrative, context, and clear priorities. A report generator transforms raw GRC data into a communication-ready document on demand, instead of requiring a GRC analyst to spend half a day formatting.

**Real-world equivalent:** Every GRC platform has a reporting module. Archer and ServiceNow generate board-ready dashboards automatically. Even simpler tools like Vanta have PDF report generation built in.

**Interview talking point:** "I understand that GRC data only drives decisions when it's in a format executives can act on. I designed a report generator that pulls from the risk register and compliance matrix to produce an executive summary — the same output a CISO would bring to a board meeting."

---

## The GRC Platform Landscape

In real GRC roles, you'll use commercial tools rather than building everything from scratch. Here's what you need to know:

### Enterprise GRC Platforms (Large Companies)
These are complex, expensive, and highly customizable:
- **ServiceNow GRC** — Most common in enterprise. Integrated with IT service management. Expensive and complex to configure.
- **Archer (RSA)** — Legacy enterprise platform. Common in financial services and heavily regulated industries.
- **MetricStream** — Common in financial services and healthcare.

### Modern Compliance Automation (Startups & Mid-Market)
These are what you'll see at companies like SecureTech:
- **Vanta** — Most popular for SOC 2 automation. Integrates with your tools (AWS, GitHub, Okta, etc.) and continuously monitors controls. Companies typically achieve SOC 2 in 3–6 months with Vanta vs. 12–18 months manually.
- **Drata** — Similar to Vanta. Strong on multi-framework support (SOC 2 + ISO 27001 + HIPAA simultaneously).
- **Secureframe** — Another SOC 2/ISO 27001 automation platform. Common in SaaS companies.
- **Sprinto** — Popular in earlier-stage startups.

### GRC-Adjacent Tools
- **Jira / Linear** — Used for tracking remediation tasks from risk assessments and gap analyses
- **Confluence / Notion** — Often used for policy documentation at smaller companies
- **Qualys / Tenable** — Vulnerability management (feeds into risk assessments)
- **Wiz / Lacework** — Cloud security posture management (automated compliance checks for cloud infrastructure)

**SecureTech context:** A company SecureTech's size preparing for SOC 2 would almost certainly use Vanta or Drata rather than building custom tools or using ServiceNow. The custom tools in this project teach you the *concepts* behind what those platforms do.

---

## How Automation Fits Into Your GRC Career

### What You'll Actually Do With Automation in a GRC Role

**Junior GRC Analyst:**
- Configure and maintain a tool like Vanta or Drata
- Connect integrations (AWS, GitHub, Okta) so the platform can collect evidence automatically
- Review automated alerts when controls drift out of compliance
- Export reports and dashboards for leadership and auditors

**Mid-Level GRC / Compliance Engineer:**
- Build custom integrations when the platform doesn't support a specific tool
- Write scripts to pull data from systems that don't have native integrations (similar to the risk scorer and compliance mapper)
- Build dashboards in tools like Tableau or PowerBI on top of GRC data
- Automate questionnaire responses using a controls library

**Senior GRC / GRC Manager:**
- Select and implement GRC platforms
- Design the data model for how risks, controls, and evidence connect
- Build the business case for automation tooling investment
- Define what gets automated vs. what requires human judgment

### What You Can Say in Interviews Right Now

Even without working with Vanta or Drata professionally, you can speak to automation because you built the logic yourself:

> "I understand GRC automation from the ground up — I built a risk scorer that applies a 5×5 matrix to a dataset and outputs a prioritized report, a compliance mapper that links equivalent controls across three frameworks, and a report generator that produces executive-ready output from raw GRC data. These tools taught me the same concepts that underpin platforms like Vanta and Drata. I'm comfortable picking up those tools quickly because I understand what they're doing under the hood."

---

## Days 8–10 Checklist

### Day 8
- [ ] Read this guide completely
- [ ] Understand what each of the three tools does (without reading code)
- [ ] Research one modern compliance platform (Vanta, Drata, or Secureframe) — look at their website, features, and how they describe themselves

### Day 9
- [ ] Read the automation README in the sidebar to understand the tool inputs/outputs
- [ ] Practice explaining each tool out loud in 60 seconds without looking at notes
- [ ] Think about how you'd use these tools in an interview answer

### Day 10
- [ ] Write the Executive Summary (in the Reports section)
- [ ] Update your skills tracker
- [ ] Final GitHub commit — your complete GRC portfolio

---

## When You're Done With the Full Program

You should be able to answer:

1. *"Walk me through a GRC program you built from scratch."*
2. *"How would you approach a SOC 2 audit for a startup?"*
3. *"What's the difference between a risk and a vulnerability?"*
4. *"How do NIST CSF and SOC 2 relate to each other?"*
5. *"What GRC tools have you worked with?"*
6. *"How would you prioritize remediation across 20 open risks?"*
7. *"Tell me about a time you communicated a complex security topic to a non-technical audience."*

Every one of these has a direct answer in something you built.
