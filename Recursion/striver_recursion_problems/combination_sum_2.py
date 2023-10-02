def combinations2(arr, target):
    n = len(arr)
    ans = []
    def recur(idx, tar, ds):
        if tar == 0:
            ans.append(ds.copy())
            return
        if idx == n:
            return
        for i in range(idx, n):
            if (i > idx) and (arr[i] == arr[i - 1]):
                continue
            if arr[i] > tar:
                break
            ds.append(arr[i])
            recur(i + 1, tar - arr[i], ds)
            ds.pop()
    recur(0, target, [])
    return ans