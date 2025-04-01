from func import *
from classes import*
Readfile_to_dict(dictval=car_dict,filepath="/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
while True:
    print("Enter Options\n(0) Exit\n(1) Update\n(2) Add\n(3) Return Make\n(4) Return Val")
    while True:
        try:
            options = int(input("Enter Options: "))
            break
        except ValueError:
            pass
    match options:
        case 0:
            Writedict_to_file(car_dict,"/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
            exit()
        case 1:
            while True:
                model = input('Enter Model: ').strip().capitalize()
                make = input("Enter Make: ").strip().capitalize()
                while True:
                    try:
                        year = int(input("Enter Year: "))
                        break
                    except ValueError:
                        print("Enter Int")
                if not (model+"-"+make+"-"+str(year)) in car_dict:
                    user_input = input("Enter Blank to Try Again: ")
                if (model+"-"+make+"-"+str(year)) in car_dict:
                    update(model+"-"+make+"-"+str(year),car_dict) 
                    break
                if not user_input == None:
                    break
            Writedict_to_file(car_dict,"/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
        case 2:
            while True:
                choice = input("Enter Type(C,Car/T,Truck/B,Bike/Blank to close): ").strip().capitalize()
                if choice in ["C","Car","T","Truck","Bike","B",None]:
                    break
                else:
                    print("Enter One the Options")
            if choice == None:
                pass
            elif choice in ["C","Car"]:
                add(car_dict,tpye="C")
            elif choice in ["B","Bike"]:
                add(car_dict,tpye="B")
            elif choice in ["T","Truck"]:
                add(car_dict,tpye="T")
            Writedict_to_file(car_dict,"/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
        case 3:
            make = input("Enter Make: ").strip().capitalize()
            print(returnmake(make,car_dict))
            Writedict_to_file(car_dict,"/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
        case 4:
            while True:
                make = input("Enter make: ").strip().capitalize()
                model = input("Enter Model: ").strip().capitalize()
                while True:
                    try:
                        year = int(input("Enter Year: "))
                        break
                    except ValueError:
                        print("Enter Int")
                if make+"-"+model+"-"+str(year) in car_dict:
                    print(car_dict[make+"-"+model+"-"+str(year)])
                else:
                    print("Not In Dict")
                Writedict_to_file(car_dict,"/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #67/data.txt")
        case _:
            pass