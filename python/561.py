#561. Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
from typing import List
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    ret = 0
    for i in range(0,len(nums),2):
        ret += min(nums[i],nums[i+1])
        
    return ret

nums = [int(x) for x in input().split()]
print(arrayPairSum(nums))