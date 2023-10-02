def kthValue(n, k):
    if n == 1 and k == 1:
        return 0
    mid = 1 << (n - 2)
    if k <= mid:
        return kthValue(n - 1, k)
    else:
        return 1 ^ kthValue(n - 1, k - mid)

def main():
    n, k = map(int, input().split())
    print(kthValue(n, k))

if __name__ == "__main__":
    main()