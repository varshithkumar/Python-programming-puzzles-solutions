def solution(A, B):
    survivals = 0
    stack = []
 
    for idx in xrange(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    #print "downstream ate candidate"
                    break
                else:
                    #print "upstream ate stack"
                    stack.pop()
 
            else:
                survivals += 1
                #print "fish size", A[idx], "survived"
        else:
            stack.append(A[idx])
            #print "stack push", A[idx]
 
    survivals += len(stack)
    #print len(stack), "downstreams survived"
 
    return survivals