# There can only be one prime divisor above sqrt of n

# Time Complexity is O(sqrt(n))
def prime_factorization(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:    # Time Complexity is O(log(n))
                n = n // i
                count += 1
            print(i, "^", count)
        i += 1
    if n > 1:
        print(n, "^", 1)