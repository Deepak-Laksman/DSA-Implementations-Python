def min_coins(idx, values, target, dp):
    if target == 0:
        return 0
    if idx == len(values):
        return float("inf")
    if dp[idx][target] != -1:
        return dp[idx][target]
    not_pick = min_coins(idx + 1, values, target, dp)
    pick = float("inf")
    if values[idx] <= target:
        pick = 1 + min_coins(idx, values, target - values[idx], dp)
    dp[idx][target] = min(pick, not_pick)
    return dp[idx][target]

def min_coins(n, num, x):
    dp = [[float("inf") for i in range(x + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if j % num[i - 1] == 0:
                dp[i][j] = j // num[i - 1]
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if num[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - num[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][x] if dp[n][x] != float("inf") else -1