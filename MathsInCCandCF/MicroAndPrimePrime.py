MAXN = 10 ** 6 + 1
primes = [True] * MAXN
prefix_primes = [0] * MAXN

def prime_sieve():
    primes[0] = primes[1] = False
    i = 2
    while i * i <= MAXN:
        if primes[i]:
            prefix_primes[i] = prefix_primes[i - 1] + 1
            for j in range(i * i, MAXN, i):
                primes[j] = False
        else:
            prefix_primes[i] = prefix_primes[i - 1]
        i += 1

    count = 0
    for i in range(MAXN):
        if primes[i]:
            count += 1
        if primes[count]:
            prefix_primes[i] = 1

    for i in range(1, MAXN):
        prefix_primes[i] += prefix_primes[i - 1]

def prime_primes(L, R):
    return prefix_primes[R] - prefix_primes[L - 1]

import sys

def main():
    prime_sieve()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        L, R = map(int, sys.stdin.readline().split())
        print(prime_primes(L, R))

if __name__ == "__main__":
    main()