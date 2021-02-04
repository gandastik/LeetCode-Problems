#1. Two Sum -Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    ret = [] 
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] + nums[j] == target and i != j):  
                ret.append(i) 
                ret.append(j) 
                return ret 

nums = [int(x) for x in input().split()]
target = int(input())
print(twoSum(nums, target))