def main():
    n = int(input())
    dp = [float("inf") for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(len(str(i))):
            dp[i] = min(dp[i], 1 + dp[i - int(str(i)[j])])
    print(dp[n])

if __name__ == "__main__":
    main()