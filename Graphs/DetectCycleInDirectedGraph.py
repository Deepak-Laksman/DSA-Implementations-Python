visited = []
graph = []
dfsVisited = []

def isCycleDFS(node):
    global visited, graph, dfsVisited
    visited[node] = True
    dfsVisited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if isCycleDFS(neighbour):
                return True
        elif dfsVisited[neighbour]:
            return True
    dfsVisited[node] = False
    return False

# Kahn's Algorithm 

# If there is a cycle, we cannot do topological sort which means the size of topo list will be less than number of vertices.
# We use this fact to check whether graph has cycle or not.

def isCycleBFS():
    global graph
    count = 0
    n = len(graph) - 1
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for node in graph[i]:
            indegree[node] += 1
    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    while len(queue):
        current = queue.pop(0)
        count += 1
        for node in graph[current]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
    if count == n:
        return False
    return True

def main():
    global visited, graph, dfsVisited
    n, m = map(int, input().split())
    visited = [False for i in range(n + 1)]
    graph = [set() for i in range(n + 1)]
    dfsVisited = [False for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
    """
    for i in range(1, n + 1):
        if not visited[i]:
            if isCycleDFS(i):
                print("Cycle Detected.")
                return
    print("No Cycle Detected.")
    """
    if isCycleBFS():
        print("Cycle Detected.")
    else:
        print("No Cycle Detected.")

if __name__ == "__main__":
    main()