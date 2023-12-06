#!/usr/bin/env python3

import re, math

sum = 1
input = []
with open('1.txt') as file:
    for line in file:
        input.append([int(line.replace(' ', '').rstrip().split(':')[1])])
for i, t in enumerate(input[0]):
    d = input[1][i]
    d1 = int(math.floor((t - math.sqrt(t*t-4*d))/2)+1)
    d2 = int(math.ceil((t + math.sqrt(t*t-4*d))/2)-1)
#    print(t, d, d1, d2, d2-d1+1)
    sum *= d2-d1+1
print(sum)
