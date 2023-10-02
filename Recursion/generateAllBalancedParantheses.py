def generateAllParantheses(open, close, string, parantheses):
    if open == 0 and close == 0:
       parantheses.append(string)
       return
    if open == 0:
        output = string + ")"
        generateAllParantheses(open, close - 1, output, parantheses)
    elif open >= close:
        output = string + "("
        generateAllParantheses(open - 1, close, output, parantheses)
    elif close > open:
        output1 = string + "("
        output2 = string + ")"
        generateAllParantheses(open - 1, close, output1, parantheses)
        generateAllParantheses(open, close - 1, output2, parantheses)


     
def main():
    n = int(input())
    parantheses = []
    generateAllParantheses(n, n, "", parantheses)
    print(*parantheses)

if __name__ == "__main__":
    main()