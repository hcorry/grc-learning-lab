"""
app.py

Flask web server for the GRC Grader.
Bound to 127.0.0.1 only — never exposed beyond localhost.

Start with: python app.py
Then open:  http://127.0.0.1:5000
"""

import os
import secrets
from dotenv import load_dotenv
from flask import (
    Flask, render_template, request, jsonify,
    session, abort, redirect, url_for
)

# Load .env before any other imports that might need the API key
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from file_manager import ARTIFACT_PATHS, ARTIFACT_LABELS, read_artifact, write_artifact
from rate_limiter import check_rate_limit
from grader import grade_artifact

app = Flask(__name__)

# SECRET_KEY is used to sign session cookies and generate CSRF tokens.
# If not set in .env, generate one at startup (it won't persist across restarts,
# which is fine for a local tool — it just means sessions reset on restart).
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

# Sidebar navigation structure — order controls display order
NAV = [
    {
        "section": "Governance — Policies",
        "items": [
            "gov_policy_information_security",
            "gov_policy_acceptable_use",
            "gov_policy_access_control",
            "gov_policy_incident_response",
            "gov_policy_data_classification",
        ]
    },
    {
        "section": "Governance — Procedures",
        "items": [
            "gov_proc_information_security",
            "gov_proc_acceptable_use",
            "gov_proc_access_control",
            "gov_proc_incident_response",
            "gov_proc_data_classification",
        ]
    },
    {
        "section": "Risk Management",
        "items": [
            "risk_methodology",
            "risk_register",
            "risk_treatment_plans",
        ]
    },
    {
        "section": "Compliance",
        "items": [
            "compliance_nist_csf",
            "compliance_soc2",
            "compliance_iso27001",
            "compliance_matrix",
            "compliance_gap_analysis",
        ]
    },
]


def _get_csrf_token():
    """Return (and create if missing) a CSRF token for the current session."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(32)
    return session["csrf_token"]


def _validate_csrf():
    """Abort with 403 if the request's CSRF token doesn't match the session."""
    token = request.headers.get("X-CSRF-Token", "")
    if not secrets.compare_digest(token, session.get("csrf_token", "")):
        abort(403)


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Redirect to the first artifact."""
    return redirect(url_for("editor", artifact_id="gov_policy_information_security"))


@app.route("/editor/<artifact_id>")
def editor(artifact_id):
    """Render the editor for a specific artifact."""
    if artifact_id not in ARTIFACT_PATHS:
        abort(404)

    content = read_artifact(artifact_id)
    csrf_token = _get_csrf_token()

    return render_template(
        "editor.html",
        nav=NAV,
        artifact_id=artifact_id,
        artifact_label=ARTIFACT_LABELS[artifact_id],
        content=content,
        csrf_token=csrf_token,
        labels=ARTIFACT_LABELS,
    )


@app.route("/save", methods=["POST"])
def save():
    """Save artifact content to the corresponding .md file."""
    _validate_csrf()

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    artifact_id = data.get("artifact_id", "")
    content = data.get("content", "")

    if artifact_id not in ARTIFACT_PATHS:
        return jsonify({"error": "Unknown artifact"}), 400

    try:
        write_artifact(artifact_id, content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "ok"})


@app.route("/grade", methods=["POST"])
def grade():
    """Grade artifact content against its rubric using Claude."""
    _validate_csrf()

    # Rate limit check
    allowed, retry_after = check_rate_limit()
    if not allowed:
        return jsonify({
            "error": f"Too many requests. Try again in {retry_after} seconds.",
            "retry_after": retry_after,
        }), 429

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    artifact_id = data.get("artifact_id", "")
    content = data.get("content", "").strip()

    if artifact_id not in ARTIFACT_PATHS:
        return jsonify({"error": "Unknown artifact"}), 400

    if not content:
        return jsonify({"error": "Nothing to grade — write something first."}), 400

    artifact_label = ARTIFACT_LABELS[artifact_id]

    try:
        result = grade_artifact(artifact_id, artifact_label, content)
    except Exception as e:
        return jsonify({"error": f"Grading failed: {str(e)}"}), 500

    return jsonify(result)


if __name__ == "__main__":
    # Sanity check — warn if API key is missing
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n⚠️  WARNING: ANTHROPIC_API_KEY not set in web_app/.env")
        print("   Grading will fail until you add it.\n")

    # 127.0.0.1 only — never 0.0.0.0
    app.run(host="127.0.0.1", port=5000, debug=False)
