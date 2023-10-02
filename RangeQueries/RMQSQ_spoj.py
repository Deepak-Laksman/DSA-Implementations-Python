class SegmentTree:
    def __init__(self, n, arr):
        self.seg = [float("inf") for i in range(4 * n)]
        self.arr = arr.copy()
        self.build(1, 1, n)

    def build(self ,idx, low, high):
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        mid = low + (high - low) // 2
        self.build(2 * idx, low, mid)
        self.build(2 * idx + 1, mid + 1, high)
        self.seg[idx] = min(self.seg[2 * idx], self.seg[2 * idx + 1])
    
    def query(self, idx, l, r, low, high):
        if low <= l and high >= r:
            return self.seg[idx]
        if l > high or r < low:
            return float("inf")
        mid = low + (high - low) // 2
        left = self.query(2 * idx, l, r, low, mid)
        right = self.query(2 * idx + 1, l, r, mid + 1, high)
        return min(left, right)

def main():
    n = int(input())
    arr = [int(a) for a in input().split()]
    q = int(input())
    seg = SegmentTree(n, arr)
    for _ in range(q):
        a, b = map(int, input().split())
        print(seg.query(1, a + 1, b + 1, 1, n))

if __name__ == "__main__":
    main()