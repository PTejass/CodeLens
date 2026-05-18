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
    "directory": "C:\\Users\\hemab\\OneDrive\\Desktop\\FlashHack\\CodeLens\\.repos\\GeekVerse",
    "extensions": ".py, .java, .c, .cpp, .js, .ts, .go, .rb, .php, .html, .css, .txt, .md, .json, .yml, .yaml, .sh",
    "files_scanned": 9,
    "total_violations": 6,
    "severity_counts": {
      "critical": 0,
      "warning": 0,
      "style": 6
    },
    "scan_time": 0.0503993034362793,
    "horspool_time": 0.0503993034362793,
    "naive_time": 0.11701631546020508
  },
  "results": {
    "index.html": [
      {
        "severity": "style",
        "pattern": "pass",
        "line": 69,
        "context": "        <p>Welcome to GeekVerse! We're passionate collectors and superhero enthusiasts dedicated to bringing you the"
      }
    ],
    "login.html": [
      {
        "severity": "style",
        "pattern": "pass",
        "line": 25,
        "context": "                    <label for=\"password\">Password:</label>"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 26,
        "context": "                    <input type=\"password\" id=\"password\" name=\"password\" required autocomplete=\"current-password\">"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 47,
        "context": "            const password = document.getElementById('password').value;"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 50,
        "context": "            if (username === 'admin' && password === 'geekverse') {"
      },
      {
        "severity": "style",
        "pattern": "pass",
        "line": 55,
        "context": "                errorElement.textContent = 'Invalid username or password!';"
      }
    ]
  }
};

const fileComparisons = {
  "index.html|login.html": {
    "similarity": 11.65,
    "lcs": 172,
    "file1": "index.html",
    "file2": "login.html",
    "lines1": 103,
    "lines2": 72
  }
};
