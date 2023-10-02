from collections import defaultdict

tree = defaultdict(list)
sums = []
evens = []

def calc_sums_and_evens_count(root, parent):
    global tree, sums, evens
    for child in tree[root]:
        if child == parent:
            continue
        calc_sums_and_evens_count(child, root)
        sums[root] += sums[child]
        evens[root] += evens[child]

def main():
    global tree, sums, evens
    n, m = map(int, input().split())
    sums = [i for i in range(n + 1)]
    evens = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
        if u % 2 == 0:
            evens[u] = 1
        if v % 2 == 0:
            evens[v] = 1
    calc_sums_and_evens_count(1, -1)
    print(*sums)
    print(*evens)

if __name__ == "__main__":
    main()