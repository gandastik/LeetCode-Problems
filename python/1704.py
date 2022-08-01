#1704. You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
def halvesAreAlike(s: str) -> bool:
    firstHalf = s[:int(len(s)/2)]
    secondHalf = s[int(len(s)/2):]
    vowels = "aeiouAEIOU"
    count_first = 0
    count_second = 0
    for i in firstHalf:
        if(vowels.find(i) != -1):
            count_first += 1
    for j in secondHalf:
        if(vowels.find(j) != -1):
            count_second += 1
    return count_first == count_second

s = str(input())
print(halvesAreAlike(s))