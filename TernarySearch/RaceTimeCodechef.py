def costFunction(arr, time):
    maxtime = float("-inf")
    mintime = float("inf")
    for s, d in arr:
        maxtime = max(maxtime, s * time + d)
        mintime = min(mintime, s * time + d)
    return maxtime - mintime

# Binary Search
def minimumDifferenceBinary(arr, k):
    l, r = 0, k
    dx = 0.000000001
    while r - l > 0.000000001:
        mid = l + (r - l) / 2
        f1 = costFunction(arr, mid)
        f2 = costFunction(arr, mid + dx)
        if f1 > f2:
            l = mid + dx
        elif f2 > f1:
            r = mid
        else:
            return f1
    return costFunction(arr, l)

# Ternary Search
def minimumDifferenceTernary(arr, k):
    l, r = 0, k
    while r - l > 0.000000001:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        f1 = costFunction(arr, m1)
        f2 = costFunction(arr, m2)
        if f1 > f2:
            l = m1
        else:
            r = m2
    return costFunction(arr, l)

def main():
    n, k = map(int ,input().split())
    arr = []
    for _ in range(n):
        s, d = map(int, input().split())
        arr.append([s, d])
    print("{:.6f}".format(minimumDifferenceBinary(arr, k)))

if __name__ == "__main__":
    main()
