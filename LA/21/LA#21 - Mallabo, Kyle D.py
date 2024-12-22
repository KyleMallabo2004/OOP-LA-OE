class FavoriteFood:
    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        self.name = name
        self.ingredient1 = ingredient1
        self._ingredient2 = ingredient2
        self.ingredient3 = ingredient3

    def get_ingredient2(self):
        return self._ingredient2

    def set_ingredient2(self, ingredient2):
        self._ingredient2 = ingredient2

    def __str__(self):
        return f"{self.name} is made with {self.ingredient1}, {self.get_ingredient2()}, and {self.ingredient3}."

pizza = FavoriteFood("Pizza", "cheese", "tomato sauce", "pepperoni")

print(pizza.get_ingredient2())
pizza.set_ingredient2("pesto sauce")
print(pizza.get_ingredient2())
print(pizza)