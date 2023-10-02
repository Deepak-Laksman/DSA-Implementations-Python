def minimumInsertions(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return n - dp[n][m]

def main():
    string = input()
    print(minimumInsertions(string, string[::-1], len(string), len(string)))

if __name__ == "__main__":
    main()