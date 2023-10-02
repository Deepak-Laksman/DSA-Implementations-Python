from max_heapify import max_heapify_iter
import math

# TC O(log(N)), SC O(1)
def extract_max(heap):
    max_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    max_heapify_iter(heap, len(heap), 0)
    return max_value

# TC O(log(N)), SC O(1)  
def increase_key(heap, key_idx, increment):
    heap[key_idx] += increment
    parent = int(math.ceil(key_idx / 2)) - 1
    while key_idx > 0 and heap[parent] < heap[key_idx]:
        heap[parent], heap[key_idx] = heap[key_idx], heap[parent]
        key_idx = parent
        parent = int(math.ceil(key_idx / 2)) - 1

# TC O(log(N)), SC O(1)
def decrease_key(heap, key_idx, decrement):
    heap[key_idx] -= decrement
    max_heapify_iter(heap, len(heap), key_idx)

# TC O(log(N)) SC O(1)
def insert_element(heap, key):
    heap.append(key)
    n = len(heap)
    key_idx = n - 1
    parent = int(math.ceil(key_idx / 2))
    while key_idx > 0 and heap[parent] < heap[key_idx]:
        heap[parent], heap[key_idx] = heap[key_idx], heap[parent]
        key_idx = parent
        parent = int(math.ceil(key_idx / 2))