#509. The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
from typing import List
def fib(n: int) -> int:
    lst = [0]
    while(len(lst) != n+1):
        if(len(lst) == 1): lst.append(1)
        else: lst.append(lst[len(lst)-2] + lst[len(lst)-1])
    return lst[n]

n = int(input())
print(fib(n))
