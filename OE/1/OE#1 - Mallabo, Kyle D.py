class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Damage Type: {self.damage_type}"

hero1 = Hero("Chou", "Fighter", "Physical")
hero2 = Hero("Cyclops", "Mage", "Magic")
hero3 = Hero("Layla", "Marksman", "Physical")
hero4 = Hero("Rafaela", "Support", "Magic")
hero5 = Hero("Alucard", "Jungle", "Physical")

def print_team_description(heroes):
    print("Mobile Legends Dream Team:")
    for hero in heroes:
        print(hero)

team = [hero1, hero2, hero3, hero4, hero5]
print_team_description(team)
