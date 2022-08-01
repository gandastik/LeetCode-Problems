#1582. Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
# A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
from typing import List
def numSpecial(mat: List[List[int]]) -> int:
    ret = 0
    for i in range(len(mat)):
        sumJ = 0 
        for j in range(len(mat[i])):
            if(sum(mat[i]) == 1 and mat[i][j] == 1):
                for k in range(len(mat)):
                    sumJ += mat[k][j]
        if(sum(mat[i]) == 1 and sumJ == 1):
            ret += 1
    return ret
#output: 1
print(numSpecial([[1,0,0],[0,1,0],[0,0,1]])) 
#output: 2
print(numSpecial([[0,0,1,0]
                ,[0,0,0,0]
                ,[0,0,0,0]
                ,[0,1,0,0]]))
#output: 1
print(numSpecial([[0,0]
                ,[0,0]
                ,[1,0]]))