def minimumCoinsCount(coins, amount):
    n = len(coins)
    dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(amount + 1):
            if j == 0:
                dp[i][j] = 0
            if i == 0:
                dp[i][j] = float("inf") - 1
            elif i > 0 and j > 0:
                if coins[i - 1] % j:
                    dp[i][j] = float("inf") - 1
                else:
                    dp[i][j] = j // coins[i - 1]
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]            
    return dp[n][amount]

def main():
    coins = [int(a) for a in input().split()]
    amount = int(input())
    print(minimumCoinsCount(coins, amount))

if __name__ == "__main__":
    main()