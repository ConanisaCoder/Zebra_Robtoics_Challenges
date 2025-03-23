from math import *
read_file = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #53/questions.md","r")
question_one = read_file.readline()
count = 0
print(question_one,end="")
answer_one = int(read_file.readline())
input_one = int(input("Enter number: "))
if input_one == answer_one:
    print("Correct")
    print("The answer is: " + str(answer_one))
    count += 1/3
else:
    print("Wrong")
    print("The answer is: " + str(answer_one))
question_two = read_file.readline()
print(question_two,end="")
answer_two = int(read_file.readline())
input_two = int(input("Enter number: "))
if input_two == answer_two:
    count +=1/3
    print("Correct")
    print("The answer is: " + str(answer_two))
else: 
    print("Wrong")
    print("The answer is: " + str(answer_two))
question_three =read_file.readline()
print(question_three,end="")
answer_three = read_file.readline()
input_three = input("Enter answer: ")
if input == answer_three:
    print("Correct")
    print("The answer is: " + str(answer_three))
    count += 1/3
else:
    print("Wrong")
    print("The answer is: " + str(answer_three))
count =round(count * 100)
print(str(count) +"%")
read_file.close()