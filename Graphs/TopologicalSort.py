graph = []
visited = []
stack = []

def dfs(node):
    global graph, visited, stack
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            visited[neighbour] = True
            dfs(neighbour)
    stack.append(node)

# Kahn's Algorithm

# Intuition is if we reduce the incoming edges, then that vertex becomes eligible to be added in the topo sort list as it doesn't have
# anymore incoming edges

def bfs():
    global graph
    topo = []
    n = len(graph) - 1
    indegree = [0] * (n + 1)
    indegree[0] = -1
    for i in range(1, n + 1):
        for node in graph[i]:
            indegree[node] += 1
    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    while len(queue):
        current = queue.pop(0)
        topo.append(current)
        for node in graph[current]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
    return topo

def main():
    global graph, visited, stack
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    graph = [set() for i in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    print(*stack[::-1])
    print(*bfs())
    
if __name__ == "__main__":
    main()