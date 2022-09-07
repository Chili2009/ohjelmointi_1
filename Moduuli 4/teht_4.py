#Kirjoita peli, jossa tietokone arpoo
# kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti,
# kunnes tämä arvaa oikein. Kunkin arvauksen
# jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa,
# että tietokone ei saa vaihtaa lukuaan
# arvauskertojen välissä.

import random

tk_luku = random.randrange(1, 11)
luku = int(input("Arvaa kokonaisluku 1-10 : "))
while luku != tk_luku:
    if luku > tk_luku:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
    luku = int(input("Arvaa kokonaisluku 1-10: "))
else:
    print("Oikein!")