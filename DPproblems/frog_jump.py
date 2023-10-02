def frog_jumps(arr):
    n = len(arr)
    if n == 1:
        return 0
    prev2, prev = 0, abs(arr[1] - arr[0])
    for i in range(3, n + 1):
        prev2, prev = prev, min(prev + abs(arr[i - 1] - arr[i - 2]), prev2 + abs(arr[i - 1] - arr[i - 3]))
    return prev