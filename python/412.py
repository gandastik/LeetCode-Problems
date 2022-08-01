#412. Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
from typing import List
def fizzBuzz(n: int) -> List[str]:
    ret = []
    for i in range(1,n+1):
        if(i % 3 == 0 and i % 5 == 0):
            ret.append("FizzBuzz")
        elif(i % 3 == 0):
            ret.append("Fizz")
        elif(i % 5 == 0):
            ret.append("Buzz")
        else:
            ret.append(str(i))
    return ret

n = int(input())
print(fizzBuzz(n))