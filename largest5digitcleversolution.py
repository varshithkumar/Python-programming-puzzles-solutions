def solution(d):
  for x in '9876543210':
    for y in '9876543210':
      for z in '9876543210':
        for a in '9876543210':
          for b in '9876543210':
            if d.find(x+y+z+a+b) != -1:
              return int(x+y+z+a+b)


def solution(digits):
    max = 0
    if len(digits) < 5:
        return 0
    elif len(digits) == 5:
        return int(digits)
    else:
        for i in range(len(digits)-4):  
            if int(digits[i:i+5]) > max:
                max = int(digits[i:i+5])
            else:
                continue
    return max