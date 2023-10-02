def insert(stack, value):
    if len(stack) == 0:
        stack.append(value)
        return
    temp = stack.pop()
    insert(stack, value)
    stack.append(temp)

def reverse(stack):
    if len(stack) == 1:
        return
    value = stack.pop()
    reverse(stack)
    insert(stack, value)

def main():
    stack = [int(a) for a in input().split()]
    reverse(stack)
    print(*stack)

if __name__ == "__main__":
    main()