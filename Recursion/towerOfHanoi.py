def arrangement(source, helper, destination, n):
    if n == 1:
        print("Moving plate " + str(n) + " from " + source + " to " + destination)
        return
    arrangement(source, destination, helper, n - 1)
    print("Moving plate " + str(n) + " from " + source + " to " + destination)
    arrangement(helper, destination, source, n - 1)
    
def main():
    n = int(input())
    arrangement("1", "2", "3", n)  # 1 -> source, 2 -> helper, 3 -> destination

if __name__ == "__main__":
    main()
