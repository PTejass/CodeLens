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
