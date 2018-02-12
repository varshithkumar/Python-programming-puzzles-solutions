def solution(N):
    # write your code in Python 3.6
    binarray = []
    index = 0
    while N > 0:
        binarray.append(N%2)
        N//=2
        
    current_gap = max_gap = 0
    
    for i in range(len(binarray)):
        if binarray[i] == 1:
            index = i
            break
            

            
    for num in binarray[index:]:
        if num == 1:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
            
        else:
            current_gap+=1
            
    return max_gap    