def solution(S):
    # write your code in Python 2.7
    stack = []
    opens = '({['
    close = ')}]'
    parens = [('(',')'),('[',']'),('{','}')]
    for char in S:
        if char in opens:
            stack.append(char)
        elif char in close:
            if len(stack)==0:
                return 0
            else:
                last = stack.pop()
                if (last,char) not in parens:
                    return 0
    if len(stack)==0:
        return 1
    else:
        return 0