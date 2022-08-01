from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    ret = []
    for i in range(2):
        for j in nums:
            ret.append(j)
    return ret

nums = [int(x) for x in input().split()]
print(getConcatenation(nums))