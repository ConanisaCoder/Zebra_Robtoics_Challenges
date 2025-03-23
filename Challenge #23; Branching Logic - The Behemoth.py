'''
Write a program that checks the height of the person and determines if they are allowed on the roller coaster, The Behemoth.
You are only allowed to go on The Behemoth if you are taller than 4 feet.
'''

heigth = int(input("What is your heigth in feet: "))
if heigth >= 4:
    print("You are allowed onto the ride.")
else:
    print("You are not allowed onto the ride.")