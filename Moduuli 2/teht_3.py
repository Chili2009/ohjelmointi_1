#Kysytään tiedot

kanta= float(input("Anna suoakulmion kanta"))
korkeus = float( input("Anna suorakulmion korkeus"))


#laskutoimitukset
A=kanta *korkeus
piiri= (kanta * 2) + (korkeus * 2)

# tulostukset

print(f"Ala = {A}")
print(f"piiri = {piiri}")

