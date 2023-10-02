# Codechef - SNSocialization

from collections import deque

def main():
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        grid = []
        for __ in range(n):
            grid.append(list(map(int, input().split())))
        max_val = float("-inf")
        for i in range(n):
            for j in range(m):
                if grid[i][j] > max_val:
                    max_val = grid[i][j]
        queue = deque()
        visited = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == max_val:
                    queue.append((i, j, 0))
                    visited[i][j] = 1
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)] 
        ans = 0
        while len(queue):
            x, y, t = queue.popleft()
            ans = max(ans, t)
            for k, l in dir:
                if not (0 <= x + k < n and 0 <= y + l < m):
                    continue
                if visited[x + k][y + l]:
                    continue
                visited[x + k][y + l] = 1
                queue.append((x + k, y + l, t + 1))
        print(ans)

if __name__ == "__main__":
    main()

