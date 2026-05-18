import json
import os
import sys

# Ensure scanner module can be imported
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from scanner.horspool import build_shift_table
from scanner.similarity import calculate_similarity, longest_common_substring

def main():
    print("Building static dashboard data...")
    
    # 1. Load banned patterns
    config_path = "config/banned_patterns.json"
    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found.")
        return
        
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    # 2. Build shift tables for all patterns
    shift_tables = {}
    for severity, patterns in config.items():
        for pattern in patterns:
            shift_tables[pattern] = {
                "severity": severity,
                "table": build_shift_table(pattern),
                "length": len(pattern)
            }
            
    # 3. Load latest scan report
    scan_report = {}
    scan_cache_path = "reports/output/.last_scan.json"
    if os.path.exists(scan_cache_path):
        with open(scan_cache_path, "r", encoding="utf-8") as f:
            scan_report = json.load(f)
    else:
        print("Warning: No .last_scan.json found. Dashboard will have empty scan results.")
        print("Please run `python main.py scan sample_codebase` to populate data.")
        
    # 4. Compute Pairwise Similarities for "Compare" feature
    file_comparisons = {}
    if "results" in scan_report and "metadata" in scan_report:
        base_dir = scan_report["metadata"].get("directory", "")
        file_contents = {}
        
        # Read contents
        for rel_path in scan_report["results"].keys():
            abs_path = os.path.join(base_dir, rel_path) if not os.path.isabs(rel_path) else rel_path
            try:
                with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                    file_contents[rel_path] = f.read()
            except Exception as e:
                print(f"Warning: Could not read {abs_path} for comparison: {e}")
                
        # Compare all unique pairs
        filenames = list(file_contents.keys())
        for i in range(len(filenames)):
            for j in range(i + 1, len(filenames)):
                f1 = filenames[i]
                f2 = filenames[j]
                text1 = file_contents[f1]
                text2 = file_contents[f2]
                
                sim = calculate_similarity(text1, text2)
                lcs = longest_common_substring(text1, text2)
                
                key = f"{f1}|{f2}"
                file_comparisons[key] = {
                    "similarity": round(sim, 2),
                    "lcs": lcs,
                    "file1": f1,
                    "file2": f2,
                    "lines1": len(text1.splitlines()),
                    "lines2": len(text2.splitlines())
                }
            
    # 5. Generate data.js
    os.makedirs("static_dashboard", exist_ok=True)
    out_path = "static_dashboard/data.js"
    
    js_content = f"""// AUTO-GENERATED DATA FOR STATIC DASHBOARD

const shiftTables = {json.dumps(shift_tables, indent=2)};

const scanReport = {json.dumps(scan_report, indent=2)};

const fileComparisons = {json.dumps(file_comparisons, indent=2)};
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully generated {out_path}")

if __name__ == "__main__":
    main()
