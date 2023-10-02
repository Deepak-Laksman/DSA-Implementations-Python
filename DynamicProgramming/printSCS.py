def SCS(text, pattern, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return printSCS(text, pattern, n, m, dp)

def printSCS(text, pattern, n, m, table):
    answer = []
    i, j = n, m
    while i > 0 and j > 0:
        if text[i - 1] == pattern[j - 1]:
            answer.insert(0, text[i - 1])
            i -= 1
            j -= 1
        else:
            if table[i][j - 1] > table[i - 1][j]:
                answer.insert(0, pattern[j - 1])
                j -= 1
            else:
                answer.insert(0, text[i - 1])
                i -= 1
    while i > 0:
        answer.insert(0, text[i - 1])
        i -= 1
    while j > 0:
        answer.insert(0, pattern[j - 1])
        j -= 1
    return "".join(answer)

def main():
    text = input()
    pattern = input()
    print(SCS(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()