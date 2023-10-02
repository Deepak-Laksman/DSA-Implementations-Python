class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def isEmpty(self):
        if len(self.stack1) == 0:
            return True
        return False

# Time Complexity is O(2N), Space COmplexity is O(2N) 
    def push(self, val):
        while not self.isEmpty():
            self.stack2.append(self.top())
            self.pop()
        self.stack1.append(val)
        while len(self.stack2):
            self.stack1.append(self.stack2[-1])
            self.stack2.pop(-1)

    def pop(self):
        if self.isEmpty():
            return
        self.stack1.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.stack1[-1]

def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.top())
    queue.pop()
    print(queue.top())

if __name__ == "__main__":
    main()