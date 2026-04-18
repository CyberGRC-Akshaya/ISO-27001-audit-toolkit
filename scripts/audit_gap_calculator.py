#!/usr/bin/env python3
"""
ISO 27001:2022 Audit Gap Calculator
====================================
Author: Akshaya | GRC Portfolio
Usage: python audit_gap_calculator.py

Calculates compliance scores, identifies gaps, and generates a summary report.
"""

from datetime import datetime

# ── Control Database ──
CONTROLS = {
    "5_ORG": {
        "name": "5. Organisational Controls",
        "controls": {
            "A.5.1": "Policies for information security",
            "A.5.2": "IS roles and responsibilities",
            "A.5.3": "Segregation of duties",
            "A.5.4": "Management responsibilities",
            "A.5.5": "Contact with authorities",
            "A.5.7": "Threat intelligence",
            "A.5.9": "Information asset inventory",
            "A.5.12": "Classification of information",
            "A.5.15": "Access control",
            "A.5.16": "Identity management",
            "A.5.17": "Authentication information",
            "A.5.18": "Access rights",
            "A.5.19": "IS in supplier relationships",
            "A.5.24": "IS incident management planning",
            "A.5.26": "Response to IS incidents",
            "A.5.29": "IS during disruption",
            "A.5.30": "ICT readiness for business continuity",
        }
    },
    "6_PEOPLE": {
        "name": "6. People Controls",
        "controls": {
            "A.6.1": "Screening",
            "A.6.2": "Terms of employment",
            "A.6.3": "IS awareness training",
            "A.6.4": "Disciplinary process",
            "A.6.5": "Responsibilities after termination",
            "A.6.7": "Remote working",
            "A.6.8": "IS event reporting",
        }
    },
    "7_PHYSICAL": {
        "name": "7. Physical Controls",
        "controls": {
            "A.7.1": "Physical security perimeters",
            "A.7.2": "Physical entry",
            "A.7.4": "Physical security monitoring",
            "A.7.7": "Clear desk and screen",
            "A.7.10": "Storage media",
            "A.7.14": "Secure disposal of equipment",
        }
    },
    "8_TECH": {
        "name": "8. Technological Controls",
        "controls": {
            "A.8.2": "Privileged access rights",
            "A.8.5": "Secure authentication",
            "A.8.7": "Protection against malware",
            "A.8.8": "Technical vulnerability management",
            "A.8.12": "Data leakage prevention",
            "A.8.15": "Logging",
            "A.8.16": "Monitoring activities",
            "A.8.20": "Network security",
            "A.8.22": "Segregation of networks",
            "A.8.24": "Use of cryptography",
            "A.8.25": "Secure development lifecycle",
            "A.8.32": "Change management",
        }
    }
}

# ── Sample Assessment Results ──
# Replace with your actual audit results
# Status: "C" = Conforming, "PC" = Partial, "NC_Minor", "NC_Major", "NA"
SAMPLE_RESULTS = {
    "A.5.1": "C",   "A.5.2": "C",    "A.5.3": "PC",   "A.5.4": "C",
    "A.5.5": "C",   "A.5.7": "NC_Minor", "A.5.9": "PC", "A.5.12": "C",
    "A.5.15": "C",  "A.5.16": "C",   "A.5.17": "C",   "A.5.18": "NC_Minor",
    "A.5.19": "C",  "A.5.24": "C",   "A.5.26": "C",   "A.5.29": "PC",   "A.5.30": "C",
    "A.6.1": "C",   "A.6.2": "C",    "A.6.3": "NC_Minor", "A.6.4": "C",
    "A.6.5": "C",   "A.6.7": "PC",   "A.6.8": "C",
    "A.7.1": "C",   "A.7.2": "C",    "A.7.4": "C",    "A.7.7": "NC_Minor",
    "A.7.10": "PC", "A.7.14": "C",
    "A.8.2": "C",   "A.8.5": "C",    "A.8.7": "C",    "A.8.8": "NC_Minor",
    "A.8.12": "PC", "A.8.15": "C",   "A.8.16": "C",   "A.8.20": "C",
    "A.8.22": "C",  "A.8.24": "C",   "A.8.25": "PC",  "A.8.32": "C",
}

def score_result(status):
    return {"C": 1.0, "PC": 0.5, "NC_Minor": 0.0, "NC_Major": 0.0, "NA": None}.get(status, 0)

def calculate_scores(results):
    category_scores = {}
    all_scores = []

    for cat_id, cat_data in CONTROLS.items():
        cat_scores = []
        findings = []
        for ctrl_id, ctrl_name in cat_data["controls"].items():
            status = results.get(ctrl_id, "PC")
            score = score_result(status)
            if score is not None:
                cat_scores.append(score)
                all_scores.append(score)
            if status in ("NC_Minor", "NC_Major", "PC"):
                findings.append((ctrl_id, ctrl_name, status))
        avg = sum(cat_scores) / len(cat_scores) * 100 if cat_scores else 0
        category_scores[cat_id] = {
            "name": cat_data["name"],
            "score": avg,
            "total": len(cat_scores),
            "conforming": sum(1 for s in cat_scores if s == 1.0),
            "findings": findings
        }

    overall = sum(all_scores) / len(all_scores) * 100 if all_scores else 0
    return category_scores, overall

def print_report(results):
    category_scores, overall = calculate_scores(results)
    width = 65

    print("=" * width)
    print("  ISO 27001:2022 AUDIT GAP ANALYSIS REPORT")
    print(f"  Generated: {datetime.now().strftime('%d %B %Y %H:%M')}")
    print("=" * width)

    # Overall score
    bar_len = int(overall / 2)
    bar = "█" * bar_len + "░" * (50 - bar_len)
    print(f"\n  OVERALL COMPLIANCE SCORE")
    print(f"  [{bar}] {overall:.1f}%")

    if overall >= 90:
        verdict = "CERTIFICATION READY ✅"
    elif overall >= 75:
        verdict = "NEAR READY — Minor NCs to resolve ⚠️"
    elif overall >= 60:
        verdict = "IMPROVEMENT NEEDED — Multiple gaps 🟡"
    else:
        verdict = "SIGNIFICANT GAPS — Major programme work required 🔴"
    print(f"  Status: {verdict}\n")

    # Category breakdown
    print("-" * width)
    print(f"  {'CATEGORY':<42} {'SCORE':<10} {'FINDINGS'}")
    print("-" * width)

    for cat_id, data in category_scores.items():
        score_bar = "█" * int(data['score']/5) + "░" * (20 - int(data['score']/5))
        nc_count = len(data['findings'])
        flag = "⚠️" if nc_count > 0 else "✅"
        print(f"  {data['name']:<42} {data['score']:.0f}%     {flag} {nc_count} finding(s)")

    # Findings detail
    print("\n" + "=" * width)
    print("  FINDINGS REQUIRING ACTION")
    print("=" * width)

    for cat_id, data in category_scores.items():
        if data["findings"]:
            print(f"\n  📂 {data['name']}")
            for ctrl_id, ctrl_name, status in data["findings"]:
                icon = {"PC": "🟡", "NC_Minor": "🟠", "NC_Major": "🔴"}.get(status, "⚪")
                label = {"PC": "Partial", "NC_Minor": "Minor NC", "NC_Major": "Major NC"}.get(status, status)
                print(f"     {icon} [{ctrl_id}] {ctrl_name}")
                print(f"        Status: {label}")

    print("\n" + "=" * width)
    print("  SUMMARY")
    print("=" * width)
    all_findings = []
    for data in category_scores.values():
        all_findings.extend(data["findings"])

    print(f"  Controls assessed:    {sum(d['total'] for d in category_scores.values())}")
    print(f"  Fully conforming:     {sum(d['conforming'] for d in category_scores.values())}")
    print(f"  Partial conformance:  {sum(1 for _, _, s in all_findings if s == 'PC')}")
    print(f"  Minor NC:             {sum(1 for _, _, s in all_findings if s == 'NC_Minor')}")
    print(f"  Major NC:             {sum(1 for _, _, s in all_findings if s == 'NC_Major')}")
    print(f"\n  Overall score:        {overall:.1f}%")
    print("=" * width)

if __name__ == "__main__":
    print_report(SAMPLE_RESULTS)
