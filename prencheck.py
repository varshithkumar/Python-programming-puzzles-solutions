def valid_parentheses(string):
    l = []
    for character in string:
        if character == '(':
            l.append('(')
        elif character == ')':
            if l == []:
                return False
            else:
                l.pop()
    if l == []:
        return True
    else:
        return False