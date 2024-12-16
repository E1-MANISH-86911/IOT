# 1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length = float(input("Enter the length of rectangle: "))
bredth = float(input("Enter the bredth of rectangle: "))
print(f"Area of rectangle = {length * bredth}")
perimeter = (length + bredth) * 2
print(f"Perimeter of rectangle = {perimeter}")