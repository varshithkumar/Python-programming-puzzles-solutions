
def triangle_type(a, b, c):
  if (a+b)<=c or (a+c)<=b or (b+c)<=a:
      return 0
  elif ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
      return 2
  elif (a**2 > (b**2 + c**2)) or (b**2 > (a**2 + c**2)) or (c**2 > (a**2 + b**2)):
      return 3
  else:
      return 1