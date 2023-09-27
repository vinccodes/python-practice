class Car:
    def __init__(self, model, make, year, color):
        self.model = model
        self.make = make
        self.year = year
        self.color = color

    def startEngine(self):
        print("Car engine has been started")

    def stopEngine(self):
        print("Car engine has been stopped")


myCar = Car('camry','toyota', '2006', 'silver')
print(myCar.startEngine())