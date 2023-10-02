class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, val):
        if self.head is None:
            temp = Node(val)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(val)
            temp.next = self.head.next
            self.head = temp

    def insertLast(self, val):
        if self.tail is None:
            temp = Node(val)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(val)
            self.tail.next = temp
            self.tail = temp

    def insertAt(self, val, position):
        if self.head is None:
            temp = Node(val)
            self.head = temp
            self.tail = temp
        else:
            current = self.head
            i = 1
            while i != position or current.next is not None:
                current = current.next
                i += 1
            temp = Node(val)
            if current.next is None:
                current.next = temp
                self.tail = temp
            else:
                temp.next = current.next
                current.next = temp

    def deleteFirst(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def deleteLast(self):
        if self.head is None:
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        temp = current.next
        current.next = None
        self.tail = current
        del temp

    def deleteAt(self, position):
        if self.head is None:
            return
        i = 1
        current = self.head
        while current.next is not None or i != position - 1:
            current = current.next
            i += 1
        if current.next is None:
            self.deleteLast()
        else:
            temp = current.next
            current.next = current.next.next
            del temp

    def printList(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            print(current.val, end = " ")
        print()
