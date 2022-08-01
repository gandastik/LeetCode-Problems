#884. We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Return a list of all uncommon words. 
# You may return the list in any order.
from typing import List
def uncommonFromSentences(A: str, B: str) -> List[str]:
    dic = {}
    for i in A.split():
        dic[i] = 0
    for i in A.split():
        dic[i] += 1
    for i in B.split():
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    ret = []
    for i in dic.keys():
        if(dic[i] == 1):
            ret.append(i)
    return ret

A = str(input())
B = str(input())
print(uncommonFromSentences(A, B))