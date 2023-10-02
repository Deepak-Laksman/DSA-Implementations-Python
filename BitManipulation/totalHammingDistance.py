import sys

def calculateHammingDistance(n, array):
    totalDistance = 0
    countOfZeroes = 0
    for i in range(32):
        countOfZeroes = 0
        for j in range(n):
            if (array[j] & (1 << i)) == 0:
                countOfZeroes += 1
        if (n - countOfZeroes != 0) and (n - countOfZeroes != n):
            totalDistance += max(n - countOfZeroes, countOfZeroes)
    return totalDistance

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(calculateHammingDistance(n, array))

if __name__ == "__main__":
    main()