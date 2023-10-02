# To find minimum distance from source node to all other nodes 
# Also Bellman Ford Algorithm can find negative cycles

# Steps to be followed
# 1.Store all the edges
# 2.Update the distances of each edge for n - 1 times
# 3.If at the nth iteration, any of the values of distances changes, then there is a negative cycle

# Time Complexity is O(n * m) and Space Complexity is O(n)

def main():
    n, m = map(int, input().split())
    dist = [float("inf")] * (n + 1)
    edges = []
    for _ in range(m):
        u, v, wt = map(int, input().split())
        edges.append([u, v, wt])
    source = int(input())
    dist[source] = 0
    for _ in range(n - 1):
        for u, v, wt in edges:
            if dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    flag = -1
    for u, v, wt in edges:
        if dist[u] + wt < dist[v]:
            flag = 1
            break
    if flag == 1:
        print("Negative Cycle exists")
    else:
        print(*dist)

if __name__ == "__main__":
    main()