# Time Complexity is O(n log(log(n)))
# Space Complexity is O(n)

n = 10 ** 6 + 1
primes = [True] * n

def prime_sieve():
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1