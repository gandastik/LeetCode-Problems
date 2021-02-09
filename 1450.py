#1450. Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
from typing import List
def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if(queryTime <= endTime[i] and queryTime >= startTime[i]):
                count+=1
        return count

startTime = [int(x) for x in input().split()]
endTime = [int(x) for x in input().split()]
queryTime = int(input())
print(busyStudent(startTime, endTime, queryTime))