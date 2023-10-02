from collections import defaultdict

graph = defaultdict(list)
visited = []
stack = []
distances = []

# Approach

# Basically we are trying to find the topological sorting order for the DAG.
# This is done so that we can traverse the graph from the vertices which have 0 indegree, that is, they cannot be reached from any other vertex.
# Then we check whether there is way to reach the current vertex, if yes, then we update the distances of the adjacent nodes.

def topoSort(i):
    global graph, visited, stack
    visited[i] = True
    for node, weight in graph[i]:
        if not visited[node]:
            topoSort(node)
    stack.append(i)

def findShortestPath(source):
    global stack, graph, distances
    distances[source] = 0
    while len(stack):
        current = stack.pop()
        for node, weight in graph[current]:
            if distances[current] != float("inf"):
               distances[node] = min(distances[node], distances[current] + weight)

def main():
    global graph, visited, stack, distances
    n, m, source = map(int, input().split())
    visited = [False] * (n + 1)
    distances = [float("inf")] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    for i in range(1, n + 1):
        topoSort(i)
    findShortestPath(source)
    print(*distances)

if __name__ == "__main__":
    main()