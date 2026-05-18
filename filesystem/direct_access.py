def index_file_lines(filepath):
    """
    Creates an index of byte offsets for each line in the file.
    Returns a list of byte offsets where index `i` is the offset of line `i+1`.
    """
    offsets = []
    with open(filepath, 'rb') as f:
        offset = 0
        for line in f:
            offsets.append(offset)
            offset += len(line)
    return offsets

def read_line_direct(filepath, line_number, offsets):
    """
    Simulates direct (random) access by jumping to the exact byte offset of a line.
    line_number is 1-indexed.
    """
    if line_number < 1 or line_number > len(offsets):
        return None
        
    offset = offsets[line_number - 1]
    with open(filepath, 'rb') as f:
        f.seek(offset)
        line = f.readline()
        return line.decode('utf-8', errors='ignore')
