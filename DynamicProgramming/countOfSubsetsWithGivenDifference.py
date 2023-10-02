def countSubsets(values, target):
    n = len(values)
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = 1
            if i > 0 and values[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - values[i - 1]] + dp[i - 1][j]
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

def countSubsets1dDP(values, target):
    n = len(values)
    dp = [0] * (n + 1)
    dp[0] = 1
    for val in values:
        for sum in range(target, val - 1, -1):
            dp[sum] += dp[sum - val]
    return dp[target]

def countOfSubsetsWithGivenDifference(values, difference):
    total = sum(values)
    if (total + difference) % 2 or (abs(total) < abs(difference)):
        return 0
    else:
        val = (total - difference) // 2
        return countSubsets1dDP(values, val)

def main():
    values = [int(a) for a in input().split()]
    difference = int(input())
    print(countOfSubsetsWithGivenDifference(values, difference))

if __name__ == "__main__":
    main()