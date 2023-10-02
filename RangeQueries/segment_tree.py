import sys
 
# sys.stdin, sys.stdout = open("input.txt", "r"), open("output.txt", "w")

class segment_tree:

    def __init__(self, n, arr):
        self.seg = [float("inf") for i in range(2 * n + 1)]
        self.arr = arr
        self.n = n
        self.build()

    # TC is O(4*N)
    def build(self):
        for i in range(self.n):
            self.seg[i + self.n] = self.arr[i]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = min(self.seg[2 * i], self.seg[2 * i + 1])

    # TC is O(log(N))
    def find_min(self, l, r):
        l += self.n
        r += self.n
        mini = float("inf")
        while l < r:
            if l & 1:
                mini = min(mini, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                mini = min(mini, self.seg[r])
            l //= 2
            r //= 2
        return mini

    # TC is O(log(N))
    def point_update(self, pos, val):
        pos += self.n
        self.seg[pos] = val
        while pos > 1:
            pos //= 2
            self.seg[pos] = min(self.seg[2 * pos], self.seg[2 * pos + 1])

def main():
    n, q = map(int, input().split())
    arr = [int(a) for a in input().split()]
    seg = segment_tree(n, arr)
    for _ in range(q):
        l, r = map(int, input().split())
        print(seg.find_min(l - 1, r))

if __name__ == "__main__":
    main()