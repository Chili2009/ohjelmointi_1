#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).
username = "python"
password = "rules"
yritys = input(f"Syötä Käyttäjätunnus: ")
yritys2 = input("Syötä Salasana: ")
i = 1
while i < 5:
    if yritys == username and yritys2 == password:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        i += 1
        yritys = input("Syötä Käyttäjätunnus: ")
        yritys2 = input("Syötä Salasana: ")
if i == 5:
    print("Pääsy evätty")