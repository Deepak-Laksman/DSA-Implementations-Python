def findMaxProfitRecursive(weights, values, capacity, n):
    if capacity == 0 or n == 0:
        return 0
    if weights[n - 1] <= capacity:
        return max(values[n - 1] + findMaxProfitRecursive(weights, values, capacity - weights[n - 1], n - 1), \
            findMaxProfitRecursive(weights, values, capacity, n - 1))
    else:
        return findMaxProfitRecursive(weights, values, capacity, n - 1)

def findMaxProfitMemoization(weights, values, capacity, n, memo = None):
    if memo is None:
        memo = {}
    if capacity == 0 or n == 0:
        return 0
    if (n - 1, capacity) in memo.keys():
        return memo[(n - 1, capacity)]

    if weights[n - 1] <= capacity:
        memo[(n - 1, capacity - weights[n - 1])] = max(values[n - 1] +
            findMaxProfitMemoization(weights, values, capacity - weights[n - 1], n - 1, memo), \
            findMaxProfitMemoization(weights, values, capacity, n - 1, memo))
        return memo[(n - 1, capacity - weights[n - 1])]
    else:
        memo[(n - 1, capacity)] = findMaxProfitMemoization(weights, values, capacity, n - 1, memo)
        return memo[(n - 1, capacity)]

def findMaxProfitTabulation(weights, values, capacity, n):
    dp = [[0 for i in range(capacity + 1)]for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]

def main():
    weights = [int(a) for a in input().split()]
    values = [int(a) for a in input().split()]
    n = len(weights)
    capacity = int(input())
    print(findMaxProfitTabulation(weights, values, capacity, n))

if __name__ == "__main__":
    main()