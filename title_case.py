def title_case(title, minor_words):
    title_list = [i for i in title]
    if title_list[0].isalpha() and title_list[0].islower():
            title_list = title_list[0].upper() + title_list[1:]
            
    for i in range(1,len(title_list)):
        if title_list[i].isalpha():
            if title_list[i-1] == ' ' and title_list[i].islower():
                title_list[i] = title_list[i].upper()                    
            elif title_list[i].isupper():
                title_list[i] = title_list[i].lower()
    title = ''.join(title_list)      
    new_list = title.split()
    minor_list = minor_words.split()
    for i in range(1, len(new_list)):
        if new_list[i].lower() in minor_list:
            new_list[i] = new_list[i].lower()
    string = ' '.join(new_list)
    return string