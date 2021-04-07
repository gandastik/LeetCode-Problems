#1046. We have a collection of stones, each stone has a positive integer weight.
# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
from typing import List
def lastStoneWeight(stones: List[int]) -> int:
    stones = sorted(stones, reverse=True)
    while(len(stones) > 1):
        if(stones[0] - stones[1] > 0):
            stones.append(stones[0] - stones[1])
            stones.pop(0)
            stones.pop(0)
        else:
            stones.pop(0)
            stones.pop(0)
        stones.sort(reverse=True)
    if(len(stones) == 0):
        return 0
    return stones[0]

stones = [int(x) for x in input().split()]
print(lastStoneWeight(stones))