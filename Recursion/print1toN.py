def printI(n, i):
    if i == n:
        print(i)
        return
    print(i, end = " ")
    printI(n, i + 1)

def printN(n):
    if n == 0:
        print()
        return
    printN(n - 1)
    print(n, end = " ")

def main():
    n = int(input())
    printI(n, 1)
    printN(n)

if __name__ == "__main__":
    main()