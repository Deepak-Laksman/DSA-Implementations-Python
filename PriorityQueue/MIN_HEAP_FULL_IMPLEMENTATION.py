from math import ceil

class Min_Heap:

    def __init__(self, max_size = 10000):
        self._heap = [float("inf")] * max_size
        self._max_size = max_size
        self._last_idx = -1

    def heapify(self, n, i):
        while True:
            l, r = 2 * i + 1, 2 * i + 2
            smallest = i
            if l < n and self._heap[l] < self._heap[smallest]:
                smallest = l
            if r < n and self._heap[r] < self._heap[smallest]:
                smallest = r
            if smallest != i:
                self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
                i = smallest
            else:
                break

    def percolate_up(self, idx):
        parent = int(ceil(idx / 2)) - 1
        while idx > 0 and self._heap[parent] > self._heap[idx]:
            self._heap[parent], self._heap[idx] = self._heap[idx], self._heap[parent]
            idx = parent
            parent = int(ceil(idx / 2))
    
    def push(self, value):
        if self._last_idx >= self._max_size - 1:
            print("Heap Overflow")
            return
        self._heap[self._last_idx + 1] = value
        self._last_idx += 1
        self.percolate_up(self._last_idx)

    def pop(self):
        min_value = self._heap[0]
        self._heap[0] = self._heap[self._last_idx]
        self._last_idx -= 1
        self.heapify(self._last_idx, 0)
        return min_value

def main():
    min_heap = Min_Heap(100)
    for i in range(100):
        min_heap.push(i)
    for i in range(100):
        print(min_heap.pop(), end = " ")

if __name__ == "__main__":
    main()