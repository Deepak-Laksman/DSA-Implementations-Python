import sys

def findSetBit(n):
    i = 0
    while (n & 1) == 0:
        i += 1
        n >>= 1
    return i

def findTwoUniqueNumbers(n, array):
    xor = 0
    for i in range(n):
        xor ^= array[i]
    setBitPosition = findSetBit(xor)
    bitmask = (1 << setBitPosition)
    firstNumber, secondNumber = 0, 0
    for i in range(n):
        if (bitmask & array[i]):
            firstNumber ^= array[i]
        else:
            secondNumber ^= array[i]
    return firstNumber, secondNumber
    

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(findTwoUniqueNumbers(n, array))

if __name__ == "__main__":
    main()