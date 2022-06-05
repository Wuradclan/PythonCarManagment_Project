class Car:
    carid = 0
    def __init__(self, name, model, year, price):
        Car.carid+=1
        self.id = Car.carid
        self.CarName = name
        self.Model = model
        self.year =  year
        self.price =  price