# TC O(log(N)) SC O(log(N))
def min_heapify_algo(arr, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    n = len(arr)
    if l <= n - 1 and arr[l] < arr[smallest]:
        smallest = i
    if r <= n - 1 and arr[r] < arr[smallest]:
        smallest = i
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify_algo(arr, n, smallest) 

# TC O(log(N)) SC O(1)
def min_heapify_iter(arr, n, i):
    while True:
        l, r = 2 * i + 1, 2 * i + 2
        smallest = i
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
        else:
            break