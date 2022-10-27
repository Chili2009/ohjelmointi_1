#number = 1
#while number <= 1000:
    #if (number % 3 == 0):
        #print(number)
    #number = number + 1



#tuumat = float(input("Anna tuumat(negatiivinen lopettaa): "))
#while tuumat >= 0:
        #sentit = tuumat * 2.54
        #print(f"{sentit:.2f}cm")
        #tuumat = float(input("anna tuumat(negatiivinen lopettaa): "))

#tuumat = float(input("Anna tuumat(negatiivinen lopettaa): "))
#while tuumat >= 0:
    #sentit = tuumat * 2.54
    #print(f"{sentit:.2f}cm")
    #tuumat = float(input("anna tuumat(negatiivinen lopettaa): "))

#user = input("Sano luku: ")
#minvalue = maxvalue = int(user)

#while user != "":
    #user = input("Sano luku: ")
    #if user == "":
     #   break
    #userint = int(user)
    #if userint < minvalue:
     #   minvalue = int(user)
    #if userint > maxvalue:
     #   maxvalue = userint

#print(f"Pienin arvo: {minvalue}, suurin arvo: {maxvalue}")

#import random

#arvaus_on = random.randint(1,11)
#arvaus = int(input("Arvaa kokonaisluku 1-10: "))
#while arvaus != arvaus_on:
    #if arvaus > arvaus_on:
        #print("liian suuri arvaus")
    #else:
        #print("liian pieni arvaus")
    #arvaus = int(input("Arvaa kokonaisluku 1-10: "))

#else:
    #print("arvaus oikein!")

user = "python"
password = "rules"
anna1 = input(f"anna käyttäjätunnus: ")
anna2 = input(f"anna salasana: ")
i = 1
while i < 5:
    if anna1 == user and anna2 == password:
        print("Tervetuloa")
        break
    else:
        print("pääsy evätty")
        i += 1
        anna1 = input("Anna käyttäjätunnus: ")
        anna2 = input("Anna salasana: ")
if i == 5:
    print("pääsy evätty")


















































































