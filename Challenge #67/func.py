from classes import *
car_dict= {}
# key = make-model-year
# Car Class
def update(dictkey):
    match dictkey._classvar:
        case "Car":
            print("Blank To Not Change")
            while True:
                    year = int(input(f"Enter Year ({dictkey.year}): ")) or None
                    doors = int(input(f"Enter Doors({dictkey.doors}): ")) or None
                    price = int(input(f"Enter Price({dictkey.price}): ")) or None
                    milleage = int(input(f"Enter Milleage ({dictkey.milleage}): ")) or None
                    yearinstance,doorsinstance,priceinstance,milleageinstance = isinstance(year,(int,type(None))), isinstance(doors,(int,type(None))),isinstance(price,(int,type(None))), isinstance(milleage,(int,type(None)))
                    if (yearinstance,doorsinstance,priceinstance,milleageinstance).count(True) == 4:
                        break
            make = input("Enter Make: ").strip().capitalize() or None
            model = input("Enter Model: ").strip().capitalize() or None
            while True:
                available = input("Enter Availablilty(True,T/False,F): ").strip().capitalize() or None
                if available in ["T","True"]:
                    available = bool(available)
                    break
                elif available in ["F","False"]:
                    available = bool(available)
                elif available == None:
                    break
            while True:
                used = input("Enter Usage(True,T/False,F): ").strip().capitalize() or None
                if used in ["T","True"]:
                    used= bool(used)
                    break
                elif used  in ["F","False"]:
                    used = bool(used)
                elif used == None:
                    break
            dictkey.update(make=make,model=model,Price=price,Year=year,Used=used,milleage=milleage,Doors=doors,Available = available)
        case "Truck":
            print("Blank To Not Change")
            while True:
                    year = int(input(f"Enter Year ({dictkey.year}): ")) or None
                    doors = int(input(f"Enter Doors({dictkey.doors}): ")) or None
                    price = int(input(f"Enter Price({dictkey.price}): ")) or None
                    milleage = int(input(f"Enter Milleage ({dictkey.milleage}): ")) or None
                    yearinstance,doorsinstance,priceinstance,milleageinstance = isinstance(year,(int,type(None))), isinstance(doors,(int,type(None))),isinstance(price,(int,type(None))), isinstance(milleage,(int,type(None)))
                    if (yearinstance,doorsinstance,priceinstance,milleageinstance).count(True) == 4:
                        break
            make = input("Enter Make: ").strip().capitalize() or None
            model = input("Enter Model: ").strip().capitalize() or None
            while True:
                available = input("Enter Availablilty(True,T/False,F): ").strip().capitalize() or None
                if available in ["T","True"]:
                    available = bool(available)
                    break
                elif available in ["F","False"]:
                    available = bool(available)
                elif available == None:
                    break
            while True:
                used = input("Enter Usage(True,T/False,F): ").strip().capitalize() or None
                if used in ["T","True"]:
                    used= bool(used)
                    break
                elif used  in ["F","False"]:
                    used = bool(used)
                elif used == None:
                    break
            while True:
                bed = input("Enter Bed(Short,Long): ").strip().capitalize()
                if bed in ["Short","Long"]:
                    break
            while True:
                typevar = input("Enter Tpye(Full,Mid): ").strip().capitalize()
                if typevar in ["Full","Mid"]:
                    break
            dictkey.update(typevar=typevar,make =make,model =model,bed= bed,Price=price,Year= year,Used=used,milleage=milleage,Doors=doors,Available = available)
        case "Bike":
            print("Blank To Not Change")
            while True:
                    year = int(input(f"Enter Year ({dictkey.year}): ")) or None
                    doors = int(input(f"Enter Doors({dictkey.doors}): ")) or None
                    price = int(input(f"Enter Price({dictkey.price}): ")) or None
                    milleage = int(input(f"Enter Milleage ({dictkey.milleage}): ")) or None
                    yearinstance,doorsinstance,priceinstance,milleageinstance = isinstance(year,(int,type(None))), isinstance(doors,(int,type(None))),isinstance(price,(int,type(None))), isinstance(milleage,(int,type(None)))
                    if (yearinstance,doorsinstance,priceinstance,milleageinstance).count(True) == 4:
                        break
            make = input("Enter Make: ").strip().capitalize() or None
            model = input("Enter Model: ").strip().capitalize() or None
            while True:
                available = input("Enter Availablilty(True,T/False,F): ").strip().capitalize() or None
                if available in ["T","True"]:
                    available = bool(available)
                    break
                elif available in ["F","False"]:
                    available = bool(available)
                elif available == None:
                    break
            while True:
                used = input("Enter Usage(True,T/False,F): ").strip().capitalize() or None
                if used in ["T","True"]:
                    used= bool(used)
                    break
                elif used  in ["F","False"]:
                    used = bool(used)
                elif used == None:
                    break
            while True:
                typevar = input("Enter Type (Standard,Sport): ").strip().capitalize()
                if typevar in ["Standard","Sport"]:
                    break
            dictkey.update(typevar=typevar,make =make,model =model,Price=price,Year= year,Used=used,milleage=milleage,Doors=doors,Available = available)
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
            used = True(make=make,model=model,Price=price,Year=year,Used=used,milleage=milleage,Doors=doors,Available = available)
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
    elif tpye == "B": # FIX
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
    elif tpye == "T": #FIX
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