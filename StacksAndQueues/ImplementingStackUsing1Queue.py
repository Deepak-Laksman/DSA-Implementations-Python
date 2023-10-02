class Stack:

    def __init__(self):
        self.queue = []

# Time Complexity -> O(N), Space Complexity -> O(N)
    def push(self, val):
        self.queue.append(val)
        n = len(self.queue)
        if n > 1:
            for i in range(n - 1):
                self.queue.append(self.top())
                self.pop()
    
    def pop(self):
        self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

def main():
    stack = Stack()
    stack.push(3)
    stack.push(10)
    stack.push(1)
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.pop()

if __name__ == "__main__":
    main()