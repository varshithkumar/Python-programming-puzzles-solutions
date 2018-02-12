#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    count = 0
    if n == m:
        if sum(s) == d:
            return 1
    for i in range(n - m + 1):
        if i == (n-m):
            if sum(s[i:]) == d:
                count += 1
        else:
            if sum(s[i:i+m]) == d:
                count += 1
    return count           

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)