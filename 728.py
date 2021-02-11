#728. A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
from typing import List
def selfDividingNumbers(left: int, right: int) -> List[int]:
    ret = []
    def isDivingNum(n: int) -> bool:
        temp = n
        while(temp > 0):
            r = temp % 10
            if(r == 0):
                return False
            if(n % r != 0):
                return False                    
            temp = temp // 10
        return True
    
    for i in range(left, right+1):
        if(isDivingNum(i)):
            ret.append(i)
    return ret

left = int(input())
right = int(input())
print(selfDividingNumbers(left, right))