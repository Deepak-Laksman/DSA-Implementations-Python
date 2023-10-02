def deleteMiddle(stack, middle, size):
    if middle == 1:
        stack.pop()
        if size % 2 == 0:
            stack.pop()
        return
    value = stack.pop()
    deleteMiddle(stack, middle - 1, size)
    stack.append(value)

def main():
    stack = [int(a) for a in input().split()]
    length = len(stack)
    if length & 1:
        deleteMiddle(stack, length // 2 + 1, length)
    else:
        deleteMiddle(stack, length // 2, length)
    print(*stack)

if __name__ == "__main__":
    main()