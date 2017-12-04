def tribonacci(signature,n):
    #your code here
    if n == 0:
      return []
    elif n < 3 and n > 0:
      return signature[:n]
    elif n == 3:
      return signature
    elif n == 4:
      return signature + [sum(signature)]
    else:  
        for i in range(n-4):
            if i == 0:
              s = sum(signature)
              signature.append(s)
            signature.append(signature[i+1]+signature[i+2]+signature[i+3])
    return signature    