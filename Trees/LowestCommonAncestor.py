from collections import defaultdict

tree = defaultdict(list)
parents = []
ancestor = []

def dfs(node, parent):
    global tree, parents
    for child in tree[node]:
        if child != parent:
            parents[child] = node
            dfs(child, node)

def path(node, path_list = []):
    global parents
    while parents[node] != node:
        path_list.append(node)
        node = parents[node]
    return path_list[::-1]

def find_lca(path_x, path_y):
    n, m = len(path_x), len(path_y)
    i, j = 0, 0
    while i < n and j < m:
        if path_x[i] != path_y[j]:
            return path_x[i - 1]
        i += 1
        j += 1

def main():
    global tree, parents, ancestor
    n, m = map(int, input().split())
    parents = [0] * (n + 1)
    ancestor = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    x, y = map(int, input().split())
    dfs(1, -1)
    parents[1] = 1
    path_x = path(x)
    path_y = path(y)
    lca = find_lca(path_x, path_y)
    print(lca)


if __name__ == "__main__":
    main()

# Sample Test Case
"""
13 12 
1 2
1 3
1 13
2 5
5 6
5 7
5 8
8 12
3 4
4 9
4 10
10 11
"""