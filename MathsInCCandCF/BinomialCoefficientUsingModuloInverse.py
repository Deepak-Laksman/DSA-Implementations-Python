mod = 10 ** 9 + 7

MAXN = 10 ** 6 + 1
factorial = [1] * MAXN

def pre_computation():
    for i in range(2, MAXN):
        factorial[i] = (factorial[i - 1] * i) % mod

def inverse(a):
    return pow(a, mod - 2, mod)

def binomial_coefficient(n, r):
    denom = inverse(factorial[r])
    denom = (denom * inverse(factorial[n - r])) % mod
    answer = (factorial[n] * denom) % mod
    return answer

import sys

def main():
    pre_computation()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        n, r = map(int, sys.stdin.readline().split())
        if r > n:
            print(0)
        else:
            print(binomial_coefficient(n, r))

if __name__ == "__main__":
    main()