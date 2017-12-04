def solution(A):
    # write your code in Python 2.7
    if len(A) == 1:
        return A[0]
    d = {}
    for num in A:
        d[num] = 0
    for num in A:
        d[num]+=1
    for num in d:
        if d[num]%2==1:
            return num