# Time Complexity is O(log(n))
def power(a, b):
    ans = 1
    while b > 0:
        if b & 1:
            ans *= a
        a *= a
        b >>= 1
    return ans

def recur_power(a, b, memo = None):
    if memo is None:
        memo = {}
    if b == 0:
        return 1
    if b in memo.keys():
        return memo[b]
    temp = recur_power(a, b // 2, memo)
    if b % 2:
        ans = temp * temp * a
    else:
        ans = temp * temp
    memo[b] = ans
    return ans