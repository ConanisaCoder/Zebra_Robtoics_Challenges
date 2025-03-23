'''

Create a program that displays the following menu for a user to manage their travel destination wish list:

Add a travel destination
Find a travel destination
Remove a travel destination
Sort destinations by alphabet
Count destinations

You can have a default list to begin.

'''
travel_destination = ["London","Paris","New York"]
print(travel_destination)
x = input("Would you Like to anything (True/False): ")
while x == "True": 
        menu = input("What would like to do \n Add a travel destination (1) \n Find a Travel destination (2) \n Remove a Travel destination (3) \n Sort destinations by alphabet (4) \n Count destinations (5) \nInput: ")
        if menu == "1" :
            x = int(input("How many would you like to add: "))
            for i in range (0,x,1):
                add = input("What would you like to add: ")
                travel_destination.append(add)
            print(travel_destination)
        if menu == "2":
            find = input("What do you want to find: ")
            if find in travel_destination:
                index = travel_destination.index(find)
                print("The location you mentioned is in the travel desnation")
                print(f"The location you are loking is in list is in {index}")
        if menu == "3":
            print(travel_destination)
            remove = input('What you like to remove: ')
            travel_destination.remove(remove)
            print(f"This what it likes after you remove it \n {travel_destination}")
        if menu == "4": 
            sort = travel_destination.sort()
            print(sort)
        if menu == "5": 
            Location_count = input("What location would you like to count: ")
            print(travel_destination.count(Location_count))
        x = input("Keep going (True/False): ")

while x== "False": 
    print(travel_destination)
    input("Press enter to Close: ")