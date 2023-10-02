import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    # Degenerate Case
    if a == 0 and b == 0:
        if c == 0:
            print("Infinite Solutions")
        else:
            print("No Solutions")
    elif c % g:
        print("No Solutions")
    else:
        print("Solution exists")

if __name__ == "__main__":
    main()