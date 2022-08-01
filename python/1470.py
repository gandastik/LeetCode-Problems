from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    l = int(len(nums) / 2)
    ret = []
    for i in range(l):
        ret.append(nums[i])
        ret.append(nums[i+l])
    return ret

print(shuffle([2,5,1,3,4,7], 3))