def unbounded_memo(idx, profit, weight, W, dp):
    if W == 0:
        return 0
    if idx == len(profit):
        return 0
    if dp[idx][W] != -1:
        return dp[idx][W]
    not_pick = unbounded_memo(idx + 1, profit, weight, W, dp)
    pick = 0
    if weight[idx] <= W:
        pick = profit[idx] + unbounded_memo(idx, profit, weight, W - weight[idx], dp)
    dp[idx][W] = max(not_pick, pick)
    return dp[idx][W]

def unbounded_0_1(n, w, profit, weight):
    dp = [[0 for i in range(w + 1)] for j in range(n)]
    for i in range(1, w + 1):
        dp[0][i] = profit[0] * (i // weight[0]) if weight[0] <= i else 0
    for i in range(n):
        for j in range(1, w + 1):
            if weight[i] <= j:
                dp[i][j] = max(dp[i - 1][j], profit[i] + dp[i][j - weight[i]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n - 1][w]