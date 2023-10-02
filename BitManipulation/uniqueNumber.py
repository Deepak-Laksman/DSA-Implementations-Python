import sys

def findUniqueNumber(n, array):
    xor = 0
    for i in range(n):
        xor ^= array[i]
    return xor

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(findUniqueNumber(n, array))

if __name__ == "__main__":
    main()