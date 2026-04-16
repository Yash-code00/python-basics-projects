class vehicle():
    def __init__(self,brand,year,speed):
        self.brand = brand
        self.year = year
        self.speed = speed
    def accerlate(self,increare):
        if increare <= 0:
            print("pls enter the adding speed")
        else:
            self.speed += increare
    def decrese(self,decre):
        if decre < 0:
            print("pls enter plus value")
        elif decre > self.speed:
            self.speed = 0 
            print("vehicle stopped")
        else:
            self.speed -= decre
    def info(self):
        return f"the brand {self.brand} and the year of makeing {self.year} and the speed is {self.speed} km/h "
class car(vehicle):
    def __init__(self, brand, year, speed, doors):
        self.door = doors
        super().__init__(brand, year, speed)
    def honk(self):
        print("pee pee")
    def info(self):
        return f"the brand {self.brand} and the year of makeing {self.year} and the speed is {self.speed} km/h doors {self.door}"
class motorc(vehicle):
    def __init__(self, brand, year, speed,sidecar=False):
        self.side = sidecar
        super().__init__(brand, year, speed)
    def wheelie(self):
        if self.speed > 20:
            print("wheelie done")  
        else:
            print("wheelie can't be done")
    def info(self):
        return f"the brand {self.brand} and the year of makeing {self.year} and the speed is {self.speed} km/h and sidecare {self.side} "

    
m1=motorc("harley",2019,35)
m2=motorc("Honda",2021,15,True)
c1=car("toyota",2020,50,4)

c1.decrese(-60)
print("this is a car",c1.info())
c1.honk()
print("this is a motorcycle",m1.info())
m1.wheelie()
print("this is a motorcycle",m2.info())
m2.wheelie()

    

