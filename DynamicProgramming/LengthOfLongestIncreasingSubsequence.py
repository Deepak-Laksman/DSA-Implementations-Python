from bisect import bisect_left

arr = []

def lengthOfLIS(idx, prev, memo = None):
    global arr
    if memo is None:
        memo = {}
    if (idx, prev) in memo:
        return memo[(idx, prev)]
    if idx == len(arr):
        return 0
    take = 0
    if prev < arr[idx]:
        take = 1 + lengthOfLIS(idx + 1, arr[idx], memo)
    not_take = lengthOfLIS(idx + 1, prev, memo)
    memo[(idx, prev)] = max(take, not_take)
    return memo[(idx, prev)]

def lengthOfLISTabulation(arr):
    n = len(arr)
    dp = [1] * (n)
    maxi = float("-inf")
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(1 + dp[j], dp[i])
        maxi = max(maxi, dp[i])
    return maxi

def printLIS(arr):
    n = len(arr)
    dp = [1] * (n)
    hash = [i for i in range(n)]
    maxi, max_idx = float("-inf"), -1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    hash[i] = j
        if maxi < dp[i]:
            maxi = dp[i]
            max_idx = i
    lis = []
    lis.append(arr[max_idx])
    k = max_idx
    for i in range(maxi - 1):
        lis.append(arr[hash[k]])
        k = hash[k]
    print(lis[::-1])

def LISoptimal(arr):
    n = len(arr)
    endIdx = []
    endIdx.append(arr[0])
    length = 1
    j = 0
    for i in range(1, n):
        if arr[i] > endIdx[j]:
            endIdx.append(arr[i])
            length += 1
            j += 1
        else:
            endIdx[bisect_left(endIdx, arr[i], 0, len(endIdx) - 1)] = arr[i]
    return length
    

def main():
    global arr
    arr = [int(a) for a in input().split()]
    print((LISoptimal(arr)))

if __name__ == "__main__":
    main()