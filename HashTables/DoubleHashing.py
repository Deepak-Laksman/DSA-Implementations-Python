# Here we will implement double hashing.
# The basic idea of double hashing is if a hash value points to an index in the array which is already occupied,
# We use another hash function to hash this hash value to get another value and hence collisions can be reduced.

class DoubleHash:
    def __init__(self, SIZE = None, PRIME = None):
        self.SIZE = SIZE
        self.PRIME = PRIME
        self.HashTable = [-1] * self.SIZE
        self.currentSize = 0

    def isFull(self):
        if self.currentSize == self.SIZE:
            return True
        return False

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        return False

    def hash1(self, key):
        return key % self.SIZE

    def hash2(self, key):
        return self.PRIME - (key % self.PRIME)

    def insertHash(self, value):
        if self.isFull():
            return
        index = self.hash1(value)
        index2 = self.hash2(value)
        i = 1
        if self.HashTable[index] != 0:
            while i:
                newIndex = (index + i * index2) % self.SIZE
                if self.HashTable[newIndex] != 0:
                    self.HashTable[newIndex] = value
                    break
                else:
                    i += 1
        else:
            self.HashTable[index] = value
        self.currentSize += 1

    def search(self, value):
        if self.isEmpty():
            return
        index = self.hash1(value)
        index2 = self.hash2(value)
        i = 0
        while self.HashTable[(index + i * index2) % self.SIZE] != value:
            if self.HashTable[(index + i * index2) % self.SIZE] != 0:
                return False, -1
            else:
                i += 1
        return True, (index + i * index2) % self.SIZE
