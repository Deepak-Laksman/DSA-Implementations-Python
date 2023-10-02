def unboundedKnapsack(values, weights, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] <= capacity:
        return max(values[n - 1] + unboundedKnapsack(values, weights, capacity - weights[n - 1], n), unboundedKnapsack(values, weights, capacity, n - 1))
    else:
        return unboundedKnapsack(values, weights, capacity, n - 1)

def unboundedKnapsackDP(values, weights, capacity, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i > 0 and weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i][j - weights[i - 1]], dp[i - 1][j])
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]

def unboundedKnapsack1dDP(values, weights, capacity, n):
    dp = [0] * (capacity + 1)
    for i in range(capacity + 1):
        for j in range(n):
            if values[j] <= i:
                dp[i] = max(dp[i - weights[j]] + values[j], dp[i])
    return dp[capacity]

def main():
    values = [int(a) for a in input().split()]
    weights = [int(w) for w in input().split()]
    capacity = int(input())
    n = len(values)
    print(unboundedKnapsack1dDP(values, weights, capacity, n))

if __name__ == "__main__":
    main()