def is_safe(row, col, val, board):
    for i in range(9):
        if board[row][i] == val:
            return False
        if board[i][col] == val:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val:
            return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                continue
            for val in range(1, 10):
                if is_safe(row, col, val, board):
                    board[row][col] = val
                    if solve(board):
                        return True
                    board[row][col] = '.'
            return False
    return True