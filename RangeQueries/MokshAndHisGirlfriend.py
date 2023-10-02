# The problem is find the maximum number of m's in the array after performing q - 1 out of the given q queries.

# The idea here is to first perform all the queries first and make the array.
# Also we have to maintain 2 arrays to store count of m's and m + 1's in each index.

# Then once again we traverse through all queries and use the following formula,  total count - loss of m's + gain of m's
# Loss of m's = no. of m's in range of the query, which can be found using prefix count array of m
# Gain of m's = no. of m + 1's in range of the query, which can be found using prefix count array of m + 1

def main():
    n, q, m = map(int ,input().split())
    queries = []
    array = [0] * n

    for _ in range(q):
        l, r = map(int, input().split())
        array[l] += 1
        if r != n - 1:
            array[r + 1] -= 1
        queries.append((l, r))
    
    for i in range(1, n):
        array[i] += array[i - 1]
    
    prefixCountM = [0] * n
    prefixCountM_1 = [0] * n
    prefixCountM[0] = 1 if array[0] == m else 0
    prefixCountM_1[0] = 1 if array[0] == m + 1 else 0
    
    for i in range(1, n):
        prefixCountM_1[i] = 1 if array[i] == m + 1 else 0
        prefixCountM[i] = 1 if array[i] == m else 0
        prefixCountM[i] += prefixCountM[i - 1]
        prefixCountM_1[i] += prefixCountM_1[i - 1]
    
    total_ms = prefixCountM[n - 1]
    max_ms = 0
    for l, r in queries:
        if l == 0:
            loss = prefixCountM[r]
            gain = prefixCountM_1[r]
            max_ms = max(max_ms, total_ms - loss + gain)
        else:
            loss = prefixCountM[r] - prefixCountM[l - 1]
            gain = prefixCountM_1[r] - prefixCountM_1[l - 1]
            max_ms = max(max_ms, total_ms - loss + gain)
    print(max_ms)

if __name__ == "__main__":
    main()    