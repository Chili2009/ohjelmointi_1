vuosi = int(input("Anna vuosi: "))
if vuosi % 4 == 0 and (v % 100 != 0 or vuosi % 400 == 0):
    print("Karkasuvuosi")
else:
    print("Ei karkausvuosi")