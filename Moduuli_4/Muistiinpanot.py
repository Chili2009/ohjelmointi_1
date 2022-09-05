command = ""
while command != "lopeta":          #while true jatkaa looppia loputtomiin
    command = input("komento> ")
    #muutetaan command arvo pieniksi kirjaimiksi
    command = command.lower()
    #print(f"suoritetaan toiminto {command}")
    if command == "tulosta":
        print("printtaillaan jotain")
    elif command == "piirrä" or command == "Piirrä":
        i = 0
        while i < 3:
            i += 1
            print("#####")
    elif command == "lopeta":
        print("lopetetaan ohjelma. heippa!")
        break #break = lopetus käsky looppeihin
    else:
        print("virheellinen komento. yritä uudelleen")

print("ohjelma sammutettu")
