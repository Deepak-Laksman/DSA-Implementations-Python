import sys

def allSubsets(n, setInput):
    lastNum = 1 << n
    subsets = [[],]
    for i in range(1, lastNum):
        currentSet = []
        for j in range(32):
            bitmask = 1 << j
            if i & bitmask:
                currentSet.append(setInput[j])
        subsets.append(currentSet)
    return subsets


def main():
    n = int(sys.stdin.readline())
    setInput = [int(a) for a in sys.stdin.readline().split()]
    print(*allSubsets(n, setInput))

if __name__ == "__main__":
    main()