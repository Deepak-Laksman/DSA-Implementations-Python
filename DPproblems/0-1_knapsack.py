def knapsack_0_1(idx, values, weights, W, dp):
    if W == 0:
        return 0
    if idx == len(values):
        return 0
    if dp[idx][W] != -1:
        return dp[idx][W]
    not_pick = knapsack_0_1(idx + 1, values, weights, W, dp)
    pick = 0
    if weights[idx] <= W:
        pick = values[idx] + knapsack_0_1(idx + 1, values, weights, W - weights[idx], dp)
    dp[idx][W] = max(not_pick, pick)
    return dp[idx][W]

def knapsack_0_1_tab(n, values, weights, W):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][W]