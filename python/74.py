#74. Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
            if(target >= row[0] and target <= row[-1]):
                for col in row:
                    if(col == target):
                        return True
    return False

#2 testcases
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))