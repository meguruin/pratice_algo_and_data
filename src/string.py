# cls: calculate Longest Common Subsequence of two strings
# e.g.) cls("aaabbbc", "xaacx") -> "aac"
# time complexity: O(len(x)len(y))
def lc_subsequence(x, y):
    lx, ly = len(x), len(y)
    if lx == 0 or ly == 0:
        return ""
    dp = [[0 for _ in range(ly + 1)] for _ in range(lx + 1)]
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if x[i - 1] == y[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    res = ""
    i = lx
    j = ly
    while i >= 1 and j >= 1:
        if x[i - 1] == y[j - 1]:
            res = x[i - 1] + res
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            elif dp[i][j] == dp[i][j - 1]:
                j -= 1
    return res


# e.g.) cls("aaabbbc", "xaacx") -> "aa"
def lc_substring(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
    mx = -1
    pos = -1
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if mx < dp[i][j]:
                    mx = dp[i][j]
                    pos = i
    return s1[pos - mx:pos]
