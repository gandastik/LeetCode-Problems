#867. Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    ret = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            if(j < len(matrix)):
                temp.append(matrix[j][i])
        ret.append(temp)
    return ret

print(transpose([[1,2,3],[4,5,6],[7,8,9]])) #[[1,4,7],[2,5,8],[3,6,9]]
print(transpose([[1,2,3],[4,5,6]])) #[[1,4],[2,5],[3,6]]