def pig_it(text):
    l = text.split()
    s = ''
    for word in l:
        if word in '!?/\.,<>=+-*@#$%^&()"`~':
            s += word
        else:    
            s += word[1:] + word[0] + 'ay '
    if s[-1] in '!?/\.,<>=+-*@#$%^&()"`~':
        return s
    else:
        return s[:len(s)-1]


def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])