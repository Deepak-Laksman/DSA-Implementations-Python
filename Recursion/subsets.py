def makeSubsets(input, output):
    if len(input) == 0:
        print(output)
        return
    output1 = output
    output2 = output
    output2 += input[0]
    input = "" + input[1:]
    makeSubsets(input, output1)
    makeSubsets(input, output2)

def main():
    string = input().strip("\n")
    makeSubsets(string, "")

if __name__ == "__main__":
    main()