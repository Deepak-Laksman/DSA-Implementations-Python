def main():
    # n -> number of vertices
    # m -> number of edges
    n, m = map(int, input().split())
    
    # storing graph in the form of ADJACENCY MATRIX
    # Space Used = n^2 approx.
    graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        # undirected graph
        graph[u][v] = graph[v][u] = 1
    
    # storing graph in the form of ADJACENY LIST
    # Space Used = n + 2 * m
    graph2 = [set() for i in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph2[u].add(v)
        graph2[v].add(u)

    # if weights are also present, then we will push weight along with the vertex, graph2[u].add([v, w])
    print(graph)
    print(graph2)
    

if __name__ == "__main__":
    main()