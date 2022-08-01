#961. In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.
from typing import List
def repeatedNTimes(A: List[int]) -> int:
    temp = [0 for x in range(10000)]
    for i in A:
        temp[i] += 1
    for i in range(10000):
        if(temp[i] == len(A) / 2):
            return i

A = [int(x) for x in input().split()]
print(repeatedNTimes(A))