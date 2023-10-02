def main():
    n, m = map(int, input().split())
    arr = [int(a) for a in input().split()]
    dp = [1 for i in range(n)]
    for i in range(n):
        if i - 1 >= 0 and i + 1 < n:
            val = abs(arr[i - 1] - arr[i + 1])
            if val == 0:
                dp[i] = 3 * dp[i - 1]
            elif val == 1:
                dp[i] = 2 * dp[i - 1]
            else:
                dp[i] = dp[i - 1] 