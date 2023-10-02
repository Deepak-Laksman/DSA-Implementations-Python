def merge(array, l, mid, r):
    k = l
    leftArray = array[l : mid]
    rightArray = array[mid : r]
    i, j = 0, 0
    left, right = len(leftArray), len(rightArray)
    while i < left and j < right:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1
    while i < left:
        array[k] = leftArray[i]
        i += 1
        k += 1
    while j < right:
        array[k] = rightArray[j]
        j += 1
        k += 1
    
def mergeSort(array, l, r):
    if (r - l) > 1:
        mid = l + (r - l) // 2
        mergeSort(array, l, mid)
        mergeSort(array, mid + 1, r)
        merge(array, l, mid, r)

def sortArray(array, n):
    if n == 1:
        return
    sortArray(array, n - 1)
    mergeSort(array, 0, n)

# Another Approach

def insert(array, value):
    if len(array) == 0 or array[len(array) - 1] <= value:
        array.append(value)
        return
    temp = array[len(array) - 1]
    array.pop()
    insert(array, value)
    array.append(temp)

def sorting(array):
    if len(array) == 0:
        return
    temp = array[len(array) - 1]
    array.pop()
    sorting(array)
    insert(array, temp)

def main():
    n = int(input())
    array = [int(a) for a in input().split()]
    sorting(array)
    print(*array)

if __name__ == "__main__":
    main()