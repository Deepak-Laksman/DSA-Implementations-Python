# Prefix Sum

# Useful to get total sum of elements in range i to j in O(1)

def makePrefixSumArray(array):
    n = len(array)
    prefixSum = [0] * (n)
    prefixSum[0] = array[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + array[i]
    return prefixSum


# Prefix Count

# This is done for a particular value in the array, usually in binary arrays

# Useful to get frequency of a number in the given range in O(1)

def makePrefixCountArray(array):
    n = len(array)
    prefixCount = [0] * (n)
    prefixCount[0] = 1 if array[0] == 0 else 0
    for i in range(1, n):
        prefixCount[i] = 1 if array[i] == 0 else 0
        prefixCount[i] += prefixCount[i - 1]
    return prefixCount