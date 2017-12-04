def verify_uniquestring(s):

  chars = set()

  for let in s:

    if let in chars:

      return False

    else:

      chars.add(let)

  return True

  
print (verify_uniquestring('fliper'))


      
  