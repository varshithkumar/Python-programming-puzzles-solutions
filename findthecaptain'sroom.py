def findcaptainroom():
    k = int(input())
    d = {}
    rooms = list(map(int, input().split()))
    
    for i in rooms:
        d[i] = 0
        
    for i in rooms:
        d[i]+=1
        
    for i in d:
        if d[i]==1:
            return i
        
print (findcaptainroom())    