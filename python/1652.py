#1652. You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
from typing import List
def decrypt(code: List[int], k: int) -> List[int]:
    ret = []
    for i in range(len(code)):
        _sum = 0
        if(k > 0):
            for j in range(k):
                _sum += code[(i+1+j)%len(code)]
        elif(k < 0):
            for j in range(abs(k)):
                _sum += code[i-j-1]
        else:
            for j in range(len(code)):
                ret.append(0)
            break
        ret.append(_sum)
    return ret

code = [int(x) for x in input().split()]
k = int(input())
print(decrypt(code, k))