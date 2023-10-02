def subsetWithSumAsTarget(values, target):
    n = len(values)
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif values[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - values[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    if dp[n][target] == target:
        return True
    else:
        return False

def subsetWithSumAsTargetBoolean(values, target):
    n = len(values)
    dp = [[False for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif values[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - values[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

def main():
    values = [int(a) for a in input().split()]
    target = int(input())
    print(subsetWithSumAsTargetBoolean(values, target))

if __name__ == "__main__":
    main()