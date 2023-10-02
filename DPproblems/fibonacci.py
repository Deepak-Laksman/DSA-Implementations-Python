# TC -> O(n), SC -> O(n) + O(n) [stack space]
def fib_mem(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        print("varudha")
        return dp[n]
    dp[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return dp[n]

# TC -> O(n), SC -> O(n)
def fib_tab(n, dp):
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# TC -> O(n), SC -> O(1)
def fib_space(n):
    prev = 0
    prev2 = 1
    for i in range(2, n + 1):
        cur = prev + prev2
        prev = prev2
        prev2 = cur
    return prev2 if n != 0 else prev

def main():
    n = int(input())
    dp = [0] * (n + 1)
    print(fib_mem(n, dp))

if __name__ == "__main__":
    main()