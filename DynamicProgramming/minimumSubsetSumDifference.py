def subsetSum(values, target):
    n = len(values)
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if i > 0 and values[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - values[i - 1]], dp[i - 1][j])
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

def minimumSubsetSumDiff(values):
    total = sum(values)
    return abs(total - 2 * subsetSum(values, total // 2))

def main():
    values = [int(a) for a in input().split()]
    print(minimumSubsetSumDiff(values))

if __name__ == "__main__":
    main()