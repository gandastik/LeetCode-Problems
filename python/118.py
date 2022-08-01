#118. Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(numRows: int):
    ret = [[1]]
    for i in range(numRows-1):
        row = [1]
        for j in range(len(ret[-1])):
            row.append(sum(ret[-1][j:j+2]))
        ret.append(row)
    return ret

numRows = int(input())
print(generate(numRows))