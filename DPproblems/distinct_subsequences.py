def count_distinct_subsequences_memo(i, j, s, t, dp):
    if j < 0:
        return 1
    if i < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == t[j]:
        dp[i][j] = count_distinct_subsequences_memo(i - 1, j - 1, s, t, dp) + count_distinct_subsequences_memo(i - 1, j, s, t, dp)
    else:
        dp[i][j] = count_distinct_subsequences_memo(i - 1, j, s, t, dp)
    return dp[i][j]

def count_distinct_subsequences(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]