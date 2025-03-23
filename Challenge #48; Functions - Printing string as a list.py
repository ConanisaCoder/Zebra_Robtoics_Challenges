'''
Your program should take in a string and print out the string as a list. 
Create a function called stringToList to help you do this.
'''
def stringToList(string):
    stringToList_List = []
    for i in string:
        stringToList_List.append(i)
    print(stringToList_List)
string = input("Enter string: ")
stringToList(string)