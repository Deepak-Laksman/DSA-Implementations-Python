import sys

def minimumRefills(L, A, B, gasStations):
    refills = 0
    start = A
    n = len(gasStations)
    previous = A
    currentFuel = L
    i = 0
    while i < n:
        distance = gasStations[i] - start
        if distance < currentFuel:
            previous = gasStations[i]
            currentFuel -= distance
        elif distance == currentFuel:
            refills += 1
            start = gasStations[i]
            currentFuel = L
        else:
            refills += 1
            start = previous
            currentFuel = L
        i += 1
    if currentFuel >= B - start:
        return refills
    else:
        if currentFuel != L:
            if L >= B - gasStations[n - 1]:
                return refills + 1
        return "IMPOSSIBLE"

# Different Approach

# Time complexity is O(n) as currentRefills variable changes from 0 to n only atmost
def minimumRefills2(L, A, B, gasStations):
    numRefills = 0
    currentRefills = 0
    while currentRefills <= B:
        lastRefill = currentRefills
        while currentRefills < B and gasStations[currentRefills + 1] - gasStations[lastRefill] <= L:
            currentRefills += 1
        if currentRefills == lastRefill:
            return "IMPOSSIBLE"
        if currentRefills <= B:
            numRefills += 1
    return numRefills

sys.stdin, sys.stdout = open("input.txt", "r"), open("output.txt", "w")

def main():
    L = int(sys.stdin.readline())  # Maximum possible distance that can be travelled with fully filled tank
    A, B = map(int , sys.stdin.readline().split())
    gasStations = [int(g) for g in sys.stdin.readline().split()]
    print(minimumRefills(L, A, B, gasStations))

if __name__ == "__main__":
    main()