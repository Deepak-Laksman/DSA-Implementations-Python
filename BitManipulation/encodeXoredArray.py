import sys

def findOriginalArray(n, xorArray, first):
    original = [0] * (n + 1)
    original[0] = first
    for i in range(n):
        original[i + 1] = xorArray[i] ^ original[i]
    return original

def main():
    n, first = map(int, sys.stdin.readline().split())
    xorArray = [int(a) for a in sys.stdin.readline().split()]
    print(*findOriginalArray(n, xorArray, first))

if __name__ == "__main__":
    main()