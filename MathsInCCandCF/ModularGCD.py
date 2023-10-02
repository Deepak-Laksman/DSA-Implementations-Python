mod = 10 ** 9 + 7

import sys
import math

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        A, B, N = map(int, sys.stdin.readline().split())
        if A == B:
            return (pow(A, N, mod) + pow(B, N, mod)) % mod
        else:
            if A > B:
                x = A - B
            else:
                x = B - A
            a1 = pow(A, N, x)
            b1 = pow(B, N, x)
            print(math.gcd((a1 + b1) % x, x))

if __name__ == "__main__":
    main()