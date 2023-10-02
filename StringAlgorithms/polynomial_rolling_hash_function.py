def hash_function(s):
    hash_value = 0
    p = 1
    m = 10 ** 9 + 9
    for i in range(len(s)):
        hash_value = (hash_value + (ord(s[i]) - 96) * p) % m
        p = (p * 31) % m
    return hash_value

def group_duplicate_strings(string_list):
    hashes = []
    for i in range(len(string_list)):
        hashes.append((hash_function(string_list[i]), i))
    hashes.sort()
    groups = [[hashes[0][1]]]
    for i in range(1, len(hashes)):
        if hashes[i][0] == hashes[i - 1][0]:
            groups[-1].append(hashes[i][1])
        else:
            groups.append([hashes[i][1]])
    return groups

def count_unique_substrings_string(s):
    n = len(s)
    pow = [1 for i in range(n)]
    m = 10 ** 9 + 9
    p = 31
    for i in range(1, n):
        pow[i] = (pow[i - 1] * p) % m
    h = [0 for i in range(n + 1)]
    for i in range(n):
        h[i + 1] = (h[i] + (ord(s[i]) - 96) * pow[i]) % m
    count = 0 
    for l in range(1, n + 1):
        substrings_of_size_l = set()
        for i in range(n - l + 1):
            hash_value = (h[i + l] - h[i] + m) % m
            hash_value = (hash_value * pow[n - i - 1]) % m
            substrings_of_size_l.add(hash_value)
        count += len(substrings_of_size_l)
    return count

def main():
    strings = input()
    print(count_unique_substrings_string(strings))

if __name__ == "__main__":
    main()