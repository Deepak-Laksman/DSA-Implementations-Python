def spacePermutations(input, output):
    if len(input) == 0:
        print(output)
        return
    output1 = output + input[0]
    output2 = output + " " + input[0]
    input = input[1:]
    spacePermutations(input, output1)
    spacePermutations(input, output2)

def main():
    string = input().strip("\n")
    spacePermutations(string[1:], string[0])

if __name__ == "__main__":
    main()