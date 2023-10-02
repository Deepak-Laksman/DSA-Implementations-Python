def is_safe(row, col, matrix):
    # upper left diagonal
    x, y = row - 1, col - 1
    while x >=0 and y >= 0:
        if matrix[x][y] == 'Q':
            return False
        x -= 1
        y -= 1
    # upper right diagonal
    x, y = row - 1, col + 1
    while x >= 0 and y < len(matrix):
        if matrix[x][y] == 'Q':
            return False
        x -= 1
        y += 1
    # up in same column
    x = row - 1
    while x >= 0:
        if matrix[x][col] == 'Q':
            return False
        x -= 1
    return True

def n_queens(n):
    matrix = [['.' for i in range(n)] for j in range(n)]
    arrangements = []
    def backtrack(mat, row):
        nonlocal n
        if row == n:
            temp = []
            for r in mat:
                temp.append("".join(r))
            arrangements.append(temp)
            return
        for col in range(n):
            if is_safe(row, col, mat):
                mat[row][col] = 'Q'
                backtrack(mat, row + 1)
                mat[row][col] = '.'
    return arrangements