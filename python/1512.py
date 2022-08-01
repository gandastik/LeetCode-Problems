from typing import List

def numIdenticalPairs(nums: List[int]) -> int :
    counter = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] == nums[j]):
                counter += 1
    return counter

print(numIdenticalPairs([1,1,1,1]))
