# Sliding windows
def lengthOfLongestSubstring(s: str):
    seen = {}
    left = 0
    ret = 0
    for right in range(len(s)):
        # check if you have seen the char before
        if s[right] not in seen:
            ret = max(ret, right - left + 1)
        # have seen the character before
        else:
            # in the case that the char that have been seen is not in the sliding window (index < left)
            if seen[s[right]] < left:
                ret = max(ret, right - left + 1)
            # in the case that the char that have been seen is in the sliding window (index >= left)
            else:
                # move the sliding windows (move the left pointer to the last character)
                left = seen[s[right]] + 1
        # mark the seen character's index
        seen[s[right]] = right
    return ret

print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("pwwkew")) # 3
print(lengthOfLongestSubstring("au")) # 2
print(lengthOfLongestSubstring("dvdf")) # 3
print(lengthOfLongestSubstring("aabaab!bb")) # 3