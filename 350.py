#350. Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    ret = []
    for i in nums1:
        if i in nums2:
            ret.append(i)
            nums2.remove(i)
    return ret

nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]
print(intersect(nums1, nums2))