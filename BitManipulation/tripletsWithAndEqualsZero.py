# INCOMPLETE

import sys

def tripletsCount(n, array):
    hashmap = {}
    for i in range(n):
        if array[i] in hashmap.keys():
            hashmap[array[i]] += 1
        else:
            hashmap[array[i]] = 1

    triplets = 0
    for i in range(n):
        for j in range(n):
            andValue = array[i] & array[j]
            if i == j:
                triplets += n - 1
            elif andValue in hashmap.keys():
                triplets += hashmap[andValue]
    
    return triplets - 1

def main():
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]
    print(tripletsCount(n, array))

if __name__ == "__main__":
    main()