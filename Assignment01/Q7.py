'''7) Using for loop, write and run a Python program to find factorial from 0 to
10.'''
def function(num):
    fact = 1
    while(num > 0):
        fact *= num
        num -= 1
    return fact

for var in range(10):
    print(f"Factorial of {var} = {function(var)}")