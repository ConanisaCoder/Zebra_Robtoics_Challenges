from classes import *
car_dict= {}
# key = make-model-year
# Car Class
def add_car(dictval):
    make = input("Enter Make: ").strip().lower().capitalize()
    model = input("Enter Model: ").strip().lower().capitalize()
    while True:
        try:
            year = int(input("Enter Year: "))
            price = int(input("Enter Price: "))
            mileage = int(input("Enter Mileage: "))
            door = int(input("Enter Doors: "))
            break
        except ValueError:
            pass
    finding_used = True
    while finding_used == True:
        used_t_f = input("Is the Car used (y/n): ").lower()
        if used_t_f == "y" or used_t_f == "n":
            finding_used = False
    if used_t_f == "y":
        used = True
    else:
        used = False
    finding_available = True
    while finding_available == True:
        ava_t_f = input("Is this car available (y/n): ").lower()
        if ava_t_f == "y" or ava_t_f == "n":
            finding_available = False
    if ava_t_f == "y":
        available = True
    else: 
        available = False
    dictval[make+"-"+model+"-"+str(year)] = Car(make,model,year,price,used,mileage,door,available)
def returnmake(make,dictval):
    listmodel = []
    for val in dictval:
        if make in val:
            listmodel.append(listmodel)
    print("The Number of " + str(make) +": " + str(len(listmodel)))
def reutrnval(key,dictval):
    make = str(dictval[key].make)
    model = str(dictval[key].model)
    year = str(dictval[key].year)
    price = str(dictval[key].price)
    used = str(dictval[key].used)
    millage = str(dictval[key].milleage)
    doors = str(dictval[key].doors)
    available = str(dictval[key].available)
    print("Make: " + make)
    print("Model: " + model)
    print("Year: " + year)
    print("Price: " +price)
    print("Used: " + used)
    print("Milleage: "+ millage)
    print("Doors: " + doors)
    print("Available: " + available)
def updateval(key,dictval): #update A Store Val with the Car Class
    updating = True
    while updating == True:
        print("(0) Close\n(1) Make\n(2) Model\n(3) Year\n(4) Price\n(5) Usage\n(6) Mileage\n(7) Doors\n(8) Availablitly ")
        while True:
            try:
                updatevalchoice = int(input("Enter Value: "))
                break
            except ValueError:
                pass
        match updatevalchoice:
            case 0:
                updating = False
            case 1:
                newmake = input("Enter Make: ").strip().lower().capitalize()
                dictval[key].make = newmake
            case 2:
                newmodel = input("Enter Model: ").strip().lower().capitalize()
                dictval[key].model = newmodel
            case 3:
                while True:
                    try:
                        newyear = int(input("Enter Year: "))
                        break
                    except ValueError:
                        pass
                dictval[key].year = newyear
            case 4:
                while True:
                    try:
                        newprice = int(input("Enter Price: "))
                        break
                    except ValueError:
                        pass
                dictval[key].price = newprice
            case 5:
                findingused = True
                while findingused == True:
                    findingusedval = input("Is the car used (y/n): ").lower()
                    if findingusedval == "y" or findingusedval == "n":
                        findingused = False
                if findingused == "y":
                    dictval[key].used = True
                elif findingused == "n":
                    dictval[key].used = False
            case 6:
                while True:
                    try:
                        newmilleage = int(input("Enter Milleage: "))
                        break
                    except ValueError:
                        pass
                dictval[key].milleage = newmilleage
            case 7:
                while True:
                    try:
                        newdoors = int(input("Enter Doors: "))
                        break
                    except ValueError:
                        pass
                dictval[key].doors = newdoors
            case 8:
                findingava = True
                while findingava == True:
                    ava = input("Avaiable (y/n): ").lower()
                    if ava == "y" or ava == "n":
                        findingava = False
                if ava == "y":
                    dictval[key].available = True
                else:
                    dictval[key].available = True 

