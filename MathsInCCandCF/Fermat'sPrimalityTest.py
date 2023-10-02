# We will check the equality of the expression a ^ (n - 1) % n = 1, where a in [2, n - 2]
# If its false, then n is not prime, else we try for another 4 values of a to confirm that n is prime.

def power(a, b, p):
    ans = 1
    while b > 0:
        if b & 1:
            ans = (ans * a) % p
        b >>= 1
        a = (a * a) % p
    return ans

from random import randint

def FermatPrimalityTest(n, iter = 5):
    if n <= 4:
        return n == 2 or n == 3
    for i in range(iter):
        a = randint(2, n - 2)
        if power(a, n - 1, n) != 1:
            return False
    return True

import sys

def main():
    n = int(sys.stdin.readline())
    print(FermatPrimalityTest(n))

if __name__ == "__main__":
    main()