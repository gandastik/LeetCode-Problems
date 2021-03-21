from typing import List
def singleNumber(nums: List[int]) -> int:
    for i in nums:
        if(nums.count(i) == 1):
            return i

nums = [int(x) for x in input().split()]
print(singleNumber(nums))