import os
from filesystem.sequential_access import read_file_sequential
from scanner.multipattern import AhoCorasick

def get_supported_files(directory, extensions):
    """
    Recursively scans the directory for files with supported extensions.
    Yields file paths.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                yield os.path.join(root, file)

def scan_directory(directory, patterns, extensions=('.py', '.java', '.c', '.cpp', '.js')):
    """
    Scans a directory for specific patterns using sequential file access
    and Dev 1's multi-pattern matching algorithm.
    Returns a list of violations.
    """
    violations = []
    
    # Pre-compile the Aho-Corasick automaton
    ac = AhoCorasick()
    for p in patterns:
        ac.add_pattern(p)
    ac.build()
    
    for filepath in get_supported_files(directory, extensions):
        try:
            for line_number, line in read_file_sequential(filepath):
                results = ac.search(line)
                for pattern, indices in results.items():
                    if indices:
                        violations.append({
                            'file': filepath,
                            'line': line_number,
                            'pattern': pattern,
                            'indices': indices,
                            'content': line.strip()
                        })
        except Exception as e:
            pass # Ignore files that can't be read
            
    return violations
