

#class CarManagement:

from distutils.log import info


def main():
    from Car import Car
    from CarList import CarList
    dbfile = "database.txt"

    print('Welcomne to CarDataBaseManager!')


    def printheader():
        print('-'*160)
        print('|'+'Id'.center(30)+'| '+' Name'.center(30)+'| '+'Model'.center(30)+'| '+' Year'.center(30)+'| '+'Price'.center(30)+ '|')
        print('-'*160)



    def loadCarData(obj:CarList):
        
            f = open(dbfile,'r',encoding = 'utf-8')
            obj.carsList=[]
            lines = []
            printheader()
            #obj.carsList = [Car() for i in range(enumerate(f))]
            for i, line in enumerate(f):
                carinfolist = list(line.split(", "))
                #exec('var_' + str(i) + ' = ' + str(i))
                #print(carinfolist)
                obj.carsList.append(Car(carinfolist[1],carinfolist[2],carinfolist[3],carinfolist[4].strip('\n')))
                #print(obj.carsList)
                if(len(carinfolist)>0):
                    #print(obj.carsList[i].id, obj.carsList[i].CarName)
                    print("|{0}| {1}| {2}| {3}| {4}|".format(str(obj.carsList[i].id).center(30),str(obj.carsList[i].CarName).center(30),str(obj.carsList[i].Model).center(30),str(obj.carsList[i].year).center(30), str(float(str(obj.carsList[i].price).strip("\n"))).center(30)))
                    print('-'*160)
            

    def saveCarListToDB(obj:CarList):
        f = open(dbfile,'w',encoding = 'utf-8')
        for car in obj.carsList:
            data =  "{0}, {1}, {2}, {3}, {4}\n".format(car.id,car.CarName,car.Model,car.year,car.price)
            f.writelines(data)
            print("{0}, {1}, {2}, {3}, {4}".format(car.id,car.CarName,car.Model,car.year,car.price))
    
    def search(query:str):
        printheader()
        for i in range(len(listCars.carsList)):
            if(query in str(listCars.carsList[i]) or query.upper() in str(listCars.carsList[i]) or query.lower() in str(listCars.carsList[i])):
                print("|{0}| {1}| {2}| {3}| {4}|".format(str(listCars.carsList[i].id).center(30),str(listCars.carsList[i].CarName).center(30),str(listCars.carsList[i].Model).center(30),str(listCars.carsList[i].year).center(30), str(float(str(listCars.carsList[i].price).strip("\n"))).center(30)))
                print('-'*160)
        input("enter any key tpo go back to the menu ")
    
    def removeCar(id):
        car : Car
        for car in listCars.carsList:
            if int(car.id)==int(id):
                listCars.carsList.remove(car)
                print('\n',car.id,' Name = ',car.CarName, ' is removed')
        saveCarListToDB(listCars)
        search('')

        

    listCars = CarList()
    loadCarData(listCars)
    while 1:
        print('What would you like to do ?')
        

        print('1- Add a car')
        print('2- Search for a car')
        print('3- Save the database file')
        print('4- Remove a car by id\n')
        print('\n5- Quit')
        action = input('What do you want to do ?')
        if str(action) == '':
            print('Please Chose and option from this list')

        if int(action)==1:
            if (action == 'q' or action == 'Q'):
                quit = input('Do you wanna quit? enter "y" for yes or "n" for NO  : ')
                if (quit == 'y' or quit == 'Y'): break
                else :continue
            carName = str(input('Enter Car Name : '))
            if (carName  == 'q' or carName  == 'Q'):
                quit = input('Do you wanna quit? enter "y" for yes or "n" for NO  : ')
                if (quit == 'y' or quit == 'Y'): break
                else :continue
            brand = str(input('what is the brand  : '))
            if (brand  == 'q' or brand  == 'Q'):
                quit = input('Do you wanna quit? enter "y" for yes or "n" for NO  : ')
                if (quit == 'y' or quit == 'Y'): break
                else :continue
            
            year = str(input ('Year of manufacture : '))
            if (year  == 'q' or year  == 'Q'):
                quit = input('Do you wanna quit? enter "y" for yes or "n" for NO  : ')
                if (quit == 'y' or quit == 'Y'): break
                else :continue
            price = str(input('Price of car : '))
            if (price  == 'q' or price  == 'Q'):
                quit = input('Do you wanna quit? enter "y" for yes or "n" for NO  : ')
                if (quit == 'y' or quit == 'Y'): break
                else :continue
            listCars.addCar(Car(carName,brand,year,price))

        if int(action)==2:
            print('Search for a car by any terms')
            query = input('Enter your search query: ')
            print('searchin for the query : '+query)
            search(query)

        if int(action) == 3:
            #search('')
            car:Car
            for car in listCars.carsList:
                print(car)
            save = input('do you wan tto save to database ? enter (y) for yes and (n) for No :')
            if save == 'y' or save == 'Y':
                saveCarListToDB(listCars)

        if int(action) == 4:
            carid = input('enter the Car id to remove')
            confirm = input('confirm removing Car id :  enter (y) for Yes or (n) for No : ')
            if confirm == 'y' or confirm == 'Y':
                removeCar(carid)
            else: input("enter any key tpo go back to the menu ")

        if int(action) == 5:
            #search('')
            car:Car
            for car in listCars.carsList:
                print(car)
            save = input('do you wan to save to database  and Quit? enter (y) for yes and (n) for No  : ')
            if save == 'y' or save == 'Y':
                saveCarListToDB(listCars)
            break

            


    
if __name__ == "__main__":
    main()


