class Car:
    def __init__(self,make:str,model:str,Year:int,Price:int,Used:bool,Mileage:int,Doors:int,Available:bool): #Str,Str,Int,Int,Boolean,Int,Int,Boolean
        self.make = make
        self.model = model
        self.year = Year
        self.price = Price
        self.used = Used 
        self.milleage = Mileage
        self.doors = Doors
        self.available = Available
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
class Bike(Car):
    def __init__(self,tpyevar,make:str,model:str,Year:int,Price:int,Used:bool,Mileage:int,Doors:int,Available:bool):
        Car.__init__(make,model,Year,Price,Used,Mileage,Doors,Available)
        if tpyevar== "standard".capitalize() or tpyevar== "Sport Bike":
            self._tpyervar  = tpyevar
class Truck(Bike):
    def __init__(self,tpyevar:str,bed:str,make:str,model:str,Year:int,Price:int,Used:bool,Mileage:int,Doors:int,Available:bool):
        Bike.__init__(tpyevar,make,model,Year,Price,Used,Mileage,Doors,Available)
        if bed == "Long" or bed == "Short":
            bed += " bed"
            self.bed = bed