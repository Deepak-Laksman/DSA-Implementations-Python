from build_max_heap import build_max_heap
from max_heapify import max_heapify_iter

from build_min_heap import build_min_heap
from min_heapify import min_heapify_iter

# Using Max Heap
# Best for sorting elements in ascending order
# TC O(Nlog(N)) SC O(1)
def heap_sort_max(arr, n):
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify_iter(arr, i, 0)

# Using Min Heap
# Best for sorting elements in descending order
# TC O(Nlog(N)) SC O(1)
def heap_sort_min(arr, n):
    build_min_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify_iter(arr, i, 0)

def main():
    arr = [int(a) for a in input().split()]
    heap_sort_min(arr, len(arr))
    print("Array in descending order using min heap: ", *arr)
    heap_sort_max(arr, len(arr))
    print("Array in ascending order using max heap: ", * arr)

if __name__ == "__main__":
    main()