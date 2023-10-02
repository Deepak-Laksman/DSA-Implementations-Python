from math import sin, pi

def costFunction(a, b, x):
    return (x * x + a * x + b) / sin(x)

def findMinimumBinary(a, b):
    l, r = 0, pi / 2
    dx = 0.000001
    while r - l > dx:
        mid = l + (r - l) / 2
        c1 = costFunction(a, b, mid)
        c2 = costFunction(a, b, mid + dx)
        if c1 > c2:
            l = mid + dx
        elif c2 > c1:
            r = mid
        else:
            return c1
    return costFunction(a, b, l)

def findMinimumTernary(a, b):
    l, r = 0, pi / 2
    while r - l > 0.000001:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        c1 = costFunction(a, b, m1)
        c2 = costFunction(a, b, m2)
        if c1 > c2:
            l = m1 
        elif c2 > c1:
            r = m2
        else:
            l, r = m1, m2
    return costFunction(a, b, l)

def main():
    tc = int(input())
    for _ in range(tc):
        a, b = map(float, input().split())
        print(findMinimumBinary(a, b))
        
if __name__ == "__main__":
    main()