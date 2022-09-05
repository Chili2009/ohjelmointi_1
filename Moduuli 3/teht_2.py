User = input("Hyttiluokka: ")

if User == ("LUX") or User == ("lux"):
    print("LUX on parvekkeellinen hytti yläkannella")
elif User == ("A") or User ==("a"):
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif User ==("B") or User ==("b"):
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif User ==("C") or User == ("c"):
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka.")