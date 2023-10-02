from collections import defaultdict

tree = defaultdict(list)
depth = []

def dfs(node, parent):
    global tree, depth, max_depth, max_node
    for child in tree[node]:
        if child == parent:
            continue
        depth[child] = depth[node] + 1
        dfs(child, node)

# Time Complexity is O(N), Space Complexity is O(N)

def main():
    global tree, depth, max_depth, max_node
    n, m = map(int, input().split())
    depth = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    dfs(1, -1)
    max_depth, max_node = -1, -1
    for i in range(n + 1):
        if depth[i] > max_depth:
            max_depth = depth[i]
            max_node = i
        depth[i] = 0
    dfs(max_node, -1)
    max_depth = max(depth)
    print(max_depth)

if __name__ == "__main__":
    main()