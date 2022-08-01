from typing import List
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    count = 0
    for i in arr1:
        check = True
        for j in arr2:
            if( abs(i - j) <= d):
                check = False
                break
        if(check):
            count+=1
    return count

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
d = int(input())
print(findTheDistanceValue(arr1, arr2, d))