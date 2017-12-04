def fib(n):
  a=0
  b=1
  for i in range(n):
    yield a 
    a,b = b,a+b
    
l = list(fib(50))
#print (l)

def solution(A,k):
  for i in range(k):
    A.insert(0,0)
    A[0] = A.pop()
  return A

    
    
#print (solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],8))  

l = [9,8,7,6]
k = [9,8,7]

def oddoccurence(A):
  res = 0 
  for i in A:
    res ^= i 
  return res  
    
#print(oddoccurence([9,3,9,3,9,7,9]))


def s(n):
  result=0
  for i in range(n):
    result+=i+1
  return result
  
  
print (s(10))


















    