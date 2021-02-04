#7. Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
def reverse(x: int) -> int:
    temp = x
    if(x < 0):
        temp *= -1
    rev = 0
    while(temp > 0):
        r = temp % 10 
        rev = rev * 10 + r
        temp = temp // 10
    if(rev <= -2**31 or rev >= 2**31-1): return 0    
    elif(x < 0): return -1*rev
    return rev

n = int(input())
print(reverse(n))