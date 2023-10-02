def build(idx, low, high, seg, arr):
    if low == high:
        seg[idx] = arr[low]
        return
    mid = low + (high - low) // 2
    build(2 * idx + 1, low, mid, seg, arr)
    build(2 * idx + 2, mid + 1, high, seg, arr)
    seg[idx] = min(seg[2 * idx + 1], seg[2 * idx + 2])

def find_min(low, high, l, r, seg):
    if low == high:
        return seg[low]
    elif l > high or r < low:
        return float("inf")
    mid = low + (high - low) // 2
    return min(find_min(low, mid, l, r, seg), find_min(mid + 1, high, l, r, seg))

def point_update(idx, i, low, high, seg, arr):
    if low == high:
        seg[low] = arr[i]
        return
    mid = low + (high - low) // 2
    if i <= mid:
        point_update(2 * idx + 1, i, low, mid, seg, arr)
    else:
        point_update(2 * idx + 2, mid + 1, high, seg, arr)
    seg[idx] = min(seg[2 * idx + 1], seg[2 * idx + 2])

def main():
    n, m, q = map(int, input().split())
    arr1 = [int(a) for a in input().split()]
    arr2 = [int(a) for a in input().split()]
    seg1 = [0 for i in range(4 * n)]
    seg2 = [0 for i in range(4 * m)]
    build(0, 0, n - 1, seg1, arr1)
    build(0, 0, m - 1, seg2, arr2)
    for _ in range(q):
        t = [int(a) for a in input().split()]
        if t[0] == 1:
            ans = min(find_min(0, n - 1, t[1], t[2], seg1), find_min(0, m - 1, t[3], t[4], seg2))
            print(ans)
        else:
            if t[1] == 1:
                arr1[t[2]] = t[3]
                point_update(0, t[2], 0, n - 1, seg1, arr1)
            else:
                arr2[t[2]] = t[3]
                point_update(0, t[2], 0, m - 1, seg2, arr2)

if __name__ == "__main__":
    main()