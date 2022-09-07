#Kirjoita parametriton funktio,
# joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heitäNoppaa():
    luku = random.randint(1, 6) #(1 ja 6 parametrit)
    return luku

while True:
   silmäLuku = heitäNoppaa()
   print(silmäLuku)
   if silmäLuku == 6:
        break




