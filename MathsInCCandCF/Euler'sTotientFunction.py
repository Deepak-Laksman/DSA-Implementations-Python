import sys

# Number of co_primes of N = (N * (P1 - 1) * (P2 - 1) * ... * (Pk - 1)) // (P1 * P2 * P3 * ... * Pk)

# Time Complexity is O(sqrt(N))
def count_co_primes(N):
    result = N
    i = 2
    while i * i <= N:
        if N % i == 0:
            result *= (i - 1)
            result = result // i
            while N % i == 0:
                N = N // i
        i += 1
    if N > 1:
        result //= N
        result *= (N - 1)
    return result

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        N = int(sys.stdin.readline())
        print(count_co_primes(N))

if __name__ == "__main__":
    main()