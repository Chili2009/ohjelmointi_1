def laskekolmionala(kanta, korkeus):
    a = (kanta * korkeus) / 2
    print(f"Kolmion ala on {a:.2f}")
    return A


ka= float(input("Anna kolmion kanta  : "))
ko = float(input("Anna kolmion korkeus : "))
PintAla = laskekolmionala(ka, ko)
pinta(f"Kolmion ala on {pintaAla:.2f}")
