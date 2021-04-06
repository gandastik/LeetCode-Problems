#1394. Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
from typing import List
def findLucky(arr: List[int]) -> int:
    dic = {}
    for i in arr:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    #iterate through the key of dic in descending order 
    #bc we need to return the largest order if there's two or more lucky number
    for i in sorted(dic.keys(),reverse=True):
        if(dic[i] == i):
            return i
    return -1

arr = [int(x) for x in input().split()]
print(findLucky(arr))