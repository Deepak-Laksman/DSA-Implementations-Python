# Problem

# Given a number N, and Q queries, for each query K, find the number of common divisors of K and N

# Solution Approach

# First we prime factorize N
# Now for every prime in prime factorization of N, we will find its power in GCD(N, K)
# Then, we take minimum power value of every prime in both N and GCD(N, K).
# Finally, we put it in the number of divisors formula.

N = 0
spf = []
primes_map = {}

def pre_computation(N):
    global spf
    n = N + 1
    spf = [-1] * n
    # prime factorizing N using sieve
    for i in range(2, n):
        if spf[i] == -1:
            spf[i] = i
            for j in range(i * i, n, i):
                if spf[j] == -1:
                    spf[j] = i
    # taking all prime divisors of N and putting them with their respective power in a dictionary
    while spf[N] != -1:
        if spf[N] not in primes_map.keys():
            primes_map[spf[N]] = 1
        else:
            primes_map[spf[N]] += 1
        N = N // spf[N]
    if N > 1:
        primes_map[N] = 1

def number_of_divisors_of_N_that_are_not_multiples_of_K(K):
    number_divisors_of_N = 1
    for key in primes_map:
        number_divisors_of_N *= (primes_map[key] + 1)
    if K > N:
        return number_divisors_of_N
    number_of_divisors_of_N_that_are_multiple_of_K = number_of_divisors_of_N_that_are_multiples_of_K(K)
    return number_divisors_of_N - number_of_divisors_of_N_that_are_multiple_of_K

def number_of_divisors_of_N_that_are_multiples_of_K(K):
    if K > N:
        return 0
    number_of_divisors = 1
    # for every prime divisor in primes_map, we are finding the respective power of that divisor in K
    for key in primes_map.keys():
        count = 0
        while K % key == 0:
            count += 1
            K //= key
            if count > primes_map[key]:
                return 0
        # applying the number of divisors formula, we are finding the multiples of K that are divisors of N
        # for that particular prime factor
        number_of_divisors *= (primes_map[key] - count + 1)
    return number_of_divisors

def number_of_common_divisors(G):
    number_of_divisors = 1
    # for every prime divisor in primes_map, we are finding the respective power of that divisor in G
    for key in primes_map.keys():
        count = 0
        while G % key == 0:
            count += 1
            G //= key
        # applying the number of divisors formula, we are taking minimum to find the number of common divisors
        number_of_divisors *= (min(count, primes_map[key]) + 1)
    return number_of_divisors

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import sys

def main():
    global N
    N, Q = map(int, sys.stdin.readline().split())
    pre_computation(N)
    for q in range(Q):
        T, K = map(int, sys.stdin.readline().split())
        if T == 1:
            G = gcd(N, K)
            print(number_of_common_divisors(G))
        elif T == 2:
            print(number_of_divisors_of_N_that_are_multiples_of_K(K))
        else:
            print(number_of_divisors_of_N_that_are_not_multiples_of_K(K))

if __name__ == "__main__":
    main()