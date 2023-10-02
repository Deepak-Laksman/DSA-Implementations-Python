from math import sqrt

def costFunction(points, point):
    cost = 0
    for x, y in points:
        cost = max(cost, sqrt((x - point) * (x - point) + y * y))
    return cost

# Binary Search
def minimumTimeAndPointBinary(points):
    l, r = -200000, 200000
    dx = 0.00001
    while r - l > dx:
        mid = l + (r - l) / 2
        c1 = costFunction(points, mid)
        c2 = costFunction(points, mid + dx)
        if c1 > c2:
            l = mid + dx
        elif c2 > c1:
            r = mid
        else:
            return mid, c1
    return l, costFunction(points, l)

# Ternary Search
def minimumTimeAndPoint(points):
    l, r = -200000, 200000
    while r - l > 0.00001:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        c1 = costFunction(points, m1)
        c2 = costFunction(points, m2)
        if c1 > c2:
            l = m1
        elif c2 > c1:
            r = m2
        else:
            l, r = m1, m2
    return l, costFunction(points, l)

def main():
    n = int(input())
    points = []
    for _ in range(n):
        points.append([float(a) for a in input().split()])
    print(*minimumTimeAndPoint(points))

if __name__ == "__main__":
    main()