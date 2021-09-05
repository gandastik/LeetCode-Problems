#383. Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstrcut(ransomNote: str, magazine: str) -> bool:
    dicA = {}
    dicB = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        dicA[i] = 0
        dicB[i] = 0
    for i in ransomNote:
        dicA[i] += 1
    for i in magazine:
        dicB[i] += 1
    for i in ransomNote:
        if(dicB[i] < dicA[i]):
            return False
    return True 

ransomNote = str(input())
magazine = str(input())
print(canConstrcut(ransomNote, magazine))