def parenmatcher(opener, closer):

  openers = '{[('
  closers = '}])'

  return openers.index(opener) == closers.index(closer)




def parencheck(par):

  balanced = True

  s = []

  for paren in par:

    if paren in '{[(':

      s.append(paren)

    else:

      if len(s) == 0:

        balanced = False

      else:

        top = s.pop()

        if not parenmatcher(top, paren):

          balanced = False

  return (len(s) == 0) and balanced

  
print(parencheck('[[(())]]')) 