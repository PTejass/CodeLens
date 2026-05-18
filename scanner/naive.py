def search(text, pattern):
    """
    Searches for all occurrences of 'pattern' in 'text' using a Naive matching approach.
    Returns a list of starting indices where the pattern matches.
    """
    indices = []
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return indices

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            indices.append(i)

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
    print(f"Testing Naive algorithm with pattern: '{pattern}'")
    for i, text in enumerate(mock_texts):
        print(f"Text {i+1}: '{text}' -> Found at: {search(text, pattern)}")
