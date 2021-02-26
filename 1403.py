#1403. Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
from typing import List
def minSubsequence(nums: List[int]) -> List[int]:
    arr = sorted(nums)
    arr.reverse()
    i = 0
    while(sum(arr[:i+1]) <= sum(arr[i+1:])):
        i+=1
    return arr[:i+1]

nums = [int(x) for x in input().split()]
print(minSubsequence(nums))