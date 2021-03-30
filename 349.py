#349. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))

nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]
print(intersection(nums1, nums2))