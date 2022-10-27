class Dog:
    counter = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Dog.counter += 1
    def bark(self, times):
        for i in range(times):
            if self.weight > 10:
                print (f"wuf wuf! Olen {self.name}")
            else:
                print(f"wuf wuf! olen {self.name}")


dog1 = Dog("Rekku", 8)
dog2 = Dog("Ruffe", 12)
dog1.bark(3)
dog2.bark(1)
print("koiria yhteensä:", Dog.counter)

#print("koira 1:", dog1.name, dog1.weight, "kg")
#print("koira 2:", dog2.name, dog2.weight, "kg")
