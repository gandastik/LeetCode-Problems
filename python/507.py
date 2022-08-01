#507. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
import math
def checkPerfectNumber(num: int) -> bool:
    _sum = 0
    i = 1
    while(i <= math.sqrt(num)):
        if(num % i == 0):
            if(num / i == i):
                _sum += i
            else: _sum += i + num/i
        i+=1
    _sum -= num
    if(_sum == num):
        return True
    return False
num = int(input())
print(checkPerfectNumber(num))