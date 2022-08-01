#1051. Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
# Notice that when a group of students is selected they can reorder in any possible way between themselves 
# and the non selected students remain on their seats.
from typing import List
def heightChecker(heights: List[int]) -> int: 
    lst = sorted(heights)
    count =0 
    for i in range(len(lst)):
        if(lst[i] != heights[i]):
            count+=1
    return count 

heights = [int(x) for x in input().split()]
print(heightChecker(heights))