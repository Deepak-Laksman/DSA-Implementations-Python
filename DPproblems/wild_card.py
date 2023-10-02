def wild_memo(i, j, s, t, dp):
    if i < 0 and j < 0:
        return True
    if j < 0:
        return False
    if i < 0:
        if t[:j + 1] == "*"*(j + 1):
            return True
        return False
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == t[j] or t[j] == "?":
        dp[i][j] = wild_memo(i - 1, j - 1, s, t, dp)
        return dp[i][j]
    if t[j] == "*":
        dp[i][j] = wild_memo(i - 1, j, s, t, dp) or wild_memo(i, j - 1, s, t, dp)
        return dp[i][j]
    if s[i] != t[j]:
        dp[i][j] = False
        return dp[i][j]

def wild_tab(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[0][i] = True if t[:i] == "*" * i else False
    for i in range(1, m + 1):
        dp[i][0] = False
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1] or t[j - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]
            elif t[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif s[i - 1] != t[j - 1]:
                dp[i][j] = False
    return dp[m][n] 