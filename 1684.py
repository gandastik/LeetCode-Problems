# You are given a string allowed consisting of distinct characters 
# and an array of strings words. A string is consistent if all characters in 
# the string appear in the string allowed.
# return the number of consistent strings in the array words.
from typing import List
def countConsistentStrings(allowed: str, words: List[str]) -> int:
    count = 0
    for i in words:
        check = True
        for j in i:
            if(allowed.find(j) == -1):
                check = False
                break
        if(check):
            count+=1
    return count

allowed = str(input())
words = [str(x) for x in input().split()]
print(countConsistentStrings(allowed, words))