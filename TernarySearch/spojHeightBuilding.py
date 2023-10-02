def costFunction(heights, costs, height):
    cost = 0
    for i in range(len(heights)):
        cost += abs(heights[i] - height) * costs[i]
    return cost

# Binary Search
def findHeightBinary(heights, costs):
    l, r = min(heights), max(heights)
    while l < r:
        mid = l + (r - l) // 2
        c1 = costFunction(heights, costs, mid)
        c2 = costFunction(heights, costs, mid + 1)
        if c1 > c2:
            l = mid + 1
        elif c2 > c1:
            r = mid 
        else:
            return c1
    return costFunction(heights, costs, l)

# Ternary Search
def findHeightTernary(heights, costs):
    l, r = min(heights), max(heights)
    while l < r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        c1 = costFunction(heights, costs, m1)
        c2 = costFunction(heights, costs, m2)
        if c1 > c2:
            l = m1 + 1
        elif c2 > c1:
            r = m2 - 1 
        else:
            l, r = m1 + 1, m2 - 1
    return costFunction(heights, costs, l)

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        heights = [int(a) for a in input().split()]
        costs = [int(a) for a in input().split()]
        print(findHeightBinary(heights, costs))

if __name__ == "__main__":
    main()