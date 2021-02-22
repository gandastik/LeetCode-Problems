#1295. Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List
def findNumbers(nums: List[int]) -> int:
    ret = 0
    for i in nums:
        temp = i
        count = 0
        while(temp > 0):
            count += 1
            temp = temp // 10
        if(count % 2 == 0):
            ret += 1
    return ret 

nums = [int(x) for x in input().split()]
print(findNumbers(nums))