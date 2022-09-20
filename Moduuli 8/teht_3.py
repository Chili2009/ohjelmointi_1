#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

def haku ():
    icao = input ('syötä lentokentän ICAo-koodi:')
    sql = 'select latitude_deg, longitude_deg from airport where gps_code = "' + icao + '"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    response =kursori.fetchall()
    return response

print('lasketaan kahden lentokentän etäisyys!\n')
loc1 = haku()
loc2 = haku()
print (loc1)
print(type(loc1(0)))

gap = distance.distance((loc1, loc2), loc2).km
print(gap)
