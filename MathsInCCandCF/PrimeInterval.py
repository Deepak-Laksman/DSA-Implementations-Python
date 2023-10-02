def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
    return True

def primeInterval(L, R):
    while L <= R:
        if is_prime(L):
            print(L, end = " ")
        L += 1
    print()