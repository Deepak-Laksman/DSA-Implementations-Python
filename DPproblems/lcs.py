def lcs(s, t) :
    n1 = len(s)
    n2 = len(t)
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]

def main():
    s = input()
    t = input()
    print(lcs(s, t))

if __name__ == "__main__":
    main()