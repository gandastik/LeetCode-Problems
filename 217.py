#217. Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    temp = {}
    for i in nums:
        try:
            temp[i] += 1
            return True
        except:
            temp[i] = 0
    return False

nums = [int(x) for x in input().split()]
print(containsDuplicate(nums))