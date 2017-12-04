def timeConversion(s):
    if 'PM' in s:
        if int(s[:2]) != 12:
            return str(int(s[:2])+12)+s[2:8]
        else:
            return s[:8]
    elif 'AM' in s:
        if int(s[:2]) == 12:
            return '00'+s[2:8]
        else:
            return s[:8]