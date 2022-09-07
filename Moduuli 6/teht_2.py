#Muokkaa edellistä funktiota siten,
# että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä
# jatketaan pääohjelmassa kunnes saadaan nopan
# maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.


import random

#Palauttaa nopan arvotun silmäluvun.
# Tahkojen lukumäärä annetaan parametrina
def heitäNoppaa(tahkot):
    luku = random.randint(1, tahkot) #(1 ja 6 parametrit)
    return luku
tahkoLKM = int(input("Kuinka monta tahkoa? "))
while True:
   silmäLuku = heitäNoppaa(tahkoLKM)
   print(silmäLuku)
   if silmäLuku == tahkoLKM:
        break




