"""
file_manager.py

Safe read/write for GRC artifact markdown files.
Uses an explicit whitelist — no dynamic path construction from user input.
"""

import os

# Base directory of the project (one level up from web_app/)
_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Explicit map of artifact IDs to relative paths within the project.
# ONLY these paths can be read or written — nothing else.
ARTIFACT_PATHS = {
    # Program overview & company reference
    "program_overview":                  "GRC_Lab/program_overview.md",
    "company_profile":                   "GRC_Lab/securetech_company_profile.md",

    # Automation theory
    "guide_automation_theory":           "GRC_Lab/04_Automation/day8_10_guide_automation_theory.md",
    "automation_readme":                 "GRC_Lab/04_Automation/README.md",

    # Reports
    "report_executive_summary":          "GRC_Lab/05_Reports/executive_summary.md",

    # Guides (split by section)
    "guide_day1_policies":               "GRC_Lab/01_Governance/day1_guide_policies.md",
    "guide_day2_procedures":             "GRC_Lab/01_Governance/day2_guide_procedures.md",
    "guide_day3_4":                      "GRC_Lab/02_Risk/day3_4_guide.md",
    "guide_day5_7":                      "GRC_Lab/03_Compliance/day5_7_guide.md",

    # Governance — Overview
    "gov_overview":                      "GRC_Lab/01_Governance/governance_overview.md",

    # Governance — Policies
    "gov_policy_information_security":  "GRC_Lab/01_Governance/policies/information_security_policy.md",
    "gov_policy_acceptable_use":        "GRC_Lab/01_Governance/policies/acceptable_use_policy.md",
    "gov_policy_access_control":        "GRC_Lab/01_Governance/policies/access_control_policy.md",
    "gov_policy_incident_response":     "GRC_Lab/01_Governance/policies/incident_response_policy.md",
    "gov_policy_data_classification":   "GRC_Lab/01_Governance/policies/data_classification_policy.md",

    # Governance — Procedures
    "gov_proc_information_security":    "GRC_Lab/01_Governance/procedures/information_security_procedure.md",
    "gov_proc_acceptable_use":          "GRC_Lab/01_Governance/procedures/acceptable_use_procedure.md",
    "gov_proc_access_control":          "GRC_Lab/01_Governance/procedures/access_control_procedure.md",
    "gov_proc_incident_response":       "GRC_Lab/01_Governance/procedures/incident_response_procedure.md",
    "gov_proc_data_classification":     "GRC_Lab/01_Governance/procedures/data_classification_procedure.md",

    # Risk Management
    "risk_methodology":                 "GRC_Lab/02_Risk/risk_methodology.md",
    "risk_register":                    "GRC_Lab/02_Risk/risk_register.md",
    "risk_treatment_plans":             "GRC_Lab/02_Risk/risk_treatment_plans.md",

    # Compliance
    "compliance_nist_csf":              "GRC_Lab/03_Compliance/framework_controls/nist_csf_2.md",
    "compliance_soc2":                  "GRC_Lab/03_Compliance/framework_controls/soc2_criteria.md",
    "compliance_iso27001":              "GRC_Lab/03_Compliance/framework_controls/iso27001_annex_a.md",
    "compliance_matrix":                "GRC_Lab/03_Compliance/compliance_matrix.md",
    "compliance_gap_analysis":          "GRC_Lab/03_Compliance/gap_analysis.md",
}

# Human-readable labels for the sidebar
ARTIFACT_LABELS = {
    "program_overview":                  "Program Overview & Schedule",
    "company_profile":                   "SecureTech Inc. — Company Profile",
    "guide_automation_theory":           "Days 8–10 Guide: Automation Theory",
    "automation_readme":                 "Automation Tools — Reference",
    "report_executive_summary":          "Executive Summary",
    "guide_day1_policies":               "Day 1 Guide: Policies",
    "guide_day2_procedures":             "Day 2 Guide: Procedures",
    "guide_day3_4":                      "Day 3–4 Guide: Risk Management",
    "guide_day5_7":                      "Day 5–7 Guide: Compliance",
    "gov_overview":                      "Governance Overview",
    "gov_policy_information_security":  "Information Security Policy",
    "gov_policy_acceptable_use":        "Acceptable Use Policy",
    "gov_policy_access_control":        "Access Control Policy",
    "gov_policy_incident_response":     "Incident Response Policy",
    "gov_policy_data_classification":   "Data Classification Policy",
    "gov_proc_information_security":    "Information Security Procedure",
    "gov_proc_acceptable_use":          "Acceptable Use Procedure",
    "gov_proc_access_control":          "Access Control Procedure",
    "gov_proc_incident_response":       "Incident Response Procedure",
    "gov_proc_data_classification":     "Data Classification Procedure",
    "risk_methodology":                 "Risk Methodology",
    "risk_register":                    "Risk Register",
    "risk_treatment_plans":             "Risk Treatment Plans",
    "compliance_nist_csf":              "NIST CSF 2.0",
    "compliance_soc2":                  "SOC 2 Criteria",
    "compliance_iso27001":              "ISO 27001 Annex A",
    "compliance_matrix":                "Compliance Matrix",
    "compliance_gap_analysis":          "Gap Analysis",
}


def _resolve(artifact_id):
    """
    Returns the absolute path for an artifact_id, or raises ValueError
    if the ID is not in the whitelist.
    """
    if artifact_id not in ARTIFACT_PATHS:
        raise ValueError(f"Unknown artifact: {artifact_id!r}")
    return os.path.join(_BASE, ARTIFACT_PATHS[artifact_id])


def read_artifact(artifact_id):
    """
    Read and return the content of a whitelisted artifact file.
    Returns empty string if the file doesn't exist yet.
    """
    path = _resolve(artifact_id)
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_artifact(artifact_id, content):
    """
    Write content to a whitelisted artifact file.
    Creates parent directories if needed.
    Raises ValueError for unknown artifact IDs.
    """
    path = _resolve(artifact_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
