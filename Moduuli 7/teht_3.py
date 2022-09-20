#työntekijät = {
    #"Viivi": ("bulevardi", "050-1234567"),
    #"Ahmed": ("tehtaankatu", "040-1112223"),
    #"Pekka":("liisankatu", "050-7654321",)}

#tiedot = työntekijät ["Viivi"]
#print(tiedot[0])
#print(tiedot[1])




#Kirjoita ohjelma lentoasematietojen hakemiseksi
# ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja
# nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja
# tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

#tulostaa valikon ja palauttaa käyttäjän valinnan.
def valitse():
    print("1 - syötä uusi")
    print("- haku")
    print("0 - lopetus")

#lisää uuden lentoaseman annettuun sanakirjaan.
def lisaauusi(aseemat):
    icao = input("Aseman ICAO-koodi: ")
    nimi = input("Aseman nimi: ")
    asemat[icao] = nimi


#tulostaa halutun aseman annetusta sanakirjasta
def hae(asemat):

#pääohjelma
lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisaauusi(lentoasemat)
    elif valinta == 2:
        hae(lentoasemat)
    valinta = valitse()




