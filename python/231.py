#231. Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

def isPowerOfTwo(n):
    if(n == 1):
        return True
    if(n % 2 != 0):
        return False
    return isPowerOfTwo(n//2)

n = int(input())
print(isPowerOfTwo(n))