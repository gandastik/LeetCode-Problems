#1636. Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
from typing import List
def frequencySort(nums: List[int]) -> List[int]:
    dic = {}
    for i in set(nums):
        x = nums.count(i)
        try:
            dic[x].append(i)
        except:
            dic[x] = [i]
    print(dic)
    ret = []
    for i in sorted(dic):
        for j in sorted(dic[i], reverse=True):
            ret.extend([j]*i)
    return ret

nums = [int(x) for x in input().split()]
print(frequencySort(nums))