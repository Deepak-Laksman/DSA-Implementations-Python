import math
import sys

primes_list = []

def prime_sieve():
    MAXN = 10 ** 6 + 1
    primes = [True] * MAXN
    primes[0] = primes[1] = False
    i = 2
    while i * i <= MAXN:
        if primes[i]:
            for j in range(i * i, MAXN, i):
                primes[j] = False
        i += 1
    for i in range(2, MAXN):
        if primes[i]:
            primes_list.append(i)
    del primes

def segmented_sieve(L, R):
    if L == 1:
        L += 1

    primes = [True] * (R - L + 1)

    for prime in primes_list:
        if prime * prime <= R:
            start_value = (L // prime) * prime

            if start_value < L:
                start_value += prime

            for j in range(start_value, R + 1, prime):
                if j != prime:
                    primes[j - L] = False

    for i in range(L, R + 1):
        if primes[i - L]:
            print(i, end = " ")

    print()

def main():
    prime_sieve()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        L, R = map(int, sys.stdin.readline().split())
        segmented_sieve(L, R)

if __name__ == "__main__":
    main()