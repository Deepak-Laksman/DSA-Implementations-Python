class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, val):
        if self.head is None:
            node = DoublyNode(val)
            self.head = node
            self.tail = node
        else:
            temp = self.head.next
            node = DoublyNode(val)
            self.head = node
            node.next = temp

    def insertLast(self, val):
        if self.head is None:
            node = DoublyNode(val)
            self.head = node
            self.tail = node
        else:
            node = DoublyNode(val)
            temp = self.tail.prev
            self.tail = node
            node.prev = temp

    def insertAt(self, val, position):
        if self.head is None:
            node = DoublyNode(val)
            self.head = node
            self.tail = node
        else:
            current = self.head
            i = 1
            while i <= position - 1:
                current = current.next
                i += 1
            node = DoublyNode(val)
            node.next = current.next
            current.next.prev = node
            node.prev = current
            current.next = node

