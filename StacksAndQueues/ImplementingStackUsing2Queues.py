class Stack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def isEmpty(self):
        if len(self.queue1) == 0:
            return True
        return False

# Time Complexity is O(N), Space Complexity is O(2N)
    def push(self, val):
        self.queue2.append(val)
        while not self.isEmpty():
            self.queue2.append(self.top())
            self.pop()
        self.queue2, self.queue1 = self.queue1, self.queue2

    def pop(self):
        self.queue1.pop(0)
    
    def top(self):
        return self.queue1[0]

def main():
    stack = Stack()
    stack.push(1)
    stack.push(-1)
    stack.push(3)
    print(stack.top())
    stack.pop()
    print(stack.top())

if __name__ == "__main__":
    main()