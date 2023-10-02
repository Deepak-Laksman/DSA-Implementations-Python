def maximumProfit(price, n):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    length = [i for i in range(1, n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i > 0 and length[i - 1] <= j:
                dp[i][j] = max(price[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j])
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    return dp[n][n]

def main():
    price = [int(a) for a in input().split()]
    n = len(price)
    print(maximumProfit(price, n))

if __name__ == "__main__":
    main()