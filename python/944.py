#944. You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid.
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.
from typing import List
def minDeletionSize(strs: List[str]) -> int:
    a = "abcdefghijklmnopqrstuvwxyz"
    ret = 0
    for j in range(len(strs[0])):
        for i in range(len(strs)-1):
            if(a.find(strs[i][j]) > a.find(strs[i+1][j]) ):
                ret += 1
                break
    return ret

strs = [str(x) for x in input().split()]
print(minDeletionSize(strs))