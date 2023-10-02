def LCSubstring(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0
    maxi = float("-inf")
    for i in range(n + 1):
        maxi = max(maxi, max(dp[i]))
    return maxi

def main():
    text = input()
    pattern = input()
    print(LCSubstring(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()