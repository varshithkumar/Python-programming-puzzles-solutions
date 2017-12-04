def solution(A):
    # write your code in Python 2.7
    if len(A)<=1:
        return 0
    n = len(A)    
    max_price_from_here = A[n-1]
    max_profit = 0
    for i in range(n-2,-1,-1):
        max_profit = max(max_profit, max_price_from_here - A[i])
        max_price_from_here = max(max_price_from_here, A[i])
    if max_profit > 0:
        return max_profit
    else:
        return 0