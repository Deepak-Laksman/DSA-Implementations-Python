def rabin_karp_matching(text, pattern):
    modulo = 10 ** 9 + 7
    n, m = len(text), len(pattern)
    hash_text = [0 for i in range(n)]
    powers = [0 for i in range(n)]
    powers[0] = 1
    hash_pattern = ord(pattern[0]) - 96
    p = 31
    # finding hash value of pattern
    for i in range(1, m):
        hash_pattern = (hash_pattern + (ord(pattern[i]) - 96) * p) % modulo
        p = (p * p) % modulo
    p = 31
    # making hash of prefixes in text
    hash_text[0] = ord(text[0]) - 96
    for i in range(1, n):
        powers[i] = (powers[i - 1] * p) % modulo
        hash_text[i] = (hash_text[i - 1] + (ord(text[i]) - 96) * powers[i]) % modulo

    # finding substrings with hash value same as pattern in text
    ans = []
    for i in range(n - m):
        if i == 0:
            hash_substring = (hash_text[i + m - 1] + modulo) % modulo
            if hash_substring == hash_pattern:
                ans.append(0)
        else:
            hash_substring = (hash_text[i + m - 1] + modulo - hash_text[i - 1]) % modulo
            if hash_substring * powers[i] == hash_pattern:
                ans.append(i)

    return ans