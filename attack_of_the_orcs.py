"""
Author: Luis de Olano
e-mail: lm_olano@hotmail.com
Version: 0.0.1
"""

import random


print("""The war between humans and their arch enemies, the Orcs, was in the offing. A
huge army of Orcs was heading toward the human establishments. They were
virtually destroying everything in their way. The great kings of the human race
joined hands to defeat their worst enemy for the great battle of their time. Men were
summoned to join the rest of the army. Sir Foo, one of the brave knights guarding
the southern plains, began a long journey toward the east, through an unknown
dense forest. For two days and two nights, he moved cautiously through the thick
woods. On his way, he spotted a small isolated settlement. Tired and hoping to
replenish his food stock, he decided to take a detour. As he approached the village, he
saw five huts. There was no one to be seen around. Hesitantly, he decided to enter a
hut...""")

no_huts = 5
choices = ['enemy', 'friend', 'unoccupied']

huts = [random.choice(choices) for el in range(no_huts)]

selected_hut = int(input('Please, select a hut number (1-5)'))

if huts[selected_hut - 1] == 'enemy':
    print('you lose')
else:
    print('you win')

pass