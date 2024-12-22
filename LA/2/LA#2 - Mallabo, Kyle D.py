class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

character = hero("Aamon", "Jungle")
character2 = hero("Lancelot", "Jungle")
print(character.name, character.role, character2.name, character2.role)