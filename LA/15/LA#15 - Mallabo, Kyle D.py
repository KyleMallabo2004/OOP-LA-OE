class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Bark!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Chirp!"

class Fish:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "" #Or None if you want to explicitly indicate no sound

def animal_sounds(animal): #Added underscore for better naming convention
    print(f"{animal.name}: {animal.speak()}")

dog = Dog("Doggo")
cat = Cat("Kitty")
bird = Bird("Tweety")
fish = Fish("Goldie")

animals = (dog, cat, bird, fish)

for animal in animals:
    animal_sounds(animal)