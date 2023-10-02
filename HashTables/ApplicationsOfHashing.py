# Rabin-Karp's Algorithm

# We need to find the number of occurrences of a specific string in another string

# Now in this algorithm, we just create a hash function for the strings. Now to compare 2 strings,
# we just call the hash function and calculate hash value of both the specific string and
# the substring of the main string. If they are equal, then we call the isEqual() function to check
# character by character. So this reduces the number of calls to the isEqual() function whose
# time complexity is O(length of specific string). The overall time complexity is
# O((length of main string) * (length of specific string))

import math
mod = 10 ** 7 + 9

def hashFunction(string, n, x):
    hashArray = [0] * (n - x + 1)
    q = 31
    y = int(math.pow(31, x))
    for i in range(n - x - 1, -1, -1):
        hashArray[i] = (q * hashArray[i + 1] + ord(string[i]) - 97 - y * ord(string[i + x]) - 97) % mod
    return hashArray

def hashFunctionTest(string, n):
    hashValue = 0
    x = 1
    for i in range(n):
        hashValue = (hashValue + (ord(string[i]) - 96) * (i + 1)) * x
        x += 1
    return hashValue

def isEqual(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        x = len(string1)
        for i in range(x):
            if string1[i] != string2[i]:
                return False
        return True

def rabinKarp(string, target):
    n = len(string)
    x = len(target)
    hashArray = hashFunction(string, n, x)
    answer = []
    hashValueOfTarget = hashFunction(target, n, x)
    for i in range(n - x + 1):
        subString = string[i: i + x]
        if hashArray[i] == hashValueOfTarget:
            if isEqual(subString, target):
                answer.append(i)
    return answer

import sys

def main():
    string = sys.stdin.readline().strip("\n")
    target = sys.stdin.readline().strip("\n")
    print(*rabinKarp(string, target))

if __name__ == "__main__":
    main()