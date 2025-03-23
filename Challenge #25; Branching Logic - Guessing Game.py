import random
'''
Generate a random number between 1 and 5, 
and ask the user to guess the number. 
If the user guesses correctly, congratulate the user on guessing correctly; 
if not, wish them good luck next time.
'''

rand_num = random.randint(1,5)
ticket = int(input("What is the number on your ticket: "))
if ticket == rand_num:
    print("You have won the lottery")
else:
    print("Better luck next time")