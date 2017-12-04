def solution(N):
    # write your code in Python 2.7
    i = 1
    result = 0
    while (i*i)<N :
        if (N%i)==0:
            result = i
        i+=1
    if i*i == N:
        result = i
    return 2*(result + (N/result))   