# hash value of whole string in O(n)
# modulo multiplicative inverse in O(nlog(n))
# hash value of substring in O(1)

modulo = 10 ** 9 + 7
hash = []
powers = []
inverse = []

def power(a, b):
    global modulo
    ans = 1
    while b:
        if b & 1:
            ans = (ans * a) % modulo
        b >>= 1
        a = (a * a) % modulo
    return ans


def substring_hashing(string):
    global modulo, hash, powers, inverse
    n = len(string)
    hash = [0 for i in range(n + 1)]
    powers = [1 for i in range(n)]
    hash[0] = 0
    p = 31
    for i in range(1, n):
        powers[i] = (powers[i - 1] * p) % modulo
    for i in range(0, n):
        inverse[i] = power(powers[i], modulo - 2)
        hash[i + 1] = (hash[i] + (ord(string[i]) - 96) *  powers[i]) % modulo
    
def get_hash_of_substring(l, r):
    global modulo, hash, inverse
    if l == 0:
        return hash[r]
    return (((hash[r + 1] - (hash[l] * powers[r - l + 1]) % modulo) + modulo) % modulo)
        