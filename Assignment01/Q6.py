'''6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
epts the number as an argument.'''
def function(num):
    fact = 1
    while(num > 0):
        fact *= num
        num -= 1
    return fact

num = int(input("Enter a number to find it's factorial: "))
print(f"Factorial of {num} = {function(num)}")
