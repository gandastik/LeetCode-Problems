#1464. Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
from typing import List
def maxProduct(nums: List[int]) -> int:
    nums.sort(reverse=True)
    return (nums[0] - 1) * (nums[1] -1)

nums = [int(x) for x in input().split()]
print(maxProduct(nums))