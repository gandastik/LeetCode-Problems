#88. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while( m > 0 and n > 0):
        if(nums1[m-1] >= nums2[n-1]):
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    while(n > 0):
        nums1[:n] = nums2[:n]

nums1 = [int(x) for x in input().split()]
m = len(nums1)
nums2 = [int(x) for x in input().split()]
n = len(nums2)
for i in range(n):
    nums1.append(0)

merge(nums1, m, nums2, n)
print(nums1)