# Used to find strongly connected components

# Strongly connected components are a set of nodes where from meach node we can go to every other node in the component

# Steps to be followed

# 1. We need the nodes sorted in terms of finish time, that is, we can use topological sort
# 2. Now we need to transpose the graph, that is reverse all the edges so that we won't go to another connected component from one connected component
# 3. Now we need to do dfs on the topo order and add the nodes visited in every traversal in a list and add it to the main list. This list has all
#    the strongly connected components

# Overall Time and Space Complexity is O(n + m)

from collections import defaultdict

# Directed Graph
graph = defaultdict(list)
visited = []
topo_order = []

# Time Complexity -> O(n)
def topologicalSort(current):
    global graph, visited, topo_order
    visited[current] = 1
    for adjacent in graph[current]:
        if not visited[adjacent]:
            topologicalSort(adjacent)
    topo_order.append(current)

# Time Complexity -> O(n + m)
def find_connected_component(current, node_list, graph):
    global visited
    visited[current] = 1
    for adjacent in graph[current]:
        if not visited[adjacent]:
            node_list.append(adjacent)
            node_list = find_connected_component(adjacent, node_list, graph)
    return node_list

def main():
    global graph, visited, topo_order
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Doing topological sort
    for i in range(1, n + 1):
        if not visited[i]:
            topologicalSort(i)

    # Making a graph that is transpose to the existing one
    graph_transpose = defaultdict(list)
    for u in range(1, n + 1):
        for v in graph[u]:
            graph_transpose[v].append(u)
    
    # Reintializing visited to start a new dfs
    visited = [0] * (n + 1)
    strongly_connected_components = []

    # Time Complexity is O(n + m)
    # Visiting nodes in topo order
    for i in range(n - 1, -1, -1):
        if not visited[topo_order[i]]:
            node_list = find_connected_component(topo_order[i], [topo_order[i]], graph_transpose)
            strongly_connected_components.append(node_list)

    print(*strongly_connected_components)
    
if __name__ == "__main__":
    main()