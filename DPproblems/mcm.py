def mcm(i, j, arr, dp):
    if i == j:
        return 0
    if dp[i][j] != float("inf"):
        return dp[i][j]
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], arr[i - 1] * arr[k] * arr[j] + mcm(i, k, arr, dp) + mcm(k + 1, j, arr,dp))
    return dp[i][j]
    
def matrixMultiplication(arr, n):
    dp = [[float("inf") for i in range(n)] for j in range(n)]
    return mcm(1, len(arr) - 1, arr, dp)

def matrixMultiplication_tab(arr, n):
    dp = [[float("inf") for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j])
    return dp[1][n - 1]