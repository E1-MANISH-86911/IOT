#3) Find and display the largest number of a list without using built-in function 
# max(). Your program should ask the user to input values in list from keyboard.
def find_max(l1):
    max=0
    for i in l1:
        if i > max:
            max = i
    return max

n = int(input("Enter the size of list: "))
l1 = []
for i in range(n):
    data = int(input(f"Enter the list data at index {i}: "))
    l1.append(data)
print(f"Maximum number in the list: {find_max(l1)}")