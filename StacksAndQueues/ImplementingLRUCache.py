class Node:

    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

head = Node(-1, -1)
tail = Node(-1, -1)

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        head.next = tail
        tail.prev = head

    def addnode(self, node):
        temp = head.next
        node.next = temp
        node.prev = head
        head.next = node
        temp.prev = node

    def deletenode(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev

    def put(self, key, value):
        if key in self.map:
            reqNode = self.map[key]
            self.deletenode(reqNode)
            del self.map[key]
            newNode = Node(key, value)
            self.addnode(newNode)
            self.map[key] = head.next
        else:
            if len(self.map) == self.capacity:
                delnode = tail.prev
                del self.map[delnode.key]
                self.deletenode(delnode)
                newnode = Node(key, value)
                self.addnode(newnode)
                self.map[key] = head.next
            else:
                newnode = Node(key, value)
                self.addnode(newnode)
                self.map[key] = head.next
    
    def get(self, key):
        if key in self.map:
            required = self.map[key]
            value = required.val
            del self.map[key]
            self.deletenode(required)
            self.addnode(required)
            self.map[key] = head.next
            return value
        else:
            return -1


def main():
    lru = LRU(3)
    lru.put(5, 101)
    lru.put(7, 111)
    lru.put(9, 1010)
    print(lru.get(7))
    print(lru.get(100))
    lru.put(7, 1011)
    lru.put(11, 1011)
    print(lru.get(5))

if __name__ == "__main__":
    main()