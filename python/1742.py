#1742. You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
# put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
from typing import List
def countBalls(lowLimit: int, highLimit: int) -> int:
    #100000 --> 99999 = 9+9+9+9+9 = 45 is the most possible balls number
    ret = [0 for x in range(46)]
    for i in range(lowLimit, highLimit+1):
        temp = i
        Sum = 0
        while(temp > 0):
            r = temp % 10
            temp = temp // 10
            Sum += r
        ret[Sum] += 1
    ret.sort(reverse=True)
    return ret[0]

lowLimit = int(input())
highLimit = int(input())
print(countBalls(lowLimit, highLimit))