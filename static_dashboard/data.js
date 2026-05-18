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
    "directory": "C:\\Users\\hemab\\OneDrive\\Desktop\\FlashHack\\CodeLens\\sample_codebase",
    "extensions": ".py, .java, .c, .cpp, .js",
    "files_scanned": 3,
    "total_violations": 37,
    "severity_counts": {
      "critical": 5,
      "warning": 2,
      "style": 30
    },
    "scan_time": 0.002012968063354492,
    "horspool_time": 0.002012968063354492,
    "naive_time": 0.004387378692626953
  },
  "results": {
    "auth.py": [
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
    "bro.py": [
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
    "helper.js": [
      {
        "severity": "critical",
        "pattern": "exec(",
        "line": 4,
        "context": "    // CRITICAL: Dangerous execution pattern (matching \"exec(\")"
      },
      {
        "severity": "critical",
        "pattern": "exec(",
        "line": 5,
        "context": "    let result = exec(cmd);"
      },
      {
        "severity": "warning",
        "pattern": "FIXME",
        "line": 8,
        "context": "    // FIXME: This is vulnerable to command injection!"
      },
      {
        "severity": "style",
        "pattern": "goto",
        "line": 10,
        "context": "    // STYLE: global variable declaration or goto style patterns"
      },
      {
        "severity": "style",
        "pattern": "global ",
        "line": 10,
        "context": "    // STYLE: global variable declaration or goto style patterns"
      }
    ]
  }
};

const fileComparisons = {
  "auth.py|bro.py": {
    "similarity": 1.51,
    "lcs": 16,
    "file1": "auth.py",
    "file2": "bro.py",
    "lines1": 17,
    "lines2": 56
  },
  "auth.py|helper.js": {
    "similarity": 14.22,
    "lcs": 22,
    "file1": "auth.py",
    "file2": "helper.js",
    "lines1": 17,
    "lines2": 14
  },
  "bro.py|helper.js": {
    "similarity": 1.23,
    "lcs": 16,
    "file1": "bro.py",
    "file2": "helper.js",
    "lines1": 56,
    "lines2": 14
  }
};
