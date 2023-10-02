from min_heapify import min_heapify_iter
import math

def extract_min(heap):
    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    min_heapify_iter(heap, len(heap), 0)
    return min_value

def decrease_key(heap, key_idx, decrement):
    heap[key_idx] -= decrement
    parent = int(math.ceil(key_idx / 2))
    while key_idx > 0 and heap[parent] > heap[key_idx]:
        heap[parent], heap[key_idx] = heap[key_idx], heap[parent]
        key_idx = parent
        parent = int(math.ceil(key_idx / 2))

def increase_key(heap, key_idx, increment):
    heap[key_idx] += increment
    min_heapify_iter(heap, len(heap), key_idx)

def insert_element(heap, key):
    heap.append(key)
    n = len(heap)
    key_idx = n - 1
    parent = int(math.ceil(key_idx / 2))
    while key_idx > 0 and heap[parent] > heap[key_idx]:
        heap[parent], heap[key_idx] = heap[key_idx], heap[parent]
        key_idx = parent
        parent = int(math.ceil(key_idx / 2))