# Shift Key world  
'''
earth -- > mars sky--> sea fire--> water
gold --> dirt canvas -- > soccer tales --> tail
story -- music  dreams --> shower stone -- > Firefox
'''
readfile = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #60/test.txt","r")
reading = readfile.read()
reading = reading.strip()
newreading = ""
for letter in reading:
    newletter = chr(ord(letter) -1)
    newreading += newletter
print(newreading)
readfile.close()