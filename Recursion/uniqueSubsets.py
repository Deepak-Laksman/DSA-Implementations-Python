def makeUniqueSubsets(input, output, result):
    if len(input) == 0:
        result.add(output)
        return
    output1 = output2 = output
    output2 += input[0]
    input = "" + input[1: ]
    makeUniqueSubsets(input, output1, result)
    makeUniqueSubsets(input, output2, result)

def main():
    string = input().strip("\n")
    result = set()
    makeUniqueSubsets(string, "", result)
    print(*result)

if __name__ == "__main__":
    main()