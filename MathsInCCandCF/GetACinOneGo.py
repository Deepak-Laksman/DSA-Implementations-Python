import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        a, b = map(int, sys.stdin.readline().split())
        g = gcd(a, b)
        if a == 1 or b == 1:
            print(0)
        elif g != 1:
            print(a * b - a - b + 1)
        else:
            print(-1)

if __name__ == "__main__":
    main()