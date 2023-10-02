visited = []
graph = []

# Time Complexity is O(N + E), Space Complexity is O(N + E) + O(N) + O(N)

def dfs(i):
    stack = [i]
    visited[i] = True
    while True:
        if len(stack) == 0:
            break
        while len(stack) > 0:
            current = stack.pop()
            print(current, end = " ")
            for node in graph[current]:
                if not visited[node]:
                    visited[node] = True
                    stack.append(node)

def dfs2(i):
    global visited, graph
    # Take action on vertex after entering vertex
    visited[i] = True
    print(i, end = " ")
    for node in graph[i]:
        if not visited[node]:
        # Take action on child node before entering child node
            dfs(node)
        # Take action on child node after exiting child node
    # Take action on vertex before exiting vertex

def main():
    global visited, graph
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    graph = [set() for i in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs2(i)

if __name__ == "__main__":
    main()