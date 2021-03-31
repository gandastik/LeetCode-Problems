#1078. Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
# For each such occurrence, add "third" to the answer, and return the answer.
from typing import List
def findOcurrences(text: str, first: str, second: str) -> List[str]:
    lst = [str(x) for x in text.split()]
    ret = []
    for i in range(len(lst)):
        if(lst[i] == first and i < len(lst) - 2):
            if(lst[i+1] == second):
                ret.append(lst[i+2])
    return ret

text = str(input())
first = str(input())
second = str(input())
print(findOcurrences(text, first, second))