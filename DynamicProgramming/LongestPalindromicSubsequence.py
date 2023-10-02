def LPS(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

def main():
    string = input()
    reverse = string[::-1]
    print(LPS(string, reverse, len(string), len(reverse)))

if __name__ == "__main__":
    main()