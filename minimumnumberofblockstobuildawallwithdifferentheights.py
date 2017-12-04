def solution(H):
    # write your code in Python 2.7
    stack = []
    blocks = 0
    for height in H:
        while len(stack)!=0 and height < stack[-1]:
            stack.pop()
            blocks+=1
        if len(stack) == 0 or height > stack[-1]:
            stack.append(height)
    return (len(stack)+blocks) 