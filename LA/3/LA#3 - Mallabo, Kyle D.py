class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        print(f"{self.name} is a {self.role} hero")

name = hero("Aamon", "Jungle")
name.describe()