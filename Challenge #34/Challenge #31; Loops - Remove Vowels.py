'''
Write a program to get input from the user,
and remove all the vowels (a,e,i,o,u) from the sentence and print the result back on screen.
'''

print("Program to To remove vowels")
vowels = "AaEeIiOoUu"
result = ""
index = 0 
sentence = input("Input setence: ")
for i in sentence:
    char = sentence[index]
    if char not in vowels:
        result += char
    index += 1
print(result)
