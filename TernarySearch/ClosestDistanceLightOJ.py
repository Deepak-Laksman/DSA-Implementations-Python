from math import sqrt

def distance(a, b, c, d):
    return sqrt((a - c) ** 2 + (b - d) ** 2)

# Ternary Search
def minimumDistance(arr):
    l1, r1 = arr[0], arr[1]
    l2, r2 = arr[2], arr[3]
    l3, r3 = arr[4], arr[5]
    l4, r4 = arr[6], arr[7]
    while distance(l1, r1, l2, r2) > 0.000001:
        mx1, my1 = l1 + (l2 - l1) / 3, r1 + (r2 - r1) / 3
        mx2, my2 = l2 - (l2 - l1) / 3, r2 - (r2 - r1) / 3
        mx3, my3 = l3 + (l4 - l3) / 3, r3 + (r4 - r3) / 3
        mx4, my4 = l4 - (l4 - l3) / 3, r4 - (r4 - r3) / 3
        c1 = distance(mx1, my1, mx3, my3)
        c2 = distance(mx2, my2, mx4, my4)
        if c1 > c2:
            l1, r1 = mx1, my1
            l3, r3 = mx3, my3
        elif c2 > c1:
            l2, r2 = mx2, my2
            l4, r4 = mx4, my4
        else:
            l1, r1 = mx1, my1
            l2, r2 = mx2, my2
            l3, r3 = mx3, my3
            l4, r4 = mx4, my4
    return min(distance(l1, r1, l3, r3), distance(l2, r2, l4, r4))

def main():
    tc = int(input())
    for _ in range(tc):
        arr = [float(a) for a in input().split()]
        distance = minimumDistance(arr)
        if distance - int(distance) > 0.000001:
            print("Case " + str(_ + 1) + ":", distance)
        else:
            print("Case " + str(_ + 1) + ":", int(distance))
            

if __name__ == "__main__":
    main()