import random
'''
Make a list to store 10 words.
Pick a random word from the list and save it somewhere.
Print the length of the random word.
Give players 5 chances to guess the letters in the word while giving them appropriate success and failure messages.
Hint: you can use if i in word - to check if a particular letter is in the word.
On the 6th attempt, ask them to guess the whole word. Compare the randomly selected words with the user’s guess; if it is correct, the user wins.
'''
print("Guess the Programing Langugue")
words = ["Java", "Python", "Javascript", "C++", "C", "Golang", "Ruby","PHP", "Swift", "Koltin"]
word = words[random.randrange(1, 10)]
print("The length of the word is " + str(len(word)) + " charcters")
print("You have " + str(5) + " tries to get the word correct")
for i in range(0,5,1):
    guess = input("Guess: ")
    index = 0
    for i in guess:
        guess_string = ""
        char = guess[index]
        if char in word:
            guess_string += char
            print("You got some of the letter correct which where; " + guess_string)
        else:
            print("Not in word")
        index += 1
print("Now guess the word")
final_guess = input("What is your Final Guess: ")
if final_guess == word:
    print("You won")
else:
    print("You lost")
print("The word was " + word)