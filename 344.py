#344. Write a function that reverses a string. The input string is given as an array of characters s.

def reverseString(s):
    def reverseS(i, j, s):
        if(i == j or i == len(s) / 2):
            return None
        s[i], s[j] = s[j], s[i]
        reverseS(i+1, j-1, s)
    reverseS(0, len(s)-1, s)

str = [str(x) for x in input()]
reverseString(str)
print(str)