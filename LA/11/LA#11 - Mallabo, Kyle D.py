class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"I'm using {self.brand} {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

cp = Android("Huawei", "Nova y70")
cp.describePhone()