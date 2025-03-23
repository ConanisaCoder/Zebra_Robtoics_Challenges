'''
Extend challenge 23 to add the following rides and height restrictions; 
the program should print ALL rides the users are allowed to go on.
'''
heigth = int(input("How tall are you in inches: "))
if heigth<40:
    print("You are unable to go on any ride.")
elif heigth>=40 and heigth<48:
    print("You are able to ride on Tree Top Adventure, Taxi Jam, Sugar Shack.")
elif heigth >=48 and heigth<54:
     print("You are able to ride on Tree Top Adventure, Taxi Jam, Sugar Shack, Vortex, Lumber Jack, Flying Canoes ")
elif heigth >= 54:
    print("You are able to ride on Tree Top Adventure, Taxi Jam, Sugar Shack, Vortex, Lumber Jack, Flying Canoes, Flight Deck, Behemoth, Leviathan.")