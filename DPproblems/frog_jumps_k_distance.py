def frog_jumps_k_distance(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = abs(arr[1] - arr[0])
    for i in range(3, n + 1):
        mini = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                mini = min(mini, dp[i - j] + abs(arr[i - 1] - arr[i - j - 1]))
            else:
                break
        dp[i] = mini
    return dp[n]

def frog_jumps_k_distance_space_optimized(arr, k):
    n = len(arr)
    prev = [0] * (k + 1)
    prev[1] = 0
    prev[2] = abs(arr[1] - arr[0])
    for i in range(3, k + 1):
        mini = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                mini = min(mini, prev[i - j] + abs(arr[i - 1] - arr[i - j]))
            else:
                break
        prev[i] = mini
    
    for i in range(k + 1, n + 1):
        mini = float("inf")
        for j in range(1, k + 1):
            print(i, j)
            if i - j >= 0:
                mini = min(mini, prev[i - j] + abs(arr[i - 1] - arr[i - j]))
            else:
                break
        for i in range(1, k):
            prev[i] = prev[i + 1]
        prev[k] = mini
    return prev[k]

def main():
    k = int(input())
    arr = [int(a) for a in input().split()]
    print(frog_jumps_k_distance(arr, k))

if __name__ == "__main__":
    main()