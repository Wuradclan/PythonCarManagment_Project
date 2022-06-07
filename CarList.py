from Car import Car


class CarList:
    from Car import Car
    def __init__(self):
        self.carsList = []
    
    def addCar(self,obj:Car):
        car:Car
        isInDB = False
        for car in self.carsList:
            if obj.CarName == car.CarName and obj.Model == car.Model and obj.year == car.year and obj.price == car.price:
                print('\nCar already exists in database. Not adding again!\n')
                isInDB=True
                
            elif obj.CarName != car.CarName and obj.Model != car.Model and obj.year != car.year and obj.price != car.price:
                isInDB = False
        
        if isInDB==False:
            self.carsList.append(obj)
            print('\n',obj.id,' ',obj.CarName,' is added to the list\n\n')

    

