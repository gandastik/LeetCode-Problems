from typing import List
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    dic = dict()
    total = 0
    count = 0
    boxTypes.sort()
    print(boxTypes)
    for i in boxTypes:
        dic[i[1]] = i[0]
    temp = sorted(list(dic.keys()))
    temp.reverse()
    print(dic)
    i = 0
    while(count < truckSize):
        boxes = truckSize - dic[temp[i]]
        if(count + dic[temp[i]] > truckSize):
            total += ( truckSize - count ) * temp[i]
            count += (boxes - dic[temp[i]])
            break
        else:
            count += dic[temp[i]]
            total += dic[temp[i]] * temp[i]
        i+=1
    return total

# print(maximumUnits([[1,3],[2,2],[3,1]], 4))
# print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
print(maximumUnits([[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]], 13))