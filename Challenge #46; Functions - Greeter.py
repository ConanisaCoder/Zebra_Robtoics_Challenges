'''
Write a function greeter(name) that takes in a person's name and prints out a greeting.
The greeting must be at least three lines, and the person's name must be in each line.
Use your function to greet at least three different people.
Bonus: Store your three people in a list, and call your function from a for loop.
'''
name_list = []
index = 0
def greeter_name(name):
    print("Hello there " + name)
    print("Welcome to Cloudy Hotel " + name)
    print("Enjoy your stay " + name)
name_count = abs(int(input("Enter the amount of people visiting the hotel today: ")))
for i in range(0,name_count,1):
    name_input = input("Enter name: ").strip()
    name_list.append(name_input)
for i in name_list:
    name =  name_list[index]
    print("")
    greeter_name(name)
    print("")
    index += 1