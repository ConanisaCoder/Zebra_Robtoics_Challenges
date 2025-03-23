'''
Accept a number, n, from the user and calculate the sum of all numbers between 1 and n including n.

For example, if user gives 10 as an input, the output should be 55.
'''
n = int(input("What number would like to calculate: "))
for i in range(0,n+1,1): 
    x = i + n
    print(x)