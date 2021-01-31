# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
from typing import List
def smallerNumbersThanCurrent(nums: List[int] ) -> List[int]:
    ret = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] > nums[j]):
                ret[i] += 1
    return ret

nums = [int(x) for x in input().split()]    
print(smallerNumbersThanCurrent(nums))