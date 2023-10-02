def cross_product(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x * x + y * y

def jarvis_march_for_convex_hull(points, n):
    hull = []
    # to get left most point
    start = 0
    for i in range(1, n):
        if (points[i][0] < points[start][0]) or (points[i][0] < points[start][0] and points[i][1] < points[start][1]):
            start = i

    hull.append(points[i])

    # getting point that is most clockwise and farthest from current point
    while True:
        pt = 0
        for i in range(n):
            if points[i] == hull[-1]:
                continue
            z_axis = cross_product(hull[-1], points[pt], points[i])
            # if z_axis == -1, then the point is clockwise with respect to pt and hull[-1]
            # if z_axis == 0, then the point is collinear, so we need to find the farthest point 
            if (z_axis == -1) or (z_axis == 0 and distance(points[i], hull[-1]) > distance(points[pt], hull[-1])):
                pt = i
        if points[pt] == hull[0]:
            break
        else:
            hull.append(points[pt])

    return hull

def main():
    n = int(input())
    points = []
    for _ in range(n):
        u, v = map(int, input().split())
        points.append([u, v])
    hull = jarvis_march_for_convex_hull(points, n)
    p1, p2 = None, None
    cur_max_distance = 0
    for i in range(len(hull)):
        for j in range(i + 1, len(hull)):
            if distance(hull[i], hull[j]) > cur_max_distance:
                p1, p2 = hull[i], hull[j]
    print(cur_max_distance, p1, p2)

if __name__ == "__main__":
    main()