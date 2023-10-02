def casePermutations(input, output, result):
    if len(input) == 0:
        result.add(output)
        return
    output1 = output
    output2 = output
    if input[0].isalpha():
        output1 += input[0].lower()
        output2 += input[0].upper()
    else:
        output1 += input[0]
        output2 += input[0]
    input = input[1:]
    casePermutations(input, output1, result)
    casePermutations(input, output2, result)

def main():
    string = input().strip("\n")
    result = set()
    casePermutations(string, "", result)
    print(*result)

if __name__ == "__main__":
    main()