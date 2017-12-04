def selection_sort(A):

  n =len(A)

  for i in range(n):

    minimal = i
 
    for j in range((i+1), n):

      if A[j] < A[minimal]:

        minimal = j
 
    A[i],A[minimal] = A[minimal],A[i]

  return A
 
  
A = [2,44,5,1,3,66,7,90,89]


def counting_sort(A,k):

  n = len(A)

  count = [0]*(k+1)

  for i in range(n):

    count[A[i]] += 1

  
  p = 0
 
  for i in range(k+1):

    for j in range(count[i]):

      A[p] = i
 
      p += 1

  return A
 
  
def minsize(A):

  n = len(A)

  size, result = 0,0
 
  for i in range(n):

    if A[i] == 0:
      size+=1
    else:
      size-=1
  result = max(result, -size)
  return result
  
def fishcount(A,B):
  stack =[]
  survivals = 0 
  for i in range(len(A)):
    if B[i] == 0:
      while len(stack)!=0:
        if stack[-1]>A[i]:
          break
        else:
          stack.pop()
      else:
        survivals+=1 
    else:
      stack.append(A[i])
      
    return survivals+len(stack)  

  
def lengthOfLongestSubstring(s):
    string = s[0]
    array = []
    for i in range(len(s)-1):

      if s[i]!=s[i+1]:

        string+=s[i+1]

      else:

        array.append(string)

        string = ''

    array.append(string)
    
    return array
    
 
 
print(lengthOfLongestSubstring('abcabcbb'))  
  