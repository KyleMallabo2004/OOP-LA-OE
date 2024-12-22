class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def basic_attack(self, target):
        target.health = target.health - self.attack_power

Aamon = Player("Aamon", 800, 100)
Gusion = Player("Gusion", 700, 90)

print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Aamon.basic_attack(Gusion)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Aamon.basic_attack(Gusion)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Gusion.basic_attack(Aamon)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Aamon.basic_attack(Gusion)
Gusion.basic_attack(Aamon)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Gusion.basic_attack(Aamon)
Gusion.basic_attack(Aamon)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Gusion.basic_attack(Aamon)
Gusion.basic_attack(Aamon)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

Aamon.basic_attack(Gusion)
Aamon.basic_attack(Gusion)
print(Aamon.name, Aamon.health, Aamon.attack_power)
print(Gusion.name, Gusion.health, Gusion.attack_power)

print(Aamon.name, "won the match.")