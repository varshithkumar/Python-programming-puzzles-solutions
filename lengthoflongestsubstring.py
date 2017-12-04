from functools import reduce

def lengthOfLongestSubstring(s):
    string = s[0]
    array = []
    for i in range(1,len(s)):
      if s[i] not in string:
        string+=s[i]
      else:
        array.append(string)
        string = ''
    array.append(string)
   
    array = reduce((lambda x, y : x if len(x)>len(y) else y), array)

    return array

print(lengthOfLongestSubstring('abcabcbb'))  