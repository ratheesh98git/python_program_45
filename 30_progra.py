#30) Python program to shuffle deck of cards.

import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

s=[{"rank":rank,"suit":suit} for rank in ranks for suit in suits]

random.shuffle(s)

for ca in s:
    print(f"{ca['rank']} of {ca['suit']}")