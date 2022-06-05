from fileinput import close
from typing import final


def main():
    from Car import Car

    def getLastID():
        f = open("test.txt",'r',encoding = 'utf-8')

        last_line = f.readlines()[-1]
        return last_line.split(", ")[0]

        


    def printheader():
        print('-'*160)
        print('|'+'Id'.center(30)+'| '+' Name'.center(30)+'| '+'Model'.center(30)+'| '+' Year'.center(30)+'| '+'Price'.center(30)+ '|')
        print('-'*160)

    def readCarData():
        
            f = open("test.txt",'r',encoding = 'utf-8')
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
        with open("test.txt",'a+',encoding = 'utf-8') as f:
            f.readline()
            carid = int(getLastID())+1
            f.write("\n")
            data = "{0}, {1}, {2}, {3}, {4}".format(carid,obj.CarName,obj.Model,obj.year,obj.price)
            f.write(data)
            print("Car added to Database")
            
            
    c = Car('A3','AUDI','2023', '50000.0')
    c1 = Car('XRT','mazda','2022', '10000.0')
    c2 = Car('CRV','honda','2022', '10000.0')
    addCarToDB(c)
    addCarToDB(c1)
    addCarToDB(c2)
    readCarData()


if __name__ == "__main__":
    main()