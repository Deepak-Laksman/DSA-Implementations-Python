visited = []
graph = []

# Time Complexity of BFS is O(n + E), Space Complexity of BFS is O(n + E) + O(n) + O(n)

def bfs(i):
    queue = [i]
    visited[i] = True
    while True:
        if len(queue) == 0:
            break
        while len(queue) > 0:
            current = queue.pop(0)
            print(current, end = " ")
            for node in graph[current]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True           

def main():
    global visited, graph
    n, m = map(int, input().split())
    graph = [set() for i in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)

if __name__ == '__main__':
    main()