import tarfile


class Node:

    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRU:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def addnode(self, node):
        temp = self.head.next
        node.next = temp
        self.head.next = node
        node.prev = self.head
        temp.prev = node

    def deletenode(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev

    def get(self, key):
        if key in self.map:
            required = self.map[key]
            value = required.val
            self.deletenode(required)
            self.addnode(required)
            self.map[key] = self.head.next
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            required = self.map[key]
            self.deletenode(required)
            newnode = Node(key, value)
            self.addnode(newnode)
            self.map[key] = self.head.next
        else:
            newnode = Node(key, value)
            self.addnode(newnode)
            self.map[key] = self.head.next

class LFU:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.freqList = {}
        self.map = {}

    def put(self, key, value):
        if key in self.map:
            pass
        else:
            if len(self.map) == self.capacity:
                pass
            else:
                freq = 1
                if freq not in self.freqList:
                    self.freqList[freq] = LRU()
                    self.freqList[freq].put(key, value)
                    self.map[key] = self.freqList[freq].head.next
                else:
                    self.freqList[freq].put(key, value)
                    self.map[key] = self.freqList[freq].head.next


def main():
    pass

if __name__ == "__main__":
    main()