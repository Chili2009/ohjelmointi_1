#class Dog:
 #   def __init__(self, name, birth_Year, bark = "Wuh Wuh"):
  #      self.name = name
   #     self.birth_Year = birth_Year
    #    self.bark = bark

#    def barking(self, times):
 #       for i in range(times):
  #          print(self.bark)
   #     return


#dog1 = Dog("Akseli", 2001)
#dog2 = Dog("Mia", 1995, "dorka")
#dog3 = Dog("Jasmin", 1997, "olen kissa")
#dog4 = Dog("Lutri", 1999, "ne ampu rytkön Villen!")

#dog1.barking(5)
#dog2.barking(8)
#dog3.barking(2)
#dog4.barking(7)

class Car:
    def __init__(self, register_Number, top_Speed):
        self.register_Number = register_Number
        self.top_Speed = top_Speed
        self.velocity = 0
        self.traveled_Distance = 0

    cars = ["Toyota", "BMW", "Mersu", "Honda",
            "lancia", "Volvo", "Volkswagen", "Kia",
            "Hyundai", "Nissan"]
    for i in range(10):
        cars.append(cars("a" + i, 10))

    for car in cars:
     print (cars.print_info())

    def print_info(self):
        print(f"Auton {self.register_Number} "
              f"huippunopeus {self.top_Speed} km/h "
              f"tämänhetkinen nopeus {self.velocity} km/h "
              f"kuljettu matka {self.traveled_Distance} km/h ")


    def accelerate(self, speed_Change):
        if 0 < self.velocity + speed_Change < self.top_Speed:
            self.velocity = self.velocity + speed_Change
        elif self.velocity + speed_Change <= 0:
            self.velocity = 0
        elif self.velocity + speed_Change > self.top_Speed:
            self.velocity = self.top_Speed

    def traveled(self, hours):
        self.traveled_Distance = {self.velocity * hours + self.traveled_Distance}


Toyota = Car("ABC-1", 142)
Toyota.print_info()
Toyota.accelerate(30)
Toyota.accelerate(70)
Toyota.accelerate(50)
Toyota.print_info()
Toyota.accelerate(-200)
Toyota.traveled(1.5)
Toyota.print_info()


















