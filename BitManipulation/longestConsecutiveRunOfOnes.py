import sys

def longestOnesCount(n):
    answer = 0
    count = 0 
    while n:
        if n & 1:
            count += 1
        else:
            answer = max(answer, count)
            count = 0
        n >>= 1
    answer = max(answer, count)
    return answer

def main():
    n = int(sys.stdin.readline())
    print(longestOnesCount(n))
    
if __name__ == "__main__":
    main()