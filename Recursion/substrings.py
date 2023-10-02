




# INCOMPLETE






def printSubstringsHelper(string, start, end):
    if len(string) == end - start:
        print(string[start:end])
        return
    print(string[start:end])
    printSubstringsHelper(string, start, end + 1)

def printSubstrings(string, start):
    if len(string) == start:
        return
    printSubstringsHelper(string[start:], start, start + 1)
    printSubstrings(string, start + 1)

def main():
    string = input().strip("\n")
    printSubstrings(string, 0)

if __name__ == "__main__":
    main()