def reverseLinkedListUsingStack(head):
    if not head or not head.next:
        return head
    current = head
    stack = []
    while current:
        stack.append(current)
        current = current.next
    node = stack[len(stack) - 1]
    head = node
    stack.pop()
    while len(stack) > 0:
        node.next = stack[len(stack) - 1]
        stack.pop()
        node = node.next
    node.next = None
    return head

def balancedParantheses(string):
    if string == "":
        return
    stack = []
    if string[0] == "}" or string[0] == "]" or string[0] == ")":
        return False
    stack.append(string[0])
    n = len(string)
    i = 1
    while len(stack) != 0 and i < n:
        if string[i] == "}":
            x = stack.pop()
            if x != "{":
                return False
        elif string[i] == "]":
            x = stack.pop()
            if x != "[":
                return False
        elif string[i] == ")":
            x = stack.pop()
            if x != "(":
                return False
        else:
            stack.append(string[i])
        i += 1
    if len(stack) > 0:
        return False
    return True

# Infix, Prefix, Postfix

# Infix -> operator is placed in between operators
# Prefix -> created to remove ambiguity of brackets while calculating expressions with brackets
# Postfix -> operands will be preceded by operators

import math

def performOperation(operand1, operand2, operator):
    if operator == "+":
        return int(operand2) + int(operand1)
    elif operator == "-":
        return int(operand2) - int(operand1)
    elif operator == "*":
        return int(operand2) * int(operand1)
    elif operator == "^":
        return int(math.pow(int(operand2), int(operand1)))
    elif operator == "/":
        return int(operand2) // int(operand1)

def evaluatePostfix(postfix):
    operators = ["+", "-", "*", "/", "^"]
    n = len(postfix)
    stack = []
    for i in range(n):
        if postfix[i] not in operators:
            stack.append(postfix[i])
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = performOperation(operand1, operand2, postfix[i])
            stack.append(result)
    return stack[0]

def evaluatePrefix(prefix):
    operators = ["+", "-", "*", "/", "^"]
    n = len(prefix)
    stack = []
    for i in range(n - 1, -1 , -1):
        if prefix[i] not in operators:
            stack.append(prefix[i])
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = performOperation(operand2, operand1, prefix[i])
            stack.append(result)
    return stack[0]

def convertInfixToPostfix(infix):
    operators = {}
    operators["+"] = 0
    operators["-"] = 0
    operators["*"] = 1
    operators["/"] = 1
    operators["^"] = 2
    stack = []
    postfix = []
    n = len(infix)
    for i in range(n):
        if infix[i] not in operators.keys():
            postfix.append(infix[i])
        else:
            if len(stack) == 0:
                stack.append(infix[i])
            else:
                if operators[stack[len(stack) - 1]] < operators[infix[i]]:
                    stack.append(infix[i])
                else:
                    while len(stack) > 0 and operators[stack[len(stack) - 1]] >= operators[infix[i]]:
                        postfix.append(stack.pop())
                    stack.append(infix[i])
    if len(stack) > 0:
        n = len(stack)
        while n > 0:
            postfix.append(stack.pop())
            n -= 1
    return postfix

import sys

def main():
    """
    print("Enter a bracket sequence to check whether its valid or not:", end = "\t")
    bracketSequence = sys.stdin.readline().strip("\n")
    print(balancedParantheses(bracketSequence))
    print("Enter a Postfix Expression whose value need to be calculated:", end = "\t")
    postfix = sys.stdin.readline().strip("\n")
    print(evaluatePostfix(postfix))
    print("Enter a Prefix Expression whose value need to be calculated:", end = "\t")
    prefix = sys.stdin.readline().strip("\n")
    print(evaluatePrefix(prefix))
    """
    print("Enter Infix Expression that need to be converted into Postfix:", end = "\t")
    infix = sys.stdin.readline().strip("\n")
    print(*convertInfixToPostfix(infix))

if __name__ == "__main__":
    main()