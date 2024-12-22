class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


my_car = Car("honda", "blue")
another_car = Car("toyota", "red")


print(my_car.brand, my_car.color)      
print(another_car.brand, another_car.color) 


my_car.color = "green"
print(my_car.brand, my_car.color)      