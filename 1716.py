
def totalMoney(n: int) -> int:
    #sum of the mathematic sequence of numbers is S = n/2(a1 + an)
    a = n // 7
    r = n % 7
    a1 = 1.0
    an = 7.0
    ret = 0
    for i in range(a):
        ret += 7/2 * (a1 + an)
        a1+=1
        an+=1
    for i in range(r):
        ret += a1
        a1+=1
    return int(ret)

print(totalMoney(10))