import sys

MAXN = 10 ** 6 + 1
ETF = [0] * MAXN

def ETF_using_sieve():
    for i in range(2, MAXN):
        ETF[i] = i
    i = 2
    ETF[0] = ETF[1] = 0
    while i * i <= MAXN:
        if ETF[i] == i:
            ETF[i] = i - 1
            for j in range(i * i, MAXN, i):
                ETF[j] *= i - 1
                ETF[j] //= i
        i += 1

def main():
    ETF_using_sieve()
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        N = int(sys.stdin.readline())
        print(ETF[N])

if __name__ == "__main__":
    main()