from math import ceil

n = 4000 + 1
primes = [True] * n

prime_set = set()

def prime_sieve():
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    for i in range(2, n):
        if primes[i]:
            prime_set.add(i)

def find_ways(n):
    global prime_set
    ans = 0
    val = 1
    for prime in prime_set:
        count = 0
        flag = -1
        while n % prime == 0:
            n //= prime
            count += 1
            if flag == -1:
                val *= prime
                flag = 1
        if count % 2:
            ans += 1
        ans += int(ceil(count / 2))
    return ans + val


def main():
    n = int(input())
    prime_sieve()
    print(find_ways(n))

if __name__ == "__main__":
    main()