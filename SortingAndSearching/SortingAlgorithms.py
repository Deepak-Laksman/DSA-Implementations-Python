# Time Complexity O(n ^ 2) Space Complexity O(1)

# Bubble Sort

def bubbleSort(array, n):
    for i in range(n - 1):
        swapped = False
        for j in range(i + 1, n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
                swapped = True
        if not swapped:
            return

# Selection Sort

def selectionSort(array, n):
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if array[j] < array[minIndex]:
                minIndex = j
        if i != minIndex:
            array[minIndex], array[i] = array[i], array[minIndex]

# Insertion Sort

def insertionSort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Time Complexity O(n * log(n)) Space Complexity is O(1)

# Heap Sort

def heapify(array, n, i):
    largest = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    if leftChild < n and array[leftChild] > array[largest]:
        largest = leftChild
    if rightChild < n and array[rightChild] > array[largest]:
        largest = rightChild
    if i != largest:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)

def heapSort(array, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    for i in range(n):
        print(array[n - i - 1], end = " ")
    print()

# Time Complexity O(n * log(n)) Space Complexity O(n)

# Merge Sort

def merge(array, start, middle, end):
    left = array[start: middle]
    right = array[middle: end]
    i, j, k = 0, 0, 0
    l = len(left)
    r = len(right)
    while i < l and j < r:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < l:
        array[k] = left[i]
        k += 1
        i += 1
    while j < r:
        array[k] = right[j]
        k += 1
        j += 1

def mergeSort(array, start, end):
    while start < end:
        middle = (start + end) // 2
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)

# Time Complexity O(n * log(n)) Space Complexity O(1)

# Quick Sort

def partition(array, start, end):
    pivot = end
    j = start
    for i in range(start, end - 1):
        if array[i] < array[pivot]:
            array[j], array[i] = array[i], array[j]
            j += 1
    array[pivot], array[j + 1] = array[j + 1], array[pivot]
    return j + 1

def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

def main():
    """
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    bubbleSort(array, len(array))
    print(array)
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    selectionSort(array, len(array))
    print(array)
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    insertionSort(array, len(array))
    print(array)
    """
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    heapSort(array, len(array))
    print(array)
    """
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    mergeSort(array, 0, len(array) - 1)
    print(array)
    array = [3, 5, 1, 9, 11, 10, 50, 43, 29, 33, 54]
    quickSort(array, 0, len(array) - 1)
    print(array)
    """

if __name__ == "__main__":
    main()
