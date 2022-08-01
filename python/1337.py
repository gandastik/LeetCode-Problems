#1337. You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
from typing import List
def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    temp = dict()
    for i in range(len(mat)):
        temp[i] = sum(mat[i])
    temp = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1])}
    ret = list(temp.keys())
    return ret[:k]

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(kWeakestRows(mat, k))