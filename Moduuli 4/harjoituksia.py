


    #kiinteä määrä toistokertoja
#kerrat = int(input("montako kertaa tervehdiitään"))
#tehdyt = 0
#while tehdyt<kerrat:
    #print("hyvää huomenta")
    #tehdyt = tehdyt + 1

   #käyttäjä lopettaa toiston
#comand = input("Anna komento: ")
#while comand!= "lopeta":
    #print ("Suoritan toiminnon: " + comand)
    #comand = input("anna komento: ")
#print("toiminnot lopetettu.")

        #vaihteleva määrä toistoja

#import random
#dice1 = dice2 = thrown = 0
#while (dice1!=6 or dice2!=6):
    #dice1 = random.randint(1,6)
    #dice2 = random.randint(1,6)
    #thrown = thrown + 1
#print(f"Needed {thrown:d} thrown.")

        #sisäkkäiset toistorakenteet

#first = 1      #1 muuttuu 5 asti
#while first <=5:
    #second = 1  #1 muuttuu 5 asti
    #while second <=5:  #while toistaa 5 asti
        #print(f"{first} time {second} is {first*second:d}")   # first kerrotaan secondilla
        #second = second +1
    #first = first + 1

#import random
#toistot = 0
#heitot_yhteensä = 0
#while toistot < 10:

   # noppa1 = noppa2 = heitot = 0
   # while ( noppa1!=6 or noppa2!=6):
      #  noppa1 = random.randint(1,6)
      #  noppa2 = random.randint(1,6)
      #  heitot = heitot + 1
   # print(f"tarvittiin {heitot:d} heittoa.")
   # toistot = toistot + 1
   # heitot_yhteensä = heitot_yhteensä + heitot

#heitot_keskimäärin = heitot_yhteensä/toistot
#print(f"heitot keskimäärin: {heitot_keskimäärin:6.2f}")

