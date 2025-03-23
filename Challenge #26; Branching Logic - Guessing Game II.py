import random
'''
Ask them to guess the number 3 times (we have not learned repeated loops yet, so you will have the same code repeated 3 times).
If the user’s guess is less than the actual number, tell the user “The number is less than your guess”
If the user’s guess is greater than the actual number, tell the user “The number is greater than your guess”
If the user's guess equals the random number, tell the user “You guessed it right!”
'''
random_num= random.randint(1,5)
guess_1 = int(input("Guess 1-5: "))
if guess_1 == random_num:
    print("You guessed it rigth")
    input("Press enter to close: ")
elif guess_1 < random_num:
    print("The number is greater than your guess") 
elif guess_1 > random_num:
    print("The number is less than your guess")
if not guess_1 == random_num:
    print("This your second chance")
    guess_2 = int(input("Guess 1-5: "))
    if guess_2 == random_num:
        print("You guessed it rigth")
        input("Press enter to close: ")
    elif guess_2 > random_num:
        print("The number is less than your guess")
    elif guess_2 < random_num:
        print("The number is greater than your guess")
    if not guess_2 == random_num:
        print("One last chance")
        guess_3 = int(input("Guess 1-5: "))
        if guess_3 == random_num:
            print("You Won")
        else:
            print("Its over you lost") 