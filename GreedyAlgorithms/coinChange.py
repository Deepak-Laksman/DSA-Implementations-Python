import sys

def minimumDenominations(n, amount, denominations):
    denominations.sort(reverse = True)
    denominationsUsed = 0
    i = 0
    while i < n and amount > 0:
        if denominations[i] <= amount:
            amount -= denominations[i]
            denominationsUsed += 1
        else:
            i += 1
    if amount != 0:
        return -1
    return denominationsUsed


def main():
    n, amount = map(int, sys.stdin.readline().split())
    denominations = [int(d) for d in sys.stdin.readline().split()]
    print(minimumDenominations(n, amount, denominations))

if __name__ == "__main__":
    main()