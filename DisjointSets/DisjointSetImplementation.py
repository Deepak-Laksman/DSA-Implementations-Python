# Here we are using tree concept to represent sets.
# The root of the tree will be the identifier.
# We will have 2 arrays, 1. parent array which stores parent of each node, and parent of all the nodes is their root
# 2. rank array, this stores the height of each set(tree), when we merge two sets, we merge the smaller
# one to the larger one. This is when the rank is used. and if two sets of same height are merged,
# then the resulting height is increased by one.

class DisjointSet:
    def __init__(self):
        self.maxSize = 100000
        self.parent = [0] * self.maxSize
        self.rank = [0] * self.maxSize

    def makeSet(self, val):
        self.parent[val] = val

    def find(self, val):
        if val != self.parent[val]:
            val = self.parent[val]
        return val

    def union(self, val1, val2):
        if self.parent[val1] == self.parent[val2]:
            return
        if self.rank[val1] > self.rank[val2]:
            for i in range(10000):
                if self.parent[i] == self.parent[val2]:
                    self.parent[i] = self.parent[val1]
            self.rank[val1] += 1
        else:
            for i in range(100000):
                if self.parent[i] == self.parent[val1]:
                    self.parent[i] = self.parent[val2]
                self.rank[val2] += 1
