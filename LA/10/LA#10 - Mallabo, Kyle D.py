class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"{self.brand} {self.model} uses {self.fuel_type}")

class Car(Vehicle):
    pass

vroom = Car("Ford", "Everest", "Diesel")
vroom.describeVehicle()

class Motorcycle(Vehicle):
    pass

broom = Motorcycle("Ducati", "Panigale", "Unleaded")
broom.describeVehicle()