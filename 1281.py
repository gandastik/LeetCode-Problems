#1281. Given an integer number n, return the difference between the product of its digits and the sum of its digits.
def subtractProductAndSum(n: int) -> int:
    temp = n
    Sum = 0
    product = 1
    while(temp > 0):
        r = temp % 10
        Sum += r
        product *= r
        temp = temp // 10
    return product - Sum 

n = int(input())
print(subtractProductAndSum(n))