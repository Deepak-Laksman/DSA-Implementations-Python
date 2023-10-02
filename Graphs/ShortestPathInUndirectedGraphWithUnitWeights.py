from collections import defaultdict
visited = []
graph = defaultdict(list)

def bfs(source, n):
    global visited, graph
    visited = [False] * (n + 1)
    distances = [float("inf") for i in range(n + 1)]
    queue = [source]
    visited[source] = True
    distances[source] = 0
    while len(queue):
        current = queue.pop(0)
        for node in graph[current]:
            if not visited[node]:
                distances[node] = min(distances[node], distances[current] + 1)
                queue.append(node)
                visited[node] = True
    return distances

def main():
    global visited, graph
    n, m, source = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append((v))
        graph[v].append(u)
    print(*bfs(source, n)[1:])

if __name__ == "__main__":
    main()