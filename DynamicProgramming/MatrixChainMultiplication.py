def MCM(array, i, j):
    if i >= j:
        return 0
    cost = float("inf")
    for k in range(i, j):
        tempCost = MCM(array, i, k) + MCM(array, k + 1, j) + array[i - 1] * array[k] * array[j]
        cost = min(cost, tempCost)
    return cost

def MCMmemoized(array, i, j, memo = None):
    if memo is None:
        memo = {}
    if i >= j:
        return 0
    if (i, j) in memo.keys():
        return memo[(i, j)]
    cost = float("inf")
    for k in range(i, j):
        tempCost = MCMmemoized(array, i, k, memo) + MCMmemoized(array, k + 1, j, memo) + array[i - 1] * array[k] * array[j]
        cost = min(cost, tempCost)
        memo[(i, j)] = cost
    return memo[(i, j)]

def MCMdp(array):
    n = len(array)
    dp = [[float("inf") for i in range(n)] for j in range(n)]
    # cost of multiplying same matrix = 0
    for i in range(1, n):
        dp[i][i] = 0
    # L is chain length, that is, j - i + 1
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + array[i - 1] * array[k] * array[j])
    return dp[1][n - 1]

def main():
    array = [int(a) for a in input().split()]
    print(MCMdp(array))

if __name__ == "__main__":
    main()