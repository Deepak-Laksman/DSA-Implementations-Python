def isValidSequence(bracketSequence):
    brackets = ["(", "{", "["]
    n = len(bracketSequence)
    if n == 0:
        return True
    stack = []
    stack.append(bracketSequence[0])
    i = 1
    while i < n:
        if bracketSequence[i] in brackets:
                stack.append(bracketSequence[i])
        else:
            if len(stack) == 0:
                return False
            elif bracketSequence[i] == "}" and stack[-1] != "{":
                return False
            elif bracketSequence[i] == "]" and stack[-1] != "[":
                return False
            elif bracketSequence[i] == ")" and stack[-1] != "(":
                return False
            else:
                stack.pop()
        i += 1
    if len(stack) > 0:
        return False
    return True

def main():
    bracketSequence = input().strip("\n")
    print(isValidSequence(bracketSequence))

if __name__ == "__main__":
    main()