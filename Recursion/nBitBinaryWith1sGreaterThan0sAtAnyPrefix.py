def makeNbitBinaryNumber(onesCount, zeroesCount, number, n):
    if onesCount + zeroesCount == n:
        print(number)
        return
    if onesCount > zeroesCount + 1:
        number1 = number + "0"
        makeNbitBinaryNumber(onesCount, zeroesCount + 1, number1, n)
        number2 = number + "1"
        makeNbitBinaryNumber(onesCount + 1, zeroesCount, number2, n)
    else:
        number1 = number + "1"
        makeNbitBinaryNumber(onesCount + 1, zeroesCount, number1, n)

def main():
    n = int(input())
    number = ""
    makeNbitBinaryNumber(0, 0, number, n)

if __name__ == "__main__":
    main()