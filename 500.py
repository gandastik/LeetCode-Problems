#500. Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
from typing import List
def findWords(words: List[str]) -> List[str]:
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    ret = []
    for word in words:
        check = set()
        for i in word:
            if( i in first):
                check.add("first")
            if( i in second):
                check.add("second")
            if( i in third) :
                check.add("third")
        if(len(check) == 1):
            ret.append(word)
    return ret

words = [str(x) for x in input().split()]
print(findWords(words))