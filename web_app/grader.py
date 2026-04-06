"""
grader.py

Loads rubrics and calls the Claude API to grade GRC artifact content.
The API key is never exposed outside this module — it's loaded from .env
by app.py before this module is used.
"""

import json
import os
import anthropic

# Map artifact IDs to their rubric file
_RUBRIC_MAP = {
    "gov_policy_information_security":  "policies",
    "gov_policy_acceptable_use":        "policies",
    "gov_policy_access_control":        "policies",
    "gov_policy_incident_response":     "policies",
    "gov_policy_data_classification":   "policies",
    "gov_proc_information_security":    "policies",
    "gov_proc_acceptable_use":          "policies",
    "gov_proc_access_control":          "policies",
    "gov_proc_incident_response":       "policies",
    "gov_proc_data_classification":     "policies",
    "risk_methodology":                 "risk",
    "risk_register":                    "risk",
    "risk_treatment_plans":             "risk",
    "compliance_nist_csf":              "compliance",
    "compliance_soc2":                  "compliance",
    "compliance_iso27001":              "compliance",
    "compliance_matrix":                "compliance",
    "compliance_gap_analysis":          "compliance",
}

_RUBRICS_DIR = os.path.join(os.path.dirname(__file__), "rubrics")

# Cache loaded rubrics so we don't re-read files on every request
_rubric_cache = {}


def _load_rubric(artifact_id):
    rubric_name = _RUBRIC_MAP.get(artifact_id)
    if not rubric_name:
        raise ValueError(f"No rubric for artifact: {artifact_id!r}")
    if rubric_name not in _rubric_cache:
        path = os.path.join(_RUBRICS_DIR, f"{rubric_name}.json")
        with open(path, "r", encoding="utf-8") as f:
            _rubric_cache[rubric_name] = json.load(f)
    return _rubric_cache[rubric_name]


_SYSTEM_PROMPT = """You are a senior GRC Manager with 15+ years of experience in information security governance, risk management, and compliance programs. You are reviewing work submitted by a junior GRC Analyst who is actively learning and building their first GRC program for a cybersecurity startup called SecureTech Inc.

Your role is to give them the kind of feedback a great manager gives: honest, technically precise, and deeply educational. You don't just say what's missing — you explain WHY it matters, what an auditor or assessor would think when they see it, and exactly how to fix it.

Tone: Direct and knowledgeable, but patient and encouraging. You use correct GRC terminology (control objectives, residual risk, trust service criteria, annex controls, likelihood x impact matrix, etc.) but you always explain what those terms mean in plain language immediately after using them. Never assume the reader already knows the jargon.

Feedback length: Substantial. Minimum 3 paragraphs. If there's a lot to say, say it — this person needs to understand the material deeply to succeed in interviews and on the job.

You MUST respond with valid JSON in exactly this structure — no extra text before or after:
{
  "score": <integer 0-10>,
  "max_score": 10,
  "checklist": [
    {"item": "<criterion name>", "status": "<pass|partial|fail>", "note": "<one sentence explanation>"}
  ],
  "feedback": "<3-5 paragraphs of narrative feedback>"
}

Scoring: Award points proportional to how well each required and recommended criterion is met. Required criteria with weight 2 are worth up to 2 points. Required criteria with weight 1 are worth up to 1 point. Recommended criteria add bonus points up to the max score of 10.

Checklist statuses:
- pass: criterion is clearly met
- partial: criterion is attempted but incomplete or unclear
- fail: criterion is missing or significantly wrong"""


def grade_artifact(artifact_id, artifact_label, content):
    """
    Grade a GRC artifact against its rubric using Claude.

    Returns a dict with keys: score, max_score, checklist, feedback
    Raises on API errors.
    """
    rubric = _load_rubric(artifact_id)

    rubric_text = json.dumps(rubric, indent=2)

    user_message = f"""Please grade the following GRC artifact.

Artifact type: {artifact_label}
Artifact ID: {artifact_id}

Rubric:
{rubric_text}

--- SUBMITTED CONTENT BELOW ---

{content}

--- END OF SUBMITTED CONTENT ---

Evaluate the content against each rubric criterion and return your response as JSON."""

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        system=_SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    raw = message.content[0].text.strip()

    # Parse and validate the response
    result = json.loads(raw)

    # Ensure required keys are present
    for key in ("score", "max_score", "checklist", "feedback"):
        if key not in result:
            raise ValueError(f"Claude response missing key: {key!r}")

    return result
