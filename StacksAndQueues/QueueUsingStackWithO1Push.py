class Queue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, val):
        self.input.append(val)

    def isEmpty(self):
        if len(self.output) == 0:
            return True
        return False

# Time Complexity is O(N), Space Complexity is O(2N)
    def top(self):
        if self.isEmpty():
            while len(self.input):
                self.output.append(self.input[-1])
                self.input.pop(-1)
            return self.output[-1]
        else:
            return self.output[-1]

# Time Complexity is O(N), Space COmplexity is O(2N)
    def pop(self):
        if self.isEmpty():
            while len(self.input):
                self.output.append(self.input[-1])
                self.input.pop(-1)
            self.output.pop(-1)
        else:
            self.output.pop(-1)

def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.top())
    queue.pop()
    print(queue.top())
    queue.pop()

if __name__ == "__main__":
    main()