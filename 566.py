# #566. You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

from typing import List

def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    if(r*c != m*n):
        return mat
    else:
        new_mat = []
        lst = []
        for row in mat:
            for col in row:
                lst.append(col)
        idx = 0
        for i in range(r):
            rows = []
            for j in range(c):
                rows.append(lst[idx])
                idx += 1
            new_mat.append(rows)
        return new_mat
        
#testcase: mat = [[1,2], [3,4]], r = 1, c = 4
mat = [[1,2], [3,4]]
print(matrixReshape(mat, 1, 4))