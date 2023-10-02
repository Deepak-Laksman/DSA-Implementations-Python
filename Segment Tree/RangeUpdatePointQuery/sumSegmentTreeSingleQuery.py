# This a sum segment tree that updates a range but queries only for single value

class SumSegmentTree:

    def __init__(self, n, arr, arr2):
        self. n = n
        self.arr = arr.copy()
        self.size = 4 * n
        if (n & (n - 1)) == 0:
            self.size = 2 * n
        self.seg = [0 for i in range(self.size)]
        self.build(1, 0, n - 1)

    def build(self, idx, l, r):
        if l == r:
            self.seg[idx] = self.arr[l]
            return
        mid = (l + r) // 2
        self.build(2 * idx, l, mid)
        self.build(2 * idx + 1, mid + 1, r)
    
    def update(self, idx, l, r, start, end, val):
        if l > end or r < start:
            return
        if l == r:
            self.seg[idx] += val
        elif start <= l and end >= r:
            self.seg[idx] += val
        else:
            mid = (l + r) // 2
            self.update(2 * idx, l, mid, start, end, val) 
            self.update(2 * idx + 1, mid + 1, r, start, end, val)

    def query(self, idx, l, r, i):
        if l == r:
            return self.seg[idx]
        else:
            self.seg[2 * idx] += self.seg[idx]
            self.seg[2 * idx + 1] += self.seg[idx]
            self.seg[idx] = 0
            mid = (l + r) // 2
            if l <= i and i <= mid:
                return self.query(2 * idx, l, mid, i)
            else:
                return self.query(2 * idx + 1, mid + 1, r, i)

def main():
    n, q = map(int, input().split())
    arr = [int(a) for a in input().split()]
    segtree = SumSegmentTree(n, arr)
    for _ in range(q):
        inp = [int(a) for a in input().split()]
        if len(inp) == 2:
            print(segtree.query(1, 0, n - 1, inp[1]))
        else:
            segtree.update(1, 0, n - 1, inp[1], inp[2], inp[3])

if __name__ == "__main__":
    main()