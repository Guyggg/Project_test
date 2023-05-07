class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on: Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class Pickup(Vehicle):
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on: Air")

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()