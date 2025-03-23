from func import *
readdata = open("/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #66/data.txt","r")
listread = readdata.readlines()
intval = 0
endval = 7
while endval <len(listread):
    datalist = listread[intval:endval]
    make = str(datalist[0][datalist[0].index(":")+1: ].strip())
    model = str(datalist[1][datalist[1].index(":")+1: ].strip())
    year = int(datalist[2][datalist[2].index(":")+1: ].strip())
    price = int(datalist[3][datalist[3].index(":")+1: ].strip())
    used = bool(datalist[4][datalist[4].index(":")+1: ].strip())
    milleage = int(datalist[5][datalist[5].index(":")+1: ].strip())
    doors = int(datalist[6][datalist[6].index(":")+1: ].strip())
    available = bool(datalist[-1][datalist[-1].index(":")+1: ].strip())
    car_dict[make+"-"+model+"-"+str(year)] = Car(make,model,year,price,used,milleage,doors,available)
    intval += 8
    endval += 8
running  = True
while running == True:
    if len(car_dict) > 0:
        writedata = open("/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #66/data.txt","w")
        for val in car_dict:
            make,model,year,price,used,milleage,doors,available = car_dict[val].make,car_dict[val].model,car_dict[val].year,car_dict[val].price,car_dict[val].used,car_dict[val].milleage,car_dict[val].doors,car_dict[val].available
            listdata = ["Make: " + str(make), "Model: " +str(model), "Year: " + str(year), "Price: " + str(price), "Used: " +str(used), "Milleage: " + str(milleage),"Doors: " + str(doors), "Available: " +str(available)]
            writedata.write("\n".join(listdata))
        writedata.close()
    print("(0) Close \n(1) Add Car\n(2) Return Make\n(3) Return Value\n(4) Update Val\n(5) Set Unaviable\n(6) Update mileage\n(7) Stringify\n(8) Set Used/Unused")
    while True:
        try:
            input_choice = int(input("Enter Choice: "))
            break
        except ValueError:
            pass
    if input_choice < 0 :
        input_choice = 0 
    elif  input_choice > 5:
        input_choice = 5
    match input_choice:
        case 0:
            running = False
        case 1:
            add_car(car_dict)
        case 2:
            make= input("Enter Make: ").strip().lower().capitalize()
            returnmake(make,car_dict)
        case 3:
            make = input("Enter make: ").strip().lower().capitalize()
            model = input("Enter Model: ").strip().lower().capitalize()
            while True:
                try:
                    year = int(input("Enter Year: "))
                    break
                except ValueError:
                    pass
            reutrnval(make+"-"+model+"-"+str(year),car_dict)
        case 4: 
            make = input("Enter make: ").strip().lower().capitalize()
            model = input("Enter Model: ").strip().lower().capitalize()
            while True:
                try:
                    year = int(input("Enter Year: "))
                    break
                except ValueError:
                    pass
            updateval(make+"-"+model+"-"+str(year),car_dict)
        case 5: #FIX
            make = input("Enter Make: ").strip().lower().capitalize()
            model = input("Enter Model: ").strip().lower().capitalize()
            while True:
                try:
                    year = int(input("Enter Val Error: "))
                    break
                except ValueError:
                    pass
                year = str(year)
            car_dict[make +"-"+model+"-"+str(year)].marksold()
        case 6:
            make = input("Enter Make: ").strip().lower().capitalize()
            model = input("Enter Model: ").strip().lower().capitalize()
            while True:
                try:
                    year = int(input("Enter Val Error: "))
                    break
                except ValueError:
                    pass
                year = str(year)
            car_dict[make +"-"+model+"-"+str(year)].changemillage()
        case 7:
            make = input("Enter Make: ").strip().lostringifywer().capitalize()
            model = input("Enter Model: ").strip().lower().capitalize()
            while True:
                try:
                    year = int(input("Enter Val Error: "))
                    break
                except ValueError:
                    pass
                year = str(year)
            print(car_dict[make +"-"+model+"-"+str(year)].stringify())