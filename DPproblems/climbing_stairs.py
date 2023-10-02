def climb(n):
    prev, prev2 = 1, 1
    for i in range(2, n + 1):
        prev2, prev = prev, prev + prev2
    return prev