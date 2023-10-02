def main():
    modulo = 10 ** 9 + 7
    n, target = map(int, input().split())
    coins = [int(a) for a in input().split()]
    coins.sort()
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], target + 1):
            if coins[i] <= j:
                dp[j] = (dp[j] + dp[j - coins[i]]) % modulo
    print(dp[target])

if __name__ == "__main__":
    main()