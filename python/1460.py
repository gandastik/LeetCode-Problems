#1460. Given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
# Return True if you can make arr equal to target, or False otherwise.
from typing import List
def canBeEqual(target: List[int], arr: List[int]) -> bool:
    return sorted(target) == sorted(arr)

target = [int(x) for x in input().split()]
arr = [int(y) for y in input().split()]
print(canBeEqual(target, arr))