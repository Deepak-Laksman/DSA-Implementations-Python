def isAaSubsequenceOfBRecursive(text, pattern, n, m):
    if n == 0 or m == 0:
        return False
    if text[n - 1] == pattern[m - 1]:
        return True or isAaSubsequenceOfBRecursive(text, pattern, n - 1, m - 1)
    else:
        return isAaSubsequenceOfBRecursive(text, pattern, n - 1, m) or isAaSubsequenceOfBRecursive(text, pattern, n, m - 1)

def isAaSubsequenceOfB(text, pattern, n, m):
    dp = [[False for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[n][m]

def main():
    text, pattern = input().split()
    LCS = isAaSubsequenceOfB(text, pattern, len(text), len(pattern))
    print(LCS)

if __name__ == "__main__":
    main()