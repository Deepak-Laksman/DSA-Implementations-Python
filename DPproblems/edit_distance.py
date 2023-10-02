def edit_memo(i, j, s, t, dp):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == t[j]:
        dp[i][j] = edit_memo(i - 1, j - 1, s, t, dp)
    else:
        dp[i][j] = 1 + min(edit_memo(i - 1, j, s, t, dp), edit_memo(i - 1, j - 1, s, t, dp), edit_memo(i, j - 1, s, t, dp))
    return dp[i][j]

def edit_tab(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    return dp[m][n]