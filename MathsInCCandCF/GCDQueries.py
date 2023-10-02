# You are given an array of size N, and Q queries with two values L and R.
# You have to find the gcd of all the numbers excluding the range L ... R the array.

# Getting WA
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

prefix_gcd = [0] * 100001
suffix_gcd = [0] * 100001

def calc_prefix_suffix(array, N):
    for i in range(N):
        prefix_gcd[i] = gcd(prefix_gcd[i - 1], array[i])
    for i in range(N - 1, 0, -1):
        suffix_gcd[i] = gcd(suffix_gcd[i + 1], array[i])

def gcd_in_range(L, R):
    return gcd(prefix_gcd[L - 1], suffix_gcd[R + 1])

import sys

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        N, Q = map(int, sys.stdin.readline().split())
        array = [int(a) for a in sys.stdin.readline().split()]
        array.insert(0, 0)
        calc_prefix_suffix(array, N + 1)
        for q in range(Q):
            L, R = map(int, sys.stdin.readline().split())
            print(gcd_in_range(L, R))

if __name__ == "__main__":
    main()