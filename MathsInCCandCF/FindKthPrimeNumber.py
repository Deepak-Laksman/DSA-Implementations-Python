# Problem

# Given a range of numbers, for every query k, find the kth prime number in that range

MAXN = 90000001
primes = [True] * MAXN
primes_list = []

def prime_sieve():
    primes[0] = primes[1] = False
    i = 2
    while i * i <= MAXN:
        if primes[i]:
            primes_list.append(i)
            for j in range(i * i, MAXN, i):
                primes[j] = False
        i += 1
    for i in range(MAXN):
        if primes[i]:
            primes_list.append(i)

import sys

def main():
    prime_sieve()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        k = int(sys.stdin.readline())
        print(primes_list[k - 1])

if __name__ == "__main__":
    main()