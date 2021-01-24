# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
from typing import List
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    ret = []
    for i in range(len(nums)):
        ret.insert(index[i], nums[i])
    return ret
    
lst = [int(x) for x in input().split()]
index = [int(x) for x in input().split()]
print(createTargetArray(lst, index))