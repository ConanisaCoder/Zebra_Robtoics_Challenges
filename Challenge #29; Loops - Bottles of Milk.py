'''
Write a program to create lyrics for the famous song with the following lines, and print on the console.

99 bottles of milk on the wall, 99 bottles of milk.
Take one down and pass it along, 98 bottles of milk on the wall.

And so..on til'

1 bottle of milk on the wall, 1 bottle of milk.
Take one down and pass it around, no more bottles of milk on the wall.
No more bottles of milk on the wall, no more bottles of milk.
Go to the store and buy some more, 99 bottles of milk on the wall.
'''

milk = 99

while milk> 1:
    print(str(milk) +" bottles of milk on the wall, " + str(milk) + " bottles of milk")
    milk -= 1
    print("Take one down and pass it along, " + str(milk) + " bottles of milk on the wall")
while milk == 1:
    print(str(milk) + " bottle of milk on the wall, " + str(milk) + (" bottle of milk"))
    print("Take on down and pass it around, no more bottles of milk")
    print("Go to the store and buy some more, " + (str(99)) + " bottles of milk on the wall.")
    milk -= 1
else:
    input("Press enter to close: ")