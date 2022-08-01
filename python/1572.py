#1572. Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if(i+j == len(mat)-1):
                    res += mat[i][j]
                if(i == j):
                    res += mat[i][j]
        if(len(mat) % 2 != 0):
            return res-mat[len(mat)//2][len(mat)//2]
        return res
        
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(diagonalSum(arr))