#4] Write a Python function to find the maximum of three numbers.

def function(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(f"num1 is greater") 
    elif (num2 > num1 and num2 > num3):
        print(f"num2 is greater") 
    elif (num3 > num1 and num3 > num2):
        print(f"num3 is greater")
    else:
        print("All numbers are equal")
        
function(5, 2, 9)
function(5, 9, 2)
function(10, 2, 9)
function(4, 4, 4)