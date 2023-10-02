def numberOfPath (N, K, arr):
    def recur(i, j, k):
        if k < 0:
            return 0
        if i == N or j == N:
            return 0
        if i == N - 1 and j == N - 1:
            if k == 0:
                return 1
            else:
                return 0
        elif i == N - 1:
            return recur(i, j + 1, k - arr[i][j + 1])
        elif j == N - 1:
            return recur(i + 1, j, k - arr[i + 1][j])
        else:
            return recur(i + 1, j, k - arr[i + 1][j]) + recur(i, j + 1, k - arr[i][j + 1])
    return recur(0, 0, K - arr[0][0])

ans = 0

def numberOfPaths(n, k, arr):
    def recur(i, j, k):
        global ans
        if i == n or j == n:
            return 
        k -= arr[i][j]
        if k < 0:
            return 
        if i == n - 1 and j == n - 1 and k == 0:
            ans += 1
            return
        recur(i, j + 1, k, ans + 1)
        recur(i + 1, j, k, ans + 1)
    recur(0, 0, k)
    return ans

    

def main():
    k = int(input())
    n = int(input())
    arr = [int(a) for a in input().split()]
    mat = []
    for i in range(0, len(arr), n):
        mat.append(arr[i: i + n])
    print(numberOfPaths(n, k, mat))

if __name__ == "__main__":
    main()