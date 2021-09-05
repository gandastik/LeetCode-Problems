#387. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s: str) -> int:
    dic = {}
    for i in s:
        try:
            dic[i] += 1
        except:
            dic[i] = 0
    for i in range(len(s)):
        if(dic[s[i]] == 0):
            return i
    return -1

s = str(input())
print(firstUniqChar(s))