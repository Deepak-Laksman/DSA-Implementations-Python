MAXN = 10 ** 6 + 1
phi = [0] * MAXN

def precomputation():
    phi[1] = 0
    for i in range(2, MAXN):
        phi[i] = i
    i = 2
    while i * i <= MAXN:
        if phi[i] == i:
            phi[i] = i - 1
            for j in range(i * i, MAXN, i):
                phi[j] //= i
                phi[j] *= (i - 1)
        i += 1

def gcd_count(x, N):
    return phi[N // x]

def total_gcd_sum(N):
    result = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            d1 = i
            d2 = N // i
            result += d1 * gcd_count(d1, N)
            if d1 != d2:
                result += d2 * gcd_count(d2, N)
        i += 1
    return result

import sys

def main():
    precomputation()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        N = int(sys.stdin.readline())
        print(total_gcd_sum(N))

if __name__ == "__main__":
    main()