import heapq
import sys

def findMaximumValue(W, weights, values):
    wvTuple = list(zip(weights, values))
    wvTuple.sort(reverse = True, key = lambda t : t[1] / t[0])
    currentWeight = 0
    knapsack = 0
    i = 0
    n = len(weights)
    itemsTaken = []
    while i < n and currentWeight < W:
        if wvTuple[i][0] + currentWeight <= W:
            knapsack += wvTuple[i][1]
            currentWeight += wvTuple[i][0]
            itemsTaken.append([weights[i][0], weights[i][0]])
            if currentWeight == W:
                return knapsack
        else:
            temp = W - currentWeight
            ratio = weights[i][0] // temp
            if ratio > 0:
                currentWeight += ratio * weights[i][0]
                knapsack += ratio * weights[i][1]
                itemsTaken.append([weights[i][0], ratio])
                if W == currentWeight:
                    return knapsack
        i += 1
    return knapsack

def main():
    W = int(sys.stdin.readline())
    weights = [int(w) for w in sys.stdin.readline().split()]
    values = [int(v) for v in sys.stdin.readline().split()]
    print(findMaximumValue(W, weights, values))

if __name__ == "__main__":
    main()