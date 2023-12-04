#!/usr/bin/env python3

import re

cards = []
colon_pos = 0
bar_pos = 0
with open('1.txt') as file:
    for line in file:
        line = line.rstrip()
        if colon_pos == 0:
            colon_pos = line.find(':')
            bar_pos = line.find('|')
        win = [int(x)
               for x in re.split(r' +', line[colon_pos+1:bar_pos].strip())]
        my = [int(x)
              for x in re.split(r' +', line[bar_pos+1:].strip())]
        cards.append([len(set(win).intersection(set(my))), 1])
cards_len = len(cards)
total = cards_len
for n, card in enumerate(cards):
    for w in range(card[1]):
        if card[0] > 0:
            for r in range(card[0]):
                if n+1+r < cards_len:
                    cards[n+1+r][1] += 1
                    total += 1

print(total)
