#905. Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
def sortArrayByParity(A: List[int]) -> List[int]:
    even = []
    odd = []
    for i in A:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    ret = [] 
    for i in even:
        ret.append(i)
    for i in odd:
        ret.append(i)
    return ret

A = [int(x) for x in input().split()]
print(sortArrayByParity(A))