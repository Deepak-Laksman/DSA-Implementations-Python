
def LCS(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return printLCS(dp, text, pattern)

def printLCS(table, text, pattern):
    answer = []
    i, j = len(text), len(pattern)
    while i > 0 and j > 0:
        if text[i - 1] == pattern[j - 1]:
            answer.insert(0, text[i - 1])
            i -=1
            j -=1
        else:
            if table[i - 1][j] > table[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return "".join(answer)

def main():
    text = input()
    pattern = input()
    print(LCS(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()