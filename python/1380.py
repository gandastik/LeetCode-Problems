#1380. Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
from typing import List
def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    lucky_col = []
    lucky_rows = []
    ret = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(m):
        col = []
        for j in range(n):
            col.append(matrix[j][i])
        lucky_col.append(max(col))
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[i][j])
        lucky_rows.append(min(row))
    print(lucky_col)
    print(lucky_rows)
    for i in lucky_col:
        for j in lucky_rows:
            if(i==j):
                ret.append(i)
    return ret

print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))