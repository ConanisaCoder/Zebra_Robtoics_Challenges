'''
Write a program that checks if the input string has an “e", and if it does, print "Has e". 
Otherwise, print “invalid input”. 
Remember you can use string functions that you learned before to help you.
'''
letter = input("Enter the keyword: ")
letter_find = letter.find("e")

if letter_find >= 0:
    print("Has E")
else: 
    print("Invalid Input")