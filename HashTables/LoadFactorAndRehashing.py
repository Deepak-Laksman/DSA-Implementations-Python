# Load Factor

# While using direct chaining, there may be more than 1 value in the key index of the array.
# So if the size of the array is m and there are n values to be stored, then the load factor is n/m.
# We need to keep this minimum to get a better time complexity for searching.
# For searching the time complexity is O(1 + Load Factor).

# Rehashing

# Rehashing is the method where we create a double sized bucket array and hash all the values once again and put them in
# their appropriate index in the new bucket array.
# This reduces the Load Factor. This is done when the load factor crosses 0.75.

# Implementing Rehashing

class Map:
    class MapNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    buckets = list()
    size = 0
    bucketsCount = 0
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self):
        self.bucketsCount = 5
        self.buckets = [None] * Map.bucketsCount

    def getBucketIndex(self, key):
        hashCode = hash(key)
        return hashCode % self.bucketsCount

    def insert(self, key, value):
        bucketIndex = self.getBucketIndex(key)
        head = Map.buckets[bucketIndex]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        newMapNode = Map.MapNode(key, value)
        head = Map.buckets[bucketIndex]
        newMapNode.next = head
        Map.buckets[bucketIndex] = newMapNode
        Map.size += 1
        loadFactor = (1 * Map.size) // Map.bucketsCount
        if loadFactor > Map.DEFAULT_LOAD_FACTOR:
            self.rehash()

    def rehash(self):
        temp = Map.buckets
        bucketsCount = 2 * Map.bucketsCount
        Map.buckets = [None] * bucketsCount
        Map.size = 0
        Map.bucketsCount *= 2
        lengthOfOldBuckets = len(temp)
        for i in range(lengthOfOldBuckets):
            head = temp[i]
            while head is not None:
                key = head.key
                value = head.value
                self.insert(key, value)
                head = head.next