def oddOrEven(n):
    if n & 1:
        return "ODD"
    else:
        return "EVEN"

def clearIthBit(n, i):
    bitmask = ~(1 << i)
    n &= bitmask
    return n

def setIthBit(n, i):
    bitmask = (1 << i)
    n |= bitmask
    return n

def getIthBit(n, i):
    bitmask = (1 << i)
    iThBit = 1 if (n & bitmask) else 0
    return iThBit

def updateIthBit(n, i):
    bit = getIthBit(n, i)
    if bit:
        n = clearIthBit(n, i)
    else:
        n = setIthBit(n, i)
    return n

def clearRangeOfBits(n, i, j):
    bitMask1 = (1 << i)
    bitMask2 = (1 << (j + 1)) - 1
    bitMask = bitMask1 | bitMask2
    n &= bitMask
    return n

def clearLastIbits(n, i):
    bitmask = (-1 << i)
    n &= bitmask
    return n

def isPowerOfTwo(n):
    if n & (n - 1):
        return True
    else:
        return False

def isPowerOfFour(n):
    if n & (n - 1) and n % 3 == 1:
        return True
    else:
        return False

def countBitsFast(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

def convertToBinary(n):
    binary = 0
    p = 1
    while n:
        binary += p * (n & 1)
        p *= 10
        n >>= 1
    return binary