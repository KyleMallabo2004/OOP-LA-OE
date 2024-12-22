class Car:  
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car("honda", "blue") 
print(my_car.brand, my_car.color)
my_car.color = "red"
print(my_car.brand, my_car.color)

another_car = Car("Toyota", "white") 
print(another_car.brand, another_car.color)