# Time Complexity is O(log(m))
def modulo_inverse(a, m):
    return pow(a, m - 2, m)