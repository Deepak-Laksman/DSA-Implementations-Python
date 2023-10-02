def combinations(arr, target):
    ans = []
    n = len(arr)
    def recur(idx, tar, ds):
        nonlocal ans, n
        if tar == 0:
            ans.append(ds.copy())
            return
        if idx == n:
            return
        if arr[idx] <= tar:
            ds.append(arr[idx])
            recur(idx, tar - arr[idx], ds)
            ds.pop()
        recur(idx + 1, tar, ds)
    recur(0, target, [])
    return ans