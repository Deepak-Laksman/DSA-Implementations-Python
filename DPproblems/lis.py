def lis_memo(i, arr, prev, dp):
    if i == len(arr):
        return 0
    if dp[i][prev + 1] != -1:
        return dp[i][prev] 
    take = 0
    if prev == -1 or arr[i] > arr[prev]:
        take = 1 + lis_memo(i + 1, arr, i, dp)
    not_take = lis_memo(i + 1, arr, prev, dp)
    dp[i][prev + 1] = max(take, not_take)
    return dp[i][prev + 1]

def lis(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

def print_lis(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    h = {}
    maxi, max_idx = dp[0], 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[i] < 1 + dp[j]:
                    h[i] = j
                    dp[i] = 1 + dp[j]
        if dp[i] > maxi:
            maxi = dp[i]
            max_idx = i
    j = max_idx
    lis = []
    while True:
        lis.append(arr[j])
        if j not in h:
            break
        j = h[j]
    lis.reverse()
    return lis

def binary_search(self, s, e, prev, target):
        ans = len(prev) + 1
        while s <= e:
            mid = s + (e - s) // 2
            if prev[mid] == target:
                return mid
            elif prev[mid] < target:
                s = mid + 1
            else:
                ans = min(ans, mid)
                e = mid - 1
        return ans

# O(log(N))
def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [nums[0]]
        length = 1
        for i in range(1, n):
            if nums[i] > prev[-1]:
                prev.append(nums[i])
                length += 1
            else:
                idx = self.binary_search(0, len(prev) - 1, prev, nums[i])
                prev[idx] = nums[i]
        return length

def main():
    arr = [int(a) for a in input().split()]
    print(*print_lis(arr))

if __name__ == "__main__":
    main()