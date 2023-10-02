# We will be taking the LCS only once in the final string, so all the characters other than lcs need to be taken as such,
# so final answer will be total length - lcs

def SCS(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return n + m - dp[n][m]

def main():
    text = input()
    pattern = input()
    print(SCS(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()