'''2] Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639'''

num = int(input("Enter a 4 digit number: "))
num1 = int(num)
a = int(num % 10)
num = int(num / 10)
b = int(num % 10)
num = int(num / 10)
c = int(num % 10)
num = int(num / 10)
d = num

print(f"a. {d} {c} {b} {a}")
print(f"b. {num1} = {d*1000} + {c*100} + {b*10} + {a}")
print(f"c. {a}{b}{c}{d}")