wrtiefule= open("/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Classes/Mod 2/C_3 Reading a File/test.txtt","w") # creates a new file, If the file not there it Create on and there is one is erase it
read_file =open("/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Classes/Mod 2/C_3 Reading a File/helloword.java","r") #read file, if file not there it will return an Error
file_add =open("/home/oco/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Classes/Mod 2/C_3 Reading a File/helloword.java","a") # append file, if there is no file
print(read_file.read()) #returns the Whole file in the form of plain text
print(read_file.readline()) #read online of the file and then moves to read the next on and the file
print(read_file.read(1)) #This method allows you to read a certain number of letters at a time
print(read_file.readlines()) #THis method allows you to read
read_file.close()