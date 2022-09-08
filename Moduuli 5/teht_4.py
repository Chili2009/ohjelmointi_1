#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

# Kaupungin nimet

kaupungit = []

for n in range(5):
    kaupunki = input("Anna kapungin nimi")
    kaupungit.append(kaupunki)
    #print(kaupungit) välituloste jos epäilee ettei ohjelma toimi
for n in kaupungit:
    print(n)
