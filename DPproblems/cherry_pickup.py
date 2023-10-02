def pickup(i, j1, j2, m, n, mat, memo = None):
    if memo is None:
        memo = {}
    if j1 < 0 or j1 > n - 1 or j2 < 0 or j2 > n - 1:
        return float("-inf")
    if i == m - 1:
        if j1 == j2:
            return mat[i][j1]
        else:
            return mat[i][j1] + mat[i][j2]
    if (i, j1, j2) in memo:
        return memo[(i, j1, j2)]
    maxi = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if j1 + x == j2 + y:
                maxi = max(maxi, mat[i][j1 + x] + pickup(i + 1, j1 + x, j2 + y, m, n, mat, memo))
            else:
                maxi = max(maxi, mat[i][j1 + x] + mat[i][j2 + y] + pickup(i + 1, j1 + x, j2 + y, m, n, mat, memo))
    memo[(i, j1, j2)] = maxi
    return memo[(i, j1, j2)]