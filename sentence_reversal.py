def sentence_reversal(s):

  l = s.split()

  new_list = []

  n = 0

  while n < len(l):

    new_list.append(l.pop())

  return ' '.join(new_list)


print(sentence_reversal('   this is good'))  
   

def sentencereversal(string):

  strlist = string.split()

  x = ''

  for word in strlist[:len(strlist)-1]:

    x += strlist.pop() + ' '

  return x+strlist[-1]
   