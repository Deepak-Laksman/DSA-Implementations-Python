def countSubsetSums(values, target):
    n = len(values)
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = 1
            elif values[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - values[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

def main():
    values = [int(a) for a in input().split()]
    target = int(input())
    print(countSubsetSums(values, target))

if __name__ == "__main__":
    main()