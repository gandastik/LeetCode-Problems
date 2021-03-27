#1694. You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.
# Return the phone number after formatting.
def reformatNumber(number: str) -> str:
    a = ""
    for i in number:
        if(i.isnumeric()):
            a += i
    ret = ""
    while(len(a) > 4):
        ret += a[:3] + "-"
        a = a[3:]
    if(len(a) == 4):
        ret += a[:2] + "-"
        a = a[2:]
        ret += a[:2]
        a = a[2:]
    elif(len(a) == 3):
        ret += a[:3]
    elif(len(a) == 2):
        ret += a[:2]
    return ret

number = str(input())
print(reformatNumber(number))