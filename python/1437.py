#1437. Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
from typing import List
def kLengthApart(nums: List[int], k: int) -> bool:
    for i in range(len(nums)):
        if(nums[i] == 1 and i != len(nums) - 1):
            try:
                if(abs(i - nums.index(1, i+1)) <= k):
                    return False
            except:
                print("error")
    return True

nums = [int(x) for x in input().split()]
k = int(input())
print(kLengthApart(nums, k))