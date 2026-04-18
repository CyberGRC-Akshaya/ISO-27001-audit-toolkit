#!/usr/bin/env python3
"""
ISO 27001 Audit — Risk & Control Gap Heatmap Generator
======================================================
Author: Akshaya | GRC Portfolio
Usage: python risk_heatmap.py [--csv input.csv] [--output heatmap.png]

Generates a visual risk heatmap from audit findings or risk register data.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import argparse
import csv
import os
from datetime import datetime

# Default sample data — replace with your risk register
DEFAULT_RISKS = [
    {"id": "R-001", "name": "Unauthorised Access\n(Privileged Accounts)", "likelihood": 4, "impact": 5, "control": "A.8.2"},
    {"id": "R-002", "name": "Data Breach\n(Misconfigured Cloud)", "likelihood": 3, "impact": 5, "control": "A.8.23"},
    {"id": "R-003", "name": "Ransomware Attack", "likelihood": 4, "impact": 5, "control": "A.8.7"},
    {"id": "R-004", "name": "Insider Threat\n(Data Exfiltration)", "likelihood": 2, "impact": 5, "control": "A.8.12"},
    {"id": "R-005", "name": "Vendor/Supply Chain\nCompromise", "likelihood": 3, "impact": 4, "control": "A.5.19"},
    {"id": "R-006", "name": "Phishing /\nBEC Attack", "likelihood": 5, "impact": 3, "control": "A.6.3"},
    {"id": "R-007", "name": "Unpatched\nVulnerabilities", "likelihood": 4, "impact": 3, "control": "A.8.8"},
    {"id": "R-008", "name": "DDoS Attack", "likelihood": 3, "impact": 3, "control": "A.8.20"},
    {"id": "R-009", "name": "Physical Security\nBreach", "likelihood": 2, "impact": 3, "control": "A.7.2"},
    {"id": "R-010", "name": "Loss of Backup\nIntegrity", "likelihood": 2, "impact": 4, "control": "A.8.13"},
    {"id": "R-011", "name": "GDPR/DPDPA\nNon-compliance", "likelihood": 3, "impact": 4, "control": "A.5.34"},
    {"id": "R-012", "name": "Change Management\nFailure (SOX)", "likelihood": 2, "impact": 5, "control": "A.8.32"},
]

def get_color(likelihood, impact):
    score = likelihood * impact
    if score >= 16:
        return '#d32f2f', 'CRITICAL'
    elif score >= 12:
        return '#e64a19', 'HIGH'
    elif score >= 6:
        return '#f57c00', 'MEDIUM'
    else:
        return '#388e3c', 'LOW'

def create_heatmap(risks, output_file='iso27001_risk_heatmap.png'):
    fig, axes = plt.subplots(1, 2, figsize=(18, 9))
    fig.patch.set_facecolor('#1a1814')

    # ── Left: Scatter Risk Heatmap ──
    ax1 = axes[0]
    ax1.set_facecolor('#1e1c18')

    # Background risk zones
    zone_colors = [
        ['#1b5e20', '#2e7d32', '#f57f17', '#e65100', '#b71c1c'],
        ['#1b5e20', '#2e7d32', '#f57f17', '#e65100', '#b71c1c'],
        ['#1b5e20', '#f57f17', '#e65100', '#b71c1c', '#b71c1c'],
        ['#f57f17', '#e65100', '#b71c1c', '#b71c1c', '#b71c1c'],
        ['#e65100', '#b71c1c', '#b71c1c', '#b71c1c', '#b71c1c'],
    ]
    for i in range(5):
        for j in range(5):
            rect = plt.Rectangle((j+0.5, i+0.5), 1, 1,
                color=zone_colors[i][j], alpha=0.12, zorder=1)
            ax1.add_patch(rect)

    # Plot each risk
    plotted = {}
    for risk in risks:
        l, im = risk['likelihood'], risk['impact']
        key = (l, im)
        offset = plotted.get(key, 0) * 0.2
        plotted[key] = plotted.get(key, 0) + 1

        color, level = get_color(l, im)
        ax1.scatter(l + offset, im + offset, c=color, s=280,
                   zorder=4, edgecolors='white', linewidths=1.5, alpha=0.95)
        ax1.annotate(risk['id'],
                    (l + offset, im + offset),
                    textcoords="offset points", xytext=(8, 4),
                    fontsize=7, color='white', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.7, edgecolor='none'))

    ax1.set_xlim(0.5, 5.5)
    ax1.set_ylim(0.5, 5.5)
    ax1.set_xlabel('Likelihood →', color='#b8892a', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Impact →', color='#b8892a', fontsize=11, fontweight='bold')
    ax1.set_title('ISO 27001 Risk Heatmap', color='#f5f0e8', fontsize=14, fontweight='bold', pad=12)
    ax1.set_xticks(range(1, 6))
    ax1.set_xticklabels(['1\nRare', '2\nUnlikely', '3\nPossible', '4\nLikely', '5\nAlmost\nCertain'],
                        color='#8a8579', fontsize=8)
    ax1.set_yticks(range(1, 6))
    ax1.set_yticklabels(['1\nNeg.', '2\nMinor', '3\nModerate', '4\nMajor', '5\nCritical'],
                        color='#8a8579', fontsize=8)
    ax1.tick_params(colors='#8a8579')
    for spine in ax1.spines.values():
        spine.set_edgecolor('#3a3830')

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#d32f2f', label='Critical (≥16)'),
        mpatches.Patch(facecolor='#e64a19', label='High (12–15)'),
        mpatches.Patch(facecolor='#f57c00', label='Medium (6–11)'),
        mpatches.Patch(facecolor='#388e3c', label='Low (<6)'),
    ]
    ax1.legend(handles=legend_elements, loc='lower right',
              facecolor='#2a2820', labelcolor='white', fontsize=8,
              edgecolor='#3a3830')

    ax1.grid(True, alpha=0.08, color='white', linestyle='--')

    # ── Right: Risk Register Bar Chart ──
    ax2 = axes[1]
    ax2.set_facecolor('#1e1c18')

    sorted_risks = sorted(risks, key=lambda r: r['likelihood']*r['impact'], reverse=True)
    names = [r['id'] + ': ' + r['name'].replace('\n', ' ') for r in sorted_risks]
    scores = [r['likelihood'] * r['impact'] for r in sorted_risks]
    colors_list = [get_color(r['likelihood'], r['impact'])[0] for r in sorted_risks]

    bars = ax2.barh(range(len(names)), scores, color=colors_list, alpha=0.85,
                    edgecolor='#3a3830', linewidth=0.5)

    ax2.set_yticks(range(len(names)))
    ax2.set_yticklabels(names, color='#c8c0b0', fontsize=8)
    ax2.set_xlabel('Risk Score (Likelihood × Impact)', color='#b8892a', fontsize=10, fontweight='bold')
    ax2.set_title('Risk Register — Priority Order', color='#f5f0e8', fontsize=14, fontweight='bold', pad=12)
    ax2.tick_params(colors='#8a8579')
    ax2.set_facecolor('#1e1c18')

    for bar, score in zip(bars, scores):
        ax2.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{score}', va='center', color='white', fontsize=8, fontweight='bold')

    ax2.axvline(x=16, color='#d32f2f', linestyle='--', alpha=0.5, linewidth=1, label='Critical')
    ax2.axvline(x=12, color='#e64a19', linestyle='--', alpha=0.5, linewidth=1, label='High')
    ax2.axvline(x=6, color='#f57c00', linestyle='--', alpha=0.5, linewidth=1, label='Medium')

    for spine in ax2.spines.values():
        spine.set_edgecolor('#3a3830')
    ax2.grid(True, alpha=0.08, color='white', axis='x', linestyle='--')
    ax2.invert_yaxis()

    # Main title
    fig.suptitle(
        f'ISO 27001:2022 Risk Assessment Dashboard\nGenerated: {datetime.now().strftime("%d %B %Y")}',
        color='#f5f0e8', fontsize=15, fontweight='bold', y=0.98
    )

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_file, dpi=150, bbox_inches='tight',
               facecolor='#1a1814', edgecolor='none')
    plt.close()
    print(f"✅ Heatmap saved: {output_file}")
    print(f"   Risks plotted: {len(risks)}")
    print(f"   Critical: {sum(1 for r in risks if r['likelihood']*r['impact'] >= 16)}")
    print(f"   High: {sum(1 for r in risks if 12 <= r['likelihood']*r['impact'] < 16)}")
    print(f"   Medium: {sum(1 for r in risks if 6 <= r['likelihood']*r['impact'] < 12)}")
    print(f"   Low: {sum(1 for r in risks if r['likelihood']*r['impact'] < 6)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ISO 27001 Risk Heatmap Generator')
    parser.add_argument('--output', default='iso27001_risk_heatmap.png', help='Output filename')
    args = parser.parse_args()
    create_heatmap(DEFAULT_RISKS, args.output)
