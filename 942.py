# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
from typing import List
def diStringMatch(S: str) -> List[int]:
    ret = []
    d = len(S)
    i = 0
    for j in S:
        if(j == "I"):
            ret.append(i)
            i+=1
        elif( j == "D"):
            ret.append(d)
            d-=1
    return ret + [i]

S = str(input())
print(diStringMatch(S)) 