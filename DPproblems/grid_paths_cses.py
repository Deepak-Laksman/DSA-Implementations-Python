def main():
    modulo = 10 ** 9 + 7
    n = int(input())
    grid = []
    for _ in range(n):
        row = input()
        temp = []
        for char in row:
            temp.append(char)
        grid.append(temp)
    if grid[0][0] == ".":
        grid[0][0] = 1
    else:
        print(0)
        return
    for i in range(1, n):
        if grid[i][0] == ".":
            grid[i][0] = grid[i - 1][0]
        else:
            grid[i][0] = 0
        if grid[0][i] == ".":
            grid[0][i] = grid[0][i - 1]
        else:
            grid[0][i] = 0
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] == ".":
                grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) % modulo
            else:
                grid[i][j] = 0
    print(grid[n - 1][n - 1])
    
if __name__ == "__main__":
    main()