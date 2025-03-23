'''
Accept a number, n, from the user and calculate the sum of all numbers between 1 and n including n.

For example, if user gives 10 as an input, the output should be 55.
'''
n = int(input("What number would like to calculate: "))
y = 1
while n>=y:
    print(n+y)
    y += 1
else:
    print("Press enter to close:")