MAXN = 10 ** 6 + 1
spf = [-1] * MAXN

def prime_factorization_using_sieve():
    for i in range(2, MAXN):
        if spf[i] == -1:
            spf[i] = i
            for j in range(i * i, MAXN, i):
                if spf[j] == -1:
                    spf[j] = i

def prime_factors(n):
    if n == 1:
        print("No prime factors for 1")
    else:
        factors = []
        while spf[n] != -1:
            factors.append(spf[n])
            n = n // spf[n]
        return factors

import sys

def main():
    prime_factorization_using_sieve()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        n = int(sys.stdin.readline())
        print(*prime_factors(n))

if __name__ == "__main__":
    main()
