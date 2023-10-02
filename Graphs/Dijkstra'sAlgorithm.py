# Shortest path from source to all other nodes in an Undirected Weighted Graph

from collections import defaultdict
from heapq import heappop, heappush

graph = defaultdict(list)
visited = []
distances = []

def dijkstra(source):
    global graph, visited, distances
    distances[source] = 0
    queue = []
    heappush(queue, (0, source))
    while len(queue):
        distance, current = heappop(queue)
        visited[current] = True
        for node, weight in graph[current]:
            if distances[current] != float("inf"):
                if distances[current] + weight < distances[node]:
                    heappush(queue, (distances[node], node))
                    distances[node] = distances[current] + weight

def main():
    global graph, visited, distances
    n, m, source = map(int , input().split())
    visited = [False] * (n + 1)
    distances = [float("inf")] * (n + 1)
    for _ in range(m):
        u, v, w = map(int , input().split())
        graph[u].append((v, w))
    dijkstra(source)
    print(*distances)

if __name__ == "__main__":
    main()