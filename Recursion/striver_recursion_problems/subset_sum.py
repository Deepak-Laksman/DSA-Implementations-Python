def subset_sum(arr):
    sums = []
    n = len(arr)
    def recur(idx, cur):
        nonlocal sums, n
        if idx == n:
            sums.append(cur)
            return
        recur(idx + 1, cur + arr[idx])
        recur(idx + 1, cur)
    recur(0, 0)
    return sums

def subset_sum_2(arr):
    subs = []
    n = len(arr)
    def recur(idx, sub):
        nonlocal subs, n
        subs.append(sub)
        for i in range(idx, n):
            if i > idx and arr[i] == arr[i - 1]:
                continue
            sub.append(arr[i])
            recur(i + 1, sub)
            sub.pop()
    recur(0, [])
    return subs

def main():
    arr = [int(a) for a in input().split()]
    arr.sort()
    print(*subset_sum(arr))

if __name__ == "__main__":
    main()