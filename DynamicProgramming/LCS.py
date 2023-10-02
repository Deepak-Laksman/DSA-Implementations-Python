def LCS(text, pattern, n, m):
    if n == 0 or m == 0:
        return 0
    if text[n - 1] == pattern[m - 1]:
        return 1 + LCS(text, pattern, n - 1, m - 1)
    else:
        return max(LCS(text, pattern, n, m - 1), LCS(text, pattern, n - 1, m))

def LCSMemoization(text, pattern, n, m, memo = None):
    if memo is None:
        memo = {}
    if n == 0 or m == 0:
        return 0
    if (n, m) in memo.keys():
        return memo[(n, m)]
    if text[n - 1] == pattern[m - 1]:
        memo[(n, m)] = 1 + LCSMemoization(text, pattern, n - 1, m - 1, memo)
    else:
        memo[(n, m)] = max(LCSMemoization(text, pattern, n, m - 1, memo), LCSMemoization(text, pattern, n - 1, m, memo))
    return memo[(n, m)]

def LCSDP(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]

def main():
    text = input()
    pattern = input()
    print(LCSDP(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()