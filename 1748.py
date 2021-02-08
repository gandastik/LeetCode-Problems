#1748. You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
from typing import List
def sumOfUnique(nums: List[int]) -> int:
    ret = 0
    arr = [0 for x in range(101)]
    for i in nums:
        arr[i] += 1
    for i in range(len(arr)):
        if(arr[i] == 1):
            ret += i
    return ret    

nums = [int(x) for x in input().split()]
print(sumOfUnique(nums))