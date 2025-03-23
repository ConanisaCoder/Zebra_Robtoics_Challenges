'''
Your challenge is to create a program that reads a suggestions file for a banking app and figures out the features in the app that need to be created or fixed.
Look for these keywords in the suggestion file and keep track of how many times each word occurs:
Password
Security
E-transfer
accounts
cards
Deposit
branch
Once you have a list of occurrences, display them to the screen in a useful and easy to read way.
'''
open_file  = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #58/text.txt","r")
password_count = 0
Security_count = 0
E_Transfer = 0
Accounts_count = 0
Card_count = 0
Deposit_count = 0
Branch_count = 0
readfile = open_file.readlines()
for reading in readfile:
    reading.lower()
    reading.replace("\n","")
    if "password" in reading:
        password_count += 1
        pass_word_features = []
        pass_word_features.append(reading)
    if "security" in reading:
        Security_count += 1
        Security_Features = []
        Security_Features.append(reading)
    if "account" in reading: 
        Accounts_count += 1
        Accounts_Features = []
        Accounts_Features.append(reading)
    if "e-transfer" in reading:
        E_Transfer += 1
        E_Transfer_Features = []
        E_Transfer_Features.append(reading)
    if "card" in reading:
        Card_count += 1
        Card_count_Features = []
        Card_count_Features.append(reading)
    if "deposit" in reading:
        Deposit_count += 1
        Deposit_Features = []
        Deposit_Features.append(reading)
    if "branch" in reading:
        Branch_count += 1
        Branch_Features = []
        Branch_Features.append(reading)
print("Features for password ("+str(password_count)+"): "+ (str(pass_word_features)))
print("Features for security ("+str(Security_count)+"): " + str(Security_Features))
print("Features for account (" +str(Accounts_count)+"): " +str(Accounts_Features))
print("Features for e-transfer (" +str(E_Transfer)+"): " +str(E_Transfer_Features))
print("Features for card(" +str(Card_count)+"): " +str(Card_count_Features))
print("Features for deposit(" +str(Deposit_count)+"): " +str(Deposit_Features))
print("Features branch(" +str(Branch_count)+"): " +str(Branch_Features))

open_file.close()