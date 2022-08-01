#1502. Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
from typing import List
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    d = arr[1] - arr[0]
    for i in range(len(arr)-1):
        if(arr[i+1] - arr[i] != d):
            return False
    arr.sort(reverse=True)
    d = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        if(arr[i+1] - arr[i] != d):
            return False
    return True

arr = [int(x) for x in input().split()]
print(canMakeArithmeticProgression(arr))