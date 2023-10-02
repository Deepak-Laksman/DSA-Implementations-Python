
# Time Complexity is O(log(max(a, b))) Space Complexity is O(log(max(a, b)))
def gcd_recur(a, b):
    if b == 0:
        return a
    return gcd_recur(b, a % b)


