from math import sqrt

def costFunction(arr, point):
    cost = sqrt((arr[0] - point) ** 2 + arr[1] ** 2) / arr[-2] + sqrt((arr[2] - point) ** 2 + arr[3] ** 2) / arr[-1]
    return cost

# missing some precisions
def minimumTimeBinary(arr):
    l, r = arr[0], arr[2]
    dx = 0.00001
    if arr[0] > arr[2]:
        l, r = r, l
    while r - l > dx:
        mid = l + (r - l) / 2
        c1 = costFunction(arr, mid)
        c2 = costFunction(arr, mid + dx)
        if c1 > c2:
            l = mid + dx
        elif c2 > c1:
            r = mid
        else:
            return c1
    return costFunction(arr, l)

def minimumTimeTernary(arr):
    l, r = arr[0], arr[2]
    if arr[0] > arr[2]:
        l, r = r, l
    while r - l > 0.00001:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        c1 = costFunction(arr, m1)
        c2 = costFunction(arr, m2)
        if c1 > c2:
            l = m1
        elif c2 > c1:
            r = m2
        else:
            l, r = m1, m2
    return costFunction(arr, l)

def main():
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        ans = minimumTimeBinary(arr)
        print("{0:.5f}".format(ans))

if __name__ == "__main__":
    main()