class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Spiderman: Name: {self.name}, Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, age):
        super().__init__('Tobey', age)
        self.movieTitle = 'Spider-Man (2002)'

class Andrew(Spiderman):
    def __init__(self, age):
        super().__init__('Andrew', age)
        self.movieTitle = 'The Amazing Spider-Man (2012)'

class Tom(Spiderman):
    def __init__(self, age):
        super().__init__('Tom', age)
        self.movieTitle = 'Spider-Man: Homecoming (2017)'

tobey = Tobey(46)
andrew = Andrew(41)
tom = Tom(27)

print(f"{tobey.name.upper()} starred in {tobey.movieTitle}")
print(f"{andrew.name.upper()} starred in {andrew.movieTitle}")
print(f"{tom.name.upper()} starred in {tom.movieTitle}")