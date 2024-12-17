'''5). Define a procedure histogram() that takes a list of integers and prints a 
histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
******* 
'''
def histogram(l1):
    for i in l1:
        print("*" * i)
l1 = []
n = int(input("Enter the size of list: "))
for i in range(n):
    data = int(input(f"Enter the data in list at index {i}:"))
    l1.append(data)
histogram(l1)

