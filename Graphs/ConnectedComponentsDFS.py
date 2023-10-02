from collections import defaultdict

visited = []
graph = defaultdict(list)

def dfs(node, this_component):
    global visited, graph
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            this_component.append(child)
            dfs(child, this_component)

def main():
    global visited, graph
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            this_component = [i]
            dfs(i, this_component)
            components.append(this_component)
    
    print(*components)

if __name__ == "__main__":
    main()