from collections import Counter
def permpal(s):
  arr = s.split()
  print(arr)
  c = Counter()
  oddcount = 0
  evencount = 0
  for char in arr[0]:
    c[char]+=1
  for char in arr[1]:
    c[char]+=1
  for char in c:
    if c[char]%2 == 0:
      evencount += 1
    elif c[char]%2 == 1:
      oddcount += 1
  if oddcount == 0 or oddcount == 1:
    print (True)
  else:
    print (False)
      
      
permpal('taco cat')     