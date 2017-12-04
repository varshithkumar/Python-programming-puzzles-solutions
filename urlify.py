def space(s):

  arr = s.split()

  news =''

  for c in arr:

    news+=c+'%20'

  return news[:-3]



print(space('Mr John Smith'))  