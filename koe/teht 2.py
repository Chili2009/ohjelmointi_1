
i = 1; #i.n alkuarvo, tähän ei enään palata


while i%5 > 0: #onko i (1) jaollinen viidellä? ei ole ehto siis toteutuu, joten toteutetaan kooodi loopin sisällä
    print (i) #tulostetaan i tässä kohtaa (1)
    i = i + 3 #in arvo muuttuu, i + 3 (1 + 3 = 4), i on nyt 4

    #tässä kohtaa palataan loopin alkuun uuden i:n arvon kanssa


while i % 5 > 0: #onko i (4) jaollinen viidellä? ei ole eli ehto toteutuu, joten toteutetaan koodi loopin sisällä
    print (i) #tulostetaan i tässä kohtaa (4)
    i = i + 3 #i:n arvo muuttuu, i + 3 (4 + 3 = 7), i arvo on nyt 7

    #palataan taas while loopin alkuun uuden i:n arvon kanssa


while i % 5 > 0: #onko i (7) jaollinen viidellä? ei ole eli ehto toteutuu, joten toteutetaan koodi loopin sisällä
    print (i) #tulostetaan i tässä kohtaa (7)
    i = i + 3 #i:n arvo nuuttuu, i + 3 (7 + 3 = 10), i on nyt 10

    #palataan taaas while loopin alkuun uuden i:n arvon kanssa

    #ehto ei enään toteudu, koska 10 % 5 = 0, joten koodia while loopin sisällä ei enään toteuteta. Siirrytään seuraavalle riville koodissa

    print (i) #tulostetaan i:n arvo tällä hetkellä, (10)

#koodi loppui, ohjelma on suoritettu loppuun. Lopullinen tuloste on siis:


1 #tuloste tulee riviltä 5
4 #tuloste tulee riviltä 11
7 #tuloste tulee riviltä 17
10 #tuloste tulee riviltä 24