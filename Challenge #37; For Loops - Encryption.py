'''
Write a program to get a sentence from the user. Only lower case letters will be typed, except for a space character. Shift all the characters by 1 position.
For example – character ‘a’ should become ‘b’, ‘b’ should become ‘c’ and so on, with ‘z’ becoming to ‘a’.
e.g.
Input: “try to take road less traveled”
Output: “usz up ublf spbe mftt usbwfmfe”
'''
sentence = input("Enter sentence: ").lower()
index = 0
encryption = ""
for i in sentence:
    char_in = sentence[index]
    new_char = chr(ord(char_in) + 1)
    char_ord = ord(char_in)
    if char_ord == 122:
        encryption += "a"
    else:
        encryption += new_char
    index += 1
print(encryption.strip().lower())
