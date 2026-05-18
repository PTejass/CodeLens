"""
CodeLens: Intelligent Code Review Assistant
============================================
A lightweight CLI-based static code analysis and review tool.

This is the main entry point. It provides the CLI interface using argparse
and delegates to the appropriate modules for scanning, reporting, and analysis.

Dev 3 Ownership: main.py, config loading, CLI skeleton, colorized output.
"""

import argparse
import sys
import os
import json
import time
from datetime import datetime

import colorama
from colorama import Fore, Back, Style

# ─── Initialize colorama for cross-platform ANSI color support ───
colorama.init(autoreset=True)

# ─── Constants ────────────────────────────────────────────────────
VERSION = "1.0.0"
SUPPORTED_EXTENSIONS = [".py", ".java", ".c", ".cpp", ".js"]
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "banned_patterns.json")
REPORT_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports", "output")
LAST_SCAN_CACHE = os.path.join(REPORT_OUTPUT_DIR, ".last_scan.json")

# ─── Severity color mapping ──────────────────────────────────────
SEVERITY_COLORS = {
    "critical": Fore.RED + Style.BRIGHT,
    "warning":  Fore.YELLOW,
    "style":    Fore.BLUE,
}

SEVERITY_LABELS = {
    "critical": "CRITICAL",
    "warning":  "WARNING",
    "style":    "STYLE",
}


# ═══════════════════════════════════════════════════════════════════
#  Banner & UI helpers
# ═══════════════════════════════════════════════════════════════════

def print_banner():
    """Print the CodeLens ASCII banner (Windows-safe ASCII art)."""
    inner_width = 58
    border = "+" + "-" * inner_width + "+"
    
    print(f"\n{Fore.CYAN + Style.BRIGHT}{border}")
    print(f"{Fore.CYAN + Style.BRIGHT}|" + " ".center(inner_width) + "|")
    
    banner_art = [
        "   ____          _      _                    ",
        "  / ___|___   __| | ___| |    ___ _ __  ___  ",
        " | |   / _ \\ / _` |/ _ \\ |   / _ \\ '_ \\/ __| ",
        " | |__| (_) | (_| |  __/ |__|  __/ | | \\__ \\ ",
        "  \\____\\___/ \\__,_|\\___|_____\\___|_| |_|___/ "
    ]
    
    for art in banner_art:
        padded_art = art.ljust(inner_width)
        print(f"{Fore.CYAN + Style.BRIGHT}|{padded_art}|")
        
    print(f"{Fore.CYAN + Style.BRIGHT}|" + " ".center(inner_width) + "|")
    
    subtitle = f"Intelligent Code Review Assistant  v{VERSION}"
    centered_subtitle = subtitle.center(inner_width)
    colored_subtitle = centered_subtitle.replace(subtitle, f"{Fore.WHITE}{subtitle}{Fore.CYAN + Style.BRIGHT}")
    
    print(f"{Fore.CYAN + Style.BRIGHT}|{colored_subtitle}|")
    print(f"{Fore.CYAN + Style.BRIGHT}{border}{Style.RESET_ALL}\n")


def print_section_header(title):
    """Print a styled section header."""
    width = 60
    print(f"\n{Fore.CYAN + Style.BRIGHT}>> {title.upper()}")
    print(f"{Fore.CYAN}{'-' * width}{Style.RESET_ALL}")


def print_success(message):
    """Print a green success message."""
    print(f"{Fore.GREEN + Style.BRIGHT}[SUCCESS]{Style.RESET_ALL} {message}")


def print_error(message):
    """Print a red error message."""
    print(f"{Fore.RED + Style.BRIGHT}[ERROR]{Style.RESET_ALL}   {message}")


def print_info(message):
    """Print a cyan info message."""
    print(f"{Fore.CYAN + Style.BRIGHT}[INFO]{Style.RESET_ALL}    {message}")


def print_warning(message):
    """Print a yellow warning message."""
    print(f"{Fore.YELLOW + Style.BRIGHT}[WARN]{Style.RESET_ALL}    {message}")


def format_violation(severity, pattern, line_number, context=""):
    """
    Format a single violation line with ANSI colors.
    
    Colors:
      Red    = Critical
      Yellow = Warning
      Blue   = Style
    """
    color = SEVERITY_COLORS.get(severity, Fore.WHITE)
    label = SEVERITY_LABELS.get(severity, severity.upper())
    output = f"  {color}[{label}]{Style.RESET_ALL} {Fore.WHITE}\"{pattern}\"{Style.RESET_ALL} found at line {Fore.CYAN}{line_number}{Style.RESET_ALL}"
    if context:
        output += f"\n         {Fore.LIGHTBLACK_EX}{context.strip()}{Style.RESET_ALL}"
    return output


# ═══════════════════════════════════════════════════════════════════
#  Configuration loader
# ═══════════════════════════════════════════════════════════════════

def load_config(config_path=None):
    """
    Load and validate the banned patterns configuration file.
    
    Expected schema:
    {
      "critical": ["pattern1", ...],
      "warning":  ["pattern1", ...],
      "style":    ["pattern1", ...]
    }
    
    Returns:
        dict: The loaded configuration with severity -> pattern list mappings.
    
    Raises:
        SystemExit: If the config file is missing, malformed, or has invalid schema.
    """
    path = config_path or CONFIG_PATH

    if not os.path.exists(path):
        print_error(f"Config file not found: {path}")
        print_info("Create a config/banned_patterns.json with 'critical', 'warning', and 'style' keys.")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in config file: {e}")
        sys.exit(1)

    # Validate schema
    required_keys = {"critical", "warning", "style"}
    missing = required_keys - set(config.keys())
    if missing:
        print_error(f"Config is missing required keys: {', '.join(missing)}")
        sys.exit(1)

    for key in required_keys:
        if not isinstance(config[key], list):
            print_error(f"Config key '{key}' must be a list of pattern strings.")
            sys.exit(1)
        for i, pattern in enumerate(config[key]):
            if not isinstance(pattern, str) or len(pattern) == 0:
                print_error(f"Config['{key}'][{i}] must be a non-empty string.")
                sys.exit(1)

    return config


def get_all_patterns(config):
    """
    Flatten config into a list of (pattern, severity) tuples.
    Useful for passing to matchers later.
    """
    patterns = []
    for severity in ("critical", "warning", "style"):
        for pattern in config.get(severity, []):
            patterns.append((pattern, severity))
    return patterns


def parse_extensions(ext_string):
    """
    Parse a comma-separated extension string into a list.
    Ensures each extension starts with a dot.
    
    Args:
        ext_string: Comma-separated extensions (e.g. ".py,.java")
    
    Returns:
        list: List of normalized extensions like [".py", ".java"]
    """
    extensions = []
    for ext in ext_string.split(","):
        ext = ext.strip()
        if not ext.startswith("."):
            ext = "." + ext
        extensions.append(ext.lower())
    return extensions


def save_scan_results(results, metadata):
    """
    Cache the last scan results to disk so `report` and `stats` commands
    can read them without re-scanning.
    """
    os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
    data = {
        "metadata": metadata,
        "results": results,
    }
    with open(LAST_SCAN_CACHE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_last_scan():
    """
    Load cached results from the last scan.
    
    Returns:
        tuple: (results_dict, metadata_dict) or (None, None) if no cache exists.
    """
    if not os.path.exists(LAST_SCAN_CACHE):
        return None, None
    try:
        with open(LAST_SCAN_CACHE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("results", {}), data.get("metadata", {})
    except (json.JSONDecodeError, KeyError):
        return None, None


# ═══════════════════════════════════════════════════════════════════
#  CLI command handlers  (Phase 3: fully wired)
# ═══════════════════════════════════════════════════════════════════

def cmd_scan(args):
    """
    Handle the `scan <directory>` command.
    Scans all matching source files using both Horspool and Naive matchers,
    prints colorized violations, and caches results for report/stats.
    """
    from scanner import horspool, naive
    from filesystem.sequential_access import read_file_sequential

    directory = os.path.abspath(args.directory)
    extensions = parse_extensions(args.ext)

    print_section_header("Scan Configuration")
    print_info(f"Target directory : {directory}")
    print_info(f"Extensions       : {', '.join(extensions)}")

    # Validate directory
    if not os.path.isdir(directory):
        print_error(f"Directory does not exist: {directory}")
        sys.exit(1)

    # Load config
    config = load_config()
    all_patterns = get_all_patterns(config)
    print_success(f"Loaded {len(all_patterns)} patterns from config")
    for severity in ("critical", "warning", "style"):
        color = SEVERITY_COLORS[severity]
        count = len(config[severity])
        print(f"    {color}{SEVERITY_LABELS[severity]}: {count} patterns{Style.RESET_ALL}")

    # Collect source files
    source_files = []
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if any(fname.lower().endswith(ext) for ext in extensions):
                source_files.append(os.path.join(root, fname))

    print_success(f"Found {len(source_files)} source file(s)")

    if not source_files:
        print_warning("No files to scan.")
        return

    # ── Scan using both algorithms ────────────────────────────────
    print_section_header("Scanning with Horspool Algorithm")

    results = {}       # {filepath: [issues]}
    total_violations = 0
    horspool_total_time = 0.0
    naive_total_time = 0.0

    for fpath in source_files:
        file_issues = []
        rel_path = os.path.relpath(fpath, directory)

        # Read file using sequential access (Dev 2)
        try:
            lines = list(read_file_sequential(fpath))
        except Exception as e:
            print_error(f"Could not read {rel_path}: {e}")
            continue

        for line_number, line_content in lines:
            for pattern, severity in all_patterns:
                # Horspool search (Dev 1)
                h_start = time.time()
                h_matches = horspool.search(line_content, pattern)
                horspool_total_time += time.time() - h_start

                # Naive search for benchmarking (Dev 1)
                n_start = time.time()
                naive.search(line_content, pattern)
                naive_total_time += time.time() - n_start

                if h_matches:
                    issue = {
                        "severity": severity,
                        "pattern": pattern,
                        "line": line_number,
                        "context": line_content.rstrip("\n\r"),
                    }
                    file_issues.append(issue)
                    total_violations += 1

        if file_issues:
            results[rel_path] = file_issues
            # Print violations for this file
            print(f"\n  {Fore.WHITE + Style.BRIGHT}File: {rel_path}{Style.RESET_ALL}")
            for issue in file_issues:
                print(format_violation(
                    issue['severity'],
                    issue['pattern'],
                    issue['line'],
                    issue['context'],
                ))

    # ── Summary ───────────────────────────────────────────────────
    print_section_header("Scan Summary")

    severity_counts = {"critical": 0, "warning": 0, "style": 0}
    for issues in results.values():
        for issue in issues:
            severity_counts[issue['severity']] += 1

    print_info(f"Files scanned   : {len(source_files)}")
    print_info(f"Files with issues: {len(results)}")
    print(f"    {Fore.RED + Style.BRIGHT}Critical : {severity_counts['critical']}{Style.RESET_ALL}")
    print(f"    {Fore.YELLOW}Warnings : {severity_counts['warning']}{Style.RESET_ALL}")
    print(f"    {Fore.BLUE}Style    : {severity_counts['style']}{Style.RESET_ALL}")
    print_info(f"Total violations: {total_violations}")

    print_section_header("Algorithm Benchmark")
    print_info(f"Horspool total : {horspool_total_time:.5f}s")
    print_info(f"Naive total    : {naive_total_time:.5f}s")
    if naive_total_time > 0:
        speedup = naive_total_time / max(horspool_total_time, 0.00001)
        print_success(f"Horspool speedup: {speedup:.2f}x")

    # Cache results
    metadata = {
        "directory": directory,
        "extensions": ', '.join(extensions),
        "files_scanned": len(source_files),
        "total_violations": total_violations,
        "severity_counts": severity_counts,
        "scan_time": horspool_total_time,
        "horspool_time": horspool_total_time,
        "naive_time": naive_total_time,
    }
    save_scan_results(results, metadata)
    print_success(f"Results cached for report/stats commands")


def cmd_report(args):
    """
    Handle the `report` command.
    Generates a TXT, JSON, or CSV report from cached scan data.
    """
    from reports.report_generator import (
        generate_txt_report,
        generate_json_report,
        generate_csv_report,
    )

    print_section_header("Report Generation")
    print_info(f"Format: {args.format.upper()}")

    results, metadata = load_last_scan()
    if results is None:
        print_warning("No scan results found. Run `scan <directory>` first.")
        return

    os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"codelens_report_{timestamp}.{args.format}"
    filepath = os.path.join(REPORT_OUTPUT_DIR, filename)

    if args.format == "txt":
        generate_txt_report(results, metadata, filepath)
    elif args.format == "json":
        generate_json_report(results, metadata, filepath)
    elif args.format == "csv":
        generate_csv_report(results, metadata, filepath)

    print_success(f"Report saved to: {filepath}")
    print_info(f"Violations captured: {metadata.get('total_violations', 0)}")


def cmd_stats(args):
    """
    Handle the `stats` command.
    Displays a full analytics dashboard from cached scan data.
    """
    print_section_header("Analytics Dashboard")

    results, metadata = load_last_scan()
    if results is None:
        print_warning("No scan results found. Run `scan <directory>` first.")
        return

    sev = metadata.get("severity_counts", {})
    total = metadata.get("total_violations", 0)

    # Find worst offending file
    worst_file = ""
    worst_count = 0
    for fname, issues in results.items():
        if len(issues) > worst_count:
            worst_count = len(issues)
            worst_file = fname

    # Find most common pattern
    pattern_freq = {}
    for issues in results.values():
        for issue in issues:
            p = issue['pattern']
            pattern_freq[p] = pattern_freq.get(p, 0) + 1
    most_common = max(pattern_freq, key=pattern_freq.get) if pattern_freq else "N/A"
    most_common_count = pattern_freq.get(most_common, 0)

    # Dashboard output
    width = 60
    print(f"\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}")
    print(f"{Fore.WHITE + Style.BRIGHT}  CODELENS ANALYTICS{Style.RESET_ALL}")
    print(f"{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\n")

    rows = [
        ("Files scanned",       str(metadata.get("files_scanned", 0))),
        ("Files with issues",   str(len(results))),
        ("Total violations",    str(total)),
        ("Critical issues",     f"{Fore.RED + Style.BRIGHT}{sev.get('critical', 0)}{Style.RESET_ALL}"),
        ("Warnings",            f"{Fore.YELLOW}{sev.get('warning', 0)}{Style.RESET_ALL}"),
        ("Style issues",        f"{Fore.BLUE}{sev.get('style', 0)}{Style.RESET_ALL}"),
        ("", ""),
        ("Most common pattern", f"\"{most_common}\" ({most_common_count} hits)"),
        ("Worst offending file", f"{worst_file} ({worst_count} issues)"),
        ("", ""),
        ("Horspool time",       f"{metadata.get('horspool_time', 0):.5f}s"),
        ("Naive time",          f"{metadata.get('naive_time', 0):.5f}s"),
        ("Scan duration",       f"{metadata.get('scan_time', 0):.5f}s"),
    ]

    for label, value in rows:
        if label == "":
            print(f"{Fore.CYAN}  {'-' * (width - 4)}{Style.RESET_ALL}")
        else:
            print(f"  {Fore.WHITE}{label:<24}{Style.RESET_ALL}{value}")

    print(f"\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}")

    # Top patterns table
    if pattern_freq:
        print_section_header("Top Patterns")
        sorted_patterns = sorted(pattern_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"  {'Pattern':<30} {'Count':>6}")
        print(f"  {'-' * 30} {'-' * 6}")
        for pattern, count in sorted_patterns:
            print(f"  {pattern:<30} {count:>6}")


def cmd_jump(args):
    """
    Handle the `jump <file> <line>` command.
    Demonstrates both sequential and direct (random) file access,
    comparing their performance side by side.
    """
    from filesystem.direct_access import index_file_lines, read_line_direct
    from filesystem.sequential_access import read_file_sequential

    filepath = os.path.abspath(args.file)
    target_line = args.line

    print_section_header("Direct Access Jump")
    print_info(f"File : {filepath}")
    print_info(f"Line : {target_line}")

    if not os.path.isfile(filepath):
        print_error(f"File not found: {filepath}")
        return

    if target_line < 1:
        print_error("Line number must be >= 1.")
        return

    # ── Method 1: Sequential access ──────────────────────────────
    print_section_header("Sequential Access (line-by-line)")
    seq_start = time.time()
    seq_result = None
    for line_num, line_content in read_file_sequential(filepath):
        if line_num == target_line:
            seq_result = line_content
            break
    seq_time = time.time() - seq_start

    if seq_result is not None:
        print_success(f"Found line {target_line} in {seq_time:.6f}s")
        print(f"    {Fore.WHITE}{seq_result.rstrip()}{Style.RESET_ALL}")
    else:
        print_warning(f"Line {target_line} not found (file has fewer lines).")

    # ── Method 2: Direct access (byte offset jump) ───────────────
    print_section_header("Direct Access (byte offset jump)")
    idx_start = time.time()
    offsets = index_file_lines(filepath)
    idx_time = time.time() - idx_start

    jump_start = time.time()
    direct_result = read_line_direct(filepath, target_line, offsets)
    jump_time = time.time() - jump_start

    if direct_result is not None:
        print_success(f"Indexed {len(offsets)} lines in {idx_time:.6f}s")
        print_success(f"Jumped to line {target_line} in {jump_time:.6f}s")
        print(f"    {Fore.WHITE}{direct_result.rstrip()}{Style.RESET_ALL}")
    else:
        print_warning(f"Line {target_line} not found (file has {len(offsets)} lines).")

    # ── Performance comparison ────────────────────────────────────
    print_section_header("Access Method Comparison")
    print_info(f"Sequential : {seq_time:.6f}s")
    print_info(f"Direct     : {idx_time + jump_time:.6f}s (index: {idx_time:.6f}s + jump: {jump_time:.6f}s)")

    if seq_result and direct_result:
        if seq_result.rstrip() == direct_result.rstrip():
            print_success("Both methods returned the same result.")
        else:
            print_warning("Results differ between methods!")


def cmd_compare(args):
    """
    Handle the `compare <file1> <file2>` command.
    Uses similarity module to compute plagiarism/copy-paste score.
    """
    from scanner.similarity import calculate_similarity, longest_common_substring

    file1 = os.path.abspath(args.file1)
    file2 = os.path.abspath(args.file2)

    print_section_header("Similarity Comparison")
    print_info(f"File 1 : {file1}")
    print_info(f"File 2 : {file2}")

    for fpath in [file1, file2]:
        if not os.path.isfile(fpath):
            print_error(f"File not found: {fpath}")
            return

    # Read file contents
    with open(file1, "r", encoding="utf-8", errors="ignore") as f:
        text1 = f.read()
    with open(file2, "r", encoding="utf-8", errors="ignore") as f:
        text2 = f.read()

    print_info(f"File 1 size: {len(text1)} chars, {len(text1.splitlines())} lines")
    print_info(f"File 2 size: {len(text2)} chars, {len(text2.splitlines())} lines")

    # ── Similarity calculations ───────────────────────────────────
    print_section_header("Analysis Results")

    # Sequence match ratio (difflib)
    sim_start = time.time()
    similarity = calculate_similarity(text1, text2)
    sim_time = time.time() - sim_start

    # Longest Common Substring
    lcs_start = time.time()
    lcs_len = longest_common_substring(text1, text2)
    lcs_time = time.time() - lcs_start

    # Determine similarity level
    if similarity >= 80:
        level_color = Fore.RED + Style.BRIGHT
        level_label = "HIGH SIMILARITY - Possible plagiarism"
    elif similarity >= 50:
        level_color = Fore.YELLOW
        level_label = "MODERATE SIMILARITY"
    else:
        level_color = Fore.GREEN
        level_label = "LOW SIMILARITY"

    # Display results
    width = 60
    print(f"\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}")

    rel1 = os.path.basename(file1)
    rel2 = os.path.basename(file2)
    print(f"  {Fore.WHITE}{rel1} <-> {rel2}{Style.RESET_ALL}")
    print(f"\n  {level_color}Similarity Score : {similarity:.1f}%{Style.RESET_ALL}")
    print(f"  {level_color}{level_label}{Style.RESET_ALL}")
    print(f"\n  {Fore.WHITE}LCS Length       : {lcs_len} characters{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}Similarity Time  : {sim_time:.5f}s{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}LCS Time         : {lcs_time:.5f}s{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}")


# ═══════════════════════════════════════════════════════════════════
#  Argument parser setup
# ═══════════════════════════════════════════════════════════════════

def build_parser():
    """
    Build and return the argparse parser with all subcommands.
    """
    parser = argparse.ArgumentParser(
        prog="codelens",
        description=(
            f"{Fore.CYAN + Style.BRIGHT}CodeLens{Style.RESET_ALL} — "
            "Intelligent Code Review Assistant. "
            "Scans source code for banned patterns, style violations, "
            "and plagiarism using efficient string matching algorithms."
        ),
        epilog=(
            f"Examples:\n"
            f"  python main.py scan ./src --ext .py,.js\n"
            f"  python main.py report --format json\n"
            f"  python main.py stats\n"
            f"  python main.py jump auth.py 42\n"
            f"  python main.py compare file1.py file2.py"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version", action="version",
        version=f"CodeLens v{VERSION}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available CodeLens commands",
    )

    # ── scan ──────────────────────────────────────────────────────
    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a directory for banned patterns and violations",
        description="Recursively scan source files for banned patterns defined in config.",
    )
    scan_parser.add_argument(
        "directory",
        help="Target directory to scan",
    )
    scan_parser.add_argument(
        "--ext",
        help="Comma-separated file extensions to include (default: .py,.java,.c,.cpp,.js)",
        default=".py,.java,.c,.cpp,.js",
    )
    scan_parser.set_defaults(func=cmd_scan)

    # ── report ────────────────────────────────────────────────────
    report_parser = subparsers.add_parser(
        "report",
        help="Generate a report from the last scan",
        description="Generate a structured report in TXT, JSON, or CSV format.",
    )
    report_parser.add_argument(
        "--format",
        choices=["txt", "json", "csv"],
        default="txt",
        help="Output format (default: txt)",
    )
    report_parser.set_defaults(func=cmd_report)

    # ── stats ─────────────────────────────────────────────────────
    stats_parser = subparsers.add_parser(
        "stats",
        help="Show the analytics dashboard",
        description="Display scan statistics, violation counts, and timing benchmarks.",
    )
    stats_parser.set_defaults(func=cmd_stats)

    # ── jump ──────────────────────────────────────────────────────
    jump_parser = subparsers.add_parser(
        "jump",
        help="Jump directly to a line in a file (direct access demo)",
        description="Uses direct (random) file access to jump to a specific line.",
    )
    jump_parser.add_argument("file", help="Path to the file")
    jump_parser.add_argument("line", type=int, help="Line number to jump to (1-indexed)")
    jump_parser.set_defaults(func=cmd_jump)

    # ── compare ───────────────────────────────────────────────────
    compare_parser = subparsers.add_parser(
        "compare",
        help="Compare two files for similarity / plagiarism",
        description="Compute similarity score between two source files.",
    )
    compare_parser.add_argument("file1", help="Path to the first file")
    compare_parser.add_argument("file2", help="Path to the second file")
    compare_parser.set_defaults(func=cmd_compare)

    return parser


# ═══════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════

def main():
    """Main entry point for the CodeLens CLI."""
    print_banner()

    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        print()
        print_info("Run 'python main.py <command> --help' for details on a specific command.")
        sys.exit(0)

    # Dispatch to the appropriate handler
    start_time = time.time()
    args.func(args)
    elapsed = time.time() - start_time

    print(f"\n{Fore.LIGHTBLACK_EX}  Completed in {elapsed:.3f}s{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
