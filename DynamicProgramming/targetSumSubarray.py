def subarraySumExists(array, target):
    curr_sum = 0
    n = len(array)
    prev_sum = 0
    start = 0
    for i in range(n):
        prev_sum = curr_sum
        curr_sum += array[i]        
        if target == curr_sum:
            return True
        elif curr_sum > target:
            curr_sum -= array[start]
            start += 1
        elif curr_sum < prev_sum and prev_sum < target:
            curr_sum = 0
    return False

def main():
    array = [int(a) for a in input().split()]
    target = int(input())
    print(subarraySumExists(array, target))

if __name__ == "__main__":
    main()