class FavoriteFood:
    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        self.name = name
        self.ingredient1 = ingredient1
        self.ingredient2 = ingredient2
        self.ingredient3 = ingredient3

    def __str__(self):
        return f"{self.name} is made with {self.ingredient1}, {self.ingredient2}, and {self.ingredient3}."

pizza = FavoriteFood("Pizza", "cheese", "tomato sauce", "pepperoni")
burger = FavoriteFood("Burger", "beef patty", "lettuce", "cheese")
sushi = FavoriteFood("Sushi", "rice", "nori", "salmon")

print(pizza)
print(burger)
print(sushi)