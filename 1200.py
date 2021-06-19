from typing import List
def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    _min = 2000000000000 
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(abs(arr[i] - arr[j]) < _min):
                print("%d %d " % (arr[i],arr[j]))
                _min = abs(arr[i]-arr[j])
    print(_min)
    ret = []
    for i in sorted(arr):
        for j in sorted(arr):
            if(i != j and abs(i - j) == _min and i < j):
                ret.append([i, j])
    return ret

print(minimumAbsDifference([1,3,6,10,15]))