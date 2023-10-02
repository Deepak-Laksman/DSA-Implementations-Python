def minimumInsertionsOrDeletions(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return [m - dp[n][m], n - dp[n][m]]

def main():
    text = input()
    pattern = input()
    print("Insertions : {a}, Deletions : {b}".format(a = minimumInsertionsOrDeletions(text, pattern, len(text), len(pattern))[0], b = minimumInsertionsOrDeletions(text, pattern, len(text), len(pattern))[1]))

if __name__ == "__main__":
    main()