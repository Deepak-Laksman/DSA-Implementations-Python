# Queue Implementation Using Arrays

class Queue:

    def __init__(self):
        self.front = self.rear = -1
        self.max = 10000
        self.queue = [0] * self.max

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self):
        if (self.rear + 1) % self.max == self.front:
            return True
        return False
    
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            return self.queue[self.front]

    def enqueue(self, val):
        if self.isFull():
            print("Stack Overflow")
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max
        self.queue[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max

# Queue Implementation Using LinkedList

class ListNode:
    
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class QueueLL:

    def __init__(self):
        self.head = self.tail = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        return self.head.val

    def enqueue(self, val):
        node = ListNode(val)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            temp = self.head
            self.head = self.head.next
            del temp
