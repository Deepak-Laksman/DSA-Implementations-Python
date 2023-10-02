class Node:
    def __init__(self, open = 0, close = 0, full = 0):
        self.open = open
        self.close = close
        self.full = full

class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.seg = [Node() for i in range(4 * n)]
        self.build(0, 0, n - 1)
    
    def build(self, idx, low, high):
        if low == high:
            if self.arr[low] == "(":
                self.seg[idx] = Node(1, 0, 0)
            else:
                self.seg[idx] = Node(0, 1, 0)
            return
        mid = low + (high - low) // 2
        self.build(2 * idx + 1, low, mid)
        self.build(2 * idx + 2, mid + 1, high)
        self.seg[idx] = self.merge(self.seg[2 * idx + 1], self.seg[2 * idx + 2])
    
    def merge(self, node1, node2):
        final = Node()
        fulls = min(node1.open, node2.close)
        final.full = node1.full + node2.full + fulls
        final.open = node1.open + node2.open - fulls
        final.close = node2.close + node1.close - fulls
        return final

    def query(self, idx, low, high, l, r):
        if low == high:
            return self.seg[idx]
        if l > high or r < low:
            return Node()
        if low >= l and high <= r:
            return self.seg[idx]
        mid = low + (high - low) // 2
        return self.merge(self.query(2 * idx + 1, low, mid, l, r), self.query(2 * idx + 2, mid + 1, high, l, r))

def main():
    string = input()
    n = int(input())
    seg = SegmentTree(len(string), string)
    for _ in range(n):
        a, b = map(int, input().split())
        node = seg.query(0, 0, len(string) - 1, a - 1, b - 1)
        print(node.full * 2)

if __name__ == "__main__":
    main()