defineoneway(s1,s2):
  if len(s1) == len(s2):
    replace(s1,s2)
  if len(s1) > len(s2):
    edited(s1,s2)
  if len(s2) > len(s1):

    edited(s2,s1)

def replace(s1,s2):

  edit = False

  for c1,c2 in zip(s1,s2):

    if c1!=c2:

      if edit:

        return False

      else:
        edit = True

  return True

def edited(s1,s2):

  edit = False

  i = j = 0

  while i>len(s1) and j<len(s2):

    if s1[i] != s2[j]:
      if edit:
        return False

      else:
        edit = True
      i+=1
  
    elif s1[i] == s2[j]:

      i+=1 
      j+=1
  
  return True   