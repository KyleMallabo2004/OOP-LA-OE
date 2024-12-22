class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"my car is {self.name} {self.brand}"


my_car = Car("Aventador", "Lamborghini")
my_car2 = Car("911", "Porsche")

print(my_car)  
print(my_car2)

del my_car2
try:
    print(my_car2)
except NameError:
    print("my_car2 has been deleted.")

print(my_car)