# Cut Edge

from collections import defaultdict

graph = defaultdict(list)
visited = []
timer = 0

# low -> lowest time of insertion of the current node
# tin -> actual time of insertion of the current node
low, tin = [], []

def printAllBridges(current, parent):
    global graph, visited, timer, low, tin
    visited[current] = 1
    timer += 1
    low[current] = tin[current] = timer
    for adjacent in graph[current]:
        if adjacent == parent:
            continue
        if not visited[adjacent]:
            printAllBridges(adjacent, current)
            low[current] = min(low[current], low[adjacent])
            if low[adjacent] > tin[current]:
                print(adjacent, "->", current)
        else:
            low[current] = min(low[current], tin[adjacent])

def main():
    global graph, visited, timer, low, tin
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
            printAllBridges(i, -1)

if __name__ == "__main__":
    main()