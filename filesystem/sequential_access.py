def read_file_sequential(filepath):
    """
    Simulates sequential file access by reading a file line by line.
    Yields (line_number, line_content).
    """
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line_number, line in enumerate(f, 1):
            yield line_number, line
