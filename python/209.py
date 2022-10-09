# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray 
# [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead. 

from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    total = 0
    ret = 1 << 63
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            ret = min(ret, right - left + 1)
            total -= nums[left]
            left += 1
    return ret if ret != 1 << 63 else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(minSubArrayLen(11, [1,2,3,4,5]))