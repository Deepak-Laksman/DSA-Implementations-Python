class DisjointSet:
    def __init__(self, n):
        self.parent = [(i) for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def find(self, node):
        if self.parent[node] == node:
            return node
        node = self.find(self.parent[node])
        return node
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return 
        else:
            if self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = parent1
            elif self.rank[parent2] > self.rank[parent1]:
                self.parent[parent1] = parent2
            else:
                self.parent[parent2] = parent1
                self.rank[parent1] += 1
        
def main():
    n, m = map(int, input().split())
    graph = []
    for _ in range(m):
        u, v, w = map(int , input().split())
        graph.append((w, u, v))
    graph.sort(key = lambda x: x[0])
    uf = DisjointSet(n)
    totalCost = 0
    for w, u, v in graph:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            totalCost += w
    print(totalCost)

if __name__ == "__main__":
    main()