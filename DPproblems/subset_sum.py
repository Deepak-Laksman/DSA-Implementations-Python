def subset(i, arr, k, dp):
    if i > len(arr):
        return False
    if k < 0:
        return False
    if k == 0:
        return True
    if i == len(arr):
        return False
    if dp[i][k] != -1:
        return dp[i][k]
    dp[i][k] = subset(i + 1, arr, k - arr[i], dp) or subset(i + 1, arr, k, dp)
    return dp[i][k]

def main():
    k = int(input())
    arr = [int(a) for a in input().split()]
    n = len(arr)
    dp = [[0 for i in range(k + 1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(n):
        for j in range(1, k + 1):
            if arr[i] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n - 1][k])

if __name__ == "__main__":
    main()