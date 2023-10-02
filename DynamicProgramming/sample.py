def LCS(text, pattern, n, m):
    if n == 0 or m == 0:
        return 0, []
    if text[n - 1] == pattern[m - 1]:
        return 1 + LCS(text, pattern, n - 1, m - 1)[0], LCS(text, pattern, n - 1, m - 1)[1] + [pattern[m - 1]]
    else:
        lcs1, lcs2 = LCS(text, pattern, n, m - 1), LCS(text, pattern, n - 1, m)
        if lcs1[0] >= lcs2[0]:
            return lcs1[0], lcs1[1]
        else:
            return lcs2[0], lcs2[1] 

def main():
    text = input()
    pattern = input()
    print(*LCS(text, pattern, len(text), len(pattern)))

if __name__ == "__main__":
    main()