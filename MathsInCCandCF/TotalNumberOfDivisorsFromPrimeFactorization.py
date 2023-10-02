import sys

# Formula for counting number of divisors is (p1 + 1) * (p2 + 1) * (p3 + 1) ...., where p1, p2, p3 are the count
# of distinct prime factors.

# Time Complexity is O(sqrt(n))
def divisors_count(n):
    answer = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            answer *= (count + 1)
        i += 1
    if n > 1:
        answer *= 2
    return answer

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        n = int(sys.stdin.readline())
        print(divisors_count(n))

if __name__ == "__main__":
    main()