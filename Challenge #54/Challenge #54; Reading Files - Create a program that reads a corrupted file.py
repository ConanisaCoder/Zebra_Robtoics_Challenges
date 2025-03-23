readObj = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #54/text.txt","r")
string =""
while True:
    readchar = readObj.read(1)
    if readchar.isalpha() == True :
        string += readchar
    if not readchar:
        break
print(string)
readObj.close()