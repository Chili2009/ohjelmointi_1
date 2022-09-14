#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä",
           "syksy","syksy", "syksy", "talvi")
month_num = int(input("Syötä kuukauden järjestysnumero (1-12): "))

if month_num < 13 and month_num > 0:
    print(f"{month_num}. Kuukausi kuuluu vuodenaikaan {seasons[month_num-1]}")
else:
    print("virheellinen syöte")




