#1408. Given an array of string words. Return all strings in words which is substring of another word in any order. 
# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
from typing import List
def stringMatching(words: List[str]) -> List[str]:
    ret = []
    for i in words:
        for j in words:
            if(j in i and j != i):
                ret.append(j)
    return set(ret)

words = [str(x) for x in input().split()]
print(stringMatching(words))