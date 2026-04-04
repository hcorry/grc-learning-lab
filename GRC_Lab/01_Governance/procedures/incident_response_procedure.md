# Incident Response Procedure

**Companion to:** Incident Response Policy
**Document Owner:** CISO
**Version:** 1.0

> 📖 **Instructions:** This is the procedure you'd grab during an actual security incident. It needs to be clear enough that someone could follow it at 2 AM while stressed. Write each procedure as specific, numbered steps.

---

## 1. Incident Reporting Procedure

<!-- YOUR WORK: Write the steps for ANY employee to report a suspected security incident.

Think about:
- What channels can they use to report? (Email? Slack channel? Phone? Incident form?)
- What information should they include? (What happened, when, what systems, what data, who's affected)
- How fast must they report? (Within 1 hour of discovery? Immediately?)
- What should they NOT do? (Don't try to fix it yourself, don't turn off the computer, don't delete anything)
- Who receives the report? (Security team? CISO? IT?)

Write 5-6 numbered steps. Keep it simple — this is for non-technical employees too.
-->

---

## 2. Incident Triage and Severity Classification

<!-- YOUR WORK: Write the steps for the security team to assess an incoming incident report.

Think about:
- Who does the initial triage? (On-call security person? CISO?)
- How do they determine severity? (Reference the severity levels from your policy)
- What questions do they ask to classify? (What type of data? How many users? Is it ongoing? Is it contained?)
- Who gets notified at each severity level?
  - Low → security team tracks it
  - Medium → CISO notified
  - High → CISO + executive team notified
  - Critical → all hands on deck, legal notified, potential external notification
- How fast must triage happen? (Within 30 minutes of report?)

Write 6-8 numbered steps.
-->

---

## 3. Incident Containment

<!-- YOUR WORK: Write the steps for containing an active incident to prevent further damage.

Think about:
- Short-term containment (immediate actions):
  - Isolate affected systems from the network
  - Disable compromised accounts
  - Block malicious IP addresses
  - Redirect traffic if needed
- Evidence preservation (BEFORE you start cleaning up):
  - Take system snapshots/images
  - Preserve logs
  - Document the current state
- Long-term containment (while you prepare for full remediation):
  - Apply temporary fixes
  - Increase monitoring on affected systems
  - Restrict access to affected areas

Write 7-10 numbered steps. This is the most critical procedure — mistakes here can make things worse.
-->

---

## 4. Incident Eradication and Recovery

<!-- YOUR WORK: Write the steps for removing the threat and restoring normal operations.

Think about eradication:
- Identify the root cause
- Remove malware, close vulnerabilities, patch systems
- Reset compromised credentials
- Verify the threat is eliminated (scan, test, verify)

Think about recovery:
- Restore systems from clean backups if needed
- Bring systems back online in a controlled manner (not all at once)
- Verify systems are functioning correctly
- Monitor for recurrence (increased monitoring for 30 days?)

Write 8-10 numbered steps covering both eradication and recovery.
-->

---

## 5. Post-Incident Review (Lessons Learned)

<!-- YOUR WORK: Write the steps for conducting a post-incident review.

Think about:
- When does the review happen? (Within 1 week of incident closure?)
- Who participates? (Everyone involved in the response)
- What questions are covered?
  - What happened? (Timeline of events)
  - What went well in our response?
  - What could we improve?
  - What are the action items? (Policy changes, control improvements, training needs)
- How are findings documented? (Post-incident report)
- Who receives the report? (Executive team, board if severe)
- How are action items tracked to completion?

Write 6-8 numbered steps. Post-incident reviews are where real improvement happens — don't skip this.
-->

---

## 6. Incident Communication Templates

<!-- YOUR WORK: Create brief templates for incident communications. These save critical time during an incident.

### Internal Notification Template
(Subject line, who it's from, what happened, what we're doing, what employees should do, where to get updates)

### External Customer Notification Template (if customer data affected)
(What happened, what data was affected, what we're doing, what customers should do, contact information)

### Regulatory Notification Template (if required by law)
(Organization details, nature of incident, data affected, timeline, remediation steps, contact)

For each template, write a brief fill-in-the-blank format that someone could quickly customize during an incident.
-->
