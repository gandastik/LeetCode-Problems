# 70. You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return n
    oneStepBefore = 2
    twoStepBefore = 1
    allWay = 0
    for i in range(2, n):
        allWay = oneStepBefore + twoStepBefore
        twoStepBefore = oneStepBefore
        oneStepBefore = allWay
    return allWay

print(climbStairs(2)) # 2
print(climbStairs(3)) # 3