def subsetSum(arr, total):
    n = len(arr)
    dp = [[False for i in range(total + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(total + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][total]

def subsetWithEqualSumExists(values):
    n = len(values)
    dp = [False for i in range(n + 1)]
    if sum(values) % 2:
        return False
    else:
        return subsetSum(values, sum(values) // 2)

def main():
    values = [int(a) for a in input().split()]
    print(subsetWithEqualSumExists(values))

if __name__ == "__main__":
    main()