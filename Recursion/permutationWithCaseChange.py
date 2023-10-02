def permutations(input, output):
    if len(input) == 0:
        print(output)
        return
    output1 = output + input[0].lower()
    output2 = output + input[0].upper()
    input = input[1:]
    permutations(input, output1)
    permutations(input, output2)

def main():
    string = input().strip("\n")
    permutations(string, "")

if __name__ == "__main__":
    main()