'''
Your code should take in the following input from a user:

Do they want to draw a circle, a square, or a triangle
The size of the shape they want to draw
The color of the shape they want to draw
Use appropriate functions where necessary (minimum 3).

Sample input:
'''
import turtle
def draw_sqaure():
    while True:
        try:
            size = float(input("Enter Side Length: "))
            break
        except ValueError:
            print("Must be an int / float: ")
    color = input("Enter color: ")
    turtle.Screen()
    sqaure = turtle.Turtle()
    sqaure.fillcolor(color)
    sqaure.begin_fill()
    for i in range(0,4,1):
        sqaure.forward(size)
        sqaure.right(90)
    sqaure.end_fill()
def draw_circle():
    while True:
        try:
            size = int(input("Enter Size: "))
            break
        except ValueError:
            print("Must be an Int")
    color = input("Enter color: ")
    turtle.Screen()
    circle = turtle.circle(size)
    circle.fillcolor(color)
    circle.begin_fill()
    circle.end_fill()

def draw_triangle():
    equal = input("Enter trianlge sides equal (y/n): ").lower()
    if equal == "y":
        while True:
            try:
                side_length = int(input("Enter side length: "))
                break
            except ValueError:
                print("Enter int")
        color = input("Enter colour: ").lower()
        turtle.Screen()
        traingle =  turtle.Turtle()
        traingle.fillcolor(color)
        traingle.begin_fill()
        for i in range(0,3,1):
            traingle.forward(side_length)
            traingle.right(120)
        traingle.end_fill()
    elif equal == "n":
        while True:
            try:
                side_length_1 = int(input("Enter Side Length One: "))
                break
            except ValueError:
                print("Must be Int")
        while True:
            try:
                side_length_2 = int(input("Enter Side Length Two: "))
                break
            except ValueError:
                print("Must be Int")
        while True:
            try:
                side_length_3 = int(input("Enter Side Length Three: "))
                break
            except ValueError:
                print("Must be Int")
        color = input("Enter color: ").lower()
        turtle.Screen()
        traingle = turtle.Turtle()
        traingle.fillcolor(color)
        traingle.begin_fill()
        traingle.foward(side_length_1)
        traingle.right(120)
        traingle.forward(side_length_2)
        traingle.right(120)
        traingle.forward(side_length_3)
        traingle.end_fill()
    else:
        print("Invalid input")
        print("Program closed")
        exit()
run_program = input("Run program (y/n): ").lower()
while run_program == "y":
    print("(1) Draw a sqaure\n(2) Draw a Circle\n(3) Draw a Triangle (4) Close Program")
    draw = input("Enter what do want to draw: ")
    if draw == "1":
        draw_sqaure()
    elif draw == "2":
        draw_circle()
    elif draw == "3":
        draw_triangle()
    elif draw == "4":
        print("Program closed: ")
        exit()
    else:
        print("Invalid input")
        print("Program Closed")
        exit()