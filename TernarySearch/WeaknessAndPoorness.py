def costFunction(arr, val):
    tot = 0
    v1 = 0
    for i in range(len(arr)):
        tot += (arr[i] - val)
        if tot < 0:
            tot = 0
        v1 = max(v1, tot)
    tot = 0
    for i in range(len(arr)):
        tot += (val - arr[i])
        if tot < 0:
            tot = 0
        v1 = max(v1, tot)
    return v1

def minimumWeakness(arr):
    l, r = -10000, 10000
    dx = 0.000000000001
    while r - l > dx:
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
    n = int(input())
    arr = [int(a) for a in input().split()]
    print(minimumWeakness(arr))

if __name__ == "__main__":
    main()