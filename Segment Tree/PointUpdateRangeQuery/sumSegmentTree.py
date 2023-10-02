class SumSegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr.copy()
        size = 4 * n
        if (n & (n - 1)) == 0:
            size = 2 * n
        self.seg = [0 for i in range(size)]
        self.build(1, 0, n - 1)
    
    def build(self, idx, l, r):
        if l == r:
            self.seg[idx] = self.arr[l]
            return 
        mid = (l + r) // 2
        self.build(2 * idx, l, mid)
        self.build(2 * idx + 1, mid + 1, r)
        self.seg[idx] = self.seg[2 * idx] + self.seg[2 * idx + 1]
    
    def query(self, idx, l, r, start, end):
        if start > r or end < l:
            return 0
        if l == r:
            return self.seg[idx]
        if start <= l and end >= r:
            return self.seg[idx]
        mid = (l + r) // 2
        ans = self.query(2 * idx, l, mid, start, end) + self.query(2 * idx + 1, mid + 1, r, start, end)
        return ans
    
    def update(self, idx, l, r, i, value):
        if l == r:
            self.seg[idx] = self.arr[l] = value
            return 
        mid = (l + r) // 2
        if (l <= i <= mid):
            self.update(2 * idx, l, mid, i, value)
        else:
            self.update(2 * idx + 1, mid + 1, r, i, value)
        self.seg[idx] = self.seg[2 * idx] + self.seg[2 * idx + 1]

def main():
    n, q = map(int, input().split())
    arr = [int(a) for a in input().split()]
    segtree = SumSegmentTree(n, arr)
    for i in range(q):
        t, l, r = map(int, input().split())
        if t == 1:
            print(segtree.query(1, 0, n - 1, l, r))
        else:
            segtree.update(1, 0, n - 1, l, r)
    


if __name__ == "__main__":
    main()