import difflib

def calculate_similarity(text1, text2):
    """
    Calculates a similarity score between two strings using difflib.
    Returns a percentage (0 to 100).
    """
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio() * 100.0

def longest_common_substring(s1, s2):
    """
    Finds the longest common substring between two strings.
    """
    m = len(s1)
    n = len(s2)
    lcs_suffix = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_suffix[i][j] = lcs_suffix[i - 1][j - 1] + 1
                result = max(result, lcs_suffix[i][j])
            else:
                lcs_suffix[i][j] = 0
                
    return result
