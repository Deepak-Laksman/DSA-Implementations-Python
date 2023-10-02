def numberOfWays(coins, amount):
    n = len(coins)
    dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(amount + 1):
            if j == 0:
                dp[i][j] = 1
            if i > 0 and coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
    return dp[n][amount]

def main():
    coins = [int(a) for a in input().split()]
    amount = int(input())
    print(numberOfWays(coins, amount))

if __name__ == "__main__":
    main()