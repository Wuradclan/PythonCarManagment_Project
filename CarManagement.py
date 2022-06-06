

#class CarManagement:

from distutils.log import info


def main():
    from Car import Car
    from CarList import CarList
    dbfile = "db.txt"

    print('Welcomne to CarDataBaseManager!')
   
    
    def getLastID():
        f = open(dbfile,'r',encoding = 'utf-8')

        last_line = f.readlines()[-1]
        return last_line.split(", ")[0]


    def printheader():
        print('-'*160)
        print('|'+'Id'.center(30)+'| '+' Name'.center(30)+'| '+'Model'.center(30)+'| '+' Year'.center(30)+'| '+'Price'.center(30)+ '|')
        print('-'*160)

    def readCarData():
        
            f = open(dbfile,'r',encoding = 'utf-8')
            lines = []
            printheader()
            #if len(f.read())>0:

            for i, line in enumerate(f):
                carinfolist = list(line.split(", "))
                #print(len(carinfolist))
                lines.append(carinfolist)
                #print(len(lines))
                if(len(carinfolist)>0):
                    print("|{0}| {1}| {2}| {3}| {4}|\n".format(str(lines[i][0]).center(30),str(lines[i][1]).center(30),str(lines[i][2]).center(30),str(lines[i][3]).center(30),str(lines[i][4]).strip("\n").center(30)))
            print('-'*160)   

    def addCarToDB(obj:Car):
        with open(dbfile,'a+',encoding = 'utf-8') as f:
            f.readline()
            carid = int(getLastID())+1
            f.write("\n")
            data = "{0}, {1}, {2}, {3}, {4}".format(carid,obj.CarName,obj.Model,obj.year,obj.price)
            f.write(data)
            print("Car{0} added to Database\n".format(obj.CarName))
            
    def addCarToList(obj:Car):
        carinfolist = []
        carinfolist.append(obj.carid)
        carinfolist.append(obj.CarName)
        carinfolist.append(obj.Model)
        carinfolist.append(obj.year)
        carinfolist.append(obj.price)
        print(carinfolist)

    def searchDb(query:str):
        
            f = open(dbfile,'r',encoding = 'utf-8')
            lines = []
            printheader()
            #if len(f.read())>0:

            for y, line in enumerate(f):
                carinfolist = list(line.split(", "))
                
                for x in carinfolist:
                    if(query in x or query.upper() in x or query.lower() in x):
                        lines.append(carinfolist)
                #print(len(lines))
            for i in range(len(lines)):
                if(len(carinfolist)>0):
                    print("|{0}| {1}| {2}| {3}| {4}|\n".format(str(lines[i][0]).center(30),str(lines[i][1]).center(30),str(lines[i][2]).center(30),str(lines[i][3]).center(30),str(lines[i][4]).strip("\n").center(30)))
                    print('-'*160)
            input("enter any key tpo go back to the menu ")   

    while 1:
        print('What would you like to do ?')
        print('1- Add a car')
        print('2- Search for a car')
        print('3- Save the database file')
        print('4- Remove a car by id\n')
        print('\n5- Quit')
        action = input('What do you want to do ?')
        if int(action)==1:
            carName = str(input('Enter Car Name : '))
            brand = str(input('what is the brand  : '))
            year = str(input ('Year of manufacture : '))
            price = str(input('Price of car : '))
            newCar =  str(Car(carName,brand,year,price))
            #addCarToDB(newCar)
            listCars = CarList()
            listCars.addCar(newCar)

        if int(action)==2:
            print('Search for a car by any terms')
            query = input('Enter your search query: ')
            print('searchin for the query : '+query)
            searchDb(query)


    
if __name__ == "__main__":
    main()


