#922. Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
def sortArrayByParityII(nums: List[int]) -> List[int]:
    odd = []
    even = []
    ret = []
    for i in nums:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    for i in range(len(nums)//2):
        ret.append(even[i])
        ret.append(odd[i])
    return ret

nums = [int(x) for x in input().split()]
print(sortArrayByParityII(nums))