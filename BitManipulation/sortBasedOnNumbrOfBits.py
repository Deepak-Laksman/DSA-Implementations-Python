import sys

def countBits(value):
    count = 0
    while value:
        value &= (value - 1)
        count += 1
    return count

def sortedArray(n, array):
    bitArray = []
    array.sort()
    for i in range(n):
        bitCount = countBits(array[i])
        bitArray.append([array[i], bitCount])
    bitArray.sort(key = lambda t: t[1])
    sortedResult = []
    for i in range(n):
        sortedResult.append(bitArray[i][0])
    return sortedResult

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(*sortedArray(n, array))

if __name__ == "__main__":
    main()