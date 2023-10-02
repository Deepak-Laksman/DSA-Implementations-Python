colors = []
graph = []

def isBipartiteBFS(i):
    global colors, graph
    queue = [i]
    colors[i] = 0
    while len(queue):
        current = queue.pop(0)
        for node in graph[current]:
            if colors[node] == -1:
                colors[node] = 1 - colors[current]
                queue.append(node)
            elif colors[node] == colors[current]:
                return False
    return True

def isBipartiteDFS(i):
    global colors, graph
    stack = [i]
    colors[i] = 0
    while len(stack):
        current = stack.pop()
        for node in graph[current]:
            if colors[node] == -1:
                colors[node] = 1 - colors[current]
                stack.append(node)
            elif colors[node] == colors[current]:
                return False
    return True

def isBipartiteDFS2(i):
    global graph, colors
    for node in graph[i]:
        if colors[node] == -1:
            colors[node] = 1 - colors[i]
            if not isBipartiteDFS2(node):
                return False
        elif colors[node] == colors[i]:
            return False
    return True

def main():
    global colors, graph
    n, m = map(int, input().split())
    colors = [-1] * (n + 1)
    graph = [set() for i in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    flag = False
    for i in range(1, n + 1):
        if colors[i] == -1:
            colors[i] = 1
            if isBipartiteDFS2(i):
                flag = True
            else:
                flag = False
                break
    if flag:
        print(*colors[1:])
    else:
        print("Not A Bipartite Graph")

if __name__ == "__main__":
    main()