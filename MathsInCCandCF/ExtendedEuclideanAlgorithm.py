def extendedEuclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extendedEuclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
