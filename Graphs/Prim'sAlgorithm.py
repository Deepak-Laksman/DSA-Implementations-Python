from collections import defaultdict
from heapq import heappush, heappop

graph = defaultdict(list)
MST = []
parent = []
key = []

def main():
    global graph, MST, key, parent

    n, m = map(int, input().split())
    MST = [False] * (n + 1)
    key = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    key[1] = 0
    queue = []
    heappush(queue, (0, 1))

    while queue:
        node = heappop(queue)[1]       
        MST[node] = True
        for adjacent, weight in graph[node]:
            if not MST[adjacent] and weight < key[adjacent]:
                parent[adjacent] = node
                key[adjacent] = weight
                heappush(queue, (key[adjacent], adjacent))
    
    for i in range(2, n + 1):
        print(parent[i], "->", i)

if __name__ == "__main__":
    main()        