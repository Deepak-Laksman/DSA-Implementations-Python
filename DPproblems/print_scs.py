def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(print_scs(dp, s, t, m, n))

def print_scs(dp, s, t, m, n):
    i, j = m, n
    scs = []
    while i >= 1 and j >= 1:
        if s[i - 1] == t[j - 1]:
            scs.append(s[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                scs.append(s[i - 1])
                i -= 1
            else:
                scs.append(t[j - 1])
                j -= 1
    while i >= 1:
        scs.append(s[i - 1])
        i -= 1
    while j >= 1:
        scs.append(t[j - 1])
        j -= 1
    scs.reverse()
    return "".join(scs)

def main():
    s = input()
    t = input()
    lcs(s, t)

if __name__ == "__main__":
    main()