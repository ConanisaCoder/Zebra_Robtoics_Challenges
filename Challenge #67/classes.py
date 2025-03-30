class Car:
    def __init__(self,make:str,model:str,Year:int,Price:int,Used:bool,milleage:int,Doors:int,Available:bool): #Str,Str,Int,Int,Boolean,Int,Int,Boolean
        self.make = make
        self.model = model
        self.year = Year
        self.price = Price
        self.used = Used 
        self.milleage = milleage
        self.doors = Doors
        self.available = Available
        self.classvar = "Car" 
    def marksold(self):
        self.available=False
    def changemillage(self):
        print(str(self.milleage))
        while True:
            try:
                newmilage = int(input("Enter mileage: "))
                break
            except ValueError:
                print("Enter Int Val")
        self.milleage =newmilage
    def stringify(self):
        return('Car: ' + str(self.make)+"-"+str(self.model)+"-"+str(self.year))
    def setused(self):
        var = ""
        setused = ["y","yes","no","n"]
        while len(var)>0 and var in setused :
            var = input('Used (y/n): ').lower()
        if var in setused[:2]:
            self.used = True
        else:
            self.used = False
    def update(self,make =None,model =None,Price=None,Year= None,Used=None,milleage=None,Doors=None,Available = None):
        self.make = make or self.make
        self.model = model or self.model
        self.price = Price or self.bed
        self.year = Year or self.year
        self.used = Used or self.used
        self.milleage = milleage or self.milleage
        self.doors = Doors or self.doors
        self.available = Available or self.available
    def __str__(self):
        return f"Car: {self.make} - {self.model} - {self.year}"
class Bike(Car):
    def __init__(self,typevar,make:str,model:str,Year:int,Price:int,Used:bool,milleage:int,Doors:int,Available:bool):
        super().__init__(make,model,Year,Price,Used,milleage, Doors,Available)
        self.classvar = "Bike"
        if typevar in ["Standard","Sport"]:
            self.typevar  = typevar + " Bike"
    def __str__(self):
        return f"Bike: {self.typevar} - {self.make} - {self.model} - {self.year}"
    def update(self,typevar=None,make =None,model =None,Price=None,Year= None,Used=None,milleage=None,Doors=None,Available = None):
        self.typevar = typevar or self.typevar
        self.make = make or self.make
        self.model = model or self.model
        self.price = Price or self.bed
        self.year = Year or self.year
        self.used = Used or self.used
        self.milleage = milleage or self.milleage
        self.doors = Doors or self.doors
        self.available = Available or self.available
class Truck(Car):
    def __init__(self,typevar:str,bed:str,make:str,model:str,Year:int,Price:int,Used:bool,milleage:int,Doors:int,Available:bool):
        super().__init__(make,model,Year,Price,Used,milleage,Doors,Available)
        if typevar in ["Full","Mid"]:
            self.typevar = typevar
        self.classvar = "Truck"
        if bed in ["Long","Short"]:
            bed += " bed"
            self.bed = bed
    def update(self,typevar=None,make =None,model =None,bed= None,Price=None,Year= None,Used=None,milleage=None,Doors=None,Available = None):
        self.typevar = typevar or self.typevar
        self.make = make or self.make
        self.model = model or self.model
        self.bed = bed or self.bed
        self.price = Price or self.bed
        self.year = Year or self.year
        self.used = Used or self.used
        self.milleage = milleage or self.milleage
        self.doors = Doors or self.doors
        self.available = Available or self.available
    def __str__(self):
        return f"Truck: {self.typevar} - {self.bed} - {self.make} - {self.model} - {self.year}"