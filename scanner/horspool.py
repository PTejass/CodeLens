def build_shift_table(pattern):
    """
    Constructs the bad-character shift table for the Horspool algorithm.
    """
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table

def search(text, pattern):
    """
    Searches for all occurrences of 'pattern' in 'text' using the Horspool algorithm.
    Returns a list of starting indices where the pattern matches.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    
    if m == 0 or m > n:
        return indices

    shift_table = build_shift_table(pattern)
    i = m - 1

    while i < n:
        k = 0
        while k < m and text[i - k] == pattern[m - 1 - k]:
            k += 1
        if k == m:
            indices.append(i - m + 1)
            i += shift_table.get(text[i], m)
        else:
            i += shift_table.get(text[i], m)

    return indices

if __name__ == "__main__":
    # Test with mock text arrays
    mock_texts = [
        "this is a simple test string",
        "another test string here",
        "no match in this one",
        "test test test"
    ]
    pattern = "test"
    print(f"Testing Horspool algorithm with pattern: '{pattern}'")
    for i, text in enumerate(mock_texts):
        print(f"Text {i+1}: '{text}' -> Found at: {search(text, pattern)}")
