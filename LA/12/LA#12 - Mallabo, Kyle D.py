class Toy():
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def describeToy(self):
        print(f"Im using {self.name} worth {self.prize}")

class Car (Toy):
    def __init__(self, name, prize):
        super().__init__(name, prize)

laruan = Car("Hot Wheels Volkswagen Beach Bomb", "$125.000")
laruan.describeToy()