# Given k queries with start and end index along with the value to be filled in the array in that range
# Print tthe final array

# Naive approach would be to fill the array in the given range with given value every single time

# TC is O(n * q)

# Optimal Approach, store the value in start index and negative of that value in end + 1 index, so at the end when u do prefix sum,
# that value will not be added to indices more than end as it will neutralize to 0 at the (end +1)th index.

# TC is O(n + q)

def main():
    # size of array and no. of queries
    n, q = map(int, input().split())
    array = [0] * n
    for _ in range(q):
        l, r, val = map(int ,input().split())
        array[l] += val
        if r != n - 1:
            array[r + 1] -= val
    for i in range(1, n):
        array[i] += array[i - 1]
    print(*array)

if __name__ == "__main__":
    main() 