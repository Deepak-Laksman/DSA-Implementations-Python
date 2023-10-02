class segment_tree:
    def __init__(self, n, arr, orr):
        self.length = power(2, n)
        self.seg = [0 for i in range(4 * self.length + 1)]
        self.n = n
        self.arr = arr
        self.build(0, 0, self.length - 1, orr)
    
    def build(self, idx, low, high, orr):
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        mid = low + (high - low) // 2
        self.build(2 * idx + 1, low, mid, not orr)
        self.build(2 * idx + 2, mid + 1, high, not orr)
        if orr:
            self.seg[idx] = self.seg[2 * idx + 1] | self.seg[2 * idx + 2]
        else:
            self.seg[idx] = self.seg[2 * idx + 1] ^ self.seg[2 * idx + 2]
        
    def update(self, idx, low, high, i, val, orr):
        if low == high:
            self.seg[idx] = val
            return
        mid = low + (high - low) // 2
        if i <= mid:
            self.update(2 * idx + 1, low, mid, i, val, not orr)
        else:
            self.update(2 * idx + 2, mid + 1, high, i, val, not orr)
        if orr:
            self.seg[idx] = self.seg[2 * idx + 1] | self.seg[2 * idx + 2]
        else:
            self.seg[idx] = self.seg[2 * idx + 1] ^ self.seg[2 * idx + 2]

def power(a, b):
    ans = 1
    while b:
        if b & 1:
            ans *= a
        a *= a
        b >>= 1
    return ans

def main():
    n, m = map(int, input().split())
    arr = [int(a) for a in input().split()]
    seg = segment_tree(n, arr, n % 2)
    length = power(2, n)
    for _ in range(m):
        a, b = map(int, input().split())
        seg.update(0, 0, length - 1, a - 1, b, n % 2)
        print(seg.seg[0])

if __name__ == "__main__":
    main()