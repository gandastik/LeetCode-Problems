#1160. You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
from typing import List
def countCharacters(words: List[str], chars: str) -> int:
    ret = 0
    for i in words:
        temp = chars
        check = True
        for j in i:
            if(temp.find(j) != -1):
                temp = temp.replace(j, "", 1)
            else:
                check = False
                break
        if(check):
            print(i)
            ret += len(i)
    return ret

words = [str(x) for x in input().split()]
chars = str(input())
print(countCharacters(words, chars))