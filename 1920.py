# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

from typing import List
def buildArray(nums: List[int]) -> List[int]:
    ret = [0 for x in range(len(nums))]
    for i in nums:
        ret[i] = nums[nums[i]]
    return ret

nums = [int(x) for x in input().split()]
print(buildArray(nums))
