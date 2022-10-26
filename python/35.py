# 35. Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

import math
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    return bsearch(nums, target, 0, len(nums)-1)

def bsearch(nums, target, l, r):
    mid = (r + l) // 2
    if(nums[0] > target):
        return 0
    if(l > r):
        return mid + 1
    if (nums[mid] == target):
        return mid
    elif(nums[mid] > target):
        return bsearch(nums, target, l, mid-1)
    elif(nums[mid] < target):
        return bsearch(nums, target, mid+1, r)
    
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3], 2))