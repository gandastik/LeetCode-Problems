from typing import List


def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if(nums[i] != val):
            nums[count] = nums[i]
            count += 1
    print(nums)
    return count 

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))