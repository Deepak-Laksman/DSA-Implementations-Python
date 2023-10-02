def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def find_any_solution(a, b, c):
    g, x1, y1 = extended_euclidean(abs(a), abs(b))
    if c % g:
        return False, 0, 0

    x = x1 * (c // g)
    y = y1 * (c // g)

    if a < 0:
        x = -x
    if b < 0:
        y = -y
    return True, x, y

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    boolean, x, y = find_any_solution(a, b, c)
    if boolean:
        print(x, y)
    else:
        print("No Solution Exists")

if __name__ == "__main__":
    main()