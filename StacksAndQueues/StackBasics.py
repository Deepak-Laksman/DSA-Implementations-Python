# Stack Implementation using Arrays

class Stack:
    def __init__(self):
        self.top = -1
        self.max = 10000
        self.stack = [] * 10000

    def push(self, val):
        if self.top >= self.max - 1:
            print("Stack Overflow.")
        else:
            self.top += 1
            self.stack[self.top] = val

    def pop(self):
        if self.top < 0:
            print("Stack Underflow.")
            return
        else:
            temp = self.stack[self.top]
            self.top -= 1
            return temp

    def peek(self):
        if self.top < 0:
            print("Stack is empty.")
        else:
            return self.stack[self.top]

    def isEmpty(self):
        if self.top < 0:
            return True
        return False

# Circular Stack Implementation Using Arrays

class CircularStack:
    
    def __init__(self):
        self.top = -1
        self.max = 10000
        self.stack = [0] * (self.max)

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if (self.top + 1) % self.max == 0:
            return True
        return False

    def push(self, val):
        if self.isFull():
            print("Stack Overflow")
            return
        else:
            self.top = (self.top + 1) % self.max
        self.stack[self.top] = val

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            self.top = (self. top - 1) % self.max
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        else:
            return self.stack[self.top]

# Implementing Stack Using LinkedLists

class ListNode:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class StackLL:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def push(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        else:
            temp = self.head
            self.head = self.head.next
            val = temp.val
            del temp
            return val
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        else:
            return self.head.val
