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

def longest_common_subsequence(s1, s2):
    """
    Finds the longest common subsequence (LCS) between two strings.
    Returns the length of the LCS.
    """
    m = len(s1)
    n = len(s2)
    
    # dp[i][j] will store the length of LCS of s1[0..i-1] and s2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[m][n]
