modulo = 10 ** 9 + 7

def recur(n, dp):
    global modulo
    if n < 0:
        return 0
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    ans = 0
    for i in range(1, 7):
        ans = (ans + (recur(n - i, dp))) % modulo
    dp[n] = ans
    return dp[n] % modulo

def main():
    global modulo
    n = int(input())
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % modulo
            else:
                break
    print(dp[n] % modulo)

if __name__ == "__main__":
    main()