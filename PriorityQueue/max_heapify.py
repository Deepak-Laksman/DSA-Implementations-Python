# TC O(log(N)) SC O(log(N))
def max_heapify_algo(arr, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    n = len(arr)
    if l <= n - 1 and arr[l] > arr[largest]:
        largest = l
    if r <= n - 1 and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify_algo(arr, n, largest)

# TC O(log(N)) SC O(1)
def max_heapify_iter(arr, n, i):
    while True:
        l, r = 2 * i + 1, 2 * i + 2
        largest = i
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break