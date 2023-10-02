def costFunction(heights, a, r, m, height):
    sum1 = 0
    sum2 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(len(heights)):
        if heights[i] < height:
            cnt1 += 1
            sum1 += heights[i]
        elif heights[i] > height:
            cnt2 += 1
            sum2 += heights[i]
    extra = sum2 - cnt2 * height
    req = cnt1 * height - sum1
    cost = 0
    if m <= a + r:
        if extra >= req:
            cost += req * m
            extra -= req
            cost += extra * r
            extra = 0
        else:
            cost += extra * m
            req -= extra
            cost += req * a
            req = 0
    else:
        cost += extra * r
        cost += req * a
    return cost

# Binary Search
def minimumCostBinary(a, rr, m, heights):
    l, r = 0, 10 ** 9 
    while l < r:
        mid = l + (r - l) // 2
        c1 = costFunction(heights, a, rr, m, mid)
        c2 = costFunction(heights, a, rr, m, mid + 1)
        if c1 > c2:
            l = mid +1
        elif c2 > c1:
            r = mid
        else:
            return c1
    return costFunction(heights, a, rr, m, l)

# Ternary Search
def minimumCostTernary(a, rr, m, heights):
    l, r = 0, 10 ** 9
    while l < r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        c1 = costFunction(heights, a, rr, m, m1)
        c2 = costFunction(heights, a, rr, m, m2)
        if c1 > c2:
            l = m1 + 1
        elif c2 > c1:
            r = m2 - 1
        else:
            l, r = m1 + 1, m2 - 1
    return costFunction(heights, a, rr, m, l)

def main():
    n, a, r, m = map(int, input().split())
    heights = [int(a) for a in input().split()]
    print(minimumCostBinary(a, r, m, heights))

if __name__ == "__main__":
    main()