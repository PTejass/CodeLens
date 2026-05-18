import json
import csv

def generate_txt_report(results, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        for filename, issues in results.items():
            f.write(f"File: {filename}\n")
            for issue in issues:
                severity = issue['severity'].upper()
                f.write(f"[{severity}] {issue['pattern']} found at line {issue['line']}\n")
            f.write("\n")

def generate_json_report(results, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

def generate_csv_report(results, filepath):
    with open(filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Severity", "Pattern", "Line"])
        for filename, issues in results.items():
            for issue in issues:
                writer.writerow([filename, issue['severity'].upper(), issue['pattern'], issue['line']])
