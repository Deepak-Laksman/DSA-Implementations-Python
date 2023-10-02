def reverse(arr):
    if len(arr) == 0:
        return
    temp = arr.pop(0)
    reverse(arr)
    arr.append(temp)

def main():
    arr = [int(a) for a in input().split()]
    reverse(arr)
    print(*arr)

if __name__ == "__main__":
    main()