class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if self.size[parentX] > self.size[parentY]:
            self.parent[parentY] = parentX
            self.size[parentX] += self.size[parentY]
        else:
            self.parent[parentX] = parentY
            self.size[parentY] += self.size[parentX]
        
    def size(self, x):
        root = self.find(x)
        return self.size[root]