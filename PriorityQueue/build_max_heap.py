from max_heapify import max_heapify_iter


# TC O(N), SC O(1)
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify_iter(arr, n, i)

def main():
    arr = [int(a) for a in input().split()]
    build_max_heap(arr)
    print(*arr)

if __name__ == "__main__":
    main()