// AUTO-GENERATED DATA FOR STATIC DASHBOARD

const shiftTables = {
  "password=": {
    "severity": "critical",
    "table": {
      "p": 8,
      "a": 7,
      "s": 5,
      "w": 4,
      "o": 3,
      "r": 2,
      "d": 1
    },
    "length": 9
  },
  "passwd=": {
    "severity": "critical",
    "table": {
      "p": 6,
      "a": 5,
      "s": 3,
      "w": 2,
      "d": 1
    },
    "length": 7
  },
  "secret_key=": {
    "severity": "critical",
    "table": {
      "s": 10,
      "e": 2,
      "c": 8,
      "r": 7,
      "t": 5,
      "_": 4,
      "k": 3,
      "y": 1
    },
    "length": 11
  },
  "api_key=": {
    "severity": "critical",
    "table": {
      "a": 7,
      "p": 6,
      "i": 5,
      "_": 4,
      "k": 3,
      "e": 2,
      "y": 1
    },
    "length": 8
  },
  "eval(": {
    "severity": "critical",
    "table": {
      "e": 4,
      "v": 3,
      "a": 2,
      "l": 1
    },
    "length": 5
  },
  "exec(": {
    "severity": "critical",
    "table": {
      "e": 2,
      "x": 3,
      "c": 1
    },
    "length": 5
  },
  "os.system(": {
    "severity": "critical",
    "table": {
      "o": 9,
      "s": 4,
      ".": 7,
      "y": 5,
      "t": 3,
      "e": 2,
      "m": 1
    },
    "length": 10
  },
  "subprocess.call(": {
    "severity": "critical",
    "table": {
      "s": 6,
      "u": 14,
      "b": 13,
      "p": 12,
      "r": 11,
      "o": 10,
      "c": 4,
      "e": 8,
      ".": 5,
      "a": 3,
      "l": 1
    },
    "length": 16
  },
  "__import__(": {
    "severity": "critical",
    "table": {
      "_": 1,
      "i": 8,
      "m": 7,
      "p": 6,
      "o": 5,
      "r": 4,
      "t": 3
    },
    "length": 11
  },
  "pickle.loads(": {
    "severity": "critical",
    "table": {
      "p": 12,
      "i": 11,
      "c": 10,
      "k": 9,
      "l": 5,
      "e": 7,
      ".": 6,
      "o": 4,
      "a": 3,
      "d": 2,
      "s": 1
    },
    "length": 13
  },
  "TODO": {
    "severity": "warning",
    "table": {
      "T": 3,
      "O": 2,
      "D": 1
    },
    "length": 4
  },
  "FIXME": {
    "severity": "warning",
    "table": {
      "F": 4,
      "I": 3,
      "X": 2,
      "M": 1
    },
    "length": 5
  },
  "HACK": {
    "severity": "warning",
    "table": {
      "H": 3,
      "A": 2,
      "C": 1
    },
    "length": 4
  },
  "XXX": {
    "severity": "warning",
    "table": {
      "X": 1
    },
    "length": 3
  },
  "BUG": {
    "severity": "warning",
    "table": {
      "B": 2,
      "U": 1
    },
    "length": 3
  },
  "DEPRECATED": {
    "severity": "warning",
    "table": {
      "D": 9,
      "E": 1,
      "P": 7,
      "R": 6,
      "C": 4,
      "A": 3,
      "T": 2
    },
    "length": 10
  },
  "goto": {
    "severity": "style",
    "table": {
      "g": 3,
      "o": 2,
      "t": 1
    },
    "length": 4
  },
  "global ": {
    "severity": "style",
    "table": {
      "g": 6,
      "l": 1,
      "o": 4,
      "b": 3,
      "a": 2
    },
    "length": 7
  },
  "from * import": {
    "severity": "style",
    "table": {
      "f": 12,
      "r": 1,
      "o": 2,
      "m": 4,
      " ": 6,
      "*": 7,
      "i": 5,
      "p": 3
    },
    "length": 13
  },
  "import *": {
    "severity": "style",
    "table": {
      "i": 7,
      "m": 6,
      "p": 5,
      "o": 4,
      "r": 3,
      "t": 2,
      " ": 1
    },
    "length": 8
  },
  "print(": {
    "severity": "style",
    "table": {
      "p": 5,
      "r": 4,
      "i": 3,
      "n": 2,
      "t": 1
    },
    "length": 6
  },
  "pass": {
    "severity": "style",
    "table": {
      "p": 3,
      "a": 2,
      "s": 1
    },
    "length": 4
  }
};

const scanReport = {
  "metadata": {
    "directory": "C:\\Users\\hemab\\OneDrive\\Desktop\\FlashHack\\CodeLens",
    "extensions": ".py",
    "files_scanned": 16,
    "total_violations": 95,
    "severity_counts": {
      "critical": 3,
      "warning": 1,
      "style": 91
    },
    "scan_time": 0.0298154354095459,
    "horspool_time": 0.0298154354095459,
    "naive_time": 0.07030892372131348
  },
  "results": {
    "build_static_data.py": [
      {
        "severity": "style",
        "pattern": "print(",
        "line": 10,
        "context": "    print(\"Building static dashboard data...\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 15,
        "context": "        print(f\"Error: {config_path} not found.\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 38,
        "context": "        print(\"Warning: No .last_scan.json found. Dashboard will have empty scan results.\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 39,
        "context": "        print(\"Please run `python main.py scan sample_codebase` to populate data.\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 54,
        "context": "    print(f\"Successfully generated {out_path}\")"
      }
    ],
    "main.py": [
      {
        "severity": "style",
        "pattern": "print(",
        "line": 53,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{border}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 54,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}|\" + \" \".center(inner_width) + \"|\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 66,
        "context": "        print(f\"{Fore.CYAN + Style.BRIGHT}|{padded_art}|\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 68,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}|\" + \" \".center(inner_width) + \"|\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 74,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}|{colored_subtitle}|\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 75,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}{border}{Style.RESET_ALL}\\n\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 81,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}>> {title.upper()}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 82,
        "context": "    print(f\"{Fore.CYAN}{'-' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 87,
        "context": "    print(f\"{Fore.GREEN + Style.BRIGHT}[SUCCESS]{Style.RESET_ALL} {message}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 92,
        "context": "    print(f\"{Fore.RED + Style.BRIGHT}[ERROR]{Style.RESET_ALL}   {message}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 97,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}[INFO]{Style.RESET_ALL}    {message}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 102,
        "context": "    print(f\"{Fore.YELLOW + Style.BRIGHT}[WARN]{Style.RESET_ALL}    {message}\")"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 181,
        "context": "    Useful for passing to matchers later."
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 271,
        "context": "        print(f\"    {color}{SEVERITY_LABELS[severity]}: {count} patterns{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 336,
        "context": "            print(f\"\\n  {Fore.WHITE + Style.BRIGHT}File: {rel_path}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 338,
        "context": "                print(format_violation("
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 355,
        "context": "    print(f\"    {Fore.RED + Style.BRIGHT}Critical : {severity_counts['critical']}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 356,
        "context": "    print(f\"    {Fore.YELLOW}Warnings : {severity_counts['warning']}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 357,
        "context": "    print(f\"    {Fore.BLUE}Style    : {severity_counts['style']}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 451,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 452,
        "context": "    print(f\"{Fore.WHITE + Style.BRIGHT}  CODELENS ANALYTICS{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 453,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\\n\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 473,
        "context": "            print(f\"{Fore.CYAN}  {'-' * (width - 4)}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 475,
        "context": "            print(f\"  {Fore.WHITE}{label:<24}{Style.RESET_ALL}{value}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 477,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 483,
        "context": "        print(f\"  {'Pattern':<30} {'Count':>6}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 484,
        "context": "        print(f\"  {'-' * 30} {'-' * 6}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 486,
        "context": "            print(f\"  {pattern:<30} {count:>6}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 525,
        "context": "        print(f\"    {Fore.WHITE}{seq_result.rstrip()}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 542,
        "context": "        print(f\"    {Fore.WHITE}{direct_result.rstrip()}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 612,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 616,
        "context": "    print(f\"  {Fore.WHITE}{rel1} <-> {rel2}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 617,
        "context": "    print(f\"\\n  {level_color}Similarity Score : {similarity:.1f}%{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 618,
        "context": "    print(f\"  {level_color}{level_label}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 619,
        "context": "    print(f\"\\n  {Fore.WHITE}LCS Length       : {lcs_len} characters{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 620,
        "context": "    print(f\"  {Fore.WHITE}Similarity Time  : {sim_time:.5f}s{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 621,
        "context": "    print(f\"  {Fore.WHITE}LCS Time         : {lcs_time:.5f}s{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 623,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{'=' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 638,
        "context": "    print(f\"\\n{Fore.CYAN + Style.BRIGHT}{'-' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 639,
        "context": "    print(f\"  {Fore.WHITE + Style.BRIGHT}{'Character':<20} {'Shift':>10}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 640,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}{'-' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 647,
        "context": "        print(f\"  {Fore.WHITE}{repr(char):<20} {shift:>10}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 650,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}{'-' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 651,
        "context": "    print(f\"  {Fore.WHITE}{'Final Table Summary:':<20}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 653,
        "context": "        print(f\"  {Fore.GREEN}{repr(char):<20} {shift:>10}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 654,
        "context": "    print(f\"  {Fore.GREEN}{'*(other)':<20} {m:>10}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 655,
        "context": "    print(f\"{Fore.CYAN + Style.BRIGHT}{'-' * width}{Style.RESET_ALL}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 777,
        "context": "        print()"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 786,
        "context": "    print(f\"\\n{Fore.LIGHTBLACK_EX}  Completed in {elapsed:.3f}s{Style.RESET_ALL}\\n\")"
      }
    ],
    "benchmarks\\performance_test.py": [
      {
        "severity": "style",
        "pattern": "print(",
        "line": 20,
        "context": "    print(\"Generating large test file...\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 26,
        "context": "    print(f\"\\nBenchmarking search for '{pattern}' in file of {len(text)} characters.\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 38,
        "context": "    print(f\"Naive: found {len(naive_res)} matches in {naive_time:.5f}s\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 39,
        "context": "    print(f\"Horspool: found {len(horspool_res)} matches in {horspool_time:.5f}s\")"
      }
    ],
    "sample_codebase\\auth.py": [
      {
        "severity": "style",
        "pattern": "pass",
        "line": 4,
        "context": "def login(username, password):"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 5,
        "context": "    # CRITICAL: Hardcoded password pattern"
      },
      {
        "severity": "critical",
        "pattern": "password=",
        "line": 6,
        "context": "    password_check = \"password=SuperSecret123\""
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 6,
        "context": "    password_check = \"password=SuperSecret123\""
      },
      {
        "severity": "critical",
        "pattern": "eval(",
        "line": 9,
        "context": "    user_data = eval(username)"
      },
      {
        "severity": "warning",
        "pattern": "TODO",
        "line": 12,
        "context": "    # TODO: Implement OAuth login instead"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 15,
        "context": "    print(\"User logged in successfully\")"
      }
    ],
    "sample_codebase\\bro.py": [
      {
        "severity": "critical",
        "pattern": "password=",
        "line": 3,
        "context": "def check_password_strength(password=):"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 3,
        "context": "def check_password_strength(password=):"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 5,
        "context": "    length_check = len(password) >= 8"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 6,
        "context": "    uppercase_check = re.search(r'[A-Z]', password)"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 7,
        "context": "    lowercase_check = re.search(r'[a-z]', password)"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 8,
        "context": "    digit_check = re.search(r'\\d', password)"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 9,
        "context": "    special_check = re.search(r'[\\W_]', password)"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 25,
        "context": "def check_passwords_from_file(filename):"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 26,
        "context": "    print(f\"Checking passwords in {filename}...\\n\")"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 26,
        "context": "    print(f\"Checking passwords in {filename}...\\n\")"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 29,
        "context": "            passwords = file.readlines()"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 31,
        "context": "        for i, password in enumerate(passwords, start=1):"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 32,
        "context": "            pwd = password.strip()"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 36,
        "context": "            strength, score, checks = check_password_strength(pwd)"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 37,
        "context": "            print(f\"Password {i}: {pwd} -> Strength: {strength} ({score}/5 requirements met)\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 40,
        "context": "        print(f\"Error: The file '{filename}' was not found.\")"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 44,
        "context": "    user_pwd = input(\"Enter a password to test its strength (or type 'exit' to quit): \")"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 46,
        "context": "        strength, score, checks = check_password_strength(user_pwd)"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 47,
        "context": "        print(f\"\\nResult: {strength} (Score: {score}/5)\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 48,
        "context": "        print(f\"Details:\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 49,
        "context": "        print(f\"- At least 8 characters: {'\u2713' if checks[0] else '\u2717'}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 50,
        "context": "        print(f\"- Uppercase letter (A-Z): {'\u2713' if checks[1] else '\u2717'}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 51,
        "context": "        print(f\"- Lowercase letter (a-z): {'\u2713' if checks[2] else '\u2717'}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 52,
        "context": "        print(f\"- Number (0-9): {'\u2713' if checks[3] else '\u2717'}\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 53,
        "context": "        print(f\"- Special character: {'\u2713' if checks[4] else '\u2717'}\")"
      }
    ],
    "scanner\\directory_scanner.py": [
      {
        "severity": "style",
        "pattern": "pass",
        "line": 43,
        "context": "            pass # Ignore files that can't be read"
      }
    ],
    "scanner\\horspool.py": [
      {
        "severity": "style",
        "pattern": "print(",
        "line": 47,
        "context": "    print(f\"Testing Horspool algorithm with pattern: '{pattern}'\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 49,
        "context": "        print(f\"Text {i+1}: '{text}' -> Found at: {search(text, pattern)}\")"
      }
    ],
    "scanner\\naive.py": [
      {
        "severity": "style",
        "pattern": "print(",
        "line": 33,
        "context": "    print(f\"Testing Naive algorithm with pattern: '{pattern}'\")"
      },
      {
        "severity": "style",
        "pattern": "print(",
        "line": 35,
        "context": "        print(f\"Text {i+1}: '{text}' -> Found at: {search(text, pattern)}\")"
      }
    ]
  }
};
