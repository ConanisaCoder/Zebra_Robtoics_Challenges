'''
A program is needed to check if the message sent is an urgent message.
Get input from the user, which is a message.
Remove all leading and trailing spaces from the message.
Print the length of the message, after the spaces are removed.
Check if the message contains “911” and print out at which index it does; if not print -1.
'''
print("Urgent message checker: ")
message = input("Input message here: ")
message = message.strip()
print (message.find("911"))
  