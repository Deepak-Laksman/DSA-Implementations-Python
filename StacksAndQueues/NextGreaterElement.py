# Time Complexity is O(2N + 2N), Space Complexity is O(2N)

def nextGreaterElement(array):
    stack = []
    n = len(array)
    nge = [-1] * n
    for i in range(2 * n - 1, -1, -1):
        while stack and stack[-1] <= array[i % n]:
            stack.pop()
        if len(stack) > 0:
            nge[i % n] = stack[-1]
        stack.append(array[i % n])
    return nge

def main():
    array = [int(a) for a in input().split()]
    print(*nextGreaterElement(array))

if __name__ == "__main__":
    main()