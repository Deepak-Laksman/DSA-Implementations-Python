def prefix_function(string):
    n = len(string)
    length = 0
    lps = [0 for i in range(n)]
    i = 1
    while i < n:
        if string[length] == string[i]:
            lps[i] = length + 1
            length += 1
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                i += 1
    return lps

def kmp_algo(text, pattern):
    pi_pattern = prefix_function(pattern)
    i, j = 0, 0
    m, n = len(text), len(pattern)
    ans = []
    while i < m:
        if text[i] == text[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = pi_pattern[j - 1]
            else:
                i += 1
        if j == n:
            ans.append(i - j)
            j = pi_pattern[j - 1]
    return ans

def main():
    text, pattern = input().split()
    print(*kmp_algo(text, pattern))

if __name__ == "__main__":
    main()