import sys

def findUniqueNumber(n, array):
    bitArray = [0] * (32)
    for i in range(n):
        for j in range(32):
            bitmask = (1 << j)
            if array[i] & bitmask:
                bitArray[j] += 1
    answer = 0
    for i in range(32):
        answer += (bitArray[i] % 3) * (1 << i)
    return answer

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(findUniqueNumber(n, array))

if __name__ == "__main__":
    main()