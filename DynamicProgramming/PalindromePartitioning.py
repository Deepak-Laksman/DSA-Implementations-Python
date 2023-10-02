def isPalindrome(string, i, j):
    x = j - i + 1
    for k in range(x):
        if string[i + k] != string[j - k]:
            return False
    return True

def minimumPartitionsToMakePalindromesRecursive(string, i, j):
    if i >= j:
        return 0
    if isPalindrome(string, i, j):
        return 0
    partitions = float("inf")
    for k in range(i, j):
        tempPartitions = minimumPartitionsToMakePalindromesRecursive(string, i, k) + minimumPartitionsToMakePalindromesRecursive(string, k + 1, j) + 1
        partitions = min(partitions, tempPartitions)
    return partitions

def minimumPartitionsToMakePalindromesMemoized(string, i, j, memo = None):
    if memo is None:
        memo = {}
    if i >= j:
        return 0
    if isPalindrome(string, i, j):
        return 0
    if (i, j) in memo.keys():
        return memo[(i, j)]
    partitions = float("inf")
    for k in range(i, j):
        if (i, k) in memo.keys() and (k + 1, j) in memo.keys():
                tempPartitions = memo[(i, k)] + memo[(k + 1, j)] + 1
        elif (i, k) in memo.keys():
                memo[(k + 1, j)] = minimumPartitionsToMakePalindromesMemoized(string, k + 1, j, memo)
        else:
            memo[(i, k)] = minimumPartitionsToMakePalindromesMemoized(string, i, k, memo)
            memo[(k + 1, j)] = minimumPartitionsToMakePalindromesMemoized(string, k + 1, j, memo)
        tempPartitions = memo[(i, k)] + memo[(k + 1, j)] + 1
        partitions = min(partitions, tempPartitions)
        memo[(i, j)] = partitions
    return memo[(i, j)]


def minimumPartitionsToMakePalindromesDP(string):
    n = len(string)
    dp = [[float("inf") for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                dp[i][j] = 0
            if isPalindrome(string, i, j):
                dp[i][j] = 0    
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1 
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
    return dp[0][n - 1]


def main():
    string = input()
    n = len(string)
    print(minimumPartitionsToMakePalindromesMemoized(string, 0, n - 1))


if __name__ == "__main__":
    main()