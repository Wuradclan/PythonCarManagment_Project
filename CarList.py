class CarList:
    from Car import Car
    def __init__(self):
        self.carsList = []
    
    def addCar(self,obj:Car):
        self.carsList.append(obj)
        print(str(obj.id)+' '+obj.CarName+' is added to the list\n\n')

    

