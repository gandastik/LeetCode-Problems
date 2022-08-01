# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
from typing import List
def arrayStringAreEqual(word1: List[str], word2: List[int]) -> bool:
    str1 = ''
    str2 = ''
    for i in word1:
        str1 += i
    for j in word2:
        str2 += j
    if(str1 == str2): return True
    return False

word1 = [str(x) for x in input().split()]
word2 = [str(x) for x in input().split()]
print(arrayStringAreEqual(word1, word2))