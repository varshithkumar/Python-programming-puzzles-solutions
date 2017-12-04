from collections import Counter
def isunique(s):
  c = Counter()
  for char in s:
    c[char]+=1
    
  for char in c:
    if c[char]>1:
      return False
  return True
  
  
print(isunique("abcdee"))  