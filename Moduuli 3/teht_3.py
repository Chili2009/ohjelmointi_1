#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
# ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko
# hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


gender = input("sukupuoli (nainen/mies)? " )
hg_value = int(input("hemoglobiinisi (g/l)? "))

if gender == "nainen":
    if hg_value < 117:
        print("hemoglobiini arvo on alhainen.")
    elif hg_value <= 175:
        print("hemoglobiini arvo normaali.")
    else:
        print("hemoglobiini arvo on korkea")

elif gender == "mies":
    if hg_value < 134:
        print ("Hemoglobiini arvo on alhainen")
    elif hg_value <= 195:
        print(" Hemoglobiini on normaali")
    else:
        print("hemoglobiini arvo on korkea" )

else:
    print("virheellinen arvo")