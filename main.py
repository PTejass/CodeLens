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
#  CLI command handlers  (Phase 1: skeleton stubs)
# ═══════════════════════════════════════════════════════════════════

def cmd_scan(args):
    """
    Handle the `scan <directory>` command.
    Phase 1: Validates inputs, loads config, prints confirmation.
    Phase 2/3: Will invoke directory walker + pattern matchers.
    """
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

    print_section_header("Scanning")
    print_info("Scan engine not yet wired (waiting for Dev 1 & Dev 2 modules).")
    print_info("Phase 2 will integrate directory walker + pattern matchers here.")

    # Placeholder: collect matching source files
    source_files = []
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if any(fname.lower().endswith(ext) for ext in extensions):
                source_files.append(os.path.join(root, fname))

    print_success(f"Found {len(source_files)} source file(s) matching {', '.join(extensions)}")
    for fpath in source_files[:10]:
        print(f"    {Fore.LIGHTBLACK_EX}{fpath}{Style.RESET_ALL}")
    if len(source_files) > 10:
        print(f"    {Fore.LIGHTBLACK_EX}... and {len(source_files) - 10} more{Style.RESET_ALL}")


def cmd_report(args):
    """
    Handle the `report` command.
    Phase 1: Skeleton that checks for cached scan data.
    Phase 2: Will generate TXT/JSON/CSV reports.
    """
    print_section_header("Report Generation")
    print_info(f"Format requested: {args.format}")

    results, metadata = load_last_scan()
    if results is None:
        print_warning("No scan results found. Run `scan <directory>` first.")
        return

    print_info("Report generator not yet wired (Phase 2 task).")
    print_info(f"Cached scan data available with {len(results)} file(s).")


def cmd_stats(args):
    """
    Handle the `stats` command.
    Phase 1: Skeleton that checks for cached data.
    Phase 3: Will display full analytics dashboard.
    """
    print_section_header("Analytics Dashboard")

    results, metadata = load_last_scan()
    if results is None:
        print_warning("No scan results found. Run `scan <directory>` first.")
        return

    print_info("Analytics dashboard not yet wired (Phase 3 task).")
    print_info(f"Cached scan data available with {len(results)} file(s).")


def cmd_jump(args):
    """
    Handle the `jump <file> <line>` command.
    Phase 1: Validates inputs.
    Phase 3: Will use direct_access module from Dev 2.
    """
    filepath = os.path.abspath(args.file)

    print_section_header("Direct Access Jump")
    print_info(f"File : {filepath}")
    print_info(f"Line : {args.line}")

    if not os.path.isfile(filepath):
        print_error(f"File not found: {filepath}")
        return

    if args.line < 1:
        print_error("Line number must be >= 1.")
        return

    print_info("Direct access module not yet wired (waiting for Dev 2).")


def cmd_compare(args):
    """
    Handle the `compare <file1> <file2>` command.
    Phase 1: Validates inputs.
    Phase 3: Will use similarity module from Dev 1/2.
    """
    file1 = os.path.abspath(args.file1)
    file2 = os.path.abspath(args.file2)

    print_section_header("Similarity Comparison")
    print_info(f"File 1 : {file1}")
    print_info(f"File 2 : {file2}")

    for fpath in [file1, file2]:
        if not os.path.isfile(fpath):
            print_error(f"File not found: {fpath}")
            return

    print_info("Similarity engine not yet wired (waiting for Dev 1 & Dev 2 modules).")


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
