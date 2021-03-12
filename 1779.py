#1779. You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
from typing import List
def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    dic = {}
    ret = 0
    for i in range(len(points)):
        if(points[i][0] == x or points[i][1] == y):
            dic[i] = points[i]
    if(len(dic) == 0):
        return -1
    else:
        for i in dic.keys():
            dic[i] = abs(dic[i][0] - x) + abs(dic[i][1] - y) 
        smallest = min(dic.values())
        for i in dic.keys():
            if(dic[i] == smallest):
                return i

print(nearestValidPoint(3,4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))
print(nearestValidPoint(3, 4, [[3,4]]))
