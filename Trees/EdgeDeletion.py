from collections import defaultdict

tree = defaultdict(list)
subtree_sum = []
cost = []

def dfs(node, parent):
    global tree, subtree_sum
    for child in tree[node]:
        if child == parent:
            continue
        dfs(child, node)
        subtree_sum[node] += subtree_sum[child]

def find_max_product(n):
    max_product = -1
    for i in range(2, n + 1):
        max_product = max(max_product, (subtree_sum[1] - subtree_sum[i]) * subtree_sum[i])
    return max_product

def main():
    global tree, subtree_sum, cost
    n, m = map(int, input().split())
    subtree_sum = [0] * (n + 1)
    cost = [int(c) for c in input().split()]
    total_sum = sum(cost)
    for i in range(1, n + 1):
        subtree_sum[i] = cost[i - 1]
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    dfs(1, -1)
    print(find_max_product(n))        

if __name__ == "__main__":
    main()