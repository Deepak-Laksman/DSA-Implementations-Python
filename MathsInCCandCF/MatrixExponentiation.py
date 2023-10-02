identity = []

def mul(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def matrix_exponentiation(matrix, n):
    ans = identity
    while n > 0:
        if n & 1:
            ans = mul(ans, matrix)
        matrix = mul(matrix, matrix)
        n >>= 1
    return ans

import sys

def main():
    global identity
    n = int(sys.stdin.readline())
    identity = [[0 for i in range(n)] for j in range(n)]
    matrix = [[int(a) for a in range(n)] for j in range(n)]
    for i in range(n):
        identity[i][i] = 1
    result = matrix_exponentiation(matrix, n)
    print(result)

if __name__ == "__main__":
    main()