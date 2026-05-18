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
    
    # Optimize space complexity to O(n)
    curr = [0] * (n + 1)
    result = 0

    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = curr[j]
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev + 1
                if curr[j] > result:
                    result = curr[j]
            else:
                curr[j] = 0
            prev = temp
                
    return result
