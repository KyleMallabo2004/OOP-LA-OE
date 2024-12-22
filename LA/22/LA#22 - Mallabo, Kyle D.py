class BirthdayParty:
    def __init__(self, theme, foods, special_dish, secret_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
        self._secret_dish = secret_dish

    def show_foods(self):
        print(f"Party Theme: {self.theme}")
        print("Foods List:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        self._reveal_secret_dish()

    def _reveal_secret_dish(self):
        print(f"Secret Dish: {self._secret_dish}")

party1 = BirthdayParty("Beach Birthday Party", ["Spaghetti", "Hotdog on Stick", "Pancit Bihon"], "Lechon", "Ube Cake")
party2 = BirthdayParty("Simple Birthday", ["Barbecue", "Chicken Lollipop", "Puto"], "Lumpiang Shanghai", "Kutsinta")
party3 = BirthdayParty("Big Birthday Party", ["Menudo", "Fried Chicken", "Macaroni Salad"], "Crispy Pata", "Mango Float")

party1.show_foods()
print("\n")
party2.show_foods()
print("\n")
party3.show_foods()