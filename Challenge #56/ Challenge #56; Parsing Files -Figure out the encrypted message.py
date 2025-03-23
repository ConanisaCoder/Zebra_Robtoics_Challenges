readObj = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge#56/text.txt","r")
readlines_readObj_encryption = readObj.readline()
readlines_readObj_encryption.strip()
val_change = int(readlines_readObj_encryption)
newstring = ""
while True:
    retruns_lines = readObj.readlines()
    if not retruns_lines:
        break
    retrun = "\n".join(retruns_lines)
    for i in retrun:
        newstring += chr(ord(i)+20)
    print(newstring)
readObj.close()