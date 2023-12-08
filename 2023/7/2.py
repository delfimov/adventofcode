#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import groupby

def compare(item1, item2):
    if item1[1] == 'J':
        return -1
    if item2[1] == 'J':
        return 1
    return item2[0] - item1[0]

def get_power(c):
    p = 0
    if c[0][0] == 5:                    # Five of a kind
        p += 7000000
    elif c[0][0] == 4:                  # Four of a kind
        p += 6000000
    elif c[0][0] == 3 and c[1][0] == 2: # Full house
        p += 5000000
    elif c[0][0] == 3 and c[1][0] == 1: # Three of a kind
        p += 4000000
    elif c[0][0] == 2 and c[1][0] == 2: # Two pair
        p += 3000000
    elif c[0][0] == 2 and c[1][0] == 1: # One pair
        p += 2000000
    else:                               # High card
        p += 1000000
    return p

def strength(item):
    names_to_hex = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A', 'J': '1'}
    hex_string = item
    for char in names_to_hex.keys():
        hex_string = hex_string.replace(char, names_to_hex[char])
    # print("0x" + hex_string, item, int("0x" + hex_string, 16))
    p = int("0x" + hex_string, 16) # cards order by names

    c = sorted([[len(list(v)),k] for k,v in groupby(sorted(item))], key=cmp_to_key(compare))

    if c[0][1] == 'J' and c[0][0] != 5:
        c[1][0] += c[0][0]
        c = c[1:]

    if c[0][0] == 5:                    # Five of a kind
        p += 7000000
    elif c[0][0] == 4:                  # Four of a kind
        p += 6000000
    elif c[0][0] == 3 and c[1][0] == 2: # Full house
        p += 5000000
    elif c[0][0] == 3 and c[1][0] == 1: # Three of a kind
        p += 4000000
    elif c[0][0] == 2 and c[1][0] == 2: # Two pair
        p += 3000000
    elif c[0][0] == 2 and c[1][0] == 1: # One pair
        p += 2000000
    else:                               # High card
        p += 1000000
    return p


sum = 0
input = []
with open('1.txt') as file:
    for line in file:
        card = []
        for i,x in enumerate(line.rstrip().split()):
            if i==1:
                card.append(int(x))
            else:
                card.append(x)
                card.insert(0, strength(x))
        input.append(card)


out = sorted(input, key=cmp_to_key(lambda item1,item2: item1[0]-item2[0]))
for i, x in enumerate(out):
    print((i+1), x)
    sum += (i+1) * x[2]

print(sum)
