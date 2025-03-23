'''
This is the same as encryption 1 (challenge 37), 
but the first input from the user should tell how many characters need to be shifted; 
it can range from 1 to 25. In Encryption 1, you shifted all characters by 1 position; 
now the user can choose any number between 1 and 25, 
and the program should be able to shift and encrypt.
'''
sentence = input("Enter Words: ").lower().strip()
encryption_mesg = ""
num = int(input("How charcters should we shift the encryption message: "))
index = 0
for i in sentence:
    char = sentence[index]
    char =  chr(ord(char) + num)
    encryption_mesg += char
    index += 1
print(encryption_mesg)

