# CodeLens: Intelligent Code Review Assistant - Implementation Plan

This document outlines the architecture, tasks, and parallelized implementation strategy for the CodeLens tool. The work is divided among 3 developers to ensure an efficient, non-blocking development process.

## Parallelized Work Strategy

The workload is split into three major domains to minimize merge conflicts and allow parallel development.

### **Developer 1: Core Algorithms & DAA Concepts**
**Focus**: Efficient string matching algorithms and performance benchmarking.
- **Tasks**:
  - Implement `horspool.py` (shift table construction, search logic).
  - Implement `naive.py` (baseline text search).
  - Implement `multipattern.py` (Trie / Aho-Corasick or single-pass multi-term matching).
  - Implement `performance_test.py` to compare Horspool and Naive algorithms on large files.

### **Developer 2: OS Concepts, Similarity & File System**
**Focus**: Simulating file access methods, file reading, and plagiarism detection.
- **Tasks**:
  - Implement `sequential_access.py` (line-by-line file reading).
  - Implement `direct_access.py` (jumping to specific line numbers via byte offsets).
  - Implement `similarity.py` (Longest Common Substring, sequence matching via `difflib`).
  - Core directory walker logic to recursively scan supported extensions (`.py`, `.java`, etc.).

### **Developer 3: CLI, Reporting & Integration**
**Focus**: User interface, CLI commands, reporting pipelines, and configuration.
- **Tasks**:
  - Setup `config/banned_patterns.json` schema and loading logic.
  - Implement CLI interface in `main.py` using `argparse`.
  - Build `report_generator.py` (TXT, JSON, CSV output).
  - Implement ANSI color terminal UI (Critical=Red, Warning=Yellow, Style=Blue).
  - Implement the analytics dashboard logic (violation stats, timings).

---

## Phased Execution Plan

### **Phase 1: Foundation & Core Logic**
- **Dev 1**: Write Horspool and Naive string matching algorithms. Test with mock text arrays.
- **Dev 2**: Implement File System access patterns (Sequential and Direct access). Ensure they can read sample large files.
- **Dev 3**: Set up the project structure, `main.py` entry point, `banned_patterns.json`, and basic `argparse` CLI skeleton.

### **Phase 2: Integration & Advanced Features**
- **Dev 1**: Build the similarity detection algorithms (LCS) and multi-pattern matching.
- **Dev 2**: Build the directory scanner that uses Dev 2's file access methods and passes content to Dev 1's algorithms.
- **Dev 3**: Create the reporting engine (JSON/CSV/TXT outputs) and integrate `colorama` for colorful terminal output.

### **Phase 3: Benchmarking & Final Polish**
- **Dev 1**: Write `performance_test.py` generating files with 10,000+ lines to benchmark the search algorithms.
- **Dev 2**: Fine-tune direct access jumping and optimize similarity scoring performance.
- **Dev 3**: Wire everything into the CLI commands (`scan`, `report`, `stats`, `jump`, `compare`). Finalize the Analytics Dashboard output.

---

## Proposed Project Structure

```txt
CodeLens/
│
├── main.py                          # Dev 3
├── config/
│   └── banned_patterns.json         # Dev 3
├── scanner/
│   ├── horspool.py                  # Dev 1
│   ├── naive.py                     # Dev 1
│   ├── multipattern.py              # Dev 1
│   └── similarity.py                # Dev 1 & 2
├── filesystem/
│   ├── sequential_access.py         # Dev 2
│   └── direct_access.py             # Dev 2
├── reports/
│   ├── report_generator.py          # Dev 3
│   └── output/
├── benchmarks/
│   └── performance_test.py          # Dev 1
└── sample_codebase/                 # All
```

## Verification Plan

### Automated Tests
- Run `python benchmarks/performance_test.py` to ensure Horspool outperforms Naive pattern matching.
- Verify JSON, CSV, and TXT reports are correctly formatted.

### Manual Verification
- Run `python main.py scan sample_codebase/` to visually verify colorized ANSI terminal output and detected violations.
- Run `python main.py compare file1.py file2.py` to test the plagiarism/similarity score generation.
- Run `python main.py jump file.py 42` to verify direct file access simulation.
