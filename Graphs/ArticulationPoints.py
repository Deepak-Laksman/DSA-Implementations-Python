# Cut Vertex

from collections import defaultdict

graph = defaultdict(list)
visited = []
timer = 0

# low -> lowest time of insertion of node, tin -> actual time of insertion of node
low, tin = [], []

articulation_points = set()

def findArticulationPoints(current, parent):
    global graph, visited, timer, low, tin, articulation_points
    visited[current] = 1
    timer += 1
    low[current] = tin[current] = timer
    children = 0
    for adjacent in graph[current]:
        if adjacent == parent:
            continue
        if not visited[adjacent]:
            findArticulationPoints(adjacent, current)
            low[current] = min(low[current], low[adjacent])
            children += 1
            if low[adjacent] >= tin[current] and parent != -1:
                articulation_points.add(current)
        else:
            low[current] = min(low[current], tin[adjacent])
    if children > 1 and parent == -1:
        articulation_points.add(current)

def main():
    global graph, visited, timer, low, tin, articulation_points
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    low = [float("inf")] * (n + 1)
    tin = [float("inf")] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        if not visited[i]:
            findArticulationPoints(i, -1)
    print(*articulation_points)

if __name__ == "__main__":
    main()