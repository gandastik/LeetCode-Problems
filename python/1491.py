#1491. Given an array of unique integers salary where salary[i] is the salary of the employee i.
# Return the average salary of employees excluding the minimum and maximum salary
from typing import List
def average(salary: List[int]) -> float:
    salary.sort()
    total = sum(salary) - salary[0] - salary[-1]
    return total / (len(salary) - 2)

salary = [int(x) for x in input().split()]
print(average(salary))