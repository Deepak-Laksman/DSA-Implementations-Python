import sys

def totalHammingDistance(first, second):
    distance = 0
    while first and second:
        if (first & 1) != (second & 1):
            distance += 1
        first >>= 1
        second >>= 1
    while first:
        if (first & 1):
            distance += 1
        first >>= 1
    while second:
        if (second & 1):
            distance += 1
        second >>= 1
    return distance

def main():
    first, second = map(int ,sys.stdin.readline().split())
    print(totalHammingDistance(first, second))

if __name__ == "__main__":
    main()