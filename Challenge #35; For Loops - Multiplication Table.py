'''
Get an input number from the user and print 
its multiplication table up til' 20.
'''
x = int(input("Please enter a number: "))
for i in range(0,21,1):
    y = x*i
    print(f"{x} x {i} = {y}")