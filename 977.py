#977. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    ret = []
    for i in nums:
        ret.append(i**2)
    return sorted(ret)

nums = [int(x) for x in input().split()]
print(sortedSquares(nums))