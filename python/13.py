def romanToInt(s: str):
  roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
  ret = 0
  for i in range(len(s)-1):
    if roman[s[i]] < roman[s[i+1]]:
      ret -= roman[s[i]]
    else:
      ret += roman[s[i]]
  return ret + roman[s[-1]]

print(romanToInt("III"))
print(romanToInt("LVIII"))
