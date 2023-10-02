def logic_space_optimized(n, mat):
    a, b, c = mat[0][0], mat[0][1], mat[0][2]
    for i in range(1, n):
        a, b, c = max(b, c) + mat[i][0], max(a, c) + mat[i][1], max(a, b) + mat[i][2]
    return max(a, b, c)

def main():
    n =  int(input())
    mat = []
    for _ in range(n):
        l = list(map(int, input().split()))
        mat.append(l)
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][0] = mat[0][0]
    dp[0][1] = mat[0][1]
    dp[0][2] = mat[0][2]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1] + mat[i][0], dp[i - 1][2] + mat[i][0])
        dp[i][1] = max(dp[i - 1][0] + mat[i][1], dp[i - 1][2] + mat[i][1])
        dp[i][2] = max(dp[i - 1][0] + mat[i][2], dp[i - 1][1] + mat[i][2])
    print(logic_space_optimized(n, mat))

if __name__ == "__main__":
    main()