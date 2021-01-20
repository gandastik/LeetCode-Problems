# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
from typing import List
def shuffleStr(s: str, indices: List[int]) -> str :
    temp = dict()
    ret = ""
    for i in range(len(s)):
        temp[indices[i]] = s[i]
    dic = sorted(temp.keys())
    for i in range(len(s)):
        ret += (temp[i])
    return ret