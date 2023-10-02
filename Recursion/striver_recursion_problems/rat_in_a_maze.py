def rat_maze(mat, n):
    paths = []
    visited = [[0 for i in range(n)] for j in range(n)]
    if mat[0][0] == 0:
        return [-1]
    visited[0][0] = 1
    def is_safe(x, y, visited):
        if not (0 <= x < n and 0 <= y < n):
            return False
        if visited[x][y] or mat[x][y]:
            return False
        return True

    def backtrack(x, y, path, visited):
        nonlocal paths
        if x > n - 1 or y > n - 1:
            return 
        if x == n - 1 and y == n - 1:
            if mat[x][y]:
                paths.append("".join(path))
            return
        # go upwards
        if is_safe(x - 1, y, visited):
            path.append("U")
            visited[x - 1][y] = 1
            backtrack(x - 1, y, path, visited)
            path.pop()
            visited[x - 1][y] = 0
        # go downwards
        if is_safe(x + 1, y, visited):
            path.append("D")
            visited[x + 1][y] = 1
            backtrack(x + 1, y, path, visited)
            path.pop()
            visited[x + 1][y] = 0
        # go left
        if is_safe(x, y - 1, visited):
            path.append("L")
            visited[x][y - 1] = 1
            backtrack(x, y - 1, path, visited)
            path.pop()
            visited[x][y - 1] = 0
        # go right
        if is_safe(x, y + 1, visited):
            path.append("R")
            visited[x][y + 1] = 1
            backtrack(x, y + 1, path, visited)
            path.pop()
            visited[x][y + 1] = 0
    backtrack(0, 0, [], visited)
    if len(paths) == 0:
        return [-1]
    return paths

