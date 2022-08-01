#242. Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(s: str, t: str) -> bool:
    for i in s:
        if(s.count(i) != t.count(i) or len(s) != len(t)):
            return False
    return True

s, t = [str(x) for x in input().split()]
print(isAnagram(s, t))