import sys

sys.stdin, sys.stdout = open("input.txt", "r"), open("output.txt", "w")

def minimumNumberOfGroups(childrenCount, childrenAges):
    groups = []
    childrenAges.sort()
    groupsCount = 1
    temp = []
    for i in range(1, childrenCount):
        if childrenAges[i] - childrenAges[i - 1] > 1:
            groupsCount += 1
            groups.append(temp)
            temp = []
        temp.append(childrenAges[i])
    return groupsCount, groups

def main():
    childrenCount = int(sys.stdin.readline())
    childrenAges = [int(a) for a in sys.stdin.readline().split()]
    print(minimumNumberOfGroups(childrenCount, childrenAges))

if __name__ == "__main__":
    main()