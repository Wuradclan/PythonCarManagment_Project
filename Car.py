class Car:
    carid = -1
    def __init__(self, name, model, year, price):
        Car.carid+=1
        self.id = Car.carid
        self.CarName = name
        self.Model = model
        self.year =  year
        self.price =  price
        #print('id = ',self.id,'name=',self.CarName,'model=', self.Model, 'year =',self.year)
    def __str__(self):
        return ('id= '+str(self.id)+', name= '+str(self.CarName)+', model= '+str(self.Model)+', year= '+str(self.year)+', price= '+str(self.price).strip("\n"))