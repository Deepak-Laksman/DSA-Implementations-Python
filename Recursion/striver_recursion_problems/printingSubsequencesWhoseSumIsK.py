def subsequences_with_sum_k(i, op, k, n, arr):
    if k < 0:
        return
    if k == 0:
        print(op)
        return
    if i == n:
        return
    op.append(arr[i])
    subsequences_with_sum_k(i + 1, op, k - arr[i], n, arr)
    op.pop()
    subsequences_with_sum_k(i + 1, op, k, n, arr)

def print_only_one_subsequence(i, op, k, n, arr):
    if k < 0:
        return False
    if k == 0:
        print(op)
        return True
    if i == n:
        return False
    op.append(arr[i])
    if print_only_one_subsequence(i + 1, op, k - arr[i], n, arr):
        return True
    op.pop()
    if print_only_one_subsequence(i + 1, op, k, n, arr):
        return True
    return False

def count_subsequences_with_sum_k(i, k, n, arr):
    if k < 0:
        return 0
    if k == 0:
        return 1
    if i == n:
        return 0
    return count_subsequences_with_sum_k(i + 1, k - arr[i], n, arr) + count_subsequences_with_sum_k(i + 1, k, n, arr)

def main():
    arr = [int(a) for a in input().split()]
    print(count_subsequences_with_sum_k(0, 5, len(arr), arr))

if __name__ == "__main__":
    main()