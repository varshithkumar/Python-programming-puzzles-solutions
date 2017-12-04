def anagram(s1,s2):
  s1 = ''.join(s1.split())
  s2 = ''.join(s2.split())
  s2_array = []
  for i in s2:
    s2_array.append(i)
  if len(s1) == len(s2):
    for i in s1:
      if i in s2_array:
        s2_array.remove(i)
      else:
        return False
        
    return True  
  else:
    return False