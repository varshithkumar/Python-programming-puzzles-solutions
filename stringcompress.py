def stringcompression(s):

  count = 1

  s1 = ''

  i = 1
 
  while i < len(s):

    if s[i] == s[i-1]:

      count+=1

    else:

      s1 = s1+s[i-1]+str(count)

      count = 1

   i+=1
 
  s1 = s1+s[i-1]+str(count)

   return s1



print (stringcompression('AAassfgghHH'))