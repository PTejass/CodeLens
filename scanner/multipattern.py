def search_multiple(text, patterns):
    """
    A simple multi-pattern matching implementation.
    Returns a dictionary mapping pattern -> list of starting indices.
    """
    results = {p: [] for p in patterns}
    
    # Simple pass using python's built-in find as a baseline, 
    # to be upgraded to Trie/Aho-Corasick.
    for pattern in patterns:
        idx = text.find(pattern)
        while idx != -1:
            results[pattern].append(idx)
            idx = text.find(pattern, idx + 1)
            
    return results
