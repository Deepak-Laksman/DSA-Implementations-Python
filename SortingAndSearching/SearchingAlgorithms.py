import math

# Linear Search

def linearSearch(array, n, target):
    for i in range(n):
        if array[i] == target:
            return i + 1
    return -1

# Binary Search

def binarySearch(array, n, target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Jump Search

def jumpSearch(array, n, target):
    block = int(math.sqrt(n))
    index = -1
    for i in range(0, n, block):
        if array[i] == target:
            return i + 1
        elif array[i] > target:
            index = i
            break
    if index == -1:
        return -1
    for i in range(index - block, index):
        if array[i] == target:
            return i + 1
    return -1