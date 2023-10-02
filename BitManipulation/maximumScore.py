import sys

def rowWiseToggle(m, n, grid, i):
    for j in range(n):
        grid[i][j] ^= 1
    return grid

def columnWiseToggle(m, n, grid, i):
    for j in range(m):
        grid[j][i] ^= 1
    return grid

def calculateScore(m, n, grid):
    totalScore = 0
    for i in range(m):
        for j in range(n):
            totalScore += grid[i][j] * (1 << (n - j - 1))
    return totalScore

def maxScore(m, n, grid):
    for i in range(m):
        if grid[i][0] != 1:
            grid = rowWiseToggle(m, n, grid, i)
    for i in range(n):
        colSum = 0
        for j in range(m):
            colSum += grid[j][i]
        if m - colSum > colSum :
            grid = columnWiseToggle(m, n, grid, i)
    return calculateScore(m, n, grid)

def main():
    m, n = map(int, sys.stdin.readline().split())
    grid = [[int(a) for a in sys.stdin.readline().split()] for j in range(m)]
    print(maxScore(m, n, grid))

if __name__ == "__main__":
    main()