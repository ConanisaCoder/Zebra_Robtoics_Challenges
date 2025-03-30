from classes import *
car_dict= {}
# key = make-model-year
# Car Class
def add(dictval,tpye="c"):
    if tpye == "c":
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
    elif tpye == "B":
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
        typevar = ""
        while not typevar in ["Standard","Sport"]: 
            typevar = input("Enter Tpye(Standard/Sport): ").strip().capitalize()
        dictval[make+"-"+model+"-"+str(year)] = Bike(typevar,make,model,year,price,used,mileage,door,available)
    elif tpye == "T":
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
    print(dictval[key])
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
def Writefile(dictval,filepath):
    pass
def Readfile_to_dict(dictval,filepath:str):
    openfiledict = open(filepath,"r")
    listdata = openfiledict.readlines()
def Writedict_to_file(dictval:dict,filepath:str):
    write_file = open(filepath,"w")
    for key in dictval:
        if (dictval[key]).classvar == "Car":
            milleage = (dictval[key]).milleage
            # Class Var,Make,Model,year,price,used,milleage,doors,Avaiable
            list_data_writedict_to_file = list_date = ["Class: " + str((dictval[key]).classvar)," Make: " +(dictval[key]).make,"Model: " +(dictval[key]).model ,"Year: " +str((dictval[key]).year),"Used: " + str((dictval[key]).used),"Milleage: " + str((dictval[key]).milleage),"Doors: " + str((dictval[key]).doors), "Available: " + str((dictval[key]).available)]
            for data in list_data_writedict_to_file:
                write_file.write(data +"\n")
            write_file.write("\n")
        elif (dictval[key]).classvar == "Bike":
            list_data_writedict_to_file = list_date = ["Class: " + str((dictval[key]).classvar)," Make: " +(dictval[key]).make,"Model: " +(dictval[key]).model ,"Year: " +str((dictval[key]).year),"Used: " + str((dictval[key]).used),"Milleage: " + str((dictval[key]).milleage),"Doors: " + str((dictval[key]).doors), "Available: " + str((dictval[key]).available), "Tpye: " + str((dictval[key]).typevar)]
            for data in list_data_writedict_to_file:
                write_file.write(data +"\n")
            write_file.write("\n")
        elif (dictval[key]).classvar == "Truck":
            list_data_writedict_to_file = list_date = ["Class: " + str((dictval[key]).classvar)," Make: " +(dictval[key]).make,"Model: " +(dictval[key]).model ,"Year: " +str((dictval[key]).year),"Used: " + str((dictval[key]).used),"Milleage: " + str((dictval[key]).milleage),"Doors: " + str((dictval[key]).doors), "Available: " + str((dictval[key]).available), "Tpye: " + str((dictval[key]).typevar), "Bed: " + str((dictval[key]).bed)]
            for data in list_data_writedict_to_file:
                write_file.write(data +"\n")
            write_file.write("\n")