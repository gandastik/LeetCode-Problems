# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.
from functools import reduce
def xorOperation(n: int, start: int) -> int:
    nums = []
    for i in range(n):
        nums.append(start + 2*i)
    ret = reduce(lambda x, y: x ^ y, nums)
    return ret

n = int(input())
start = int(input())
print(xorOperation(n, start))
