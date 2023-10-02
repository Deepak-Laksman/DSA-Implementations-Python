def insert(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return
    temp = stack.pop()
    insert(stack, value)
    stack.append(temp)

def sorting(stack):
    if len(stack) == 1:
        return
    temp = stack.pop()
    sorting(stack)
    insert(stack, temp)

def main():
    stack = [int(a) for a in input().split()]
    sorting(stack)
    print(*stack)

if __name__ == "__main__":
    main()