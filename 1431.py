#1431. Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
#For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = sorted(candies, reverse=True)
        maximum = lst[0]
        ret = []
        for i in range(len(candies)):
            if(candies[i] == maximum):
                ret.append(True)
            elif(candies[i] + extraCandies >= maximum):
                ret.append(True)
            else: ret.append(False)
        return ret
