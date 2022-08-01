#1207. Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
from typing import List
def uniqueOccurrences(arr: List[int]) -> bool:
    dic = dict()
    for i in arr:
        dic[i] = 0
    for i in arr:
        dic[i] += 1
    lst = list(dic.values())
    s = set(dic.values())
    return len(lst) == len(s) 

arr = [int(x) for x in input().split()]
print(uniqueOccurrences(arr))