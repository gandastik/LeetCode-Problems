#1399. Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
# Return how many groups have the largest size.

def countLargestGroup(n: int) -> int:
    dic = {}
    for i in range(1,37):
        dic[i] = 0
    for i in range(1, n+1):
        temp = i
        _sum = 0
        while(temp > 0):
            _sum += temp % 10
            temp = temp // 10
        dic[_sum] += 1
    lst = sorted(dic.values(), reverse=True)
    ret = 0
    _max = lst[0]
    for i in lst:
        if(i != _max):
            break
        ret += 1 
    return ret

n = int(input())
print(countLargestGroup(n))