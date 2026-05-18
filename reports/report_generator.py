"""
Report Generator Module
========================
Generates structured scan reports in TXT, JSON, and CSV formats.

Dev 3 Ownership.
"""

import json
import csv
import os
from datetime import datetime


def generate_txt_report(results, metadata, filepath):
    """
    Generate a human-readable TXT report with grouped violations and summary.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  CodeLens Scan Report\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"  Directory : {metadata.get('directory', 'N/A')}\n")
        f.write(f"  Extensions: {metadata.get('extensions', 'N/A')}\n")
        f.write(f"  Duration  : {metadata.get('scan_time', 0):.3f}s\n")
        f.write("=" * 60 + "\n\n")

        total_violations = 0
        severity_counts = {"critical": 0, "warning": 0, "style": 0}

        for filename, issues in results.items():
            if not issues:
                continue
            f.write(f"File: {filename}\n")
            f.write("-" * 60 + "\n")
            for issue in issues:
                severity = issue['severity'].upper()
                f.write(f"  [{severity}] \"{issue['pattern']}\" found at line {issue['line']}\n")
                if issue.get('context'):
                    f.write(f"           {issue['context'].strip()}\n")
                total_violations += 1
                severity_counts[issue['severity']] = severity_counts.get(issue['severity'], 0) + 1
            f.write("\n")

        # Summary
        f.write("=" * 60 + "\n")
        f.write("  SUMMARY\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Files scanned     : {metadata.get('files_scanned', 0)}\n")
        f.write(f"  Total violations  : {total_violations}\n")
        f.write(f"  Critical issues   : {severity_counts.get('critical', 0)}\n")
        f.write(f"  Warnings          : {severity_counts.get('warning', 0)}\n")
        f.write(f"  Style issues      : {severity_counts.get('style', 0)}\n")
        f.write(f"  Scan time         : {metadata.get('scan_time', 0):.3f}s\n")

        if metadata.get('horspool_time') and metadata.get('naive_time'):
            f.write(f"\n  Algorithm Benchmarks:\n")
            f.write(f"    Horspool : {metadata['horspool_time']:.5f}s\n")
            f.write(f"    Naive    : {metadata['naive_time']:.5f}s\n")

        f.write("=" * 60 + "\n")


def generate_json_report(results, metadata, filepath):
    """
    Generate a structured JSON report.
    """
    total_violations = 0
    severity_counts = {"critical": 0, "warning": 0, "style": 0}

    for issues in results.values():
        for issue in issues:
            total_violations += 1
            severity_counts[issue['severity']] = severity_counts.get(issue['severity'], 0) + 1

    report = {
        "report": {
            "generated_at": datetime.now().isoformat(),
            "tool": "CodeLens",
            "version": "1.0.0",
        },
        "metadata": metadata,
        "summary": {
            "total_violations": total_violations,
            "severity_counts": severity_counts,
        },
        "results": results,
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)


def generate_csv_report(results, metadata, filepath):
    """
    Generate a CSV report with one row per violation.
    """
    with open(filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Line", "Severity", "Pattern", "Context"])
        for filename, issues in results.items():
            for issue in issues:
                writer.writerow([
                    filename,
                    issue['line'],
                    issue['severity'].upper(),
                    issue['pattern'],
                    issue.get('context', '').strip(),
                ])
