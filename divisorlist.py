def divisors(integer):
    l = []
    for divisor in range(2, (integer//2 + 1)):
        if integer % divisor == 0:
            l.append(divisor)
        else:
            continue
    if l == []:
        return '{} is prime'.format(integer)
    else:
        return l