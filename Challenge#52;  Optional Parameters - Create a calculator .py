'''
Create a program that takes in the cost of a bill at a restaurant and calculates and returns the tip.

Bonus: Use optional parameters to allows the user to give more or less (hopefully more) than the normal 15%
'''
def calc(cost,tip=0.15):
    cost += tip * cost
    return cost
while True:
    try:
        cost_calc = int(input("Enter cost: "))
        break
    except ValueError:
        print("Enter Int")
while True:
    try:
        tip_calc = int(input("Enter tip: "))
        tip = tip_calc/100
        break
    except ValueError:
        print("Enter Int")
print(calc(cost_calc,tip))