from typing import List
import math
def findSpecialInteger(arr: List[int]) -> int:
    _25percent = math.ceil(len(arr) * 0.25)
    count = 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]): count+=1
        if(count >= _25percent): return arr[i]
        count = 1



arr = [int(x) for x in input().split()]
print(findSpecialInteger(arr))