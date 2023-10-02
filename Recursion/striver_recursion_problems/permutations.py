from collections import Counter

def permute_not_unique_elems(arr):
    n = len(arr)
    perms = []
    ctr = Counter(arr)
    def recur(i, perm, ctr):
        nonlocal perms, n
        if i == n:
            perms.append(perm.copy())
            return
        for k in ctr.keys():
            if ctr[k] >= 1:
                ctr[k] -= 1
                perm.append(k)
                recur(i + 1, perm, ctr)
                ctr[k] += 1
                perm.pop()
    recur(0, [], ctr)
    return perms

def permute_unique_elems(arr):
    n = len(arr)
    perms = []
    def recur(i, arr):
        nonlocal n, perms
        if i == n:
            perms.append(arr.copy())
            return
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            recur(i + 1, arr)
            arr[i], arr[j] = arr[j], arr[i]
    recur(0, arr)
    return perms

def main():
    arr = [int(a) for a in input().split()]
    print(*permute_not_unique_elems(arr))

if __name__ == "__main__":
    main()