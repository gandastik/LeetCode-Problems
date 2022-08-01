#496. You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.
from typing import List
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    ret = []
    for i in nums1:
        check = False
        for j in nums2[nums2.index(i):]:
            if(j > i):
                ret.append(j)
                check = True
                break
        if(check == False):
            ret.append(-1)
    return ret

nums1 = [int(x) for x in input().split()]
nums2 = [int(y) for y in input().split()]
print(nextGreaterElement(nums1, nums2))