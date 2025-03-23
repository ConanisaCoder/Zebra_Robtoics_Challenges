class Car:
    def __init__(self,make,model,Year,Price,Used,Mileage,Doors,Available): #Str,Str,Int,Int,Boolean,Int,Int,Boolean
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
