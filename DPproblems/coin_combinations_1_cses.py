def main():
    modulo = 10 ** 9 + 7
    n, target = map(int, input().split())
    coins = [int(a) for a in input().split()]
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = (dp[i] + dp[i - coins[j]]) % modulo
            else:
                continue
    print(dp[target])

if __name__ == "__main__":
    main()