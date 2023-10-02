visited = []
graph = []

def isCycleBFS(i):
    global graph
    queue = [(i, -1)]
    visited[i] = True
    parent = -1
    while len(queue):
        current, parent = queue.pop(0)
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                queue.append([node, current])
            elif parent != node:
                return True
    return False

def isCycleDFS(i):
    global graph
    stack = [(i, -1)]
    visited[i] = True
    while len(stack):
        current, parent = stack.pop()
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                stack.append([node, current])
            elif parent != node:
                return True
    return False

def isCycleDFS2(i, parent):
    global graph
    visited[i] = True
    for node in graph[i]:
        if not visited[node]:
            if isCycleDFS2(node, i):
                return True
        elif node != parent:
            return True
    return False

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
            if isCycleDFS2(i, -1):
                print("Cycle Detected.")
                return
    print("No Cycle Detected.")

if __name__ == "__main__":
    main()