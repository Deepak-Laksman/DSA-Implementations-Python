# Codeforces - Labyrinth

from collections import deque

def main():
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    x, y = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    queue = deque()
    queue.append([r - 1, c - 1, x, y])
    ans = 0
    visited = [[0] * m for i in range(n)]
    while len(queue):
        t = queue.popleft()
        tx = t[0]
        ty = t[1]
        ta = t[2]
        tb = t[3]
        if visited[tx][ty] or grid[tx][ty] != ".":
            continue
        ans += 1
        visited[tx][ty] = 1
        if tx + 1 < n:
            queue.appendleft([tx + 1, ty, ta, tb])
        if tx - 1 >= 0:
            queue.appendleft([tx - 1, ty, ta, tb])
        if ty + 1 < m and tb > 0:
            queue.append([tx, ty + 1, ta, tb - 1])
        if ty - 1 >= 0 and ta > 0:
            queue.append([tx, ty - 1, ta - 1, tb])
    print(ans)

if __name__ == "__main__":
    main()
