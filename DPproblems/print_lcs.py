def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(print_lcs(dp, m, n, s, t))

def print_lcs(dp, m, n, s, t):
    i, j =  n, m
    lcs = []
    while i >= 1 and j >= 1:
        if s[j - 1] == t[i - 1]:
            lcs.append(s[j - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    lcs.reverse()
    return "".join(lcs)

def main():
    s = input()
    t = input()
    lcs(s, t)

if __name__ == "__main__":
    main()